# Supervised and Unsupervised Machine Learning Assignment

**Name:** Lavinia Nungari

This assignment uses Python and scikit-learn to practise two class methods: Linear Regression for predicting exam scores, and K-Means for grouping customers.

## Supervised project: exam score prediction

`supervised_ml.py` learns from the supplied study-hours and exam-score examples. It asks for a number of study hours, then predicts the score using Linear Regression. The training pairs are labelled with known exam scores, so this is supervised learning.

## Unsupervised project: customer segmentation

`unsupervised_ml.py` uses the supplied monthly-spending and monthly-visits data. It scales the two features with `StandardScaler`, fits a three-cluster K-Means model, prints each customer's group, and counts the customers in each group. No group labels are provided during training.

## Set up and run

From this folder in a Windows terminal, create and activate a virtual environment:

```powershell
py -m venv --system-site-packages .venv
.\.venv\Scripts\Activate.ps1
```

Install the required packages:

```powershell
python -m pip install -r requirements.txt
```

`requirements.txt` lists the exact versions of scikit-learn and the packages it needs. On this computer those packages were already installed, so the local virtual environment reuses them instead of downloading a second copy. On a computer without them, install them with the command above.

Run the programs:

```powershell
python supervised_ml.py
python unsupervised_ml.py
```

The supervised program asks for study hours. The unsupervised program prints the cluster for each customer and the number of customers in each cluster.

## Theory questions

1. **What is supervised machine learning?** It is learning from examples that include both the input and the correct answer, so the model can estimate an answer for new input.
2. **What is unsupervised machine learning?** It looks for structure or patterns in data when the correct answers or groups have not been supplied.
3. **What is the difference between them?** Supervised learning uses known targets while training; unsupervised learning has no target column and finds patterns such as groups.
4. **Why is Linear Regression supervised?** It is trained with study hours paired with known exam scores, and learns to predict a score from hours.
5. **Why is K-Means unsupervised?** It receives customer measurements without preassigned group names and forms groups from similarities in those values.
6. **What is the difference between `fit()` and `predict()`?** `fit()` learns patterns or model settings from training data. `predict()` uses the fitted model to produce an estimate or assignment for data.
7. **Give two real-world applications of each type.** Supervised: predicting house prices from past sales, and classifying messages as spam or not spam. Unsupervised: grouping supermarket customers by shopping behaviour, and grouping news articles by similar topics.
