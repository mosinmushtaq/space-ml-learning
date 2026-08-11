Lecture: 3D Linear Equations and Plane Intersections

Instructor: Luis Serrano (DeepLearning.AI)

Context: Just as 2D linear equations represent lines and their intersections give solutions, 3D linear equations represent planes and their intersections determine solution sets.

Linear Equations in 3D: Planes
From 2D to 3D

In 2D: A linear equation with two variables represents a line.

2a + 3b = 6  ← Line in 2D plane

In 3D: A linear equation with three variables represents a plane in space.

3a - 5b + 2c = 6  ← Plane in 3D space
Planes Through the Origin
Special Case: Constant = 0

When the constant term equals 0, the plane passes through the origin (0, 0, 0).

Example:

3a - 5b + 2c = 0

Why? If we substitute a = 0, b = 0, c = 0:

3(0) - 5(0) + 2(0) = 0 ✓

The point (0, 0, 0) satisfies the equation, so the plane must pass through the origin.

Systems of 3 Equations: Plane Intersections
How Planes Intersect

Just as lines intersect to give points as solutions:

Two planes intersect → intersection is a line
Three planes intersect → intersection is typically a point (or a line, or empty)
System 1: Non-Singular System (Unique Solution)

Equations:

a + b + c = 0       ← Plane 1
a + 2b + c = 0      ← Plane 2
a + b + 2c = 0      ← Plane 3

Geometric interpretation:

Plane 1 passes through origin (0, 0, 0)
Plane 2 passes through origin (0, 0, 0)
Plane 1 and Plane 2 intersect at a line
Plane 3 also passes through origin (0, 0, 0)
All three planes intersect at a single point: (0, 0, 0)

Solution: The system has a unique solution: a = 0, b = 0, c = 0

Classification: Non-singular system — exactly one solution

System 2: Singular System (Infinite Solutions - A Line)

Equations:

a + b + c = 0       ← Plane 1
a + 2b + c = 0      ← Plane 2
a + b + 2c = 0      ← Plane 3

Geometric interpretation:

Plane 1 passes through origin (0, 0, 0)
Plane 2 passes through origin (0, 0, 0)
Planes 1 and 2 intersect at a line
Plane 3 also passes through origin (0, 0, 0)
Plane 3 intersects Planes 1 and 2, but crosses them at the SAME line
All three planes share a common line

Solution: The system has infinite solutions — every point on a line

Classification: Singular system — infinite solutions (underdetermined)

System 3: Singular System (Infinite Solutions - A Plane)

Equations:

a + b + c = 0           ← Plane 1
2a + 2b + 2c = 0        ← Plane 2
3a + 3b + 3c = 0        ← Plane 3

Why it's singular:

Plane 2 equation = 2 × Plane 1 equation
Plane 3 equation = 3 × Plane 1 equation
All three equations represent the SAME plane

Geometric interpretation:

Plane 1 passes through origin
Plane 2 is the exact same plane (just scaled by 2)
Plane 3 is the exact same plane (just scaled by 3)
Three identical planes overlapping completely

Solution: The system has infinite solutions — every point on the plane

Classification: Singular system — infinite solutions (all points on a plane)

Summary: Three Cases
System Type	Geometric Picture	Solution Set	Classification
System 1	Three planes meet at one point	Single point (0,0,0)	Non-singular
System 2	Three planes meet at one line	Entire line	Singular
System 3	Three identical planes (overlapped)	Entire plane	Singular
Key Concepts
Non-Singular vs Singular

Non-singular system:

Each equation brings independent information
No redundancies
Unique solution exists

Singular system:

Some equations are redundant (multiples of each other)
Or they're linearly dependent
Infinite solutions (line or plane) or no solutions
Visualization Challenge

Luis notes: These 3D visualizations are hard to render in 2D, so we focus on understanding which type of intersection occurs rather than perfect visual representation.

Why This Matters

Understanding plane intersections prepares us for:

Solving larger systems (4D, 5D, n-dimensional)
Matrix rank — detecting redundancy
Solution existence — when solutions exist and what form they take
Linear independence — which equations are truly independent
Next Steps
Determinants: Measure whether a system has unique solution
Matrix rank: Detect redundant equations automatically
Gaussian elimination: Algorithm to solve these systems