# CoVIRA
![Travis CI status](https://travis-ci.org/fredericokremer/covira.svg?branch=master&status=unknown)

CoVIRA (*Consensus by Voting with Iterative Re-weighting based on Agreement*) is a method
to identify weights and produce consensus predictions based on a collection of results from
predictors for multiple samples. It employs a iterative recalculations of weights based on the
weighted "agreement" between the predictors, and allows the calculation of a final prediction as well.


This algorithm was created to help on the integration of results from multiple prediction tools in a
reverse vaccinology study where no validation dataset was available for all features been inferred. Therefore,
we created a unsupervised way to estimate how accurate each predictor was for that particular case considering
that the more the results of a predictor is "confirmed" by the others, the higher it's accuracy.

## Installing 

### From PyPI

```bash
$ pip install covira
```

### From source code

```bash
$ git clone https://github.com/fredericokremer/covira
$ cd covira
$ python setup.py build
$ python setup.py install
```

## Using

```python
>>> import pandas as pd
>>> from covira import Covira
>>> df = pd.read_csv('test_data/dataset_1.csv')
>>> predictions = df.drop(['gene'], axis=1).values
>>> predictions                          # each column represents the prediction from a different tool, while each row is a different sample
array([[1, 0, 0], 
       [0, 1, 0], 
       [1, 1, 0], 
       [1, 0, 0], 
       [1, 0, 0], 
       [1, 0, 0], 
       [1, 0, 0], 
       [1, 0, 1]])
>>> covira = Covira(max_iterations=1000) # max number of iterations in the weight calculation
>>> covira.fit(predictions)              # "fit" = calculates the weights
>>> covira.predict(predictions)          # calculates the consensus prediction
array([0.1875, 0.375 , 0.5625, 0.1875, 0.1875, 0.1875, 0.1875, 0.625 ])
>>> covira.weights                       # weights calculated for each predictor
array([0.1875, 0.375 , 0.4375])
```

## Reference

Grassmann AA, Kremer FS, Dos Santos JC, Souza JD, Pinto LDS, McBride AJA. *Discovery of Novel Leptospirosis Vaccine 
Candidates Using Reverse and Structural Vaccinology*. **Front Immunol**. 2017;8:463. Published 2017 Apr 27. 
[doi:10.3389/fimmu.2017.00463](doi:10.3389/fimmu.2017.00463)
