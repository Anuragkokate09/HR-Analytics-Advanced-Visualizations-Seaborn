# 📊 **HR Analytics & Advanced Visualizations**
### *Statistical Workforce Insights with Python & Seaborn*

---

## 📝 **Project Overview**
This project performs an in-depth statistical analysis of a 2,000-record employee dataset. Unlike basic charts, this repository utilizes **Seaborn** to create density estimates and variance visualizations, helping HR departments identify compensation outliers, salary density, and workforce seniority patterns.

---

## 🛠️ **Core Visualization Features**
The main script (`Seaborn2.py`) generates a multi-dimensional dashboard with the following statistical views:

* 🧬 **KDE Plot (Kernel Density Estimate):** Visualizes the "smooth" distribution of **Annual Salary** to find the most common pay brackets.
* 🎻 **Violin Plot:** Shows the probability density of salaries across the organization, highlighting variance and spread.
* 📈 **Experience Distribution:** Combines histograms and KDE traces to analyze the professional tenure of the workforce.
* 📊 **Departmental Count Analysis:** A categorical breakdown showing staff volume across different business units.
* 🕒 **Age Demographics:** Statistical binning of employee ages to understand generational diversity.

---

## 📊 **Dataset Architecture**
The analysis is powered by `IT_Employees_Info_2000.csv`, which includes:
* **Employee Age**: Used for demographic distribution.
* **Annual Salary**: The primary metric for compensation density analysis.
* **Experience (Years)**: Used to track professional seniority.
* **Department**: Categorical field for headcount visualization.

---

## ⚙️ **Technical Stack**
* **Language:** `Python 3.x`
* **Primary Libraries:** * `Seaborn`: For advanced statistical aesthetics.
    * `Matplotlib`: For subplot grid management and axis control.
    * `Pandas`: For high-speed data frame manipulation and CSV parsing.

---

## 🚀 **How To Use**
1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/Anuragkokate09/HR-Analytics-Advanced-Visualizations-Seaborn.git](https://github.com/Anuragkokate09/HR-Analytics-Advanced-Visualizations-Seaborn.git)
2. Install Dependencies:
   ```bash
   pip install pandas seaborn matplotlib
3. Run the Script:
   ```bash
   python Seaborn2.py

---

### **3. Proper Commit Strategy**
To keep your history clean, use these commit messages when updating:

| File Type | Suggested Commit Name |
| :--- | :--- |
| **Python Script** | `feat: add statistical HR dashboard using Seaborn and Matplotlib` |
| **Dataset (.csv)** | `data: upload 2000-record IT employee info for analysis` |
| **Documentation** | `docs: complete README with technical stack and project overview` |

---

### **4. Visual Verification**
Your repository now correctly includes:
1.  **`Seaborn2.py`**: Your logic and plotting code.
2.  **`IT_Employees_Info_2000.csv`**: Your raw data.
3.  **`README.md`**: Your professional documentation.


      
