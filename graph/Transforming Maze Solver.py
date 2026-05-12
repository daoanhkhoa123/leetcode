"""
NOTE:  WE ALWAYS USE Y, X COORDINATE SYSTEM
"""
from dataclasses import dataclass
# a = {1:2}
# b= {2:3}
# print(help(a))
# print(a.update(b))
# print(a)


# define direction based on index
DIRECTION_DICT = {0:"E", 1:"S", 2:"W", 3:"N"}
NODE_DICT = {"B": -1, "X": -2}
FULL_DIR = ["S", "W", "E", "N"]
OPOSITE_DIR_DICT = {"W":"E", "E":"W","S":"N", "N": "S"}
    
EDGE1 = 1
    
def to_bits(i, max_len=4):
    # sepcial handling for bit shifting operation only
    # not add, not overflow
    while i > 15:
        i -= 15
    bits = []
    while i > 0:
        bits.append(i%2)
        i //=2
    return bits + [0] * (max_len-len(bits))

def to_direction(bits):
    return [DIRECTION_DICT[i] for i, v in enumerate(bits) if v]
            
# print(to_bits(5),  to_direction(to_bits(5)))
# print(to_bits(5*2),  to_direction(to_bits(5*2)))
# print(to_bits(2),  to_direction(to_bits(2)))
# print(to_bits(4),  to_direction(to_bits(4)))
# print([to_bits(i) for i in range(16)])

MAX_INT = 2**10
   

class Node:
    def __init__(self, y, x, val):
        self.y=y
        self.x=x
         # start is -1, end is -2, the rest are the same
        self._val = NODE_DICT.get(val,val)
        
    @property
    def value(self):
        # we want canonical number 
        if self._val == NODE_DICT["B"]:
            return 0
        if self._val == NODE_DICT["X"]:
            return 0
        return self._val

    @property
    def raw_value(self):
        return self._val
    
    @property
    def raw_bits(self):
        return to_bits(self.value)
    
    def bits(self, time):
        time %= 4
        vt = self.value * 2**time
        return to_bits(vt)

    def __repr__(self):
        return f"Node({self.y}, {self.x}); {self.value}"
    
    def blocked_direction(self, time):
        bits = self.bits(time)
        return set(to_direction(bits))
    
    def open_direction(self, time):
        return set([d for d in FULL_DIR if d not in self.blocked_direction(time)])

# frozen becaause if it alreaady in a dict
# we dont want to change it
@dataclass(frozen=True)
class TimedNode:
    node:Node
    time: int
    
    def __hash__(self):
        return hash((self.node, self.time))

    def __eq__(self, obj):
        if not isinstance(obj, TimedNode):
            return False
        return self.node == obj.node and self.time == obj.time

    
    
# n  = Node(3,0, 12)
# print(n.blocked_direction(0))
# print(n.open_direction(0))
# print(n.bits)
# n  = Node(2,1, 9)
# print(n.blocked_direction(0))
# print(n.open_direction(0))
# print(n.bits)
# raise Exception()


class InsaneQueue:
    def __init__(self, max_time):
        self.max_time = max_time
        self._cur_time = -1
        for i in range(max_time):
            setattr(self, f"queue{i}", list())
        
    @property
    def cur_time(self):
        return self._cur_time
    @cur_time.setter
    def cur_time(self, value):
        value %= self.max_time
        self._cur_time= value
        
    def __getitem__(self, idx):
        return getattr(self, f"queue{idx}")
    
    def __setitem__(self, idx, value):
        setattr(self, f"queue{idx}", value)
        
    def __bool__(self):
        # if one of them re still good, we good
        for i in range(self.max_time):
            if self[i]: # still good
                return True
        return False
    
    def __repr__(self):
        res = ["InsaneQueue{"]
        for i in range(self.max_time):
            res.append(f"Pos{i} {self[i]}")
        res.append("}")
        return "\n".join(res)
    
    def append(self, el):
        self.cur_time += 1
        self[self.cur_time].append(el)
    
    def append_at(self, el, time):
        time %= self.max_time
        self[time].append(el)
        
    def pop(self):
        self.cur_time += 1
        
        cache = self[self.cur_time]
        self[self.cur_time] = list()
        return cache
    
    def pop_at(self, time):
        time %= self.max_time
        cache = self[time]
        self[time] = list()
        return cache

class Graph:
    def __init__(self, data):
        self.height = len(data)
        self.width = len(data[0])
        self._graph = [[None for _ in range(self.width)] for __ in range(self.height)]
        
        for y in range(self.height):
            for x in range(self.width):
                self._graph[y][x] = Node(y, x, data[y][x])
                
                # special case, store start and end too
                if data[y][x] == "B":
                    self.start = self._graph[y][x]
                if data[y][x] == "X":
                    self.end = self._graph[y][x]
        if not hasattr(self, "start") or not hasattr(self, "end"):
            raise Exception("False in initialization")
                
    def __getitem__(self, idx):
        return self._graph[idx]
    
    def _get_dir(self, node_fm, node_to):
        dy = node_to.y - node_fm.y
        dx = node_to.x - node_fm.x
        
        # hack, only one of them should be 1 or -1
        if dy ** 2 + dx ** 2 != 1:
            raise Exception("Illegal move")
        
        if dy == -1:
            return "N"
        if dy == 1:
            return "S"
        if dx == 1:
            return "E"
        if dx == -1:
            return "W"
        raise Exception("Illegal move")
    
    def build_path_by_dict(self, timed_end, path_dict):
        res = [timed_end]
        for _c, bkwad in enumerate(res):
            # either the start, or time lag
            # start has special sinature tho start: None
            time_lag_counter = 0
            cur_time = bkwad.time
            new_bkwdad = TimedNode(bkwad.node, cur_time)
            while new_bkwdad not in path_dict:
                time_lag_counter += 1
                cur_time -= 1
#                 print(bkwad, "timeitme")
                if cur_time < 0:
                    raise Exception("Something wrong with the path")
                new_bkwdad = TimedNode(bkwad.node, cur_time)
                       
            pre = path_dict[new_bkwdad]
            # it's the start
            if pre == None:
                break
            
            res.append(pre)
            
        return [n for n in res[::-1]]
        
              
    def path_to_dir(self, nodes):
        """
        from a list of timed node,
        generaated lits of direction
        then to string
        
        how flatten construct:
        
        note: becaue our dict is like thi B5: A3, A1: C1
        so we got C1, A3, B5
        meaning that C1, A1 then wait to three, then B3, wait to 5, then B5
        """

        flatten = []
            
        # so here it is, assume time at 0
        if nodes[0].time > 0:
            flatten = ["_"] * nodes[0].time
                
        # notice thi only take account in the relation
        # between two nodes, which means
        # between we assume our start at fisrt node
        # which is not, becuse our start time is 0, not the first node
        for fm, to in zip(nodes[:-1], nodes[1:]):
            time_lag = to.time-fm.time
#             print(fm, to, time_lag)
            dir = self._get_dir(fm.node, to.node)

            flatten.append(dir)
            # becuse we havae accounted for time break at 
            if time_lag:
                flatten+=["_"] * time_lag
        
        flatten.append("_")
#         print("flatten dir", flatten)
#         print("len flaateen", len(flatten))
        res = []
        last_break = 0
        for i, c in enumerate(flatten):
            if c == "_": # time break
                res.append("".join(flatten[last_break:i]))
                    
                last_break = i+1

#         print("res", res)
        return res
    
    def goto_by_dir(self, node, dir):
        y = node.y
        x = node.x
        if dir == "N":
            y -= 1
        if dir == "S":
            y +=1
        if dir == "W":
            x -=1
        if dir == "E":
            x += 1
        
        if y < 0 or y >= self.height:
            raise Exception("Out of height direction")
        if x < 0 or x >= self.width:
            raise Exception("Out of width direction")
        return self[y][x]
    
    def get_adjacent(self, node, time):
        # for ech we can TRY to move
#         print("from", node, "time", time, "opened at", node.open_direction(time))
        for dir in node.open_direction(time):
            try:
                next_node = self.goto_by_dir(node, dir)
            except:
#                 print("what")
                continue
            
            # if we try to go north (from our perspective)
            # and they re not blocked on south (from their perspective)
            # a lil hack instead of flipped them we flipped us lol
#             print(OPOSITE_DIR_DICT[dir], next_node.blocked_direction(time), "adjt test")
            if OPOSITE_DIR_DICT[dir] not in next_node.blocked_direction(time):
#                 print("yield at tune", time, next_node, "from", node)
                yield next_node
            
    
    def get_timed_adjacent(self, timed_node):
        for node in self.get_adjacent(timed_node.node, timed_node.time):
            # same time
            yield TimedNode(node, timed_node.time)
    
    def flood_timed(self, timed_starts, visited_nodes = None, target_time=None):
        """ Flood everything from mny starts it can from the start at one time 
        just to get to anywhere avaialbe in the TARGET time, not from time to time
        
        So like, what if from previous time, we waited, then flood for the next time?
        then our path has a jump: {A5: B5, B3:...}, 
        then we know that get to B at three, wait for 2, then go to A at 5
        
        To make this time residual invariant, weigh should care about (time, weig)
        and updating should be like this
        new_weight = weig_dict[timed][0], weig_dict[timed][1] + EDGE1
        """

        _pre_time = None
        weig_dict = {}
        
        for timed_start in timed_starts:
            weig_dict[timed_start] = (timed_start.time,0)
            if target_time is None:
                target_time = timed_start.time
            else:
                assert(target_time == timed_start.time, "Illegal time for maany start")
        queue = [*timed_starts]
        path_dict = {}
        while queue:
            timed = queue.pop()
            for next_timed in self.get_timed_adjacent(timed):
                # if visited IN PREVIOUS TIME, then ignore
                if visited_nodes is not None and next_timed.node in visited_nodes:
                    continue
#                 print("flood: checking", next_timed.node, visited_nodes)
                                
                # new, just set it temperally, we gonna deal with logic later
                if next_timed not in weig_dict:
                    weig_dict[next_timed] = (next_timed.time, MAX_INT)
                        
                # after init, we can safely compare
                new_weight = weig_dict[timed][0], weig_dict[timed][1] + EDGE1            
                if new_weight < weig_dict[next_timed]:
                    weig_dict[next_timed] = new_weight
                    path_dict[next_timed] = timed
                
                    # append
                    queue.append(next_timed)
                    
            #sorted here for performance
            queue = sorted(queue, key = lambda x: weig_dict[x])                                
        
        # so yeah, we only need path, because weigh does not related to our use of time
        return path_dict
    
#     def flood_dir(self, start, time):
#         path_dict = self.flood_path(start, time)
#         paths =  {end: self._build_path_by_dict(end, path_dict=path_dict) for end in path_dict}
#         dirs = {end : self.path_to_dir(paths[end]) for end in paths}
#         return dirs, path_dict
                                
    def djsktra(self, start, end):
#         test = TimedNode(self[3][1],0)
#         print(*self.get_timed_adjacent(test), "aj", test.node.open_direction(0))
#         print(self[2][1].open_direction(0))
#         print(self.build_path_by_dict(test,
#                                       path_dict={}), "testing path")
#         raise Exception()
        
                
        time_dist_dict = {start : 0}
        visited = set([start])
        global_time = 0
        
        timed_start = TimedNode(start, 0)
        path_dict = {timed_start: None}
        # now all zero_th time aare got
        # notice that globl time trat from 0 anyway, so whaatever
#         path_dict.update(self.flood_timed([timed_start], visited))

        # uhh, while time of node for path is different
        # state of the graph at time 1 and 5 is the same
        # also, we always moving
        insane_q = InsaneQueue(4)
        for timed in path_dict:
            # one nodes lives 4 times before it dies
            
            for i in range(4):
                # remember to change the time before adding it
                # as cost of waiting
                # also, no mutating, because that would cause changing
                # across everything
                new_t = TimedNode(timed.node, timed.time+i)
                insane_q.append_at(new_t, new_t.time)
        
        while insane_q:
#             print("at global time:", global_time,"-"*10)
#             print(insane_q)
            # get all the nodes in previous time
            timed_nodes = insane_q.pop_at(global_time)

            global_time += 1
            # in the next time, we dont have to visit these
            for itn in range(len(timed_nodes)):
                visited.add(timed_nodes[itn].node)
                
            next_dict = self.flood_timed(timed_nodes, visited, global_time)
#             print("aadded:", *[n.node for n in next_dict])
#             print("aadded2:", next_dict)
            path_dict.update(next_dict)
            for tn in next_dict:
                if tn.node == end:
                    return path_dict, tn
                
                for i in range(4):
                    new_t = TimedNode(tn.node, tn.time+i)
                    insane_q.append_at(new_t, new_t.time)
        
        return None, None

        
def maze_solver(ar):
    graph = Graph(ar)

#     q = InsaneQueue(4)
#     for i in range(5):
#         for _ in range(4):
#             q.append(i)
#     print(q)
            
#     c = 0
#     while q:
#         print("timed", c, q.pop())
#         print("lefted", q)
#     raise Exception()


    #     y,x = 1,2
#     time = 2
#     for time in range(5):        
#         print("blocked:",graph[y][x].value, graph[y][x].bits(time), graph[y][x].blocked_direction(time))
#         print("aaa",*graph.get_timed_adjacent(TimedNode(graph[y][x], time)))
#         print("-"*10)
#     raise Exception()

    path_dict, timed_end = graph.djsktra(graph.start, graph.end)
    if path_dict is None:
        return None
    
#     print(timed_end, "endned")
#     print(path_dict, "pth_dict")
#     print(path_dict[timed_end] ,"perere")
    path = graph.build_path_by_dict(timed_end, path_dict=path_dict)
    print("pathddic", path_dict)
    print("path",path)
    dir = graph.path_to_dir(path)
#     print(dir, "dir")
    return dir
    
    """
    2,0; 1,0; 2,1; 3,1; 0,0; 0,1
    
    """                           