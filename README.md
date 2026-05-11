# Business Sales Performance Analytics
**Future Interns | Data Science & Analytics | Task 1 — FUTURE_DS_01**

![Tools](https://img.shields.io/badge/Tools-Excel%20%7C%20Tableau%20%7C%20Google%20Sheets-blueviolet?style=flat-square)
![Dataset](https://img.shields.io/badge/Dataset-Sample%20Superstore-pink?style=flat-square)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat-square)

---

## What this project is about

For this task I analysed the Sample Superstore retail dataset to understand how the business performed across different product categories, regions, and time periods. The main questions I was trying to answer were: where is the business making money, where is it losing money, and what should it focus on going forward.

---

## Dataset

**Source:** Sample Superstore — [Kaggle link](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)

The dataset covers orders from 2014 to 2017 across the US. It has about 10,000 rows with information on products, customers, regions, order dates, sales, and profit. I focused my analysis on 2017 compared to 2016 since those are the two most complete years.

---

## Tools I used

- **Excel** — built the main dashboard with KPI cards, pivot tables, and charts
- **Tableau** — created an interactive version (see the guide in /docs)
- **Google Sheets** — used for initial data exploration and pivot tables
- **Python** — wrote a script to validate that my dashboard numbers match the raw data

---

## Folder structure

```
FUTURE_DS_01/
├── data/
│   ├── Sample_Superstore.csv
│   └── FUTURE_DS_01_Sales_Analytics.xlsx
├── scripts/
│   └── analysis.py
├── docs/
│   ├── Tableau_Step_by_Step_Guide.md
│   └── Google_Sheets_Guide.md
├── screenshots/
└── README.md
```

---

## Key numbers (2017 vs 2016)

| Metric | 2017 | 2016 | Change |
|---|---|---|---|
| Revenue | $733,215 | $609,206 | +20.4% |
| Profit | $93,439 | $81,795 | +14.2% |
| Orders | 1,687 | 1,315 | +28.3% |
| Profit Margin | 12.7% | 13.4% | -0.7pp |

---

## Main findings

**Technology is the strongest category.** It brought in $271,731 with an 18.6% margin — the best of the three categories. The Canon imageCLASS Copier alone made $35,700. There is room to grow this further.

**Furniture is a problem.** The category made only $3,018 profit on $215,387 in sales — a margin of just 1.4%. The Tables sub-category was the worst offender, losing $8,141. This needs immediate attention.

**The West region leads.** It generated $250,128 in revenue with a 17.5% margin. The Central region, on the other hand, made $147K in sales but only $7.5K in profit (5.1% margin). Applying West's pricing strategy to Central could help significantly.

**Q4 is huge.** The business makes 38% of its annual revenue in Q4. That's a seasonal spike worth planning around — building inventory from Q3 and locking in early promotions would help capture it better.

**New customers in the first year are the most at risk.** Not directly visible in this dataset but worth noting when cross-referencing with customer lifetime data.

---

## Recommendations

1. Stop heavy discounting on Tables and Bookcases — they are losing money
2. Invest more in Technology products, especially Copiers which have the best margin
3. Build stock from Q3 to handle the Q4 rush without running out
4. Look at what the West region is doing differently and apply it to Central
5. Consider a loyalty or repeat-purchase incentive for Consumer customers

---

## How to run the Python script

```bash
pip install pandas openpyxl
python scripts/analysis.py
```

It will print all the key numbers and flag anything that looks off.

---

## What I learned

This was my first time doing a full sales analysis from scratch. A few things stood out to me:

The Tables finding surprised me — furniture looks fine on the surface (good revenue) but when you look at profit, it is barely breaking even. That is the kind of thing that would be invisible if you only looked at revenue.

I also spent more time than expected getting the Tableau filters working so that clicking on a region actually updates all the charts. Once it clicked it made the dashboard much more useful.

If I were to redo this I would try to bring in some customer-level data too, to see whether high-revenue products also have high repeat purchase rates.

---

## About

**Intern:** Khanyisile | Johannesburg, South Africa
**Programme:** Future Interns Data Science & Analytics Internship
**GitHub:** [github.com/khanyisiletshabalala](https://github.com/khanyisiletshabalala)
