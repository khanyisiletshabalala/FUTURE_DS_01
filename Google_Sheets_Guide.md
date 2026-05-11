# 📋 Google Sheets Setup Guide
### FUTURE_DS_01 | Business Sales Performance Analytics

---

## Step 1 — Upload the Dataset

1. Go to [sheets.google.com](https://sheets.google.com)
2. Click **New → Upload**
3. Select `data/Sample_Superstore.csv`
4. Google Sheets will open it automatically
5. Rename the sheet tab at the bottom: **Raw Data**

---

## Step 2 — Format the Header Row

1. Select **Row 1**
2. Fill color: **Dark Navy** (custom hex: `#0D1B2A`)
3. Font color: **White**
4. Bold: Yes
5. Freeze row 1: **View → Freeze → 1 row**

---

## Step 3 — Add Helper Columns

Click on the first empty column after **Profit** and add:

| Column Header | Formula (paste in Row 2, drag down) |
|---|---|
| Year | `=YEAR(C2)` |
| Month | `=MONTH(C2)` |
| Quarter | `="Q"&INT((MONTH(C2)-1)/3+1)` |
| Month Name | `=TEXT(C2,"mmm")` |
| Profit Margin % | `=IF(N2<>0, O2/N2, 0)` |
| Days to Ship | `=D2-C2` |

*(Assuming Order Date = Col C, Ship Date = Col D, Sales = Col N, Profit = Col O — adjust if different)*

---

## Step 4 — Create Pivot Table 1: Revenue by Year

1. Click anywhere in the data
2. **Insert → Pivot Table → New Sheet**
3. Name the sheet: **Pivot — Yearly**
4. Configure:
   - **Rows:** Year
   - **Values:** Sales (SUM), Profit (SUM), Order ID (COUNTA)
5. Format Sales and Profit columns as Currency

---

## Step 5 — Create Pivot Table 2: Category Performance

1. **Insert → Pivot Table → New Sheet**
2. Name: **Pivot — Category**
3. Configure:
   - **Rows:** Category
   - **Columns:** Year
   - **Values:** Sales (SUM)
4. Add a filter: Year = 2017

---

## Step 6 — Create Pivot Table 3: Regional Breakdown

1. **Insert → Pivot Table → New Sheet**
2. Name: **Pivot — Regional**
3. Configure:
   - **Rows:** Region
   - **Values:** Sales (SUM), Profit (SUM)
4. Add calculated column for Margin: `=B2/A2` (format as %)

---

## Step 7 — Create Pivot Table 4: Monthly Trend

1. **Insert → Pivot Table → New Sheet**
2. Name: **Pivot — Monthly**
3. Configure:
   - **Rows:** Month Name
   - **Columns:** Year
   - **Values:** Sales (SUM)
4. Sort rows by Month number (use the Month helper column as sort key)

---

## Step 8 — Build Charts in Google Sheets

### Chart 1: Monthly Revenue Line Chart
1. Select the Pivot — Monthly table
2. **Insert → Chart**
3. Chart type: **Line chart**
4. Series: 2016 (Blue `#2563EB`), 2017 (Pink `#ED4C8C`)
5. Title: `Monthly Revenue: 2016 vs 2017`

### Chart 2: Category Bar Chart
1. Select the Pivot — Category table
2. **Insert → Chart**
3. Chart type: **Column chart**
4. Color: Purple (`#7C3AED`)
5. Title: `Revenue by Category (2017)`

### Chart 3: Regional Horizontal Bar
1. Select the Pivot — Regional table
2. **Insert → Chart**
3. Chart type: **Bar chart**
4. Color: Blue (`#2563EB`)
5. Title: `Sales by Region (2017)`

---

## Step 9 — Create a Dashboard Sheet

1. Add a new sheet named **Dashboard**
2. Copy charts from pivot sheets and paste them here
3. Add text boxes for KPIs using **Insert → Drawing**:
   - Total Revenue: **$733,215**
   - Total Profit: **$93,439**
   - Profit Margin: **12.7%**
   - Total Orders: **1,687**

---

## ✅ Verification

Confirm your pivot totals match:

| Metric | Expected Value |
|---|---|
| 2017 Total Sales | $733,215 |
| 2017 Total Profit | $93,439 |
| Technology Sales | $271,731 |
| West Region Sales | $250,128 |
| Consumer Segment | $331,905 |

---

*Guide prepared for FUTURE_DS_01 | Future Interns Data Science & Analytics Track*
