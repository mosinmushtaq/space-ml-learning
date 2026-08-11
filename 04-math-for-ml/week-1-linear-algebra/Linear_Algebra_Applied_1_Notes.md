Linear Algebra Applied 1

Instructor: Luis Serrano (DeepLearning.AI)

Date: August 10, 2026

Key Insight: Linear algebra is the mathematical foundation for finding linear relationships in data. Linear regression finds a line (or hyperplane) that best predicts output values from input features.

What is Linear Regression?
Problem Statement

Given a dataset with:

Input features (x values) — the data we know
Output values (y values) — what we want to predict

Goal: Find a linear equation that predicts y from x with minimal error.

Real-World Example: Satellite Temperature Prediction
Cloud Coverage (%)	Temperature (°C)
20	25
45	22
80	19
50	21

Question: Given cloud coverage, predict temperature.

Linear Regression Answer: Find the line that best fits these points.

The Linear Regression Equation
Simple Form (1 Feature)

For a single input feature:

y = wx + b

Where:

y = predicted output
x = input feature
w = weight (slope) — multiplies the feature
b = bias (intercept) — fixed offset

Example:

Temperature = 0.15 × CloudCoverage + 20

If cloud coverage = 50%, then Temperature = 0.15(50) + 20 = 27.5°C

General Form (Multiple Features)

For n input features:

y = w₁x₁ + w₂x₂ + w₃x₃ + ... + wₙxₙ + b

Where:

w₁, w₂, w₃, ..., wₙ = weights (one per feature)
x₁, x₂, x₃, ..., xₙ = features (input values)
b = bias (scalar constant)
y = predicted output

Example with 3 satellite features:

RadiationLevel = w₁(CloudCoverage) + w₂(Temperature) + w₃(NDVI) + b
Dataset Notation

When working with multiple data points in a dataset:

Index Notation

Each data point gets a superscript index in parentheses:

y⁽ⁱ⁾ = w₁x₁⁽ⁱ⁾ + w₂x₂⁽ⁱ⁾ + ... + wₙxₙ⁽ⁱ⁾ + b

Where:

i = which data point (1st, 2nd, 3rd, ..., m-th)
m = total number of data points in the dataset
Example Dataset Notation

For 3 data points with 2 features:

Data Point 1: y⁽¹⁾ = w₁x₁⁽¹⁾ + w₂x₂⁽¹⁾ + b
Data Point 2: y⁽²⁾ = w₁x₁⁽²⁾ + w₂x₂⁽²⁾ + b
Data Point 3: y⁽³⁾ = w₁x₁⁽³⁾ + w₂x₂⁽³⁾ + b

Real Dataset:

i	Cloud Cover (x₁)	Temperature (x₂)	Radiation (y)
1	20	25	85
2	45	22	72
3	80	19	60

Equations:

85 = w₁(20) + w₂(25) + b      (equation 1)
72 = w₁(45) + w₂(22) + b      (equation 2)
60 = w₁(80) + w₂(19) + b      (equation 3)
The Role of Linear Algebra
Why Multiple Features Need Linear Algebra

With 1 feature, we can solve by hand:

y = wx + b

With 2 features:

y = w₁x₁ + w₂x₂ + b

With 100 features (common in satellite data):

y = w₁x₁ + w₂x₂ + ... + w₁₀₀x₁₀₀ + b

Solution: Represent this as matrix equation:

y = Xw + b

Where:

X = matrix of all features (m rows = data points, n columns = features)
w = vector of weights
b = scalar bias

Linear algebra tells us how to solve this efficiently for thousands of features and millions of data points.

Key Concepts Summary
1. Weights (w)
What: Numbers that scale/multiply each feature
How many: One per feature
Purpose: Determine the importance/impact of each feature
Example: If w₁ = 0.5 and w₂ = 0.01, then Feature 1 matters much more than Feature 2
2. Features (x)
What: Input data we measure
Example: Cloud coverage, temperature, NDVI
Role: Variables we use to predict the output
Dataset representation: Each row is a data point, each column is a feature
3. Bias (b)
What: A fixed offset added to the equation
Purpose: Allows the line to shift up or down
Example: Even if all features are zero, y ≠ 0 if b ≠ 0
Not fixed: We find the best b during training
4. Output (y)
What: What we're trying to predict
For each data point: We have an actual y and a predicted y
Goal: Make predicted y as close to actual y as possible
The Learning Process
Step 1: Initialize Weights and Bias

Start with random or zero values for w and b.

python
w = [0, 0, 0]  # Random weights for 3 features
b = 0          # Zero bias
Step 2: Make Predictions

For each data point, calculate predicted y using the equation:

y_predicted = w₁x₁ + w₂x₂ + w₃x₃ + b
Step 3: Calculate Error

Compare predicted y to actual y:

error = actual_y - predicted_y
Step 4: Update Weights and Bias

Adjust w and b to reduce error (we'll learn HOW in the Calculus section).

Step 5: Repeat

Iterate until predictions are good enough.

Visual Understanding
1D Regression (1 Feature)
y
│     ●  ← actual data points
│   ●    ●
│ ●        ●
│─────────────── x
│ ↑ best-fit line y = wx + b

Goal: Find the line that passes through (or near) all points.

2D Regression (2 Features)
      y
      │
    ● │   ●
  ●   │
    ● │
──────┼────── x₁
      │
    x₂

Goal: Find a plane (in 3D) that best fits the points.

n-D Regression (n Features)

For n features, we're finding a hyperplane in (n+1)-dimensional space.

Too complex to visualize, but the math is the same — linear algebra handles it.

Matrix Representation

Instead of writing out all equations, use matrices:

Compact Form
y = Xw + b
Expanded Form
⎡ y⁽¹⁾ ⎤   ⎡ x₁⁽¹⁾  x₂⁽¹⁾  ...  xₙ⁽¹⁾ ⎤   ⎡ w₁ ⎤
⎢ y⁽²⁾ ⎥ = ⎢ x₁⁽²⁾  x₂⁽²⁾  ...  xₙ⁽²⁾ ⎥ × ⎢ w₂ ⎥ + b
⎢  ⋮  ⎥   ⎢  ⋮     ⋮    ⋱   ⋮    ⎥   ⎢ ⋮  ⎥
⎣ y⁽ᵐ⁾ ⎦   ⎣ x₁⁽ᵐ⁾  x₂⁽ᵐ⁾  ...  xₙ⁽ᵐ⁾ ⎦   ⎣ wₙ ⎦

(m×1)  =  (m×n)  ×  (n×1)  + (scalar)

Where:

m = number of data points
n = number of features

This is why linear algebra matters: it lets us solve for w efficiently, even when m and n are huge (thousands or millions).

Why This Matters for Machine Learning
Linear Regression as Foundation

Linear regression is the simplest ML algorithm, but:

All neural networks use this equation in each layer
Gradient descent (which we'll learn in Calculus) uses this to optimize
Understanding this teaches the fundamentals for all ML
Real Satellite Example

Predict radiation levels from:

Cloud coverage (%)
Temperature (°C)
NDVI (vegetation index)
Atmospheric pressure (hPa)
Humidity (%)

Without linear algebra: We'd have to solve 100+ simultaneous equations by hand (impossible).

With linear algebra: Matrix operations solve it in milliseconds, even for millions of data points.

Key Terminology
Term	Meaning
Feature	Input variable (x)
Weight	Coefficient that scales a feature (w)
Bias	Fixed offset (b)
Prediction	Output of the equation (ŷ)
Target	Actual value we want to predict (y)
Hyperplane	The line/plane/surface our equation defines
Linear Relationship	Straight-line relationship between x and y
Regression	Predicting continuous values (not categories)
Common Misconceptions (Clarified)
Misconception 1: "Weights are slopes"

Truth: In 1D, weight IS the slope. In n-D, weights are the coordinates of a normal vector to the hyperplane, not slopes.

Misconception 2: "Bias is fixed"

Truth: Bias is initially unknown and must be learned during training, just like weights.

Misconception 3: "Linear algebra only helps with big problems"

Truth: Linear algebra provides the FRAMEWORK for solving ANY regression problem. Even simple 2-feature problems benefit from matrix notation.

Misconception 4: "The superscript (i) means powers"

Truth: The superscript (i) in x⁽ⁱ⁾ is an INDEX, not an exponent. It means "the i-th data point."
