# Iris Dataset Analysis  

## Objective  
The goal of this assignment is to:  
- Load and analyze a dataset using the **pandas** library in Python.  
- Create simple plots and charts with the **matplotlib** library for visualizing the data.  

---

## Dataset  
The dataset used is the **Iris dataset**, which contains measurements of iris flowers:  

- **sepal length (cm)**  
- **sepal width (cm)**  
- **petal length (cm)**  
- **petal width (cm)**  
- **target** (species: Setosa, Versicolor, Virginica)  

---

## Steps Performed  

### 1. Data Loading  
- Loaded the dataset into a pandas DataFrame.  
- Displayed the first few rows using `df.head()`.  
- Checked dataset structure using `df.info()` and column names.  

### 2. Data Exploration  
- Used `df.describe()` to generate summary statistics.  
- Checked for missing values with `df.isnull().sum()`.  
- Verified dataset balance across target classes with `value_counts()`.  

### 3. Basic Data Analysis  
- Calculated mean, median, and standard deviation for each feature.  
- Grouped data by species (`target`) to analyze differences.  

### 4. Data Visualization  
- **Histograms** for each feature to understand distributions.  
- **Boxplots** to detect outliers.  
- **Scatter plots** to visualize relationships between features.  
- **Pairplot (seaborn)** for multi-feature relationships.  

---

## Findings & Observations  
- **Setosa** is linearly separable from the other two species using petal length and width.  
- **Versicolor** and **Virginica** overlap in some features but can be separated with petal dimensions.  
- Sepal measurements are less effective for classification compared to petal measurements.  

---

## Requirements  
To run the notebook/script, install the following:  

```bash
pip install pandas matplotlib seaborn scikit-learn
