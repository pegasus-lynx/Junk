import re

def convert(file_name):
    data = []
    row = []

    with open(file_name, 'r') as file:
        for cnt, line in enumerate(file):
            # print(line)

            flag=True
            if len(line)<5:
                data.append(row)
                row = []
                flag=False
                
            if flag:
                row.append(line.split())

    return data


def convertFromSSF(file_name):
    res = []
    with open(file_name, 'r') as f:
        line = []
        chunk_cat = 'UNK'
        flag = False
        ign_pat = re.compile(r'(^<Sentence)|(\s*\)\))')
        mop_pat = re.compile(r'^<fs.*af=\'(.*)\'')
        for i, ln in enumerate(f):
            splt = ln.split(maxsplit=3)
            if not splt:
                continue
            # print(splt)
            if re.match('^</Sentence', ln):
                line = []
                res.append(line)
            elif re.match('.*\(\(', ln):
                chunk_cat = splt[2] if len(splt) > 2 else 'O'
                flag = True
            elif not ign_pat.match(ln):
                ftr = {
                    'word': splt[1],
                    'word_category': splt[2],
                    'chunk_category': f'{"B" if flag else "I"}-{chunk_cat}',
                }
                flag = False
                mtchs = mop_pat.match(splt[-1])
                if mtchs:
                    morph_features = mtchs.group(1).split(',')
                    ftr['morph_features'] = [(w or 'UNK') for w in morph_features]
                    line.append(ftr)
                else:
                    ftr['morph_features'] = []
    return res
