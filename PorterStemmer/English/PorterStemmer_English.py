import sys


class PorterStemmer:
    def __init__(self):

        self.word = ""
        self.last = 0
        self.cur = 0
        self.j = 0

    def cons(self, i):
        if self.word[i] in ["a", "e", "i", "o", "u"]:
            return 0
        if self.word[i] == "y":
            if i == self.cur:
                return 1
            else:
                return not self.cons(i - 1)
        return 1

    def m(self):
        """
        Measures the number of consonant sequences between k0 and j
        """
        n = 0
        i = self.cur
        while 1:
            if i > self.j:
                return n
            if not self.cons(i):
                break
            i += 1
        i += 1
        while 1:
            while 1:
                if i > self.j:
                    return n
                if self.cons(i):
                    break
                i += 1
            i += 1
            n = n + 1
            while 1:
                if i > self.j:
                    return n
                if not self.cons(i):
                    break
                i += 1
            i += 1

    def vowelinstem(self):
        for i in range(self.cur, self.j + 1):
            if not self.cons(i):
                return 1
        return 0

    def doublec(self, j):
        if j < (self.cur + 1):
            return 0
        if self.word[j] != self.word[j - 1]:
            return 0
        return self.cons(j)

    def cvc(self, i):
        if (
            i < (self.cur + 2)
            or not self.cons(i)
            or self.cons(i - 1)
            or not self.cons(i - 2)
        ):
            return 0
        ch = self.word[i]
        if ch == "w" or ch == "x" or ch == "y":
            return 0
        return 1

    def ends(self, s):
        """ends(s) is TRUE <=> k0,...k ends with the string s."""
        length = len(s)
        if s[length - 1] != self.word[self.last]:
            return 0
        if length > (self.last - self.cur + 1):
            return 0
        if self.word[self.last - length + 1 : self.last + 1] != s:
            return 0
        self.j = self.last - length
        return 1

    def setto(self, s):
        """Sets (j+1),...k to the characters in the string s, readjusting k."""
        length = len(s)
        self.word = self.word[: self.j + 1] + s + self.word[self.j + length + 1 :]
        self.last = self.j + length

    def r(self, s):
        if self.m() > 0:
            self.setto(s)

    def step1ab(self):
        """Turns terminal y to i when there is another vowel in the stem."""
        if self.word[self.last] == "s":
            if self.ends("sses"):
                self.last = self.last - 2
            elif self.ends("ies"):
                self.setto("i")
            elif self.word[self.last - 1] != "s":
                self.last = self.last - 1
        if self.ends("eed"):
            if self.m() > 0:
                self.last = self.last - 1
        elif (self.ends("ed") or self.ends("ing")) and self.vowelinstem():
            self.last = self.j
            if self.ends("at"):
                self.setto("ate")
            elif self.ends("bl"):
                self.setto("ble")
            elif self.ends("iz"):
                self.setto("ize")
            elif self.doublec(self.last):
                self.last = self.last - 1
                ch = self.word[self.last]
                if ch == "l" or ch == "s" or ch == "z":
                    self.last = self.last + 1
            elif self.m() == 1 and self.cvc(self.last):
                self.setto("e")

    def step1c(self):
        if self.ends("y") and self.vowelinstem():
            self.word = self.word[: self.last] + "i" + self.word[self.last + 1 :]

    def step2(self):
        """maps double suffixes to single ones."""
        if self.word[self.last - 1] == "a":
            if self.ends("ational"):
                self.r("ate")
            elif self.ends("tional"):
                self.r("tion")
        elif self.word[self.last - 1] == "c":
            if self.ends("enci"):
                self.r("ence")
            elif self.ends("anci"):
                self.r("ance")
        elif self.word[self.last - 1] == "e":
            if self.ends("izer"):
                self.r("ize")
        elif self.word[self.last - 1] == "l":
            if self.ends("bli"):
                self.r("ble")
            elif self.ends("alli"):
                self.r("al")
            elif self.ends("entli"):
                self.r("ent")
            elif self.ends("eli"):
                self.r("e")
            elif self.ends("ousli"):
                self.r("ous")
        elif self.word[self.last - 1] == "o":
            if self.ends("ization"):
                self.r("ize")
            elif self.ends("ation"):
                self.r("ate")
            elif self.ends("ator"):
                self.r("ate")
        elif self.word[self.last - 1] == "s":
            if self.ends("alism"):
                self.r("al")
            elif self.ends("iveness"):
                self.r("ive")
            elif self.ends("fulness"):
                self.r("ful")
            elif self.ends("ousness"):
                self.r("ous")
        elif self.word[self.last - 1] == "t":
            if self.ends("aliti"):
                self.r("al")
            elif self.ends("iviti"):
                self.r("ive")
            elif self.ends("biliti"):
                self.r("ble")
        elif self.word[self.last - 1] == "g":
            if self.ends("logi"):
                self.r("log")

    def step3(self):
        """Deals with -ic-, -full, -ness etc. similar strategy to step2."""
        if self.word[self.last] == "e":
            if self.ends("icate"):
                self.r("ic")
            elif self.ends("ative"):
                self.r("")
            elif self.ends("alize"):
                self.r("al")
        elif self.word[self.last] == "i":
            if self.ends("iciti"):
                self.r("ic")
        elif self.word[self.last] == "l":
            if self.ends("ical"):
                self.r("ic")
            elif self.ends("ful"):
                self.r("")
        elif self.word[self.last] == "s":
            if self.ends("ness"):
                self.r("")

    def step4(self):
        """Takes off -ant, -ence etc., in context <c>vcvc<v>."""
        if self.word[self.last - 1] == "a":
            if self.ends("al"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "c":
            if self.ends("ance"):
                pass
            elif self.ends("ence"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "e":
            if self.ends("er"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "i":
            if self.ends("ic"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "l":
            if self.ends("able"):
                pass
            elif self.ends("ible"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "n":
            if self.ends("ant"):
                pass
            elif self.ends("ement"):
                pass
            elif self.ends("ment"):
                pass
            elif self.ends("ent"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "o":
            if self.ends("ion") and (
                self.word[self.j] == "s" or self.word[self.j] == "t"
            ):
                pass
            elif self.ends("ou"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "s":
            if self.ends("ism"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "t":
            if self.ends("ate"):
                pass
            elif self.ends("iti"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "u":
            if self.ends("ous"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "v":
            if self.ends("ive"):
                pass
            else:
                return
        elif self.word[self.last - 1] == "z":
            if self.ends("ize"):
                pass
            else:
                return
        else:
            return
        if self.m() > 1:
            self.last = self.j

    def step5(self):
        """Removes a final -e if m() > 1, and changes -ll to -l if
        m() > 1.
        """
        self.j = self.last
        if self.word[self.last] == "e":
            a = self.m()
            if a > 1 or (a == 1 and not self.cvc(self.last - 1)):
                self.last = self.last - 1
        if self.word[self.last] == "l" and self.doublec(self.last) and self.m() > 1:
            self.last = self.last - 1

    def stem(self, p, i, j):
        self.word = p
        self.last = j
        self.cur = i
        if self.last <= self.cur + 1:
            return self.word

        self.step1ab()
        self.step1c()
        self.step2()
        self.step3()
        self.step4()
        self.step5()
        return self.word[self.cur : self.last + 1]


if __name__ == "__main__":

    data_file = open("sample.txt", "r")
    output_file = open("output.txt", "w")

    p = PorterStemmer()
    
    while 1:
        output = ""
        word = ""
        line = data_file.readline()
        if line == "":
            break
        for c in line:
            if c.isalpha():
                word += c.lower()
            else:
                if word:
                    output += p.stem(word, 0, len(word) - 1)
                    word = ""
                output += c.lower()
        
        output_file.write(output)
    
    output_file.close()
    data_file.close()