# Indian Startup Funding Analysis (2020–2025)

> **Comprehensive analysis of 1,100+ Indian startup funding deals** across sectors, cities, funding stages, and investors — featuring a 3-layer AI-powered sector reclassification system.

![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
![Pandas](https://img.shields.io/badge/Pandas-3.0-green?logo=pandas)
![SQLite](https://img.shields.io/badge/SQLite-In--Memory-lightgrey?logo=sqlite)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📊 Key Findings

| Metric | Value |
|--------|-------|
| **Total Funding** | $28.09B |
| **Total Deals** | 1,100 |
| **Peak Year** | 2021 ($6.02B, +27% YoY) |
| **Post-Winter Recovery** | 2024 (+49% bounce back) |
| **Top Sector** | Ecommerce/D2C (205 deals) |
| **Median Deal Size** | $1.1M |




## 🔬 3-Layer Sector Reclassification

The dataset suffers from severe sector mislabelling (e.g., Razorpay tagged as "EdTech", BYJU'S as "AgriTech"). We built a 3-layer correction system:

| Layer | Method | Entries | Confidence |
|-------|--------|---------|------------|
| **Layer 1** | Known company name lookup | 309 companies | 🟢 High |
| **Layer 2** | Regex pattern matching | 12 sector patterns | 🟡 Medium |
| **Layer 3** | Investor-based inference | 35 specialist investors | 🔴 Low |

**Result:** 350 rows corrected (31.8%), "Other" category reduced by 38%.

### Reclassification Results
#### Sector Distribution Change
![Before vs After Reclassification](viz_reclassification_impact(1).png)
#### Reclassification Layer Usage
![Layer Usage](viz_reclassification_layers(1).png)
#### Confidence Distribution
![Confidence](viz_reclassification_confidence(1).png)

---

## 📈 Analysis Highlights

### 8 Analytical Insights
1. **YoY Funding Trend** — Annual funding with growth rates
2. **Sector Share by Year** — Which sectors dominated when
3. **Funding Stage Distribution** — Seed to Late Stage breakdown
4. **City-wise Funding** — Geographic concentration analysis
5. **Top 15 Investors** — Most active investors by deal count
6. **Deal Size by Sector** — Min/avg/max deal sizes
7. **Sector × Stage Matrix** — Cross-tabulation heatmap
8. **Seasonality** — Monthly/quarterly funding patterns

### Projections (2026–2028)
Linear regression-based funding projections for the next 3 years.

---

## 🛠️ Setup & Usage

### Prerequisites
```bash
python -m venv .venv
.venv\Scripts\activate       # Windows
pip install -r requirements.txt
```

### Run the Notebook
```bash
jupyter notebook notebooks/indian_startup_funding_analysis.ipynb
```

### Generate Power BI Data
```bash
python scripts/generate_powerbi_data.py
```

### Run Sector Reclassification Standalone
```bash
python scripts/sector_reclassifier.py
```

---

## 📊 Dashboard Options

| Tool | File | Guide |
|------|------|-------|
| **Power BI** | `outputs/powerbi_startup_dashboard.xlsx` | `powerbi/POWERBI_GUIDE.md` |
| **Tableau** | `tableau_outputs/*.csv` | `tableau_outputs/TABLEAU_GUIDE.md` |
| **HTML** | `dashboard/McKinsey_Startup_Dashboard.html` | Open in browser |

---

## 📋 Tech Stack

- **Python 3.10+** — Core language
- **Pandas 3.0** — Data manipulation
- **SQLite** — In-memory analytical queries
- **Matplotlib + Seaborn** — Visualizations (dark theme)
- **openpyxl** — Excel export
- **Regex** — Sector reclassification patterns

---

## 📄 License

MIT License — feel free to use, modify, and distribute.

---

*Built as part of a McKinsey-style startup ecosystem analysis project.*
## 📊 Reclassification Results
![Impact of Reclassification](viz_reclassification_impact.png)
![Layer Usage](viz_reclassification_layers.png)
![Confidence](viz_reclassification_confidence.png)
