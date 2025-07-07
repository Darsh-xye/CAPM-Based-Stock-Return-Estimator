# CAPM-Based-Stock-Return-Estimator

# 📈 CAPM-Based Stock Return Estimator

Welcome to the **CAPM Return Estimator**, a Python-driven financial analysis tool that applies the **Capital Asset Pricing Model (CAPM)** to estimate the **theoretical expected return** of a stock based on its exposure to systematic market risk.

> 🔍 Example used: **Apple Inc. (AAPL)** vs the **S&P 500 Index (^GSPC)**  
> 🛠️ Tools: `pandas`, `numpy`, `yfinance`, linear algebra, financial statistics

---

## 🧠 Motivation

In quantitative finance, asset pricing models like CAPM help investors answer a fundamental question:

> *"What return should I demand from a stock, given how risky it is relative to the market?"*

This project:
- Implements the CAPM from scratch
- Derives **beta** using empirical return data
- Benchmarks theoretical vs realized returns

---

## 📐 Mathematical Foundation

The **Capital Asset Pricing Model (CAPM)** estimates the expected return of an asset \( R_i \) as:

R_i = R_f + beta_i*(R_m - R_f)

Where:
- \( R_i \) = Expected return of asset \( i \)
- \( R_f \) = Risk-free rate
- \( R_m \) = Expected return of the market
- \( beta_i ) = Sensitivity of asset \( i \)'s return to market return (systematic risk)

The **beta coefficient** is defined as:

β= Cov(R_i, R_m) / Var(R_m)



---

## 🧮 What This Project Does

✔️ Downloads **daily adjusted close prices** using `yfinance`  
✔️ Computes **daily log returns** of both stock and market  
✔️ Calculates **Beta** empirically using the covariance matrix  
✔️ Applies **CAPM formula** to get the expected annual return  
✔️ Compares against the **actual realized return** from historical data  
✔️ Annualizes all return figures using 252 trading days convention  

---

## 🔍 Sample Output
Stock: AAPL

Beta: 1.199

Market Return (Annual): 16.34%

Expected Return (CAPM): 18.79%

Actual Return (Historical): 36.53%
