from bs4 import BeautifulSoup
import pandas as pd

# Read the HTML file
with open('file.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find the table
table = soup.find('table', {'class': 'live-trading'})

# Extract data
stocks = []
for row in table.find('tbody').find_all('tr'):
    cells = row.find_all('td')
    stocks.append({
        'Symbol': cells[0].text.strip(),
        'LTP': cells[1].text.strip(),
        '% Change': cells[2].text.strip(),
        'Open': cells[3].text.strip(),
        'High': cells[4].text.strip(),
        'Low': cells[5].text.strip(),
        'Quantity': cells[6].text.strip()
    })

# Create DataFrame and save
df = pd.DataFrame(stocks)
df.to_csv('stocks.csv', index=False)
print(f"Saved {len(df)} stocks to stocks.csv")
df = pd.read_csv('stocks.csv')
print(df)