import sys
from argparse import ArgumentParser
from knn_class import Knn
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def main(args):
    (X, y) = load_iris(return_X_y=True)
    (X_train, X_test, y_train, y_test) = train_test_split(X, y, test_size=0.2, random_state=args.rs)

    knn = Knn(k=args.k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)

    print('Score:', accuracy_score(y_test, preds))

def parse_args():
    ap = ArgumentParser()
    ap.add_argument('-k', type=int, required=True,help='KNN is required')
    ap.add_argument('-rs', type=int, required=False, default=42)
    ap.add_argument('-ts', type=float, required=False, default=0.2)
    return ap.parse_args()

if __name__  == '__main__':
    args = parse_args()
    try:
        main(args)
        sys.exit(0)
    except:
        sys.exit(1)