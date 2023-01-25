import pandas as pd
import requests
import io

url = 'https://raw.githubusercontent.com/GabreioAPI/Teste2023/main/teste.csv'

s = requests.get(url).content
c = pd.read_csv(io.StringIO(s.decode('utf-8')))
#c = pd.read_csv(url)
print(c)
