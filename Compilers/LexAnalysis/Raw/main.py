import os
from regex import *

def match_text(text, tok):
    pass

def match(text, status):
    
    for i, tok in enumerate(PRIORITY_ORDER):
        res = match_text(text, tok):
        
        if res == 1:
            status[i] = 1
        elif res == -1:
            status[i] = -1
        
    return status


def check_matches(status):
    for flag in status:
        if flag == 0:
            return False
    return True


def analyze(raw):
    nchars = len(raw)
    ix = 0

    tokens = []

    while ix<nchars:
        
        p = ix  # Setting and inner loop for look-forward
        
        status = [0] * len(REGEX_RULES)
        status_index = [0] * len(REGEX_RULES)
        flag_eof = False

        while p<nchars:
    
            pref += raw[p]

            status = match(pref, status)

            if check_matches(status):
                for i,tok in enumerate(PRIORITY_ORDER):
                    if status[i]==1:
                        ix = p
                        tokens.append((tok, pref))
                        break
                break
            else:
                p += 1 
                continue

            flag_eof = True

        if flag_eof:
            for i,tok in enumerate(PRIORITY_ORDER):
                if status[i] == 1:
                    tokens.append((tok, raw[ix:]))
                    break

    return tokens

if __name__ == "__main__":
    
    input_file = "../source.c"

    with open(input_file,"r") as f:
        raw_content = f.read()
        # raw_content = "".join(raw_content)

    tokens = analyze(raw_content)

    for token in tokens:
        print(token[0], token[1])
        