import pandas as pd
from IPython.display import display

df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv") # caminho

df.info()

dataframe_novo = pd.DataFrame(df, columns=["id", "name", "neighbourhood", "room_type", "price"])
display(dataframe_novo)
