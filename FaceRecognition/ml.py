from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

digits = load_digits()
    
def prediction():
        
    # Randomly split data into 70% training and 30% test
    X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=.30)
    
    # Train a kNN model using the training set
    clf_KNN = KNeighborsClassifier()
    clf_KNN.fit(X_train, y_train)
    
    # Predictions using the kNN model on the test set
    print("Predicting labels of the test data set - %i random samples" % (len(X_test)))
    result = clf_KNN.predict(X_test)
    
    return str(accuracy_score(y_test, result))