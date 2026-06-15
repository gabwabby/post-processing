import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\babyg\Downloads\successfulCombinedFile.csv')

# Convert to numeric
df['Time'] = pd.to_numeric(df['Time'], errors='coerce')
df['p']    = pd.to_numeric(df['p'],    errors='coerce')
df = df.dropna(subset=['Time', 'p'])

print(df.dtypes)  # Time and p should now show float64

plt.plot(df['Time'], df['p'])
plt.xlabel('Time')
plt.ylabel('p')
plt.title('p vs Time')
plt.show()