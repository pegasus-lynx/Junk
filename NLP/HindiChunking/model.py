import matplotlib.pyplot as plt
plt.style.use('ggplot')

from itertools import chain

import nltk
import sklearn
import scipy.stats
from sklearn.metrics import make_scorer
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import RandomizedSearchCV

import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics

import features as features
import util as util

# Setting the training and testing data

train = util.convert("train.txt")
test = util.convert("train.txt")

train_X = [features.sentToFeatures(s) for s in train]
train_Y = [features.sentToLabels(s) for s in train]

# s

test_X = [features.sentToFeatures(s) for s in test]
test_y = [features.sentToLabels(s) for s in test]


# # Setting the model

crf = sklearn_crfsuite.CRF(algorithm="lbfgs", c1=0.1, c2=0.1, max_iterations=100, all_possible_transitions=True)
crf.fit(train_X, train_Y)

# labels = list(crf.classes_)

# print(labels)

y_pred = crf.predict(test_X)

print(metrics.flat_f1_score(test_y,y_pred,average='weighted'))

# sorted_labels = sorted(
#     labels,
#     key=lambda name: (name[1:], name[0])
# )

# print(metrics.flat_classification_report(
#     test_y, y_pred, labels=sorted_labels, digits=3
# ))