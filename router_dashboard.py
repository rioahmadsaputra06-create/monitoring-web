import pandas as pd
import matplotlib.pyplot as plt

# 1. Data JSON
data = [
    {"name": "Router A", "status": "online", "bandwidth": 28},
    {"name": "Router B", "status": "offline", "bandwidth": 35},
    {"name": "Router C", "status": "online", "bandwidth": 32}
]

# 2. Buat tabel dengan pandas
df = pd.DataFrame(data)

# Tampilkan tabel
print("Tabel Status Router:")
print(df)

# 3. Buat grafik batang
colors = ['green' if status == 'online' else 'red' for status in df['status']]
plt.bar(df['name'], df['bandwidth'], color=colors)
plt.xlabel('Nama Router')
plt.ylabel('Bandwidth (Mbps)')
plt.title('Status dan Bandwidth Router')
plt.show()
