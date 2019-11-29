import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import confusion_matrix
from sklearn.metrics import precision_recall_fscore_support
from sklearn.utils.multiclass import unique_labels




def stat_summary(label,classes,class_count):
    separator = ":"
    print()
    print()
    print (label + " Decision")
    print(" ".join([classes[0],separator,str(class_count[0])]))
    print(" ".join([classes[1],separator,str(class_count[1])]))
    print(" ".join([classes[2],separator,str(class_count[2])]))
    print(" ".join(["Total",separator,str(class_count[0]+class_count[1]+class_count[2])]))


 


def print_metrics(ground_truth, predicted, param_beta, classes):
    cm = confusion_matrix(ground_truth,predicted, labels=classes)
    ##Precession =1 for beta 0 vs Recall(infinity)
#     prf = precision_recall_fscore_support(ground_truth, predicted, beta=param_beta, average=None)
#     prf = precision_recall_fscore_support(ground_truth, predicted, beta=param_beta, average="weighted",warn_for=tuple())
    prf = precision_recall_fscore_support(ground_truth, predicted, beta=param_beta, average=None,warn_for=tuple())
    print(f'Precision, Recall, F-{param_beta} Score :')
#     print(prf)
#     print(f"Precision    :  {round(prf[0][2],4)}")
#     print(f"Recall       :  {round(prf[1][2],4)}")
#     print(f"F-score      :  {round(prf[2][2],4)}")
      print(f"Precision    :  {round(prf[0][1],4)}")
      print(f"Recall       :  {round(prf[1][1],4)}")
#       print(f"F-score      :  {round(prf[2][1],4)}")


def plot_confusion_matrix(ground_truth,predicted,ground_truth_label,predicted_label,classes,cmap,Normalize=False,title="Bencharking Score"):
    class_count = []
#     class_count = [ground_truth.count('Yes'),ground_truth.count('Maybe'),ground_truth.count('No')]
    class_count = [ground_truth.count(classes[0]),ground_truth.count(classes[1]),ground_truth.count(classes[2])]
    stat_summary(ground_truth_label,classes,class_count)
    print()
    class_count = [predicted.count('Yes'),predicted.count('Maybe'),predicted.count('No')]
#     class_count = [predicted.count(classes[0]),predicted.count(classes[1]),predicted.count(classes[2])]
    stat_summary(predicted_label,classes,class_count)

    if  Normalize:
        title = 'Normalized ' + title

    # Compute confusion matrix
    # C_{i, j} is equal to the number of observations known to be in group i but predicted to be in group j
    cm = confusion_matrix(ground_truth,predicted,classes)
    # to get the percentages for each class (often called specificity and sensitivity in binary classification) 
    # you need to normalize by row: each element in a row divided by the sum of the elements of that row.
    if Normalize:
        # find out how many samples per class have received their correct label
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
          
    
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation='nearest', cmap=cmap)
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(xticks=np.arange(cm.shape[1]),
        yticks=np.arange(cm.shape[0]),
        xticklabels=classes,
        yticklabels=classes,
        title=title,
        ylabel=ground_truth_label,
        xlabel=predicted_label)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right",rotation_mode="anchor")
    # Loop over data dimensions and create text anNotations.
    fmt = '.2f' if Normalize else 'd'
    # cm is the confusion array
    thresh = cm.max() / 2.
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(j, i, format(cm[i, j], fmt),
              ha="center", va="center",
              color="white" if cm[i, j] > thresh else "black")
    fig.tight_layout()
    return ax

   


"""
####################
# main 
####################
ground_truth= ['Yes','Yes','Yes','Yes','Maybe','Yes','Maybe','Yes','Maybe','No'] # y_true
predicted = ['Yes','No','Yes','Maybe','Yes','Yes','Yes','No','No','Yes'] # y_pred
classes = ["Yes","Maybe","No"]


param_beta = 1
print_metrics(ground_truth, predicted,param_beta,classes)

param_beta = 0.05
print_metrics(ground_truth,predicted,param_beta,classes)

plot_confusion_matrix(ground_truth,predicted,"OCV","Experian",classes,plt.cm.PuBuGn,True)
plt.ylim([2.5,-.5]) 
plt.show()
"""

###########
###########
###########
###########
###########
###########
###########


import confusion

# param_beta = 1
# confusion.print_metrics(ground_truth, predicted,param_beta,classes)

# param_beta = 0.05
# confusion.print_metrics(ground_truth,predicted,param_beta,classes)

# confusion.plot_confusion_matrix(ground_truth,predicted,"yaxis","xaxis",classes,plt.cm.PuBuGn,True)
confusion.plot_confusion_matrix(ground_truth,predicted,"yaxis","xaxis",classes,plt.cm.PuBuGn)
plt.ylim([2.5,-.5]) 
plt.show()


###############

import numpy as np
np.unique(result.me)

########
result['me'] = result['me'].apply(lambda x: 'Yes' if x == 'Maybe' else x)

#########
import confusion

param_beta = 1
confusion.print_metrics(ground_truth, predicted,param_beta,classes)

param_beta = 0.05
confusion.print_metrics(ground_truth,predicted,param_beta,classes)

# confusion.plot_confusion_matrix(ground_truth,predicted,"yaxis","xaxis",classes,plt.cm.PuBuGn,True)
confusion.plot_confusion_matrix(ground_truth,predicted,"yaxis","xaxis",classes,plt.cm.PuBuGn)
plt.ylim([2.5,-.5]) 
plt.show()

################
ground_truth = result['me'].tolist()
predicted = result['you'].tolist()
classes = ["Yes","Maybe","No"]
##############
pair = ['Yes','Yes','Yes','Yes','Maybe','Yes','Maybe','Yes','Maybe','Yes'] 
singleton = ['No','No','No','No','No','No','No','No','No','No'] 
experian = ['No','No','Yes','No','Yes','Yes','Yes','No','No','Yes'] 

# pairdf = pd.DataFrame([pair,experian])
# singletondf = pd.DataFrame([singleton,experian])

a = pd.Series(pair)
b = pd.Series(singleton)
c = pd.Series(experian)
f1=[a,b]
f2=[b,c]
ab = pd.concat(f1,axis=1)
bc = pd.concat(f2,axis=1)
ab.rename(columns={0: "me",1:"you"},inplace=True)
bc.rename(columns={0: "me",1:"you"},inplace=True)
result=ab.append(bc)
result.reset_index(inplace=True)

#####################

