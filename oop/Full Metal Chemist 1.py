VALANCE_DICT = {"H": 1, "B": 3, "C":4, "N":3, "O":2, "F":1, "Mg":2, "P":3, "S":2, "Cl":1, "Br":1}
WEIGHT_DICT = {"H": 1.0, "B": 10.8, "C":12.0, "N":14.0, "O":16.0, "F":19.0, "Mg":24.3, "P":31.0, "S":32.1, "Cl":35.5, "Br":80.0}
TEMP = "H"
VALANCE_DICT[TEMP] = VALANCE_DICT["H"]
WEIGHT_DICT[TEMP]= WEIGHT_DICT["H"]

def insane_sort(d):
    """
    count from 1
    """
    
    # because of how it is initilaized 
    # first comes first, later comes later
    # so what we do is just like, smoothen it
    # not chaning orders
    sorted_keys = sorted(d.keys())
    for k, i in zip(sorted_keys, range(1, len(d) +1)):
        d[k] = i

# d = {5: None, 4:None, 2:None} # we waant 5:3, 4:2, 2:1
# insane_sort(d)
# print(d)
def get_alphebic_weight(c, h_last=False):
    weight = 0
    if c == "C":
        weight = 0
    elif c == "H":
        if h_last:
            weight = 99
        else:
            weight = 1
    elif c == "O":
        weight = 2
    else:
        weight = 5
    return (weight, c[0], len(c))

# print(sorted(["C", "H", "O", "N"], key=get_alphebic_weight))
class Atom(object):
    
    def __init__ (self, elt, id_):
        self._id = id_
            
        self.connected = [] # must before element, haack
        self.element = elt
        
    @property
    def element(self):
        if self._element == TEMP:
            return "H"
        return self._element
    
    @element.setter
    def element(self, elt):
        # self.valance - new_valance = dict[self] - dict[new]
        new_valance_test = VALANCE_DICT[elt] - len(self.connected)
        if new_valance_test < 0:
            raise InvalidBond("Caan not chaange to lower valnce")
        
        self._element = elt
        self.weight = WEIGHT_DICT[elt]
        self._valance = VALANCE_DICT[elt]
        
    @property
    def valance(self):
        return self._valance - len(self.connected)
        
    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, i):
        self._id=i
        
    def clean_hack(self):
        self.connected = [a for a in self.connected if a.element!= TEMP]
        
    def connect(self, obj):
        if self == obj:
            raise InvalidBond("Can not connect to self?")
        
        if self.valance == 0 or obj.valance == 0:
            raise InvalidBond("Out of vlnce to connect lmo")
        
#         if self in obj.connected and obj in self.connected:
#             raise InvalidBond("Already done once")
        
        self.connected.append(obj)
        obj.connected.append(self)
    
#     def remove_all_H(self):
#         for i, atm in enumerate(self.connected):
#             if atm.element == "H":
#                 self.connected.pop(i)
#                 self.valance += 1
        
    def __str__(self):
        conn = ["H" if atm.element == "H" else f"{atm.element}{atm.id}"
                for atm in sorted(self.connected, key=lambda x: (get_alphebic_weight(x.element, True), x.id))]
        itself = f"{self.element}.{self.id}: " if self.connected else f"{self.element}.{self.id}"
                
        return "".join(["Atom(",itself, ",".join(conn), ")"])
    def __hash__(self):      return self.id
    def __eq__(self, other): return self.id == other.id
    def __repr__(self):        return str(self)
    
    
class Molecule(object):
    def __init__(self, name=str()):
        self._name=name
        self._is_locked = False
        self._formula = [[]]
    
    @property
    def formula(self):
        if not self._is_locked:
            raise UnlockedMolecule("You havent called closed yet")
        
        counter = {}
        for v in self._formula:
            for atm in v:
                elt = atm.element
                counter[elt]=counter.get(elt, 0) + 1
        
        sorted_keys = sorted(counter.keys(), key= get_alphebic_weight)
        res = []
        for k in sorted_keys:
            v = counter[k]
            res.append(k)
            if v > 1:
                res.append(str(v))
        return "".join(res)
    
    @property
    def molecular_weight(self):
        if not self._is_locked:
            raise UnlockedMolecule("call closure first pleasea")
            
        total_weight = 0
        for v in self._formula:
            for atm in v:
                total_weight += atm.weight
        return total_weight               
        
    def __len__(self):
        total = 0
        for v in self._formula:
            total += len(v)
        
        return total
        
    @property
    def atoms(self):
        res = [atm for branch in self._formula for atm in branch]
        res = sorted(res, key = lambda a:a.id)                
        return res
        
    @property
    def name(self):
        return self._name
        
    def _insert(self, atom, saved_branch_idx, connected_to):
        atom.connect(connected_to)
        
        if saved_branch_idx is not None:
            self._formula[saved_branch_idx].append(atom)
        else:
            self._formula[0].append(atom)
        
        
    def _new_atom(self, elt):
        return Atom(elt, len(self)+1)
        
    def brancher(self, *args):
        if self._is_locked:
            raise LockedMolecule()
        
        print("called, crurent length", len(self._formula), "num of branced will", len(self._formula)+len(args))
        for n_cs in args:
            # init new branch
            self._formula.append([self._new_atom("C")])
            branch_idx = len(self._formula) - 1
            for i in range(1, n_cs):
                atom = self._new_atom("C")
                self._insert(atom, branch_idx, self._formula[branch_idx][-1])                    
       
        return self
        
    def bounder(self, *args):
        if self._is_locked:
            raise LockedMolecule()
            
        print(len(self._formula), "boundre called length")
        
        for arg in args:
            c1, b1,c2,b2 = arg
            c1 -= 1
            c2 -= 1
            
            self._formula[b1][c1].connect(self._formula[b2][c2])
            elt = self._formula[b2][c2].element
        return self
        
    def mutate(self, *args):
        if self._is_locked:
            raise LockedMolecule()
        print("mutated")
        for arg in args:
            nc, nb, elt = arg
            nc -= 1
            self._formula[nb][nc].element = elt
            
        return self
        
    def add(self, *args):
        if self._is_locked:
            raise LockedMolecule()
        
        print("current before add is leng", len(self._formula))
        for arg in args:
            nc,nb,elt = arg
            nc -= 1

            atom = self._new_atom(elt)
            con = self._formula[nb][nc]
            self._insert(atom, None, con)
                
        return self
    
    def add_chaining(self, *args):
        if self._is_locked:
            raise LockedMolecule()
        print("chain added")
        nc = args[0]
        nb = args[1]
        nc -= 1

        # check for invalid chain, which only happends when low valance
        # only the last element of chaain able to has valance of 1
        # ex: if chain only has one element, then anay would suffice 
        for elt in args[2:-1]:
            if VALANCE_DICT[elt] == 1:
                raise InvalidBond("Invalid chain, only the lasta can able to has 1 valnce")
        
        first_elt = args[2]
        # because _new_atom only yeild the lastest id
        # without inserting, id wont updated, causing id collision
        # so i had to init, then add
        # first atom is special, becuse it is the only thing
        # that get connected to the branch
        atom = self._new_atom(first_elt)
        self._insert(atom, None, self._formula[nb][nc])
        # the rest connected to the chain itself, not the main branches
        
        for elt in args[3:]:
            atom = self._new_atom(elt)
            # special index saying that the lastest added atom
            self._insert(atom, None, self._formula[0][-1])
            
        # after everything is done correctly without error, we set 
        return self
        
    def closer(self):
        if self._is_locked:
            raise LockedMolecule()
        self._is_locked=True
        
        print("closedd")
        
        for branch_idx in range(len(self._formula)):
            for atm_idx in range(len(self._formula[branch_idx])):
                for _ in range(self._formula[branch_idx][atm_idx].valance):
                    atom = self._new_atom(TEMP)
                    self._insert(atom, branch_idx, self._formula[branch_idx][atm_idx])
            
        return self
        
    def unlock(self):
        self._is_locked=False
        
        print(*self._formula, sep="\n")
        print(len(self._formula), "number of btanrch, caalled unolck")
        
        # keep track of sorting dict, will be useful later
        sort_d = {}
        for b_idx in range(len(self._formula)):
            # it is this complex because you have to use del element
            # for it to dispappear from everywhere
            length = len(self._formula[b_idx])                    
            atm_idx = -1
            while atm_idx < length-1:
                atm_idx += 1
#                 print("wht", atm_idx, len(self._formula[b_idx]), length)
                if self._formula[b_idx][atm_idx].element == TEMP:
                    del self._formula[b_idx][atm_idx]
                    length -= 1
                    atm_idx -= 1
                else:
                    self._formula[b_idx][atm_idx].clean_hack()
                    sort_d[self._formula[b_idx][atm_idx].id] = None # later
        
        # clean the empty                     
        self._formula = [self._formula[0]] + [b for b in self._formula[1:] if len(b)>0]
        
        # sort idx
        # becasue we do not changing order of the atom themself
        # but rather just mutating it, a dict will do the job fine
        insane_sort(sort_d)
        for b_idx in range(len(self._formula)):
            for atm_idx in range(len(self._formula[b_idx])):
                self._formula[b_idx][atm_idx].id = sort_d[self._formula[b_idx][atm_idx].id]
    
        if not any(self._formula[1:]):
            raise EmptyMolecule("empty molecue after unlock")
        print(*self._formula, sep="\n")
        print("length after unlock:", len(self._formula))
        
        return self
        
# m = Molecule().brancher(4,2,5).bounder((1,2,1,1), (2,1,3,1))
# print([str(a) for a in m.atoms])
# m.closer()
# m.unlock()
# print([str(a) for a in m.atoms])



        
class InvalidBond(Exception):
    def __init__(self, msg= ""):
        super().__init__(msg)
        
        
class UnlockedMolecule(Exception):
    def __init__(self, msg=""):
        super().__init__(msg)
        
class LockedMolecule(Exception):
    def __init__(self, msg = ""):
        super().__init__(msg)
        
class EmptyMolecule(Exception):
    def __init__(self, msg=""):
        super().__init__(msg)
        
    
