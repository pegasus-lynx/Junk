# #! /usr/bin/env python3.1

class HindiStemmer:
    
    # prefixes = [ "अन", "अध","सम", "स्व", "वि", "अव","सु", "कु", "नि", "उत", "उन", "उप", "अप", "निस्‌", "निर्‌", "दुस्‌", "दुर्‌", "उत्", "उद्‌", "अति", "प्रति", "अधि", "निस", "परा","परि", "दुर", "अनु", "अभि"]
    
    suffixes = {
        1: ["ो", "े", "ू", "ु", "ी", "ि", "ा"],
        2: ["ाव", "कर", "ाओ", "िए", "ाई", "ाए", "ने", "नी", "ना", "ते", "ीं", "ती", "ता", "ाँ", "ां", "ों", "ें"],
        3: ["ाकर", "ाइए", "ाईं", "ाया", "ेगी", "ेगा", "ोगी", "ोगे", "ाने", "ाना", "ाते", "ाती", "ाता", "तीं", "ाओं", "ाएं", "ुओं", "ुएं", "ुआं"],
        4: ["ाएगी", "ाएगा", "ाओगी", "ाओगे", "एंगी", "ेंगी", "एंगे", "ेंगे", "ूंगी", "ूंगा", "ातीं", "नाओं", "नाएं", "ताओं", "ताएं", "ियाँ", "ियों", "ियां"],
        5: ["ाएंगी", "ाएंगे", "ाऊंगी", "ाऊंगा", "ाइयाँ", "ाइयों", "ाइयां"],
    }

    matras = ["ो", "े", "ू", "ु", "ी", "ि", "ा", "्"]
    vowels = [ "अ", "आ", "इ", "ई", "ए",  "उ", "ऊ", "ओ" ]

    def __init__(self):
        self.raw_text = []
        self.stemmed_text = []
        self.prefixes.sort()


    def add_line(self, text):
        self.raw_text.append(text)
        self.stemmed_text.append( self._stem_line(text) )

    def add_text(self, text):
        self.raw_text.append(text)
        self.stemmed_text.append( self._process(text) )

    def output(self):
        return self.stemmed_text

    def write_to_file(self, file):
        for line in self.stemmed_text:
            file.write(line)

    def _process(self, text):
        lines = text.split("।")
        processed_text = []
        for line in lines:
            if len(line) > 0:
                processed_text.append(self._stem_line(line))
        self.stemmed_text.append(processed_text)

    def _stem_line(self, line):
        if len(line) <= 1:
            return ""
        stemmed_line = ""
        for word in line.split():
            stemmed_line += self._stem_word(word)
            stemmed_line += " "
        stemmed_line += "।"
        stemmed_line += "\n"
        return stemmed_line

    def _stem_word(self, r_word):
        ss_word = self._stem_suffixes(r_word)
        # word = self._stem_prefixes(ss_word)
        return ss_word

    # def _stem_prefixes(self, word):
    #     for pref in self.prefixes:
    #         if word.startswith(pref) and self._measure(word) > self._measure(pref) +1:
    #             temp = word[len(pref):]
    #             # if temp[0] in self.matras:
    #             #     return temp[1:]
    #             while temp[0] in self.matras:
    #                 temp = temp[1:]
    #             return temp
    #     return word

    def _stem_suffixes(self, word):
        for L in 5, 4, 3, 2, 1:
            if len(word) > L + 1:
                for suf in self.suffixes[L]:
                    if word.endswith(suf):
                        return word[:-L]
        return word

    def _measure(self, word):
        x = 0
        for c in word:
            if c in self.vowels:
                x += 1
        return len(word)-x

if __name__ == '__main__':

# Reading the file
    data_file = open("sample.txt", "r")
    output_file = open("output.txt", "w")

    hs = HindiStemmer()

    for line in data_file:
        if len(line) > 0: 
            hs.add_line(line)

    hs.write_to_file(output_file)

    data_file.close()
    output_file.close()
