from sklearn.linear_model import LinearRegression

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
