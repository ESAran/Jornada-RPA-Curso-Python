import pandas as pd
from IPython.display import display

df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv") # caminho

df.info()

dataframe_novo = pd.DataFrame(df, columns=["id", "name", "neighbourhood", "room_type", "price"])

media = dataframe_novo.loc[dataframe_novo['room_type'] == 'Entire home/apt', 'price'].mean()
print("preço médio = " + str(media))
