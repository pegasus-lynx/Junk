def wordToFeatures(sent, i, mode):
    obj = sent[i]
    word = obj['word']
    tags = obj['morph_features']

    features = {
        'word': word,
        'word_postag': obj['word_category'],
    }

    # Unigram features
    for j in range(0, 4):
        if mode & (1 << j):
            features['wf'+str(j)] = tags[j+2]
    # Morph features per word
    # 0 - Root
    # 1 - Category
    # 2 - Gender (0)
    # 3 - Number (1)
    # 4 - Person (2)
    # 5 - Case (3)

    # Root word check & same
    if mode & (1 << 4):
        features['root'] = tags[0]
        features['same?'] = (tags[0] == word)

    # Bigram features
    if i > 0:
        probj = sent[i-1]
        word1 = probj['word']
        tags1 = probj['morph_features']
        features.update({
            '-1:postag': probj['word_category'],
        })

    if i < len(sent) - 1:
        nobj = sent[i+1]
        word1 = nobj['word']
        tags1 = nobj['morph_features']
        features.update({
            '+1:postag': nobj['word_category'],
        })

    return features

def sentToFeatures(sent,mode_list):
    data = {}
    for mode in mode_list:
        data[mode] = [wordToFeatures(sent,i,mode) for i in range(len(sent))]
    return data

def sentToLabels(sent):
    return [r['chunk_category'] for r in sent]
