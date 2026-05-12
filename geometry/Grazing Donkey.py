import numpy as np

FLOAT_DTYPE = np.float64
INT_DTYPE = np.int32

class Point(np.ndarray):
    def __new__(cls, y:float, x:float, dtype=FLOAT_DTYPE):
        array = np.array([y,x], dtype=dtype).view(cls)
        return array

    @property
    def y(self):
        return self[0]
    
    @property
    def x(self):
        return self[1]
      
    @y.setter
    def y(self, value:float):
        self[0] = value

    @x.setter
    def x(self, value:float):
        self[1] = value

class Segment:
    def __init__(self, start:Point, to:Point) -> None:
        self.start = start
        self.to = to
        self.cache  = {}

    def __repr__(self) -> str:
        return f"Segment(start: {self.start}, to: {self.to}) "

    @property
    def vector(self):
        return self.to - self.start
    
    @property
    def length(self):
        if "len" not in self.cache:
            self.cache["len"] = np.linalg.norm(self.vector)
        return self.cache["len"]

class Circle:
    def __init__(self, center:Point, radius:int) -> None:
        self.center = center
        self._radius = radius
        self._radius_r2 = self.radius * self.radius
        self._area = self._radius_r2 * np.pi

    def __repr__(self) -> str:
        return f"Circle(center: {self.center}, radius: {self.radius})"

    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._radius = value
        self._radius_r2 = value * value
        self._area = self._radius_r2 * np.pi
        
    @property
    def radius_r2(self):
        return self._radius_r2
    
    @property
    def area(self):
        return self._area

    def assert_on(self, x:Point):
        return 
        p = x - self.center
        assert np.isclose(p.dot(p), self.radius_r2), f"Point not on circle {self} for {x}"


def caclulate_on_segment(circle:Circle, segment:Segment, big_part:bool):
    circle.assert_on(segment.start)
    circle.assert_on(segment.to)

    triag_angle = np.arcsin(segment.length/2/circle.radius) * 2
    pie_angle = np.pi - triag_angle
    

    triag_area = circle.radius_r2 * np.sin(triag_angle) # /2 then *2 for 2 triangle
    pie_area = circle.area * pie_angle/np.pi # /2 then * 2 for two pie
    rec_area = triag_area + pie_area
    smallpie_area = (circle.area - rec_area) / 2
    
#     print("trig", triag_angle/np.pi, pie_angle/np.pi)
#     print("area", rec_area, smallpie_area, "\n")
    
    if big_part:
        return smallpie_area + rec_area
    else:
        return smallpie_area

def calculate_intersect(circle1:Circle, circle2:Circle) -> Segment:
    assert circle2.center.x == 0 and circle2.center.y == circle1.radius, f"Only for this specific setting is allowed {circle1.center}, {circle2.center}"
    
    
    intersect_y = (2 * circle1.radius_r2 - circle2.radius_r2) / 2 / circle1.radius
    x = np.sqrt(circle1.radius_r2 - intersect_y * intersect_y, dtype= circle1.center.dtype)
    
    p1 = Point(intersect_y, -x)
    p2 = Point(intersect_y, x)
    
    circle1.assert_on(p1)
    circle1.assert_on(p2)
    circle2.assert_on(p1)
    circle2.assert_on(p2)
    return Segment(p1, p2)

def cal_percentage(c1, c2, seg, big):
    a1 = caclulate_on_segment(c1, seg, big)
    a2 = caclulate_on_segment(c2, seg, False)
    return (a1 + a2) / c1.area

def get_rope_length(radius, perentage):
    radius = radius / 2
    if perentage == 0 or radius == 0:
        return 0
    # this is where the segment line is at the middle 
    middle_r = np.sqrt(2, dtype=FLOAT_DTYPE) * radius
    
    main_circle = Circle(Point(0,0), radius)
    top_circle = Circle(Point(radius, 0), 0)

    print("runingsd with ", middle_r)
    
    start = 0
    dia = radius* 2
    to = dia + 2
    cache = None
    while True:
        top_circle.radius = (start + to) // 2
        if top_circle.radius >= dia:
            return dia
        
        segment = calculate_intersect(main_circle, top_circle)
        percen = cal_percentage(main_circle, top_circle, segment, top_circle.radius > middle_r)
#         percen = percen + 5* 1e-5
        print(main_circle, top_circle)
        print('percet', percen)
        print("="*10)    
        if percen >= perentage:
            to = int(top_circle.radius+0.5)
        else:
            start = int(top_circle.radius+0.5)
        
        if cache is None or cache != top_circle.radius:
            cache = top_circle.radius
        else:
            return cache
