from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression

""" we have supervised learning and unsupervised learning

    Machine learning: the model learn the relationship between data and response

    Requirements for working with scikit-learn
        1. features and response are separate objects
        2. features and response are numeric
        3. features and resoinse should be NUMPY array
        4. features and response should have specific shapes

    Supervised Learning:
        • Classification    : response is categorical, predicted results are in a finite ordered sets (spam or ham email, iris flower type)
        • Regression        : response is order and continuous (price of house, height of person)

    store feature matrix in x, and reponse matrix in y
        _ x = iris.data
        _ y = iris.target

    Training a Machine Learning model:
        KNN (K-nearest neigbors): pick a k value, search for k observations of in the trained model that are nearest to the unknown data
                                    pick the most popular response

    4 steps modelling patter:
        1. import
        2. instantiate
        3. fit
        4. predict

"""

if __name__ == '__main__':

    # iris = datasets.load_iris()
    # print(iris.target)
    # print(iris.target.shape)
    # print(iris.target_names)
    # print(type(iris.target))
    # print(iris.feature_names)
    # print(iris.data)
    # print(iris.data.shape)


    """ KNN """
    iris = datasets.load_iris()

    x = iris.data
    y = iris.target

    knn = KNeighborsClassifier(n_neighbors=5)

    # KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski',
    #        metric_params=None, n_jobs=1, n_neighbors=1, p=2,
    #        weights='uniform')


    knn.fit(x,y)

    result = knn.predict([[5.8, 3, 5.1, 1.9]])

    print("result for KNN is:",result)



    # """ LogisticRegression """
    #
    # LR = LogisticRegression()
    #
    # LR.fit(x,y)
    #
    # LR.predict([[5.8, 3, 5.1, 1.9]])
    #
    # print("result for LogisticRegression is:",result)
