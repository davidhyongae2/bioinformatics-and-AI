import statistics
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
#havent compared to AI.
#manually parse your sentence for structure or use your favorite NLP.
#need to use numpy 1.26.4
language_fragment = ['subject + verb', 'he runs','subject+verb+object', 'he runs the meeting', 'subject+verb+complement','she is happy','subject+verb+indirectobject+directobject','he made me a pie']

if __name__ == "__main__":
	even_words = []
	odd_words = []
	total = []
	for i in range(len(language_fragment)):
		total.append(i)
		if i % 2 == 0:
			even_words.append(language_fragment[i])
		else:
			odd_words.append(language_fragment[i])
	print(even_words, odd_words)
	print(total)

#perform statistics of your language_fragment
#AI generated code.
# Gemini 2.5 pro, Google, Dec 2023,  https://gemini.google.com/.
# Mean
mean_value = statistics.mean(total)
print(f"Mean: {mean_value}")

# Median
median_value = statistics.median(total)
print(f"Median: {median_value}")

# Mode (can return multiple modes if they exist)
try:
    mode_value = statistics.mode(total)
    print(f"Mode: {mode_value}")
except statistics.StatisticsError:
    print("No unique mode found.")

# Standard Deviation
st_dev = statistics.stdev(total)
print(f"Standard Deviation: {st_dev}")

# Variance
variance = statistics.variance(total)
print(f"Variance: {variance}")
#AI generated code
# Gemini 2.5 pro, Google, Dec 2023,  https://gemini.google.com/.

# Sample language_fragment (features and target)
features_list = [[1], [2], [3], [4], [5]]
target_list = [2, 4, 5, 4, 5]

# Convert lists to NumPy arrays
X = np.array(features_list)
y = np.array(target_list)

# Split language_fragment into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train a simple Linear Regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions
predictions = model.predict(X_test)
print(f"Predictions: {predictions}")

# Evaluate the model
mse = mean_squared_error(y_test, predictions)
print(f"Mean Squared Error: {mse}")

#run language into Canva or squarespace to generate HTML program.
#embred data into generative AI
