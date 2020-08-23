import pandas as pd
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from covira import Covira

def test_covira_dataset_1():
    predictions = pd.read_csv('test_data/dataset_1.csv').drop(['gene'], axis=1).values
    covira = Covira()
    covira.fit(predictions)
    print(covira.predict(predictions))

def test_covira_dataset_2():
    predictions = pd.read_csv('test_data/dataset_2.csv').drop(['gene'], axis=1).values
    covira = Covira()
    covira.fit(predictions)
    print(covira.predict(predictions))