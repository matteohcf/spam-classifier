from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import Perceptron
from const import Dataset

email_dataset = Dataset(csv_path='../datasets/spam_ham_dataset.csv')
X_train, y_train = email_dataset.get_training_data()

estimators = {
    'KNN': KNeighborsClassifier(),
    'SVM': SVC(probability=True),
    'DecisionTree': DecisionTreeClassifier(),
    'RandomForestClassifier': RandomForestClassifier(n_estimators=10),
    'Perceptron': Perceptron()
}

for estimator_name, estimator in estimators.items():
    kfold = KFold(n_splits=10, random_state=11, shuffle=True)
    scores = cross_val_score(estimator=estimator, X=X_train, y=y_train, cv=kfold)
    print(f'{estimator_name} accuracy: {scores.mean():.2%} '+ f' - Standard Deviation: {scores.std():.2%}')

