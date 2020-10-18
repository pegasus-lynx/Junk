import os
from sregex import *

ALPHABETS = [ 
                'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
                'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
                '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '=',
                '+', '-', '*', '/', '{', '}', '_', '#', '<eps>', '"', "'"  
            ]

REGEX_RULES = {
    "NUM" : "[0-9][0-9]*",
    "KEY" : "(if|else|int|main|void|return)",
    "IDENTIFIER"  : "[a-zA-z_][a-zA-Z0-9_]*",
    "STRING" : "['\"].*['\"]",
    "PREPROCESS" : "#.*\n"
}

TOK_ORDER = [ "KEY", "IDENTIFIER", "NUM", "PREPROCESS", "STRING"]


def match_text(text, nfa):
    curr = nfa.eps_closure[nfa.start_state.state]
    # print("Start:", curr, "Text", text)
    # print('-'*80)

    for c in text:
        transition = False
        # print("Current Char :", c)

        ncurr = set()
        for state in curr:
            # print(state, nfa.states[state].adj)
            if c in nfa.states[state].adj.keys():
                transition = True
                for nstate in nfa.states[state].adj[c]:
                    ncurr = ncurr | nfa.eps_closure[nstate]

        curr = ncurr
        if not transition:
            return -1

    if nfa.final_state.state in curr:
        return 1

    return 0

def match(text, nfas):
    
    status = [0] * len(TOK_ORDER)

    for i, tok in enumerate(TOK_ORDER):
        res = match_text(text, nfas[tok])
        if res == 1:
            status[i] = 1
        elif res == -1:
            status[i] = -1

    # print(status)
    # print()    

    return status

def all_neg(status):
    for flag in status:
        if flag == 1 or flag == 0:
            return False
    return True

def analyze(raw, nfas):
    nchars = len(raw)
    ix = 0

    tokens = []
    pref = ""

    status = [1] * len(TOK_ORDER)
    # true_index = [0] * len(REGEX_RULES)

    while ix<nchars:

        nstatus = match(pref+raw[ix], nfas)

        # print(pref+raw[ix], status, nstatus)

        if all_neg(nstatus):
            
            if pref == "":
                ix += 1
                continue

            for i,tok in enumerate(TOK_ORDER):
                if status[i] == 1:
                    tokens.append((tok, pref))
                    break    
            
            pref = ""
            status = [1] * len(REGEX_RULES)
            continue
        else:
            pref += raw[ix]
            status = nstatus      

        ix += 1


    if pref != "":
        for i,tok in enumerate(TOK_ORDER):
            if status[i] == 1:
                tokens.append((tok, pref))
                break

    return tokens

if __name__ == "__main__":

    # Making NFAs from the Regex Expressions
    nfas = {}
    for tok in TOK_ORDER:
        nfas[tok] = make_nfa(parse_regex(REGEX_RULES[tok]))
        nfas[tok].get_eps_closure()

        # if tok == "NUM":
        #     print(tok, nfas[tok].start_state.state, nfas[tok].final_state.state)
        #     print('-'*30)
        #     for state, node in nfas[tok].states.items():
        #         print(state)
        #         print(node.adj)
        #         print(nfas[tok].eps_closure[state])
        #         print()
        

    # File to be scanned
    input_file = "../source.c"

    # Reading the file to be scanned
    with open(input_file,"r") as f:
        raw_content = f.read()

    # Analyzes the text as running stream and
    # return the list of tokens after lexical analysis

    print(raw_content)

    tokens = analyze(raw_content, nfas)

    # Printing the tokens obtained on lexical analysis
    print("Tokens")
    for token in tokens:
        print(token[0], token[1])
        
    # r = Regex(REGEX_RULES["KEY"])
    # print(r.expr)

    # parsed_list = parse_regex(r.expr)
    # print(parsed_list)

    # nfa = make_nfa(parsed_list)
    
    # for state, node in nfa.states.items():
    #     print(state, node.adj)

    # print("Start State : ", nfa.start_state.state)
    # print("Final State : ", nfa.final_state.state)
    