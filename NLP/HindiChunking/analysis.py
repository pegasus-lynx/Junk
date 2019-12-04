import re

def sGetChnkSeq(cSeq,pSeq):
    chnkSeq = []

    l = len(cSeq)

    for i in range(l):
        if pSeq[i][0] == 'B':
            if cSeq[i][2:] == pSeq[i][2:] and cSeq[i][0] == 'I':
                chnkSeq.append((pSeq[i][2:]+'^',i))
            else:
                chnkSeq.append((pSeq[i][2:],i))
        elif cSeq[i][0] == 'B' and cSeq[i][2:]==pSeq[i][2:]:
            # if i>0 and cSeq[i-1] == pSeq[i-1]:
            chnkSeq.append((pSeq[i][2:]+'*',i))

    return chnkSeq


def getChnkSeqCorr(data_y):
    seqs = []
    for s in data_y:
        seq = []
        for i in range(len(s)):
            if s[i][0]=='B':
                seq.append( ( s[i][2:], i) )
        seqs.append(seq)
    return seqs

def getChnkSeqPred(data_y, pred_y):
    seqs = []
    for i in range(len(data_y)):
        corr_seq = data_y[i]
        corr_pred = pred_y[i]
        seqs.append(sGetChnkSeq(corr_seq,corr_pred))
    return seqs

# def getChnkSeq(data_y, pred_y = None):
#     seqs = []
#     for i in range(len(data_y)):
#         seqs.append(getStChnkSeq(data_y[i], None if pred_y == None else pred_y[i]))
#     return seqs

# def getStChnkSeq(cSeq,pSeq):
#     chnkSeq = []
#     l = len(cSeq)
#     for i in range(l):
#         if pSeq == None:
#             if cSeq[i] == 'B':
#                 chnkSeq.append(cSeq[i][2:])
#         else:
#             if pSeq[i][0] == 'B':
#                 if cSeq[i][2:] == pSeq[i][2:] and cSeq[i][0] == 'I':
#                     chnkSeq.append(pSeq[i][2:]+'^')
#                 else:
#                     chnkSeq.append(pSeq[i][2:])
#             elif cSeq[i][0] == 'B' and cSeq[i][2:]==pSeq[i][2:]:
#                 chnkSeq.append(pSeq[i][2:]+'*')

#     return chnkSeq            

def checkCorrectStLabelLength(cSeq,pSeq):
    if len(pSeq) != len(cSeq):

        lp = len(pSeq)
        lc = len(cSeq)

        for w in pSeq:
            if w[0][-1]=='^':
                lp-=1

        if lp!=lc:
            return False

    return True


def checkCorrectLabelling(seqCorrect, seqPredicted):
    cnt = 0
    errs = ""
    for i in range(len(seqCorrect)):
        if not checkCorrectStLabelLength(seqCorrect[i],seqPredicted[i]):
            cnt += 1
            errs += str(seqCorrect[i]) + "\n" + str(seqPredicted[i]) +"\n\n"

    print("Number of sentences wrongly labelled : " + str(cnt))    
    return errs

def analyzeErrLabelling(file_name):
    pass

def makeEmptyDict(chunk_labels):
    freq = {}
    for a in chunk_labels:
        freq[a] = {}
        for b in chunk_labels:
            freq[a][b] = 0
    return freq

def addDictToDict(freq_a, freq_b, chunk_labels):
    freq = makeEmptyDict(chunk_labels)

    for a in chunk_labels:
        for b in chunk_labels:
            freq[a][b] = freq_a[a][b] + freq_b[a][b]

    return freq

# def analyzeChnkTag(chunk_labels, seqCorrect, seqPredicted, ind):
#     posn = seqPredicted[ind][1]
#     freq = makeEmptyDict(chunk_labels)
#     i=0
#     while seqCorrect[i][1] < posn:
#         i+=1

#     if seqCorrect[i][1] == seqPredicted[i][1]:
#         if seqCorrect[i][0] == seqPredicted[i][0]:
#             pass
#         elif seqCorrect[i][0] == seqPredicted[i][0][:-1]
#             pass
#         else:
#             pass
#     else:
#         pass

def getIndCorrSeq(cSeq, pSeq, ind):
    posn = pSeq[ind][1]
    i=0
    while cSeq[i][1] < posn:
        i+=1

    if cSeq[i][1] == pSeq[ind][1]:
        return i
    
    return -1

def analyzeChnkTagSeq(seqCorrect, seqPredicted, chunk_labels):

    freq_pred = makeEmptyDict(chunk_labels)
    freq_corr = makeEmptyDict(chunk_labels)

    for i in range(len(seqCorrect)):
        
        cSeq = seqCorrect[i]
        pSeq = seqPredicted[i]

        for p in range(1, len(pSeq)):
            ind = getIndCorrSeq(cSeq, pSeq, p)
            if ind == -1:
                if pSeq[p][0][-1] == '^':
                    curTag = pSeq[p][0][:-1]

                    prevTag = pSeq[p-1][0]
                    if prevTag[-1] == '*' or prevTag[-1] == '^':
                        prevTag = prevTag[:-1]

                    freq_pred[prevTag][curTag] += 1
            else:
                if pSeq[p][0][-1] == '*':
                    pass
                else:
                    curTag = pSeq[p][0]

                    prevTag = pSeq[p-1][0]
                    if prevTag[-1] == '*' or prevTag[-1] == '^':
                        prevTag = prevTag[:-1]

                    freq_pred[prevTag][curTag] += 1

        for p in range(1,len(cSeq)):
            freq_corr[cSeq[p-1][0]][cSeq[p][0]] += 1

        return [freq_pred, freq_corr]
            
def makeEmptyBndDict(chunk_labels):
    freq = {}

    for chnk in chunk_labels:
        freq[chnk] = 0

    return freq

def analyzeChnkBoundaries(seqCorrect, seqPredicted, chunk_labels):
    
    bndSkipped = makeEmptyBndDict(chunk_labels)
    bndExtras = makeEmptyBndDict(chunk_labels)
    bndPred = makeEmptyBndDict(chunk_labels)
    bndCorr = makeEmptyBndDict(chunk_labels)

    for i in range(len(seqCorrect)):

        cSeq = seqCorrect[i]
        pSeq = seqPredicted[i]

        for p in range(len(cSeq)):
            bndCorr[cSeq[p][0]] +=1

        for p in range(len(pSeq)):
            t = pSeq[p][0][-1]
            c = pSeq[p][0][:-1]
            if t == '*':
                bndSkipped[c] += 1
            elif t == '^':
                bndExtras[c] += 1
                bndPred[c] += 1
            else:
                bndPred[pSeq[p][0]] += 1

    return [bndPred, bndSkipped, bndExtras, bndCorr]