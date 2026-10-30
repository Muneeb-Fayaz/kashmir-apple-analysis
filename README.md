# 🍎 Kashmir Apple Market Analysis

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:14532d,50:16a34a,100:84cc16&height=220&section=header&text=Kashmir%20Apple%20Market&fontSize=38&fontColor=ffffff&fontAlignY=38&desc=Turning%20Agricultural%20Data%20Into%20Insights&descAlignY=60&descSize=16" width="100%" />
</p>

<p align="center">
  <b>🍏 Exploring Kashmir's Apple Industry Through Python & Data Analytics</b>
  <br/>
  <i>From orchards to markets — discovering the story behind the numbers.</i>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-Numerical%20Analysis-013243?style=for-the-badge&logo=numpy" />
  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas" />
  <img src="https://img.shields.io/badge/Status-In%20Development-orange?style=for-the-badge" />
</p>

---

## 🌿 The Idea Behind This Project

Kashmir is famous for its beautiful apple orchards and rich agricultural heritage. Behind every apple sold in the market, there is a complete economic journey — production, harvesting, grading, transportation, storage and selling.

But how does this market actually work?

Which district produces the most apples? Which varieties receive better prices? Does increased market supply affect selling prices? And how much does an apple farmer actually earn?

**Kashmir Apple Market Analysis** is a Python-based data analytics project that explores these questions using agricultural statistics and market datasets.

The goal is to turn raw data into meaningful insights about Kashmir's apple industry.

## 🍎 What Does This Project Explore?

<table>
<tr>
<td width="50%">

### 🌳 Production Analysis
- District-wise production
- Production comparisons
- Agricultural productivity
- Yearly production trends

</td>
<td width="50%">

### 💰 Price Analysis
- Variety-wise prices
- Market price comparison
- Grade-wise price differences
- Seasonal price patterns

</td>
</tr>
<tr>
<td width="50%">

### 🚚 Supply Analysis
- Market arrivals
- Supply distribution
- Transportation expenses
- Storage capacity

</td>
<td width="50%">

### 🛒 Demand Analysis
- Quantity sold
- Buyer activity
- Popular varieties
- Market demand indicators

</td>
</tr>
<tr>
<td width="50%">

### 👨‍🌾 Farmer Profitability
- Total revenue
- Production expenses
- Transportation costs
- Estimated net profit

</td>
<td width="50%">

### 📊 Statistical Analysis
- Average and median prices
- Production statistics
- Data comparisons
- Market patterns

</td>
</tr>
</table>

## 📍 Understanding Kashmir's Apple Production

The initial dataset includes official district-wise apple production statistics for Kashmir Division.

**Financial Year: 2024–25**

| District | Production (000 MT) |
|:---|---:|
| Baramulla | 479.25 |
| Anantnag | 285.00 |
| Shopian | 269.66 |
| Kupwara | 233.05 |
| Kulgam | 218.40 |
| Pulwama | 212.85 |
| Budgam | 162.82 |
| Ganderbal | 122.16 |
| Bandipora | 75.71 |
| Srinagar | 20.73 |

> Production values are expressed in thousand metric tonnes and are based on the official government statistical publication.

## 🧰 Built With

| Technology | Role |
|:---|:---|
| Python | Core application |
| NumPy | Numerical calculations |
| Pandas | Data manipulation and cleaning |
| CSV | Dataset management |

No machine learning frameworks or external database are required in the initial version.

## 📂 Project Architecture

```text
kashmir-apple-market-analysis/
│
├── data/
│   ├── raw/
│   │   ├── apple_production_official_2024_25.csv
│   │   ├── apple_prices_sample.csv
│   │   ├── apple_supply_sample.csv
│   │   └── apple_demand_sample.csv
│   │
│   └── processed/
│
├── src/
│   └── day1_inspect_data.py
│
├── notebooks/
│
├── reports/
│
├── requirements.txt
├── .gitignore
└── README.md
```

## 📊 Data Sources & Transparency

Data authenticity matters.

This project separates government statistics from practice datasets to avoid presenting illustrative figures as real market information.

**Official data sources:**

- [J&K Directorate of Economics and Statistics](https://ecostatjk.nic.in/)
- [Regional Digest of Statistics](https://ecostatjk.nic.in/showdata.aspx?q=Regional_Digest_Stat)
- [AGMARKNET](https://agmarknet.gov.in/)
- [Open Government Data India](https://data.gov.in/)
- [e-NAM](https://www.enam.gov.in/)

**Dataset classification:**

| Dataset | Status |
|:---|:---|
| Apple Production | Official government statistics |
| Apple Prices | Synthetic sample data |
| Apple Supply | Synthetic sample data |
| Apple Demand | Synthetic sample data |

⚠️ Sample datasets are created for development and practice. They do not represent actual mandi transactions, verified demand or real-time market prices.

## ⚙️ Getting Started

Want to run this project on your computer?

Follow these steps.

### 1. Clone the repository

```bash
git clone https://github.com/Muneeb-Fayaz/kashmir-apple-market-analysis.git
```

### 2. Enter the project directory

```bash
cd kashmir-apple-market-analysis
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

**Windows PowerShell**

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the project

```bash
python src/day1_inspect_data.py
```

## 🔍 Questions This Project Aims to Answer

1. Which district leads Kashmir in apple production?
2. Which apple varieties have higher average prices?
3. How do market prices change during harvesting seasons?
4. Which markets receive the highest apple arrivals?
5. Is there a relationship between supply and selling prices?
6. Which apple grades offer better returns?
7. What are the major expenses involved in apple farming?
8. How much estimated profit can a farmer generate?

## 🗺️ Development Roadmap

This project is being developed step by step.

- [x] Initial project structure
- [x] Official production dataset
- [x] Sample CSV datasets
- [x] Initial Pandas data inspection
- [ ] Data cleaning and preprocessing
- [ ] Production analysis
- [ ] Market price analysis
- [ ] Supply analysis
- [ ] Demand analysis
- [ ] Farmer profitability analysis
- [ ] Statistical reporting
- [ ] Complete terminal-based application
- [ ] Final testing and documentation

## 🎓 What I'm Learning

This project is also part of my practical learning journey in data analytics.

Through this project, I'm working on:

- Python programming
- NumPy fundamentals
- Pandas DataFrames and Series
- Data cleaning
- Exploratory Data Analysis (EDA)
- Statistical calculations
- Grouping and filtering
- Real-world dataset handling
- Business-oriented problem solving

## 🌱 Future Possibilities

After completing the core analysis, this project may be extended with:

- Historical apple price trend analysis
- More verified government market datasets
- Interactive data visualizations
- An agricultural market dashboard
- Machine learning-based price forecasting

These are future possibilities, not features of the current release.

---

## 👨‍💻 About the Developer

<p align="center">
  <img src="https://img.shields.io/badge/Developer-Muneeb%20Fayaz-166534?style=for-the-badge" />
</p>

**Muneeb Fayaz**

BCA Student | Python Developer | Data Analytics Enthusiast | Exploring AI Engineering

- GitHub: [Muneeb-Fayaz](https://github.com/Muneeb-Fayaz)
- LinkedIn: [Connect with me](https://www.linkedin.com/in/muneeb-fayaz-0440823a4)

---

<p align="center">
  <b>🍎 Made with Python, curiosity and love for Kashmir.</b>
  <br/>
  <i>Every dataset has a story. Let's discover Kashmir's.</i>
  <br/><br/>
  ⭐ If you find this project interesting, consider giving it a star!
</p>

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:84cc16,50:16a34a,100:14532d&height=110&section=footer" width="100%" />
</p>
