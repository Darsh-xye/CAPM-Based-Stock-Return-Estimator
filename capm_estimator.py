import pandas as pd
import numpy as np
import yfinance as yf

stock = 'AAPL'
market_compare = '^GSPC' 
start_date = '2019-01-01'
end_date = '2024-12-31'
risk_free_rate = 0.04  

stock_data = yf.download(stock, start=start_date, end=end_date)['Close']
market_data = yf.download(market_compare, start=start_date, end=end_date)['Close']

stock_returns = stock_data.pct_change().dropna()
market_returns = market_data.pct_change().dropna()

returns_df = pd.concat([stock_returns, market_returns], axis=1)
returns_df.columns = ['stock', 'market']
returns_df = returns_df.dropna()

cov_matrix = np.cov(returns_df['stock'], returns_df['market'])
beta = cov_matrix[0, 1] / cov_matrix[1, 1]

market_return_annual = returns_df['market'].mean() * 252
expected_return = risk_free_rate + beta * (market_return_annual - risk_free_rate)
actual_stock_return_annual = returns_df['stock'].mean() * 252

print(f"Stock: {stock}")
print(f"Beta: {beta:.3f}")
print(f"Market Return (Annual): {market_return_annual:.2%}")
print(f"Expected Return (CAPM): {expected_return:.2%}")
print(f"Actual Return (Historical): {actual_stock_return_annual:.2%}")

