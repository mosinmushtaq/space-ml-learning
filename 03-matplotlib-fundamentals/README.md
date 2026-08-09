# Matplotlib Fundamentals — Study Notes
I have used AI to make this readme so that i could revise this in a good manner

## Overview

Matplotlib is a Python library for creating visualizations (plots, graphs, charts). Essential for data analysis, pattern recognition, and machine learning portfolio building.

**Why it matters:** Satellite data is numbers. Visualization reveals hidden patterns and communicates findings clearly.

---

## Key Concepts

### Plot Types

| Plot Type | When to Use | Best For | Example |
|-----------|-------------|----------|---------|
| **Line Plot** (`plt.plot()`) | Show trends over time | Temperature trends, orbital decay, time-series data | Days vs Cloud Coverage |
| **Scatter Plot** (`plt.scatter()`) | Show relationships between variables | Correlation, outliers, two-variable analysis | NDVI vs Cloud Cover |
| **Bar Chart** (`plt.bar()`) | Compare values across categories | Category comparison, satellite comparison | Average cloud by satellite |
| **Histogram** (`plt.hist()`) | Show data distribution across ranges | Understand spread, find clustering | Temperature distribution |

---

### Plot Structure Elements

| Element | Purpose | How to Add |
|---------|---------|-----------|
| **Title** | Describe what the plot shows | `plt.title("Title Name")` or `axes[0].set_title("Title")` |
| **X-Axis Label** | Identify horizontal axis | `plt.xlabel("Label")` or `axes[0].set_xlabel("Label")` |
| **Y-Axis Label** | Identify vertical axis | `plt.ylabel("Label")` or `axes[0].set_ylabel("Label")` |
| **Legend** | Show which line/color represents which data | `plt.legend()` or `axes[0].legend()` |
| **Grid** | Add reference lines for reading | `plt.grid(axis='y', alpha=0.3)` |

---

### Styling Elements

#### Colors

| Appearance | Color Name | Short Code | Use Case |
|------------|-----------|-----------|----------|
| Red line | `'red'` | `'r'` | Danger, high values, alert conditions |
| Blue line | `'blue'` | `'b'` | Standard, safe, primary data |
| Green line | `'green'` | `'g'` | Healthy, positive, secondary data |
| Orange line | `'orange'` | — | Warning, attention, tertiary data |
| Purple line | `'purple'` | — | Categorical distinction, special marking |
| Cyan line | `'cyan'` | `'c'` | Contrast, alternative view |

**Key principle:** Use colors to distinguish datasets visually

#### Line Styles

| Style | Pattern | Code | Use Case |
|-------|---------|------|----------|
| Solid | ────── | `'solid'` or `'-'` | Primary data, main trends |
| Dashed | - - - - | `'dashed'` or `'--'` | Secondary data, alternative scenario |
| Dotted | . . . . | `'dotted'` or `':'` | Tertiary data, reference line |
| Dash-dot | -.-.-. | `'dashdot'` or `'-.'` | Special marking, deviation |

**Why:** Works in black & white; colorblind-friendly

#### Markers

| Marker | Symbol | Code | Best For |
|--------|--------|------|----------|
| Circle | ● | `'o'` | Primary data points |
| Square | ■ | `'s'` | Secondary comparison |
| Triangle | ▲ | `'^'` | Tertiary distinction |
| Star | ★ | `'*'` | Special emphasis |
| Plus | + | `'+'` | Reference point |
| X | ✕ | `'x'` | Error or anomaly |
| Diamond | ◆ | `'d'` | Outlier marking |

**Why:** Shows exact location of measurements

---

## Core Functions Reference

### Array Creation & Plotting

| Function | Purpose | Syntax | Example |
|----------|---------|--------|---------|
| `plt.plot()` | Create line plot | `plt.plot(x, y, **options)` | `plt.plot(days, temp, color='red')` |
| `plt.scatter()` | Create scatter plot | `plt.scatter(x, y, **options)` | `plt.scatter(ndvi, cloud, marker='o')` |
| `plt.bar()` | Create bar chart | `plt.bar(categories, values, **options)` | `plt.bar(satellites, avg_cloud)` |
| `plt.hist()` | Create histogram | `plt.hist(data, bins=n, **options)` | `plt.hist(temps, bins=5, color='blue')` |
| `plt.subplots()` | Create multiple plot grid | `fig, axes = plt.subplots(rows, cols)` | `fig, axes = plt.subplots(1, 3)` |

### Styling & Labels

| Function | Purpose | Syntax | Example |
|----------|---------|--------|---------|
| `plt.xlabel()` | Add x-axis label | `plt.xlabel("Label text")` | `plt.xlabel("Days")` |
| `plt.ylabel()` | Add y-axis label | `plt.ylabel("Label text")` | `plt.ylabel("Temperature (°C)")` |
| `plt.title()` | Add plot title | `plt.title("Title text")` | `plt.title("Weekly Temperature")` |
| `plt.legend()` | Show legend/key | `plt.legend()` | Shows which color = which data |
| `plt.grid()` | Add grid lines | `plt.grid(axis='y', alpha=0.3)` | Helps read values |
| `plt.savefig()` | Save plot as image | `plt.savefig("filename.png")` | `plt.savefig("plot.png")` |
| `plt.clf()` | Clear current figure | `plt.clf()` | Use between multiple plots |

### Subplot-Specific (Using axes objects)

| Function | Purpose | Syntax | Example |
|----------|---------|--------|---------|
| `axes[i].plot()` | Plot on specific subplot | `axes[0].plot(x, y)` | Line plot on first subplot |
| `axes[i].scatter()` | Scatter on specific subplot | `axes[1].scatter(x, y)` | Scatter on second subplot |
| `axes[i].hist()` | Histogram on specific subplot | `axes[2].hist(data, bins=5)` | Histogram on third subplot |
| `axes[i].set_xlabel()` | Label x-axis of subplot | `axes[0].set_xlabel("Label")` | Only affects that subplot |
| `axes[i].set_ylabel()` | Label y-axis of subplot | `axes[0].set_ylabel("Label")` | Only affects that subplot |
| `axes[i].set_title()` | Title for subplot | `axes[0].set_title("Title")` | Only affects that subplot |
| `axes[i].legend()` | Legend for subplot | `axes[0].legend()` | Shows labels for that subplot |

---

## Common Patterns

### Pattern 1: Basic Line Plot

```python
import matplotlib.pyplot as plt

days = [1, 2, 3, 4, 5]
temps = [22, 24, 19, 25, 23]

plt.plot(days, temps)
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Weekly Temperature")
plt.savefig("temp_plot.png")
```

### Pattern 2: Multiple Lines with Styling

```python
plt.plot(days, sentinel, color='red', linestyle='solid', marker='o', label='Sentinel-2')
plt.plot(days, landsat, color='blue', linestyle='dashed', marker='s', label='Landsat-8')
plt.xlabel("Days")
plt.ylabel("Cloud Coverage (%)")
plt.title("Satellite Comparison")
plt.legend()
plt.savefig("comparison.png")
```

### Pattern 3: Multiple Subplots

```python
fig, axes = plt.subplots(1, 3)  # 1 row, 3 columns

# Subplot 1: Line
axes[0].plot(days, temps, color='red')
axes[0].set_title("Temperature Trend")

# Subplot 2: Scatter
axes[1].scatter(cloud, ndvi, color='orange', marker='*')
axes[1].set_title("Cloud vs Vegetation")

# Subplot 3: Histogram
axes[2].hist(temps, bins=5, color='purple')
axes[2].set_title("Temperature Distribution")

plt.savefig("analysis.png")
```

### Pattern 4: Grid for Better Readability

```python
plt.plot(days, cloud_values, color='blue', marker='o')
plt.grid(axis='y', alpha=0.3)  # Light horizontal lines
plt.xlabel("Days")
plt.ylabel("Cloud Coverage (%)")
plt.title("Cloud Coverage Over Time")
plt.savefig("cloud_plot.png")
```

---

## Styling Parameter Combinations

| Use Case | Code |
|----------|------|
| Single line, no styling | `plt.plot(x, y)` |
| Colored line | `plt.plot(x, y, color='red')` |
| Colored + dashed line | `plt.plot(x, y, color='blue', linestyle='--')` |
| Colored + markers | `plt.plot(x, y, color='green', marker='o')` |
| Full styling + label | `plt.plot(x, y, color='red', linestyle='-', marker='s', label='Data A')` |
| Scatter with styling | `plt.scatter(x, y, color='orange', marker='*', s=100)` |
| Histogram with color | `plt.hist(data, bins=5, color='purple')` |

---

## Mistakes to Avoid

| Mistake | Problem | Solution |
|---------|---------|----------|
| Multiple plot types on one canvas | Overlapping lines, confusing | Use subplots: `plt.subplots(1, 3)` |
| Repeated parameters in one function | SyntaxError: keyword argument repeated | Use each parameter once: `plt.plot(x, y, color='red', label='Data')` |
| Defining label but no legend | Labels invisible to viewer | Add `plt.legend()` after all plots |
| Using `plt.show()` in VSCode terminal | Won't display (non-interactive environment) | Use `plt.savefig("name.png")` instead |
| Forgetting axis labels | Plot unclear to others | Always add `plt.xlabel()`, `plt.ylabel()`, `plt.title()` |
| All lines same color in multi-line plot | Can't distinguish datasets | Use different colors: red, blue, green, etc. |
| Using list addition `+` on numerical arrays | Unexpected behavior | Use NumPy: `np.array(list1) + np.array(list2)` for element-wise |

#Thank you for reading until now.
