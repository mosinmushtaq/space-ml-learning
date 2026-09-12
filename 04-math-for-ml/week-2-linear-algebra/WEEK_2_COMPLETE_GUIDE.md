# WEEK 2: SOLVING SYSTEMS OF LINEAR EQUATIONS — COMPLETE GUIDE

---

## TABLE OF CONTENTS
1. [Part A: Foundations](#part-a-foundations)
2. [Part B: Row Operations & Gaussian Elimination](#part-b-row-operations--gaussian-elimination)
3. [Part C: Non-Singular Systems](#part-c-non-singular-systems)
4. [Part D: Singular Systems](#part-d-singular-systems)
5. [Part E: Matrix Row Reduction (REF)](#part-e-matrix-row-reduction-ref)
6. [Part F: Rank of a Matrix](#part-f-rank-of-a-matrix)
7. [Part G: Reduced Row Echelon Form (RREF)](#part-g-reduced-row-echelon-form-rref)
8. [Part H: Complete Gaussian Elimination Pipeline](#part-h-complete-gaussian-elimination-pipeline)
9. [Part I: ML Applications & Debugging](#part-i-ml-applications--debugging)

---

# PART A: FOUNDATIONS

## Why Solve Systems of Equations?

**Context:** Neural networks, regression models, and optimization problems reduce to solving systems of linear equations.

**Real-world example:** 
- Neural network training = finding weights that satisfy multiple constraints simultaneously
- Linear regression = solving (X^T X)β = X^T y
- Computer graphics = transforming 3D coordinates through linear systems

**Question:** Given constraints (equations), find values (variables) that satisfy all of them.

---

## What is a System of Linear Equations?

**Definition:** A set of m equations with n unknowns.

**Example (2×2):**
```
a + b = 10          ... (equation 1)
a + 2b = 12         ... (equation 2)
```

**Goal:** Find values of a and b that make both equations true simultaneously.

---

## Solution Types (Preview)

| Type | Equations | Example | Meaning |
|------|-----------|---------|---------|
| **Unique** | Non-singular | a=8, b=2 | Exactly one solution exists |
| **Infinite** | Singular, redundant | a + b = 10 (only 1 independent equation) | Infinitely many (a,b) pairs work |
| **None** | Singular, contradictory | 0 = 2 (impossible) | No solution satisfies all equations |

---

# PART B: ROW OPERATIONS & GAUSSIAN ELIMINATION

## Row Operations (Allowed Manipulations)

**These operations preserve the solution set:**

1. **Swap rows** — Reorder equations (order doesn't affect solution)
2. **Multiply row by non-zero scalar** — Scale an equation (e.g., 2x + 3y = 5 becomes x + 1.5y = 2.5)
3. **Add/subtract multiple of one row to another** — Combine equations to eliminate variables

**Critical rule:** Whatever operation you perform, apply it to **the entire row including constants**.

---

## Elimination Method (Equation Approach)

**Step 1:** Divide to make one coefficient = 1 (simplifies elimination)

```
Equation 1: 5a + b = 17      Divide by 5 → a + 0.2b = 3.4
Equation 2: 4a - 3b = 6
```

**Step 2:** Subtract to eliminate variable

```
Equation 2 - Eq1:  (4a - 3b = 6) - (a + 0.2b = 3.4)
                  = 3a - 3.2b = 2.6
Wait, this is wrong. Correct:
Eq1: a + 0.2b = 3.4
Eq2: 4a - 3b = 6  → Divide by 4 → a - 0.75b = 1.5
Eq2 - Eq1: (a - 0.75b) - (a + 0.2b) = 1.5 - 3.4
          0a - 0.95b = -1.9
          b = 2
```

**Step 3:** Back-substitute to find other variables

```
a + 0.2(2) = 3.4
a = 3
```

**Solution:** a = 3, b = 2 ✓

---

# PART C: NON-SINGULAR SYSTEMS

## Definition

**Non-singular system:** Has **exactly one unique solution**.

**Matrix property:** det ≠ 0 (determinant is non-zero)

**Row-reduction property:** All rows are linearly independent (no row is a combination of others)

---

## Example: 2×2 Non-Singular

```
System:            Matrix:           Augmented:
5a + b = 17        [5,  1]          [5,  1 | 17]
4a - 3b = 6        [4, -3]          [4, -3 | 6]
```

**Check for singularity:**
```
det = (5)(-3) - (1)(4) = -15 - 4 = -19 ≠ 0  → Non-singular ✓
```

**Unique solution exists:** a = 3, b = 2

---

## Example: 3×3 Non-Singular

```
System:
a + b + 2c = 12
3a - 3b - c = 3
2a - b + 6c = 24

Matrix:
[1,  1,  2]
[3, -3, -1]
[2, -1,  6]

det ≠ 0 → Unique solution exists
```

---

## Quiz Example

**Solve:**
```
2a + 5b = 46
8a + b = 32
```

**Solution:** a = 3, b = 8

---

# PART D: SINGULAR SYSTEMS

## Definition

**Singular system:** Matrix has det = 0, rows are linearly dependent.

**Two outcomes:**
1. **Redundant:** Infinitely many solutions (free variables exist)
2. **Contradictory:** No solutions (impossible constraint)

---

## Case 1: Redundant (Infinite Solutions)

**Example:**
```
System:
a + b = 10
2a + 2b = 20

Row 2 = 2 × Row 1 → Linearly dependent
```

**Elimination:**
```
Divide Eq1 by 1: a + b = 10
Divide Eq2 by 2: a + b = 10

Subtract: 0 = 0 ✓ (Always true)
```

**Result:** One independent constraint (a + b = 10), **one degree of freedom**.

**Infinite solutions:** Any a and b where a + b = 10
- Example: (a, b) = (3, 7), (5, 5), (10, 0), etc.
- **Parametric form:** a = x, b = 10 - x (where x is any real number)

---

## Case 2: Contradictory (No Solutions)

**Example:**
```
System:
a + b = 10
2a + 2b = 24

Divide Eq1 by 1: a + b = 10
Divide Eq2 by 2: a + b = 12
```

**Elimination:**
```
Subtract: (a + b) - (a + b) = 12 - 10
          0 = 2  ✗ IMPOSSIBLE
```

**Result:** No values of (a, b) satisfy both equations simultaneously. **No solution.**

---

## How to Identify in Matrix Form

When you reach a row of zeros in coefficients:

**Check the constant:**

| Coefficient row | Constant | Result |
|-----------------|----------|--------|
| [0, 0, 0, ..., 0] | **0** | Redundant → Infinite solutions |
| [0, 0, 0, ..., 0] | **≠ 0** | Contradictory → No solution |

---

# PART E: MATRIX ROW REDUCTION (REF)

## Augmented Matrix

**Definition:** Combines coefficient matrix + constants column, separated by vertical bar.

**Example:**
```
System:           Augmented Matrix:
5a + b = 17       [5,  1 | 17]
4a - 3b = 6       [4, -3 | 6]
```

**Critical:** Constants travel with all row operations. If you forget the constants column, you lose information and can't solve the system.

---

## Row Echelon Form (REF) Definition

**Three properties:**

1. **Zero rows at the bottom** — All rows containing only zeros come after all non-zero rows
2. **Each non-zero row has a pivot** — Leftmost non-zero entry in each row
3. **Staircase pattern** — Each pivot is strictly to the right of all pivots above it

**Visual:**
```
✓ REF:                          ✗ NOT REF:
[2,  *,  *,  * ]               [1,  2,  3]
[0,  3,  *,  * ]               [0,  0,  4]  ← pivot in col 2
[0,  0,  5,  * ]               [0,  1,  0]  ← pivot in col 1 (should be to the right)
[0,  0,  0,  7 ]
[0,  0,  0,  0 ]  ← zero rows at bottom

Pivots: 2, 3, 5, 7
Staircase: 2 (col 0) → 3 (col 1) → 5 (col 2) → 7 (col 3)
```

---

## Key Rule: Diagonal Pattern

**In REF, reading the diagonal left to right:**

Once you hit a **zero on the diagonal, all diagonal entries to its right must also be zero**.

```
Diagonal [non-zero, non-zero, zero, zero, zero]  ✓ Valid REF
Diagonal [1, 0, 2]  ✗ Invalid (non-zero after zero)
Diagonal [2, 3, 4]  ✓ Valid (all non-zero)
Diagonal [1, 0, 0]  ✓ Valid (zeros at end)
```

---

## 2×2 Algorithm to REF

**Starting matrix:**
```
[a, b | c]
[d, e | f]
```

**Step 1:** Make [0,0] = 1 (divide R1 by a)
```
[1, b/a | c/a]
[d, e   | f]
```

**Step 2:** Make [1,0] = 0 (do R2 - d×R1)
```
[1,      b/a    | c/a]
[0, e - d(b/a)  | f - d(c/a)]
```

**Step 3 (optional but standard):** Make [1,1] = 1 (divide R2 by its pivot)
```
[1,  b/a  | c/a]
[0,   1   | f']
```

**Result:** REF achieved (zeros below diagonal, staircase pattern)

---

## 2×2 Example

**Starting:**
```
[2,  3 | 7]
[1,  4 | 5]
```

**R1 ÷ 2:**
```
[1,  1.5 | 3.5]
[1,  4   | 5]
```

**R2 - 1×R1:**
```
[1,  1.5 | 3.5]
[0,  2.5 | 1.5]
```

**R2 ÷ 2.5:**
```
[1,  1.5 | 3.5]
[0,  1   | 0.6]
```

**REF achieved** ✓

---

## 3×3 Algorithm to REF

**Two phases:**

**Phase 1: Eliminate below column 1 pivot**

- Make [0,0] = 1 (divide R1 by its value)
- Make [1,0] = 0 (R2 - (a21/a11)×R1)
- Make [2,0] = 0 (R3 - (a31/a11)×R1)

**Phase 2: Eliminate below column 2 pivot**

- Make [1,1] = 1 (divide R2 by its value)
- Make [2,1] = 0 (R3 - (a32/a22)×R2)

**Result:** Staircase pattern with all zeros below diagonal

---

## 3×3 Example

**Starting:**
```
[1,  1,  2 | 12]
[3, -3, -1 | 3]
[2, -1,  6 | 24]
```

**Phase 1:**

R2 - 3×R1:
```
[1,  1,  2 | 12]
[0, -6, -7 | -33]
[2, -1,  6 | 24]
```

R3 - 2×R1:
```
[1,  1,  2 | 12]
[0, -6, -7 | -33]
[0, -3,  2 | 0]
```

**Phase 2:**

R2 ÷ (-6):
```
[1,  1,  2  | 12]
[0,  1,  7/6| 5.5]
[0, -3,  2  | 0]
```

R3 - (-3)×R2 = R3 + 3×R2:
```
[1,  1,  2  | 12]
[0,  1,  7/6| 5.5]
[0,  0,  5.5| 16.5]
```

R3 ÷ 5.5:
```
[1,  1,  2  | 12]
[0,  1,  7/6| 5.5]
[0,  0,  1  | 3]
```

**REF achieved** ✓ (Staircase: pivots at col 0 → col 1 → col 2)

---

## Critical Mistake to Avoid

**Your mistake (Week 2):**
```
Matrix: [1, -1/2,  1/2]
        [0,    1,    3]
        [0,    0,    2]

Diagonal: [1, 1, 2]  ✓ Looks like REF
But not a pivot in [2,1] needs to be 0!
```

**The problem:** Column 2 has a pivot in row 1 (1/2) and row 2 (3), which violates the staircase rule. You stopped too early — needed to eliminate the 3 below the 1.

**Correct:**
```
R3 - 2×R2 to get [0, 0, -4]
Then R3 ÷ (-4) to get [0, 0, 1]
```

---

# PART F: RANK OF A MATRIX

## Definition

**Rank:** The number of **pivots** in REF (equivalently, the number of **non-zero rows** in REF).

```
REF:
[1,  1,  2 | 12]   ← Pivot 1 in column 0
[0,  1,  7/6| 5.5] ← Pivot 1 in column 1
[0,  0,  1  | 3]   ← Pivot 1 in column 2

Rank = 3 (three pivots)
```

---

## Rank and Solution Type

**For m×n augmented matrix (m rows, n coefficient columns):**

| Rank | Outcome |
|------|---------|
| Rank = n | Unique solution (all n variables determined) |
| Rank < n | Infinite solutions (n - rank free variables) |
| Rank < n **and** constant violation | No solution |

---

## Examples

**Example 1: Rank = 3, n = 3 → Unique solution**
```
[1,  1,  2 | 12]
[0,  1,  7/6| 5.5]
[0,  0,  1  | 3]
Rank = 3, all 3 variables determined → unique solution
```

**Example 2: Rank = 2, n = 3 → Infinite solutions**
```
[1,  1,  1 | 5]
[0,  1,  2 | 3]
[0,  0,  0 | 0]
Rank = 2, but n = 3 → one free variable → infinite solutions
```

**Example 3: Rank = 2, n = 3, contradictory → No solution**
```
[1,  1,  1 | 5]
[0,  1,  2 | 3]
[0,  0,  0 | 1]  ← Says 0 = 1 (impossible)
Rank < n but constant is non-zero → no solution
```

---

## Singular vs. Non-Singular (In Terms of Rank)

| Property | Non-Singular | Singular |
|----------|--------------|----------|
| Rank | Rank = n (all columns pivot) | Rank < n (some columns free) |
| det | det ≠ 0 | det = 0 |
| Rows | Linearly independent | Linearly dependent |
| Solution | Unique | Infinite or none |
| REF | All diagonal non-zero | Some diagonal zero |

---

# PART G: REDUCED ROW ECHELON FORM (RREF)

## Definition

RREF = REF + two additional conditions:

1. **Each pivot = 1** — Every leading entry in a row must be 1
2. **Zeros above pivots** — All entries **above** each pivot are 0

**Combined:** Identity-like structure (may have free variable columns between identity columns)

---

## Why RREF Matters

**REF:** Multiple valid REFs per matrix. Still requires back-substitution.

**RREF:** Exactly one RREF per matrix. **Solution reads directly from constants column — no back-substitution needed.**

**Example:**

REF (still needs work):
```
[1, 2, 3 | 5]
[0, 1, 4 | 6]
```
Read: 1a + 2b + 3c = 5, 1b + 4c = 6
Back-substitute: From second, b = 6 - 4c, substitute into first, etc.

RREF (solution is obvious):
```
[1, 0, -5 | -7]
[0, 1,  4 |  6]
```
Read directly: a - 5c = -7 → a = -7 + 5c
                b + 4c = 6 → b = 6 - 4c
No more work needed.

---

## Algorithm: REF → RREF (Two Phases)

**Phase 1: Make all pivots = 1**

For each non-zero row in REF, divide that row by its pivot value.

**Phase 2: Eliminate above each pivot** (bottom to top)

For each pivot, use row operations to make all entries **above** that pivot equal to 0.

---

## 2×2 Example: REF → RREF

**Starting REF:**
```
[2,  3 | 7]
[0, -5 | 10]
```

**Phase 1: Make pivots = 1**

R1 ÷ 2:
```
[1,  1.5 | 3.5]
[0, -5   | 10]
```

R2 ÷ (-5):
```
[1, 1.5 | 3.5]
[0,  1  | -2]
```

**Phase 2: Eliminate above pivots** (start from bottom pivot)

Bottom pivot: column 1 (value 1), entry above is 1.5

R1 - 1.5×R2:
```
[1, 0 | 6]
[0, 1 | -2]
```

**RREF achieved** ✓

**Solution:** x = 6, y = -2 (read directly from constants column)

---

## 3×3 Example: REF → RREF

**Starting REF:**
```
[1,  1,  2 | 12]
[0,  1, 7/6| 5.5]
[0,  0,  1 | 3]
```

**Phase 1: Make pivots = 1**

Row 1 already has pivot 1 ✓
Row 2 already has pivot 1 ✓
Row 3 already has pivot 1 ✓

**Phase 2: Eliminate above pivots** (bottom to top)

**Step 1:** Bottom pivot in column 2 (value 1), eliminate above in rows 1 and 2

R2 - (7/6)×R3:
```
[1,  1,  2 | 12]
[0,  1,  0 | 1]
[0,  0,  1 | 3]
```

R1 - 2×R3:
```
[1,  1,  0 | 6]
[0,  1,  0 | 1]
[0,  0,  1 | 3]
```

**Step 2:** Middle pivot in column 1 (value 1), eliminate above in row 1

R1 - 1×R2:
```
[1,  0,  0 | 5]
[0,  1,  0 | 1]
[0,  0,  1 | 3]
```

**RREF achieved** ✓ (Identity matrix + constants)

**Solution:** a = 5, b = 1, c = 3 (read directly from constants)

---

## Your Example (Correct)

**Starting REF:**
```
[1, 2, 3]
[0, 1, 4]
[0, 0, 1]
```

**Phase 1:** All pivots are already 1 ✓

**Phase 2:** Eliminate above (bottom to top)

R2 - 4×R3: (eliminate the 4 above the 1 in column 2)
```
[1, 2, 0]
[0, 1, 0]
[0, 0, 1]
```

R1 - 2×R2: (eliminate the 2 above the 1 in column 1)
```
[1, 0, 0]
[0, 1, 0]
[0, 0, 1]
```

**RREF achieved** ✓ (Identity matrix)

**You got it 100% correct!**

---

# PART H: COMPLETE GAUSSIAN ELIMINATION PIPELINE

## Full Algorithm

**Input:** System of equations
**Output:** Solution (unique, infinite, or none)

---

## Step 1: Build Augmented Matrix

**System:**
```
3a + 2b - c = 8
a - b + 2c = 1
2a + 3b + c = 7
```

**Augmented matrix:**
```
[3,  2, -1 | 8]
[1, -1,  2 | 1]
[2,  3,  1 | 7]
```

---

## Step 2: Forward Elimination (→ REF)

**Goal:** Transform to REF using row operations.

**For each pivot:**
1. Make pivot = 1
2. Make all entries **below** pivot = 0

**Pivot 1 (column 0):**

R1 ÷ 3:
```
[1,  2/3, -1/3 | 8/3]
[1,   -1,    2 | 1]
[2,    3,    1 | 7]
```

R2 - 1×R1:
```
[1,  2/3, -1/3 | 8/3]
[0, -5/3,  7/3 | -5/3]
[2,    3,    1 | 7]
```

R3 - 2×R1:
```
[1,  2/3, -1/3 | 8/3]
[0, -5/3,  7/3 | -5/3]
[0,  5/3,  5/3 | 5/3]
```

**Pivot 2 (column 1):**

R2 ÷ (-5/3):
```
[1,  2/3, -1/3 | 8/3]
[0,    1, -7/5 | 1]
[0,  5/3,  5/3 | 5/3]
```

R3 + (-5/3)×R2 = R3 - (5/3)×R2:
```
[1,  2/3, -1/3 | 8/3]
[0,    1, -7/5 | 1]
[0,    0,    4 | 0]
```

**Pivot 3 (column 2):**

R3 ÷ 4:
```
[1,  2/3, -1/3 | 8/3]
[0,    1, -7/5 | 1]
[0,    0,    1 | 0]
```

**Forward elimination complete** → REF ✓

---

## Step 3: Back Substitution (→ RREF)

**Goal:** Eliminate entries **above** each pivot (bottom to top).

**Step 1:** Use pivot in row 3, column 2

R2 + (7/5)×R3:
```
[1,  2/3, -1/3 | 8/3]
[0,    1,    0 | 1]
[0,    0,    1 | 0]
```

R1 + (1/3)×R3:
```
[1,  2/3,  0 | 8/3]
[0,    1,  0 | 1]
[0,    0,  1 | 0]
```

**Step 2:** Use pivot in row 2, column 1

R1 - (2/3)×R2:
```
[1,  0,  0 | 8/3 - (2/3)×1]
[0,  1,  0 | 1]
[0,  0,  1 | 0]
```

Calculate: 8/3 - 2/3 = 6/3 = 2

```
[1,  0,  0 | 2]
[0,  1,  0 | 1]
[0,  0,  1 | 0]
```

**Back substitution complete** → RREF ✓ (Identity matrix)

---

## Step 4: Extract Solution

```
[1,  0,  0 | 2]  →  a = 2
[0,  1,  0 | 1]  →  b = 1
[0,  0,  1 | 0]  →  c = 0
```

**Verify:**
- 3a + 2b - c = 3(2) + 2(1) - 0 = 6 + 2 = 8 ✓
- a - b + 2c = 2 - 1 + 0 = 1 ✓
- 2a + 3b + c = 2(2) + 3(1) + 0 = 4 + 3 = 7 ✓

**Solution:** a = 2, b = 1, c = 0

---

## Handling Singular Systems in Gaussian Elimination

**When you encounter a row of all zeros in the coefficient part:**

**Case 1: [0, 0, ..., 0 | 0]**
- Equation reads: 0 = 0 (always true)
- System is **redundant** → **Infinite solutions exist**

**Case 2: [0, 0, ..., 0 | k]** where k ≠ 0
- Equation reads: 0 = k (impossible)
- System is **contradictory** → **No solution**

**Algorithm action:** Stop and classify based on the constant.

---

# PART I: ML APPLICATIONS & DEBUGGING

## Why You Need This in Machine Learning

You won't hand-code Gaussian Elimination in ML. But understanding it is critical for:

---

## Application 1: Linear Regression (Normal Equations)

**Problem:** Minimize loss function for linear model y = Xβ

**Solution:** Solve the normal equation:
```
(X^T X)β = X^T y
```

**What's happening:** This is a system of linear equations where:
- Coefficient matrix: X^T X
- Constants vector: X^T y
- Unknown: β (weights)

**NumPy implementation:**
```python
beta = np.linalg.solve(X.T @ X, X.T @ y)
```

**What NumPy does internally:** Gaussian Elimination + back substitution

---

### Debugging: When Normal Equations Fail

**Symptom:** `numpy.linalg.LinAlgError: Singular matrix`

**Cause:** Matrix X^T X is singular (det = 0)

**Reason:** Your features are **linearly dependent** (multicollinearity)

**Examples:**
- Feature 2 = 2 × Feature 1 (perfect duplication)
- Feature 3 = Feature 1 + Feature 2 (linear combination)
- Too many features relative to samples (rank < n)

**Solution:**
```python
# Check rank
rank = np.linalg.matrix_rank(X)
n_features = X.shape[1]
if rank < n_features:
    print(f"Rank deficient! Rank={rank}, Features={n_features}")
    # Remove correlated features or use regularization
```

---

### Fix: Ridge Regression (Add Regularization)

**When X^T X is singular, add λI (lambda × identity matrix):**
```python
lambda_param = 0.01
beta = np.linalg.solve(X.T @ X + lambda_param * np.eye(X.shape[1]), X.T @ y)
```

**Effect:** Makes matrix non-singular by adding small values to diagonal

---

## Application 2: Feature Dependencies & Rank

**Problem:** You train a model with 1000 features, but loss explodes or model behaves strangely.

**Root cause:** Rank of feature matrix is much less than 1000.

**Why it matters:** Gaussian Elimination (used internally) can't find a stable unique solution.

**Debugging:**
```python
X_matrix = X.values  # Feature matrix
rank = np.linalg.matrix_rank(X_matrix)
n_features = X_matrix.shape[1]
print(f"Rank: {rank}, Features: {n_features}, Free variables: {n_features - rank}")

# If rank << n_features, remove correlated features
```

---

## Application 3: System Singularity & Invertibility

**Problem:** You need to invert a matrix A (for closed-form solutions) but `np.linalg.inv(A)` fails or returns garbage.

**Cause:** Matrix A is singular (det = 0)

**Why:** Gaussian Elimination detects det = 0 by reaching a row of zeros. Can't find inverse.

**Debugging:**
```python
det_A = np.linalg.det(A)
if abs(det_A) < 1e-10:  # Effectively zero
    print("Matrix is singular or nearly singular")
    rank = np.linalg.matrix_rank(A)
    print(f"Rank: {rank}, Expected: {A.shape[0]}")
```

**Fix:** Use `np.linalg.lstsq()` (least squares) instead of `np.linalg.inv()` when matrix is singular.

---

## Application 4: Numerical Stability

**Problem:** Matrix is technically non-singular, but Gaussian Elimination gives wildly incorrect results.

**Cause:** **Ill-conditioning** — matrix is nearly singular (close to losing independence).

**Example:**
```python
A = np.array([
    [1.0, 1.0],
    [1.0, 1.0 + 1e-10]  # Nearly identical rows
])
```

This matrix is technically non-singular (det ≈ 1e-10 ≠ 0), but almost singular. Small computational errors get amplified.

**Why it happens:** During Gaussian Elimination, division by tiny pivot values (near-zero) causes numerical instability.

**Debugging:**
```python
cond_number = np.linalg.cond(A)
if cond_number > 1e10:
    print(f"Matrix is ill-conditioned (cond={cond_number})")
    print("Small numerical errors will be amplified")
```

**Fix:**
- Use double precision floats (default in NumPy)
- Use regularization (Ridge Regression)
- Pre-condition the matrix (scaling, centering features)

---

## Application 5: Identifying Infinite Solutions

**Problem:** Your regression model has multiple optimal solutions with identical loss.

**Cause:** Feature matrix is singular with redundant rows (rank < n).

**Consequence:** Infinitely many weight vectors minimize the loss equally well.

**Debugging:**
```python
rank_X = np.linalg.matrix_rank(X)
if rank_X < X.shape[1]:
    print(f"Infinite solutions exist! Rank {rank_X} < Features {X.shape[1]}")
    # Use regularization to select one solution
    beta = np.linalg.solve(X.T @ X + 0.01 * np.eye(X.shape[1]), X.T @ y)
```

---

## Application 6: Contradictory Constraints (Overdetermined Systems)

**Problem:** More equations than unknowns (m > n). No exact solution exists.

**Example:** 1000 samples, 10 features → 1000 equations, 10 unknowns

**Solution:** Use **least squares** (finds best-fit solution minimizing error):

```python
beta, residuals, rank, s = np.linalg.lstsq(X, y, rcond=None)
```

**How it works:** Gaussian Elimination conceptually, but adapted for overdetermined systems.

---

## Summary: Gaussian Elimination in ML Pipeline

```
Step 1: Collect data (samples × features) → Matrix X
        ↓
Step 2: Check rank(X) vs n_features
        If rank < n_features → multicollinearity detected
        ↓
Step 3: Solve normal equation (X^T X)β = X^T y
        Using Gaussian Elimination internally (np.linalg.solve)
        ↓
Step 4: Check if system is singular or ill-conditioned
        If singular → add regularization λI
        If ill-conditioned → scale/center features
        ↓
Step 5: Extract solution β (if unique)
        or select best solution (if infinite)
        ↓
Step 6: Validate: rank == n_features?
        det(X^T X) ≠ 0?
        Condition number reasonable?
```

---

## Quick Debugging Flowchart

```
❌ Error: Singular matrix detected
  │
  ├─→ Check rank: np.linalg.matrix_rank(X)
  │    If rank < n → Multicollinearity
  │    → Remove correlated features or use Ridge Regression
  │
  ├─→ Check determinant: np.linalg.det(A)
  │    If ≈ 0 → Singular
  │    → Use lstsq instead of solve/inv
  │
  └─→ Check condition number: np.linalg.cond(A)
       If > 1e10 → Ill-conditioned
       → Use regularization (Ridge/Lasso)
```

---

## Key Concepts to Remember

| Concept | Meaning | In ML Context |
|---------|---------|---------------|
| **Rank** | Number of independent equations | Features should have full rank |
| **Singular** | det = 0, rows dependent | Matrix is invertible? No. |
| **Non-singular** | det ≠ 0, unique solution | Unique weights exist |
| **REF** | Staircase form below diagonal | Intermediate step to solution |
| **RREF** | Identity + solution visible | Final form, solution reads directly |
| **Pivot** | First non-zero in row | Separates independent from free variables |
| **Free variable** | No pivot in column | Infinite solutions (can take any value) |
| **Back-substitution** | Solve from bottom row up | Extract solution from RREF |
| **Ill-conditioned** | Small changes → huge errors | Numerical stability issues |

---

## Formulas to Know

**Determinant (2×2):**
```
det([a, b; c, d]) = ad - bc
```

**Determinant signaling singularity:**
```
det ≠ 0 → Non-singular, unique solution
det = 0 → Singular, infinite or no solutions
```

**Rank constraint:**
```
Rank ≤ min(m, n)  where m = rows, n = columns
Rank = n → Unique solution (if system is consistent)
Rank < n → Infinite solutions or no solution (depending on constants)
```

**Condition number (measure of ill-conditioning):**
```
cond(A) = ||A|| × ||A^-1||
cond(A) >> 1 → Ill-conditioned (unstable)
cond(A) ≈ 1 → Well-conditioned (stable)
```

---

## Practice Problems

### Problem 1: Identify the solution type

```
System:
2a + 3b = 5
4a + 6b = 10

What is the solution type? (Unique, Infinite, None)
Answer: Infinite (Row 2 = 2 × Row 1 → Rank 1 < 2 variables)
```

### Problem 2: Build augmented matrix & reduce to REF

```
3a + 2b = 8
a + b = 4

Augmented: [3, 2 | 8]
           [1, 1 | 4]

After R1 ÷ 3: [1, 2/3 | 8/3]
               [1,   1 | 4]

After R2 - R1: [1, 2/3 | 8/3]
               [0, 1/3 | 4/3]

After R2 ÷ (1/3): [1, 2/3 | 8/3]
                  [0,  1 | 4]

REF achieved. Rank = 2 = n → Unique solution
```

### Problem 3: Debug singular matrix error

**You try to solve:**
```python
A = np.array([[1, 2, 3],
              [2, 4, 6],
              [1, 2, 4]])
b = np.array([1, 2, 3])
x = np.linalg.solve(A, b)  # ← Singular matrix error!
```

**What went wrong?**

Row 2 = 2 × Row 1 (linear dependent) → Rank < 3 → Matrix singular

**Check:**
```python
rank = np.linalg.matrix_rank(A)  # Returns 2
det = np.linalg.det(A)  # Returns ~0
```

**Fix:** Use Ridge Regression or remove duplicate feature

---

## Final Checklist

- [ ] Understand row operations preserve solution set
- [ ] Can build augmented matrix from system of equations
- [ ] Can reduce 2×2 matrix to REF by hand
- [ ] Can reduce 3×3 matrix to REF by hand
- [ ] Know the three properties of REF
- [ ] Understand staircase pattern (diagonal rule)
- [ ] Can identify rank from REF
- [ ] Know relationship between rank and solution type
- [ ] Understand RREF = REF + pivots 1 + zeros above
- [ ] Can reduce REF to RREF (back-substitution)
- [ ] Can extract solution from RREF
- [ ] Understand why Gaussian Elimination matters in ML
- [ ] Can debug singular matrix errors
- [ ] Know when to use Ridge Regression vs lstsq
- [ ] Can check condition number for numerical stability

---

## End of Week 2 Guide

**Next:** Week 3 — Vectors, vector spaces, linear independence, and introduction to vector norms (foundation for distance metrics and optimization in ML).

