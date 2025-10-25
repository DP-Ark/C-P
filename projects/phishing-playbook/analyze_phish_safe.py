import pandas as pd
import tldextract

df = pd.read_csv('phishing_samples.csv')
results = []

for _, row in df.iterrows():
    url = row['url']
    t = tldextract.extract(url)
    domain = f"{t.domain}.{t.suffix}" if t.suffix else t.domain
    results.append({
        'id': row['id'],
        'url': url,
        'domain': domain
    })

pd.DataFrame(results).to_csv('analysis_results.csv', index=False)
print("[+] Safe analysis complete -> analysis_results.csv")
