# 📊 Tableau Dashboard — Step-by-Step Build Guide
### FUTURE_DS_01 | Business Sales Performance Analytics

---

## Prerequisites

- Tableau Public (free) or Tableau Desktop
- Download from: https://public.tableau.com/en-us/s/download
- Dataset: `data/Sample_Superstore.csv`

---

## Step 1 — Connect to the Data

1. Open Tableau
2. Click **"Connect to Data"** → **Text File**
3. Navigate to and select `Sample_Superstore.csv`
4. Tableau will load a data preview — verify it shows 9,994 rows
5. Check that **Order Date** and **Ship Date** are recognised as **Date** fields (look for the calendar icon)
6. If not: right-click the column header → Change Data Type → **Date**
7. Click **"Sheet 1"** at the bottom to start building

---

## Step 2 — Create Calculated Fields

Before building charts, create these calculated fields.
Go to: **Analysis menu → Create Calculated Field**

**Profit Margin %**
```
SUM([Profit]) / SUM([Sales])
```
Format as: Percentage, 1 decimal place

**Days to Ship**
```
DATEDIFF('day', [Order Date], [Ship Date])
```

**YoY Revenue Change**
```
(SUM([Sales]) - LOOKUP(SUM([Sales]), -1)) / ABS(LOOKUP(SUM([Sales]), -1))
```

---

## Step 3 — Chart 1: Monthly Revenue Trend (Line Chart)

**What it shows:** Monthly sales comparison across years

1. Drag **Order Date** to the **Columns** shelf
   - Right-click it → Select **Month** (the continuous version showing Jan–Dec)
2. Drag **Sales** to the **Rows** shelf
3. Drag **Year(Order Date)** to the **Color** card (Marks panel)
   - This creates one line per year
4. Change mark type to **Line** (top of Marks panel)
5. Format colors:
   - 2017: **Pink** (#ED4C8C)
   - 2016: **Blue** (#2563EB)
6. Right-click Y-axis → **Format** → Number → Currency ($), 0 decimal places
7. Title: `Monthly Revenue Trend: 2016 vs 2017`

---

## Step 4 — Chart 2: Revenue by Category (Bar Chart)

**What it shows:** Revenue and profit per product category

1. Drag **Category** to **Rows**
2. Drag **Sales** to **Columns**
3. Drag **Profit** to **Color** card
4. Change mark type to **Bar**
5. In the color legend, click **Edit Colors** → choose a diverging palette:
   - Negative (loss): Red (#EF4444)
   - Positive (profit): Green (#22C55E)
6. Sort bars: click the sort icon on the axis (descending by Sales)
7. Add labels: drag **Sales** to the **Label** card → format as currency
8. Title: `Revenue & Profit by Category (2017)`
9. Add a **Year filter**: drag **Year** to Filters → select **2017**

---

## Step 5 — Chart 3: Sales by Region (Horizontal Bar)

**What it shows:** Which region generates the most revenue

1. Drag **Region** to **Rows**
2. Drag **Sales** to **Columns**
3. Mark type: **Bar**
4. Drag **Sales** to **Color** → Edit colors → gradient from white to **Purple** (#7C3AED)
5. Sort by Sales descending
6. Add **Profit Margin %** to the **Tooltip**
7. Title: `Sales by Region (2017)`
8. Filter to 2017

---

## Step 6 — Chart 4: Customer Segment Pie Chart

**What it shows:** Revenue share by customer type

1. Drag **Segment** to **Color** card
2. Drag **Sales** to **Angle** card (this only appears in Pie mark type)
3. Change mark type to **Pie**
4. Drag **Sales** to **Label** → right-click → Quick Table Calculation → **Percent of Total**
5. Also drag **Segment** to **Label** so both name and % show
6. Set colors:
   - Consumer: **Pink** (#ED4C8C)
   - Corporate: **Purple** (#7C3AED)
   - Home Office: **Green** (#22C55E)
7. Title: `Sales by Customer Segment (2017)`
8. Filter to 2017

---

## Step 7 — Chart 5: Quarterly Sales by Category (Grouped Bar)

**What it shows:** How each category performs across Q1–Q4

1. Drag **QUARTER(Order Date)** to **Columns**
   - Right-click → **Discrete** → Quarter
2. Drag **Sales** to **Rows**
3. Drag **Category** to **Color**
4. Mark type: **Bar**
5. Set colors:
   - Furniture: **Pink** (#ED4C8C)
   - Office Supplies: **Purple** (#7C3AED)
   - Technology: **Green** (#22C55E)
6. Title: `Quarterly Revenue by Category (2017)`
7. Filter to 2017

---

## Step 8 — Chart 6: Top 10 Products (Horizontal Bar)

**What it shows:** Your highest-revenue products

1. Drag **Product Name** to **Rows**
2. Drag **Sales** to **Columns**
3. Mark type: **Bar**
4. Apply a **Top 10 filter**:
   - Drag **Product Name** to the Filters shelf
   - Click **Top** tab → By Field → Top 10 by Sum of Sales
5. Sort descending by Sales
6. Color: **Blue** (#2563EB)
7. Add **Profit** to Tooltip
8. Title: `Top 10 Products by Revenue (2017)`
9. Filter to 2017

---

## Step 9 — Chart 7: Sub-Category Profit/Loss (Bar Chart)

**What it shows:** Which sub-categories are profitable vs losing money

1. Drag **Sub-Category** to **Rows**
2. Drag **Profit** to **Columns**
3. Mark type: **Bar**
4. Drag **Profit** to **Color** → Edit Colors → diverging:
   - Negative end: **Red** (#EF4444)
   - Centre: White
   - Positive end: **Green** (#22C55E)
5. Add a reference line at 0: Right-click axis → Add Reference Line → Value = 0
6. Sort by Profit descending
7. Title: `Sub-Category Profit & Loss (2017)`
8. Filter to 2017

---

## Step 10 — Build the Dashboard

1. Click the **New Dashboard** button (icon at the bottom)
2. Set size: **Fixed** → **1200 × 900** pixels (or Automatic)
3. Drag sheets from the left panel onto the dashboard canvas:

**Suggested layout:**
```
┌─────────────────────────────────────────────────────┐
│  TITLE: Sales Performance Analytics Dashboard       │
│  Subtitle: Sample Superstore | FY2017 | FUTURE_DS_01│
├──────────────────────┬──────────────────────────────┤
│  Monthly Trend       │  Category Bar Chart          │
│  (Line Chart)        │                              │
├──────────────────────┼──────────────────────────────┤
│  Regional Bar        │  Segment Pie Chart           │
├──────────────────────┴──────────────────────────────┤
│  Quarterly Grouped Bar Chart                        │
├──────────────────────┬──────────────────────────────┤
│  Top 10 Products     │  Sub-Category Profit/Loss    │
└──────────────────────┴──────────────────────────────┘
```

4. Add a **Text box** at the top for the title:
   - Font: Bold, size 20
   - Text: `Sales Performance Analytics | Sample Superstore | FUTURE_DS_01`

5. Add **KPI text boxes** (one per metric):
   - Total Revenue: $733,215 ↑ 20.4%
   - Total Profit: $93,439 ↑ 14.2%
   - Profit Margin: 12.7%
   - Total Orders: 1,687

6. Set dashboard background: **Dark navy** (#0D1B2A) or white

---

## Step 11 — Add Interactivity (Filters)

1. Click each chart → click the **funnel icon** that appears → **Use as Filter**
   - Now clicking a region on the Regional chart will filter all other charts
2. Add a global **Year filter**:
   - On any sheet, drag Year to Filters → right-click → **Apply to Worksheets → All Using This Data Source**
3. Add a **Segment filter** the same way

---

## Step 12 — Publish to Tableau Public

1. **File → Save to Tableau Public**
2. Sign in with your free Tableau Public account
3. Name it: `Business Sales Performance Analytics — FUTURE_DS_01`
4. Once published, copy the URL
5. Add the Tableau Public link to your README.md and LinkedIn post

---

## ✅ Verification Checklist

Before submitting, confirm:

- [ ] Revenue for 2017 shows **$733,215**
- [ ] Profit for 2017 shows **$93,439**
- [ ] Technology is the #1 category by revenue
- [ ] West Region leads on revenue
- [ ] Tables sub-category shows a **negative profit**
- [ ] Consumer segment = largest share of pie chart
- [ ] Dashboard has a title, colour palette (pink/blue/green/purple/white)
- [ ] At least one interactive filter works
- [ ] Dashboard published to Tableau Public

---

## 🎨 Colour Reference

| Colour | Hex Code | Use |
|---|---|---|
| Pink | `#ED4C8C` | Primary accent, 2017 line |
| Blue | `#2563EB` | Secondary accent, 2016 line |
| Green | `#22C55E` | Positive/profit values |
| Purple | `#7C3AED` | Category highlights |
| White | `#FFFFFF` | Backgrounds, labels |
| Dark Navy | `#0D1B2A` | Dashboard background |
| Red | `#EF4444` | Negative/loss values |

---

*Guide prepared for FUTURE_DS_01 | Future Interns Data Science & Analytics Track*
