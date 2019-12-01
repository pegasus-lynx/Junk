def wordToFeatures(sent,i):
    word = sent[i][0]
    tags = sent[i][1:-1]

    features = {
        'bias': 1.0,
        'word': word,
        # 'word[-3:]': word[-3:],
        # 'word[-2:]': word[-2:],
        'word.isdigit()': word.isdigit(),
        'postag': tags[0],
        # 'postag[:1]': tags[1],
        # 'postag[:2]': tags[2]
    }
    if i > 0:
        word1 = sent[i-1][0]
        tags1 = sent[i-1][1:-1]
        features.update({
            '-1:postag': tags1[0],
            # '-1:postag[:1]': tags1[1],
            # '-1:postag[:1]': tags1[2],
        })
    else:
        features['BOS'] = True

    if i < len(sent)-1:
        word1 = sent[i+1][0]
        tags1 = sent[i+1][1:-1]
        features.update({
            '+1:postag': tags1[0],
            # '+1:postag[:1]': tags1[1],
            # '+1:postag[:1]': tags1[2],
        })
    else:
        features['EOS'] = True

    return features    

def sentToFeatures(sent):
    return [wordToFeatures(sent,i) for i in range(len(sent))]

def sentToLabels(sent):
    return [r[-1] for r in sent]
