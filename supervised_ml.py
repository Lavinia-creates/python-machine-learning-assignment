from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Training examples: hours studied and the corresponding exam score.
X = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
y = [30, 40, 45, 55, 65, 70, 80, 85, 90, 95]

# Train the model using the examples with known scores.
model = LinearRegression()
model.fit(X, y)

# Ask for one new study-hours value and predict its exam score.
hours = int(input("Enter hours studied: "))
predicted_score = model.predict([[hours]])[0]

print(f"Predicted exam score: {predicted_score:.2f}")

# Bonus: plot the training examples, fitted line, and this prediction.
study_hours = [row[0] for row in X]
predicted_scores = model.predict(X)

plt.scatter(study_hours, y, color="steelblue", label="Actual exam scores")
plt.plot(study_hours, predicted_scores, color="darkorange", label="Linear Regression")
plt.scatter(hours, predicted_score, color="crimson", marker="x", s=80,
            label="Your prediction")
plt.xlabel("Hours studied")
plt.ylabel("Exam score")
plt.title("Study hours and exam scores")
plt.legend()
plt.tight_layout()
plt.show()
