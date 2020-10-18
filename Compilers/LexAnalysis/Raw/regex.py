ALPHABETS = [ 
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '=',
                '+', '-', '*', '/', '{', '}', '_', '\n', '\t', '\r', '#', 'eps'  
            ]


REGEX_RULES = {
    "NUM" : "[0-9][0-9]*",
    "WS"  : "[ \n\t\r][ \n\t\r]*",
    "KEY" : "(if|else|int|main|void|return)",
    "ID"  : "[a-zA-z][a-zA-Z0-9_]*",
    "OP"  : "(\=|\(|\)|\{|\}|;|,)"
    "PRE" : "#.*"
}

PRIORITY = {
    "NUM" : 5,
    "WS"  : 4,
    "ID"  : 3,
    "KEY" : 2,
    "OP"  : 1,
    "PRE" : 0
}

PRIORITY_ORDER = [ "NUM", "WS", "ID", "KEY", "OP", "PRE"]

# Converting Regex to Table
class Regex(object):
    def __init__(self, expr):
        self.expr = expr
        self.expr_types = ["CONCAT", "ITER", "UNION", "UNIT"]

    def parse(self):
        ncunits = 0  # No of concatenated units

        nop = 0  # No of opening parantheses
        nos = 0  # No of opening square brackets

        

    def make_nfa(self, start=None):
        pass

# NFA Node
class NFANode(object):
    def __init__(self, state):
        self.state = state
        self.adj = {}

    def add_transition(self, state, alphabet):
        if alphabet not in self.adj.keys():
            self.adj[alphabet] = []

        self.adj[alphabet].append(state)


# NFA Graph Representation
class NFA(object):
    def __init__(self):
        self.states = {}
        self.num_vertices = 0

    def add_vertex(self, state):
        self.num_vertices += 1
        node = NFANode(state)
        self.states[state] = state
        return node

    def get_vertex(self, state):
        return self.states[state]

    def add_edge(self, src, dest, alphabet):
        if src not in self.states:
            self.add_vertex(src)
        if dest not in self.states:
            self.add_vertex(dest)

        self.states[src].add_transition(dest, alphabet)

    def get_vertices(self):
        return self.states.keys()

#  Shift to Regex Class
def make_nfa(expr):

    unit_expr = expr.split('|')

    start_st = "S"
    final_st = "F"

    adj_mat = dict()
    adj_mat["S"] = { x:-1 for x in ALPHABETS }
    adj_mat["F"] = { x:-1 for x in ALPHABETS }

    for uexp in unit_expr:
        pass

    

def make_table(nfa):
    transition_table = []
