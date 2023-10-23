import pandas as pd
from IPython.display import display

df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv") # caminho

df.info()

df.filter([["neighbourhood"] == "Urca", "id", "name", "room_type", "price"]).sort_values("price", ascending=False).head(1)
