import warnings
from itertools import chain
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
import sklearn
import sklearn_crfsuite
from sklearn.exceptions import UndefinedMetricWarning
from sklearn.metrics import make_scorer
from sklearn.model_selection import train_test_split, ShuffleSplit, learning_curve, RandomizedSearchCV
from sklearn_crfsuite import metrics, scorers

import features as features
import util as util
import analysis as analysis

plt.style.use('ggplot')
warnings.filterwarnings("ignore", category=UndefinedMetricWarning)

def plot_learning_curve(estimator, title, X, y, ylim=None, cv=None,
                        n_jobs=None, train_sizes=np.linspace(.1, 1.0, 5)):
    plt.figure()
    plt.title(title)
    if ylim is not None:
        plt.ylim(*ylim)
    plt.xlabel("Training examples")
    plt.ylabel("Score")
    train_sizes, train_scores, test_scores = learning_curve(
        estimator, X, y, cv=cv, n_jobs=n_jobs, train_sizes=train_sizes)
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)
    test_scores_mean = np.mean(test_scores, axis=1)
    test_scores_std = np.std(test_scores, axis=1)
    plt.grid()

    plt.fill_between(train_sizes, train_scores_mean - train_scores_std,
                     train_scores_mean + train_scores_std, alpha=0.1,
                     color="r")
    plt.fill_between(train_sizes, test_scores_mean - test_scores_std,
                     test_scores_mean + test_scores_std, alpha=0.1, color="g")
    plt.plot(train_sizes, train_scores_mean, 'o-', color="r",
             label="Training score")
    plt.plot(train_sizes, test_scores_mean, 'o-', color="g",
             label="Cross-validation score")

    plt.legend(loc="best")
    return plt

def count_and_print_errors(n, f=None, seq=None):
    cnt = 0
    if seq is not None:
        cor_seq = {}
        wrg_seq = {}
    for i, s_true_y in enumerate(test_y):
        if cnt == n:
            break
        s_pred_y = pred_y[i]
        s_x = zipped_test_x[i]
        for j, true_y in enumerate(s_true_y):
            if cnt == n:
                break
            x = s_x[j]
            pred_y = s_pred_y[j]
            if true_y != pred_y:
                cnt += 1
                if f:
                    print(" ".join([w['word'] for w in s_x]), file=f)
                    print([w['word_postag'] for w in s_x], file=f)
                    print([w for w in s_pred_y], file=f)
                    print([w for w in s_true_y], file=f)
                    print('\n', file=f)
                if seq is not None and '-1:postag' in x:
                    key = f'{x["-1:postag"]}-{x["word_postag"]}'
                    wrg_seq[key] = wrg_seq.setdefault(key, 0) + 1
            elif seq is not None and '-1:postag' in x:
                key = f'{x["-1:postag"]}-{x["word_postag"]}'
                cor_seq[key] = cor_seq.setdefault(key, 0) + 1
    if seq is not None:
        keys = set(cor_seq.keys()) | set(wrg_seq.keys())
        for key in keys:
            seq[key] = cor_seq.get(key, 0) / (cor_seq.get(key, 0) + wrg_seq.get(key, 0))
    return cnt

def find_best_hyperparameters(estimator, data_x, data_y, labels):
    # use the same metric for evaluation
    f1_scorer = make_scorer(metrics.flat_f1_score, average='weighted', labels=labels)

    # Searching in params_space for best results
    params_space = {
        'c1': scipy.stats.expon(scale=0.5),
        'c2': scipy.stats.expon(scale=0.05),
    }
    rs = RandomizedSearchCV(estimator, params_space, cv=3, n_jobs=4, n_iter=50, scoring=f1_scorer)
    rs.fit(data_x, data_y)
    print('best params:', rs.best_params_)
    print('best CV score:', rs.best_score_)
    print('model size: {:0.2f}M'.format(rs.best_estimator_.size_ / 1000000))
    return rs.best_estimator_


# This is for deciding on what features we need to do our analysis =================================================================

MODE_LIST = [0]
# MODE_LIST = [0, 1, 2, 3, 8, 11, 16, 24]
## Mode Bits
# 0 - Gender
# 1 - Number
# 2 - Person
# 3 - Case
# 4 - Root Word & Whether same

# ==================================================================================================================================

# Loading Data =====================================================================================================================

print('Loading data...')
data = util.convertFromSSF('data_clean.txt')
print(f'# of sentences = {len(data)}')
data_x = [features.sentToFeatures(s, MODE_LIST) for s in data]
data_y = [features.sentToLabels(s) for s in data]

# ==================================================================================================================================


# Setting the training and testing data ============================================================================================

print('Splitting data at 70%:30%...')
train_X, test_X, train_Y, test_y = train_test_split(data_x, data_y, test_size=0.3, random_state=123)

# ==================================================================================================================================

# Finding classification labels ====================================================================================================

labels = set(chain(*data_y))
sorted_labels = sorted(
    labels,
    key=lambda name: (name[1:], name[0])
)

# ==================================================================================================================================


# Setting the model
# c1 and c2 parameter values are obtained from randomized search in hyperparameters space
# Best estimated F1 score = 0.9745285762169615

# Setting the model ================================================================================================================

crf = sklearn_crfsuite.CRF(algorithm="lbfgs", c1=0.2096570893088954, c2=0.038587807344039826, max_iterations=50, all_possible_transitions=True)

# ==================================================================================================================================



# Working for each mode seperately ================================================================================================

for mode in MODE_LIST:

    ## Getting data specific to the mode ==========================================================================================

    zipped_train_x = [s[mode] for s in train_X]
    zipped_test_x = [s[mode] for s in test_X]
    # plot_learning_curve(crf, f'Learning curve for MODE {mode}', [s[mode] for s in train_X], train_Y, ylim=(0.7, 1.01), cv=cv, n_jobs=6)
    # plt.show()

    ## ============================================================================================================================
    
    ## Fitting the data and Predcting results =====================================================================================

    print('Fitting the model for MODE (' + str(mode) + ') ...')
    crf.fit(zipped_train_x, train_Y)
    # print('Predicting labels...')
    pred_y = crf.predict(zipped_test_x)

    ## ============================================================================================================================

    ## Error Analysis 

    ### POS Level Analysis ========================================================================================================

    # print('F1 score: ', metrics.flat_f1_score(test_y, pred_y, average='weighted'))

    # print(metrics.flat_classification_report(
    #     test_y, pred_y, labels=sorted_labels, digits=3
    # ))

    ### ============================================================================================================================
    
    ### Word/Chunk Level Analysis ==================================================================================================

    seqCorrect = analysis.getChnkSeqCorr(test_y)
    seqPredicted = analysis.getChnkSeqPred(test_y, pred_y)

    errs = analysis.check(seqCorrect, seqPredicted)

    with open("chnk_len_unmatch.txt", "w") as file:
        file.write(errs)

    # analysis.analyzeChnkSeqTags(seqCorrect, seqPredicted)
    # analysis.analyzeChnkSeqBoundaries(seqCorrect, seqPredicted)

    ### ============================================================================================================================

    ### Sentence Level Analysis ====================================================================================================

    # seq = {}
    # itms = seq.items()
    # print(f'# of Errors = {count_and_print_errors(-1, seq=seq)}')
    # for j in (1.0, 0.9, 0.8, 0.7, 0.6, 0.5):
    #     print(f'# of Sequence-level combinations with accuracy < {j} = {len(dict(filter(lambda e: e[1] < j, itms)))}')
    # print('Sequence-level combinations with accuracy < 0.4', dict(filter(lambda e: e[1] < 0.4, itms)))
    # print()

    ### ============================================================================================================================

    ## ============================================================================================================================
