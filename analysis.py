import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('bitstampUSD_1-min_data_2012-01-01_to_2018-11-11.csv.gz')
# Remove rows with all NA values except "Timestamp"
df = df.dropna(how='all', subset=['Open', 'High', 'Low', 'Close', 'Volume_(BTC)', 'Volume_(Currency)', 'Weighted_Price'])

df.set_index('Timestamp', inplace=True)  # Set 'Timestamp' as the index

# Calculate daily returns and volatility as mentioned in the previous answer

# Calculate daily returns by shifting the 'Close' column
df['Daily_Return'] = df['Close'].pct_change() * 100
window_size = 30
df['Volatility'] = df['Daily_Return'].rolling(window=window_size).std()

# Reset the index for plotting
df.reset_index(inplace=True)

# Convert 'Timestamp' column to a numpy array
x = df['Timestamp'].values

# Create the plot
plt.figure(figsize=(12, 6))
plt.plot(x, df['Volatility'].values, label='Volatility', color='blue')
plt.xlabel('Timestamp')
plt.ylabel('Volatility')
plt.title('Price Volatility Over Time')
plt.legend()
plt.grid()
plt.show()




