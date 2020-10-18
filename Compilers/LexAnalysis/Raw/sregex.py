ALPHABETS = [ 
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '=',
                '+', '-', '*', '/', '{', '}', '_', '#', '<eps>', '"', "'", "\n", 
                "\t", "\r"  
            ]

# Converting Regex to Table
class Regex(object):

    expr_types = ["CONCAT", "ITER", "UNION", "UNIT"]

    def __init__(self, expr):
        self.expr = expr

    def parse(self, expr):

        parsed_list = []

        cixs = self.cunits(expr)
        ncunits = cixs[-1]  # No of concat units in the expr

        if ncunits == 1:
            if expr[-1] == '*':

                parsed_list.append("ITER")
                parsed_list.append(self.parse(expr[:-1]))

            elif expr[0] == '(' and expr[-1] == ')':

                parsed_list = self.parse(expr[1:-1])

            elif expr[0] == '[' and expr[-1] == ']':

                parsed_list.append("UNION")
                uixs = self.uunits(expr)
                exprs = [""] * len(uixs)
                for i,u in cixs:
                    exprs[u-1] += expr[i]    
                for uexp in exprs:
                    if '-' in uexp:
                        s = uexp[0]
                        e = uexp[2]
                        for x in range(ord(s), ord(e)+1):
                            parsed_list.append(chr(x))
                    else:

                        parsed_list.append(uexp)
            elif '|' in expr:

                parsed_list.append("UNION")
                exprs = expr.split("|")
                for uexp in exprs:
                    parsed_list.append(self.parse(uexp))

            elif len(expr) > 1:

                parsed_list.append("CONCAT")
                for c in expr:
                    parsed_list.append(self.parse(c))                

            else:

                parsed_list.append("UNIT")
                parsed_list.append(expr)                    
                        
        else:
            exprs = [""] * ncunits
            for i,c in cixs:
                exprs[c-1] += expr[i]

            parsed_list.append("CONCAT")
            for uexpr in exprs:
                parsed_list.append(self.parse(uexpr))

        return parsed_list
 
    def uunits(self, expr):
        p = 1
        uixs = []
        flag = False
        for c in expr:
            if flag:
                uixs.append(p-1)
                flag=False
                continue

            if c == '-':
                uixs.append(p-1)
                flag=True
                continue
            else:
                uixs.append(p)
                p += 1

        return uixs 

    def cunits(self, expr):
        brackets = False
        escape = False
        units = []
        p = 1
        for c in expr:
            if brackets:
                units.append(p)
                if c == ')' or c == ']':
                    brackets = False
                    p += 1
                continue

            if escape:
                units.append(p)
                escape = False
            else:
                if c=="\\":
                    escape=True
                    units.append(p)
                    continue
                elif c=='(' or c=='[':
                    brackets = True
                    units.append(p)
                    continue
                elif c=='*':
                    units.append(p-1)
                else:
                    units.append(p)
                
            p += 1

        return units


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

    all_states = set()
    ix = 0

    def __init__(self):

        self.states = {}
        self.num_vertices = 0

        start = self.gen_state()
        self.start_state = self.add_vertex(start)

        final = self.gen_state()        
        self.final_state = self.add_vertex(final)

        self.head_state = self.start_state

        self.eps_closure = {}
                
    def union(self, nfa):
        self.merge_states(nfa)
        self.add_edge(self.start_state.state, nfa.start_state.state, "<eps>")
        self.add_edge(nfa.final_state.state, self.final_state.state, "<eps>")

    def concat(self, nfas):
        for nfa in nfas:
            if type(nfa) is str:
                nhead = self.gen_state()
                self.nhead_state = self.add_vertex(nhead)
                self.add_edge(self.head_state.state, self.nhead_state.state, nfa)
                self.head_state = self.nhead_state
            else:
                self.merge_states(nfa)
                self.add_edge(self.head_state.state, nfa.start_state.state, "<eps>")
                self.head_state = nfa.final_state
        self.add_edge(self.head_state.state, self.final_state.state, "<eps>")

    def recur(self):
        nstart = self.gen_state()
        nfinal = self.gen_state()
        snode = self.add_vertex(nstart)
        fnode = self.add_vertex(nfinal)

        self.add_edge(snode.state, self.start_state.state, "<eps>")
        self.add_edge(self.final_state.state, fnode.state, "<eps>")
        self.add_edge(self.final_state.state, self.start_state.state, "<eps>")
        self.add_edge(snode.state, fnode.state, "<eps>")

        self.start_state = self.states[snode.state]
        self.final_state = self.states[fnode.state]

    def recurse(self, nfa):

        self.merge_states(nfa)

        self.add_edge(self.start_state.state, nfa.start_state.state, "<eps>")
        self.add_edge(nfa.final_state.state, self.final_state.state, "<eps>")
        self.add_edge(nfa.final_state.state, nfa.start_state.state, "<eps>")
        self.add_edge(self.start_state.state, self.final_state.state, "<eps>")

    def merge_states(self, nfa):
        self.states.update(nfa.states)

    def add_vertex(self, state):
        self.num_vertices += 1
        node = NFANode(state)
        self.states[state] = node
        NFA.all_states.add(node)
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

    def gen_state(self):
        NFA.ix += 1
        return "S" + str(NFA.ix-1)

    def get_eps_closure(self):
        for state in self.states.keys():
            self.eps_closure[state] = set()
            
            cur = []
            vis = []
            cur.append(state)
            vis.append(state)

            while len(cur) > 0:
                cstate = cur[0]
                cur.pop(0)
                if "<eps>" in self.states[cstate].adj.keys():
                    for nstate in self.states[cstate].adj["<eps>"]:
                        if nstate not in vis:
                            vis.append(nstate)
                            cur.append(nstate)

            self.eps_closure[state] = set(vis)

#  Parsing regex
def parse_regex(expr, single=False):
        
    reg = Regex(expr)

    parsed_list = []

    cixs = reg.cunits(expr)
    ncunits = cixs[-1]  # No of concat units in the expr

    if ncunits == 1 or single:
        if expr[-1] == '*':
            # Setting for the iter operation
            parsed_list.append("ITER")
            parsed_list.append(parse_regex(expr[:-1]))
        
        elif expr[0] == '(' and expr[-1] == ')':
            # Checking for the paranthesis
            parsed_list = parse_regex(expr[1:-1], True)
        
        elif expr[0] == '[' and expr[-1] == ']':
            # Checking for the range operation
            expr = expr[1:-1]

            parsed_list.append("UNION")
            
            uixs = reg.uunits(expr)
            exprs = [""] * uixs[-1]
            for i,u in enumerate(uixs):
                exprs[u-1] += expr[i] 

            for uexp in exprs:
                if '-' in uexp:
                    s = uexp[0]
                    e = uexp[2]
                    for x in range(ord(s), ord(e)+1):
                        parsed_list.append(chr(x))
                else:
                    parsed_list.append(uexp)
        
        elif '|' in expr:
            # Checking for the union operation
            parsed_list.append("UNION")
            exprs = expr.split("|")
            for uexp in exprs:
                parsed_list.append(parse_regex(uexp, single))
        
        elif '.' in expr:
            # Checking for the dot operation
            parsed_list.append("UNION")
            for c in ALPHABETS:
                parsed_list.append(c)
        elif len(expr) > 1:
            parsed_list.append("CONCAT")
            for c in expr:
                parsed_list.append(c)                

        else:
            parsed_list.append("UNIT")
            parsed_list.append(expr)                    
                    
    else:
        exprs = [""] * ncunits
        for i,c in enumerate(cixs):
            exprs[c-1] += expr[i]

        parsed_list.append("CONCAT")
        for uexpr in exprs:
            parsed_list.append(parse_regex(uexpr))

    return parsed_list

#  Making NFA from parsed regex
def make_nfa(parsed_list):
    nfa = NFA()

    reg_type = parsed_list[0]
    parsed_list = parsed_list[1:]

    if reg_type == "CONCAT":   
        cnfas = []
        for reg in parsed_list:
            if type(reg) is list:
                cnfas.append(make_nfa(reg))
            elif type(reg) is str:
                cnfas.append(reg)

        nfa.concat(cnfas)

    elif reg_type == "ITER":
        nnfa = make_nfa(parsed_list[0])
        nfa.recurse(nnfa)
    elif reg_type == "UNION":
        for reg in parsed_list:
            if type(reg) is list:
                nfa.union(make_nfa(reg))
            else:
                nfa.add_edge(nfa.start_state.state, nfa.final_state.state, reg)
    elif reg_type == "UNIT":
        nfa.add_edge(nfa.start_state.state, nfa.final_state.state, parsed_list[0])

    return nfa

