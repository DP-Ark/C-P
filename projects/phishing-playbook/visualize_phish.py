import pandas as pd
import matplotlib.pyplot as plt

# Read analysis results
data = pd.read_csv('analysis_results.csv')

# Create a simple feature: domain length
data['domain_length'] = data['domain'].apply(len)

# Bar chart
plt.figure(figsize=(8,5))
data['domain_length'].plot(kind='bar', color='skyblue')
plt.title('Domain Length Analysis')
plt.xlabel('Sample Index')
plt.ylabel('Length of Domain')
plt.tight_layout()
plt.savefig('domain_length_chart.png')
print("[+] Chart saved as domain_length_chart.png")
