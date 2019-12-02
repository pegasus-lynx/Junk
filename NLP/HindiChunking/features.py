def wordToFeatures(sent, i):
    obj = sent[i]
    word = obj['word']
    tags = obj['morph_features']

    features = {
        'word': word,
        # 'chunk_postag': obj['chunk_category'],
        'word_postag': obj['word_category'],
        'word_feat5': tags[5],
        'word_feat2': tags[2],
        'word_feat3': tags[3],
    }
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

def sentToFeatures(sent):
    return [wordToFeatures(sent,i) for i in range(len(sent))]

def sentToLabels(sent):
    return [r['chunk_category'] for r in sent]
