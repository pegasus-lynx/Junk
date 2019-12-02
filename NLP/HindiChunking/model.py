import matplotlib.pyplot as plt
plt.style.use('ggplot')

from itertools import chain

import sklearn
import scipy.stats
from sklearn.metrics import make_scorer
from sklearn.model_selection import train_test_split

import sklearn_crfsuite
from sklearn_crfsuite import scorers
from sklearn_crfsuite import metrics

import features as features
import util as util

# Setting the training and testing data

# train = util.convertFromSSF("training_wx.txt")
# test = util.convertFromSSF("testing_wx.txt")

print('Loading data...')

data = util.convertFromSSF('data_clean.txt')
print(f'# of sentences = {len(data)}')
data_x = [features.sentToFeatures(s) for s in data]
data_y = [features.sentToLabels(s) for s in data]


print('Splitting data at 70%:30%...')
train_X, test_X, train_Y, test_y = train_test_split(data_x, data_y, test_size=0.3, random_state=123)

# train_X = [features.sentToFeatures(s) for s in train]
# train_Y = [features.sentToLabels(s) for s in train]

# test_X = [features.sentToFeatures(s) for s in test]
# test_y = [features.sentToLabels(s) for s in test]

# # Setting the model

crf = sklearn_crfsuite.CRF(algorithm="lbfgs", c1=0.1, c2=0.1, max_iterations=100, all_possible_transitions=True)

print('Fitting the model...')
crf.fit(train_X, train_Y)

# labels = list(crf.classes_)

# print(labels)

print('Predicting labels...')
y_pred = crf.predict(test_X)

print('F1 score: ')
print(metrics.flat_f1_score(test_y,y_pred,average='weighted'))

# sorted_labels = sorted(
#     labels,
#     key=lambda name: (name[1:], name[0])
# )

# print(metrics.flat_classification_report(
#     test_y, y_pred, labels=sorted_labels, digits=3
# ))