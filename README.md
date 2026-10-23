# Supervised and Unsupervised Machine Learning Assignment

**Name:** Lavinia Nungari

This project applies the two methods taught in class: Linear Regression to predict student exam scores and K-Means to group customers by shopping behaviour. It uses the assignment datasets and scikit-learn. Matplotlib is used for the two bonus graphs.

## Supervised project: student exam score prediction

`supervised_ml.py` prepares the supplied study-hours and exam-scores as Python lists, trains a Linear Regression model with `fit()`, asks the user for study hours, and predicts an exam score with `predict()`. It prints the predicted score to two decimal places. The training scores are known labels, so this is supervised learning.

The handout's output is an example; the program calculates its own result from the supplied training data. For 6 hours, this dataset gives a prediction of about 69.18.

## Unsupervised project: customer segmentation

`unsupervised_ml.py` uses the supplied monthly spending and shopping visit data. It scales both features with `StandardScaler`, trains K-Means with three clusters, `random_state=42`, and `n_init=10`, prints the cluster assigned to every customer, and counts the customers in each group. No correct group labels are provided to the model, so this is unsupervised learning. Cluster numbers can vary between implementations.

## Bonus graphs

Both scripts also use Matplotlib. The supervised graph shows the example scores, the fitted regression line, and the entered prediction. The unsupervised graph plots spending against visits and colours each customer by its K-Means cluster.

## Set up and run

From this folder in a Windows terminal, create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Install the listed dependencies and run the programs:

```powershell
python -m pip install -r requirements.txt
python supervised_ml.py
python unsupervised_ml.py
```

The supervised program asks for study hours. The unsupervised program prints the group and group counts. Each program then opens its bonus graph.

## Theory questions

1. **What is supervised machine learning?** It is learning from examples that include both the input and the correct answer, so the model can estimate an answer for new input.
2. **What is unsupervised machine learning?** It looks for structure or patterns in data when the correct answers or groups have not been supplied.
3. **What is the difference between them?** Supervised learning uses known targets while training; unsupervised learning has no target column and finds patterns such as groups.
4. **Why is Linear Regression supervised?** It is trained with study hours paired with known exam scores and learns to predict a score from hours.
5. **Why is K-Means unsupervised?** It receives customer measurements without preassigned group names and forms groups from similarities in those values.
6. **What is the difference between `fit()` and `predict()`?** `fit()` learns model settings from training data. `predict()` uses the fitted model to produce a prediction or cluster assignment.
7. **Give two real-world applications of each type.** Supervised: predicting house prices from past sales and classifying messages as spam or not spam. Unsupervised: grouping supermarket customers by shopping behaviour and grouping news articles by similar topics.
