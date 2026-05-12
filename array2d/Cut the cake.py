class Array2D:
    def __init__(self, data):
        self.data= data

    def __repr__(self):
        return "\n".join(self.data)
        
    def __get1key(self, ykeys):
        return self.data[ykeys]
        
    def __getitem__(self, tupls):
        if not isinstance(tupls, tuple):
            return self.__get1key(tupls)
        
        y_keys, x_keys = tupls
        if isinstance(y_keys, slice):
            return [d[x_keys] for d in self.data[y_keys]]
        else:
            return self.data[y_keys][x_keys]
    
def cut2(cake):
    ...

def cut(cake):
    cake = Array2D(cake.split("\n"))
    print(cake)
    print(cake[1:])
    print("aaa")
    print(cake[3, 1:3])
    print("aaa")
    # coding and coding...
    return []
