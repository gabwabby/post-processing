import pandas as pd 
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\babyg\Downloads\successfulCombinedFile.csv')

df['Time'] = pd.to_numeric(df['Time'], errors='coerce')
df['p']    = pd.to_numeric(df['p'],    errors='coerce')
df = df.dropna(subset=['Time', 'p'])

N = 3  
mean = df['p'].mean()
std  = df['p'].std()
df['is_spike'] = (df['p'] - mean).abs() > N * std

spikes = df[df['is_spike']]
print(f"Found {len(spikes)} spikes")
print(spikes[['Time', 'p']])

spikes[['Time', 'p']].to_csv(r'C:\Users\babyg\Downloads\pressure_spikes.csv', index=False)
print("Spikes saved to pressure_spikes.csv")

# --- Plot ---
plt.figure(figsize=(12, 5))
plt.plot(df['Time'], df['p'], label='Pressure', color='steelblue', linewidth=0.8)
plt.scatter(spikes['Time'], spikes['p'], color='red', zorder=5, label='Spikes', s=40)
plt.xlabel('Time')
plt.ylabel('Pressure (p)')
plt.title('Pressure vs Time — Spikes Highlighted')
plt.legend()
plt.tight_layout()
plt.savefig(r'C:\Users\babyg\Downloads\pressure_spikes_plot.png', dpi=150)
plt.show()
