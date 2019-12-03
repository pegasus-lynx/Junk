def wordToFeatures(sent, i, mode):
    obj = sent[i]
    word = obj['word']
    tags = obj['morph_features']

    features = {
        'word': word,
        'word_postag': obj['word_category'],
    }

    # extra_features = {
    #     'word_feat5': tags[5],
    #     'word_feat2': tags[2],
    #     'word_feat3': tags[3],
    # }

    # Unigram features
    for j in range(0, 6):
        if mode & (1 << j):
            features['wf'+str(j)] = tags[j+2]
    # print(features)

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
