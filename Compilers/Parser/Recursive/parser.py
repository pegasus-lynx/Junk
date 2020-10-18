import copy
from collections import Counter

class Grammar(object):
    def __init__(self, terms, non_terms, start, rules=None):
        self.terms = terms
        self.non_terms = non_terms
        self.start = start
        self.rules = rules

    def is_terminal(self,token):
        if token in self.terms:
            return True
        return False


class Parser(object):
    def __init__(self, grammar):
        self.gmr = grammar

    def parse(self, text):
        tokens = text.strip().split()
        tokens.append("$")
        match = []
        curr = 0
        term = self.gmr.start
        flag, curr, match = self.match(term, tokens, curr, match)

        return flag, match

    def match(self, head, tokens, ix, match):
        if self.gmr.is_terminal(head):
            if head == tokens[ix]:
                match_str = "Matched ({}:{})".format(head, tokens[ix])
                match.append(match_str)
                return True, ix+1, match
            else:
                return False, ix, match 
        elif head =="eps":
            match_str = "Matched ({})".format(head)
            match.append(match_str)
            return True, ix, match
        else:
            prules = self.gmr.rules[head]
            match.append("Matching ( {} --> ".format(head))
            for rule in prules:
                flag = True
                copy_ix = ix
                copy_match = copy.deepcopy(match) 
                for term in rule:
                    match.append("Rule : " + "".join(rule))
                    flag, copy_ix, copy_match = self.match(term, tokens, copy_ix, copy_match)
                    if not flag:
                        match.append("Not Matched\n")
                        break
                if flag:
                    match = copy.deepcopy(copy_match)
                    ix = copy_ix
                    break
            match.append(')')
            return flag, ix, match


if __name__ == "__main__":

    terms = ['id','+','*','(',')','$']
    non_terms = ['E','E\'','T','T\'','F']
    rules = {
        'E':[['T','E\'']],
        'E\'':[['+','T','E\''],['eps']],
        'T':[['F','T\'']],
        'T\'':[['*','F','T\''],['eps']],
        'F':[['(','E',')'],['id']]        
    }

    grammar = Grammar(terms, non_terms, "E", rules)

    parser = Parser(grammar)
    text = 'id * ( id + id ) + id'
    flag, matched = parser.parse(text)

    # Printing the matched
    if flag:
        print("Matched : ", text)
        print()
        bck_cnt = 0

        for x in matched:
            print('\t'*bck_cnt,x)
            cnt = Counter(x)
            bck_cnt += cnt['('] - cnt[')']

    else:
        print("Not Matched : ", text)