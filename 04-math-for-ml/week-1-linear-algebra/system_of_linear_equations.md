Systems of Linear Equations

Instructor: Luis Serrano (DeepLearning.AI)

Context: Building on linear regression, we now learn how to solve systems of equations using linear algebra.

What is a System of Linear Equations?

A system of linear equations is a collection of linear equations that we solve together. Each equation has the same variables but different coefficients and constants.

Simple Example

Given 3 equations with 3 unknowns (a, b, c):

a + b = 6
a + 2b = 16
a + b + 2c = 12

Goal: Find values for a, b, and c that satisfy ALL equations simultaneously.

Solving Systems: From Multiple Equations to Matrix Form
Step 1: Write Out All Equations

For a system with m equations and n unknowns:

w₁x₁ + b = y⁽¹⁾
w₁x₂ + b = y⁽²⁾
w₁x₃ + b = y⁽³⁾
...
w₁xₘ + b = y⁽ᵐ⁾
Step 2: Convert to Matrix Form

Instead of writing each equation, use matrix notation:

Aw = y

Where:

A = coefficient matrix (m × n)
w = unknown weights vector (n × 1)
y = result vector (m × 1)
Example: 3 Equations, 2 Unknowns
Equation 1: 1a + 1b = 10
Equation 2: 2a + 1b = 12
Equation 3: 1a + 2b = 15

Matrix Form:

⎡ 1  1 ⎤   ⎡ a ⎤   ⎡ 10 ⎤
⎢ 2  1 ⎥ × ⎢ b ⎥ = ⎢ 12 ⎥
⎣ 1  2 ⎦   ⎣   ⎦   ⎣ 15 ⎦

A          w           y
Why This Matters
From Linear Regression to Systems

In linear regression, we have:

m data points (rows)
n features (columns)
1 unknown weights vector

We're solving: Xw + b = y

This is one system of linear equations with many equations (one per data point).

Why We Need Linear Algebra

For one or two unknowns: We can solve by hand.

For 100 unknowns (100 features): We need linear algebra to:

Represent the system compactly
Solve it efficiently
Check if solutions exist
Types of Solutions
Case 1: Unique Solution

When: The system has exactly one answer.

Example:

a + b = 10
a - b = 2

Solution: a = 6, b = 4 (unique and deterministic)

Graphically: Two lines intersect at ONE point.

Case 2: Infinite Solutions (Redundant Equations)

When: One equation is a multiple of another — they contain the same information.

Example:

a + b = 10
2a + 2b = 20  ← This is just 2× the first equation

What happens: The second equation adds no new information.

Graphically: Two identical lines (overlap completely).

Implication: Any point on the line satisfies both equations.

Case 3: No Solution (Contradictory Equations)

When: Equations contradict each other.

Example:

a + b = 10
a + b = 15  ← Same left side, different results

What happens: Impossible to find values that satisfy both.

Graphically: Parallel lines that never intersect.

Complete System vs Incomplete System
Complete System (Full Rank)

Definition: Every equation brings unique information.

Characteristics:

No redundancies
No contradictions
Each data point constrains the solution

Result: Typically a unique solution.

For ML: Means we have enough data to determine weights.

Incomplete System (Rank Deficiency)

Definition: Some equations are redundant or contradictory.

Two types:

1. Redundant equations (underdetermined):

Some equations repeat information
We have fewer constraints than unknowns
Result: Multiple solutions possible

2. Contradictory equations (overdetermined):

Equations contradict each other
No solution exists that satisfies all
Result: We find the "best fit" instead