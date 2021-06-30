import requests
import openpyxl

base_url = 'https://image.cingta.com/'
lst = []
wb = openpyxl.load_workbook('cingta网图片.xlsx')

sheet = wb.active

for x, row in enumerate(sheet.rows, start=1):
    if x > 1:
        value = sheet.cell(x, 3).value
        lst.append(f"{base_url}{value}")

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'
}
for x, url in enumerate(lst):
    res = requests.get(url, header)
    with open(f'{x}.jpg', 'wb') as f:
        f.write(res.content)
