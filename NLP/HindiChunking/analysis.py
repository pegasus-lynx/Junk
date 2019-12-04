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


def check(seqCorrect, seqPredicted):
    cnt = 0
    errs = ""
    for i in range(len(seqCorrect)):
        if len(seqCorrect[i]) != len(seqPredicted[i]):
            lc = len(seqCorrect[i])
            lp = len(seqPredicted[i])

            for w in seqPredicted[i]:
                if w[0][-1]=='^':
                    lp-=1
            
            if(lc!=lp):
                cnt += 1
                errs += str(seqCorrect[i]) + "\n" + str(seqPredicted[i]) +"\n\n"

    print(cnt)    
    return errs