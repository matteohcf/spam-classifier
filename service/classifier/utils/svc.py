from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from const import Dataset

email_dataset = Dataset(csv_path='../datasets/spam_ham_dataset.csv')
X_train, y_train = email_dataset.get_training_data()
X_test, y_test = email_dataset.get_test_data()


svc = SVC(random_state=0)
svc.fit(X_train, y_train)

predictedSVC = svc.predict(X_test)
expectedSVC = y_test

confusionSVC = confusion_matrix(y_true=expectedSVC, y_pred=predictedSVC)
#print(confusionSVC)

confusion_SVC = pd.DataFrame(confusionSVC, index=range(confusionSVC.shape[0]), columns=range(confusionSVC.shape[1]))
axes = sns.heatmap(confusion_SVC, annot=True, cmap='nipy_spectral_r')
plt.xlabel('Predicted')
plt.ylabel('Real')
plt.title('Confusion Matrix')
plt.show()