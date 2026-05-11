# Task 1 - Business Sales Performance Analytics
# Dataset: Sample Superstore (Kaggle)
# Author: Khanyisile
# Future Interns - Data Science & Analytics

# I used pandas to do most of the heavy lifting here
# Make sure you run: pip install pandas openpyxl

import pandas as pd
import os

# path to the data - adjust if you moved the file
DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'Sample_Superstore.csv')

print("\nLoading dataset...")

try:
    df = pd.read_csv(DATA_PATH, encoding='latin-1')
    print(f"Loaded {len(df):,} rows successfully")
except FileNotFoundError:
    print(f"Couldn't find the file at {DATA_PATH}")
    print("Make sure Sample_Superstore.csv is in the /data folder")
    exit()

# fix the date columns - they come in as strings
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date']  = pd.to_datetime(df['Ship Date'])

# adding some useful columns
df['Year']    = df['Order Date'].dt.year
df['Month']   = df['Order Date'].dt.month
df['Quarter'] = df['Order Date'].dt.quarter

# focusing on 2017 vs 2016 - the most complete years
df16 = df[df['Year'] == 2016]
df17 = df[df['Year'] == 2017]

print(f"Years in dataset: {sorted(df['Year'].unique())}")

nulls = df.isnull().sum()
if nulls.sum() > 0:
    print("Found some nulls:", nulls[nulls > 0])
else:
    print("No missing values - data is clean")

print("\n" + "-"*55)
print("YEARLY REVENUE SUMMARY")
print("-"*55)

for yr in sorted(df['Year'].unique()):
    d = df[df['Year'] == yr]
    sales  = d['Sales'].sum()
    profit = d['Profit'].sum()
    margin = profit / sales * 100
    orders = d['Order ID'].nunique()

    print(f"\n{yr}:")
    print(f"  Revenue : ${sales:>10,.2f}")
    print(f"  Profit  : ${profit:>10,.2f}")
    print(f"  Margin  : {margin:>10.1f}%")
    print(f"  Orders  : {orders:>10,}")

s16 = df16['Sales'].sum()
s17 = df17['Sales'].sum()
p16 = df16['Profit'].sum()
p17 = df17['Profit'].sum()
o16 = df16['Order ID'].nunique()
o17 = df17['Order ID'].nunique()

print("\n" + "-"*55)
print("2017 vs 2016 - KEY CHANGES")
print("-"*55)
print(f"Revenue change : {(s17-s16)/s16*100:+.1f}%  (${s17-s16:+,.0f})")
print(f"Profit change  : {(p17-p16)/p16*100:+.1f}%  (${p17-p16:+,.0f})")
print(f"Orders change  : {(o17-o16)/o16*100:+.1f}%  ({o17-o16:+,} orders)")

print("\n" + "-"*55)
print("CATEGORY BREAKDOWN - 2017")
print("-"*55)

cat17 = df17.groupby('Category').agg(
    Sales=('Sales', 'sum'),
    Profit=('Profit', 'sum'),
    Orders=('Order ID', 'nunique')
).sort_values('Sales', ascending=False)
cat17['Margin %'] = (cat17['Profit'] / cat17['Sales'] * 100).round(1)
cat17['Share %']  = (cat17['Sales'] / s17 * 100).round(1)

print(f"\n{'Category':<20} {'Sales':>10} {'Profit':>10} {'Margin':>8} {'Share':>7}")
print("-"*57)
for cat, row in cat17.iterrows():
    print(f"{cat:<20} ${row['Sales']:>9,.0f} ${row['Profit']:>9,.0f} "
          f"{row['Margin %']:>7.1f}% {row['Share %']:>6.1f}%")

# tables losing money was a big finding
print("\n" + "-"*55)
print("SUB-CATEGORY - 2017")
print("-"*55)

subcat17 = df17.groupby('Sub-Category').agg(
    Sales=('Sales', 'sum'),
    Profit=('Profit', 'sum')
).sort_values('Profit', ascending=False)
subcat17['Margin %'] = (subcat17['Profit'] / subcat17['Sales'] * 100).round(1)

for sc, row in subcat17.iterrows():
    flag = " <- loss-making" if row['Profit'] < 0 else ""
    print(f"{sc:<20} ${row['Sales']:>9,.0f} ${row['Profit']:>9,.0f} "
          f"{row['Margin %']:>7.1f}%{flag}")

print("\n" + "-"*55)
print("REGIONAL BREAKDOWN - 2017")
print("-"*55)

reg17 = df17.groupby('Region').agg(
    Sales=('Sales', 'sum'),
    Profit=('Profit', 'sum')
).sort_values('Sales', ascending=False)
reg17['Margin %'] = (reg17['Profit'] / reg17['Sales'] * 100).round(1)

for reg, row in reg17.iterrows():
    print(f"{reg:<12} ${row['Sales']:>9,.0f} ${row['Profit']:>9,.0f} margin: {row['Margin %']:.1f}%")

print("\n" + "-"*55)
print("TOP 10 PRODUCTS - 2017")
print("-"*55)

top10 = df17.groupby('Product Name').agg(
    Sales=('Sales', 'sum'),
    Profit=('Profit', 'sum')
).sort_values('Sales', ascending=False).head(10)

for i, (prod, row) in enumerate(top10.iterrows(), 1):
    short = prod[:43] + '..' if len(prod) > 43 else prod
    print(f"{i}. {short} -> ${row['Sales']:,.0f}")

print("\n" + "-"*55)
print("NUMBERS TO CHECK AGAINST YOUR DASHBOARD")
print("-"*55)
print(f"""
  2017 Total Revenue  : ${s17:,.2f}
  2017 Total Profit   : ${p17:,.2f}
  2017 Profit Margin  : {p17/s17*100:.1f}%
  2017 Orders         : {o17:,}
  Tables profit/loss  : ${df17[df17['Sub-Category']=='Tables']['Profit'].sum():,.2f}
  West Region Revenue : ${df17[df17['Region']=='West']['Sales'].sum():,.2f}
  Tech Revenue        : ${df17[df17['Category']=='Technology']['Sales'].sum():,.2f}
""")
