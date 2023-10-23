import pandas as pd
from IPython.display import display

df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv") # caminho

df.info()

dataframe_novo = pd.DataFrame(df, columns=["id", "name", "neighbourhood", "room_type", "price"])

quantidade = dataframe_novo[
    (dataframe_novo["neighbourhood"] == "Copacabana") &
    (dataframe_novo["price"] >= 500) &
    (dataframe_novo["price"] <= 700)
].shape[0]

print("quantidade de hoteis em Copacabana entre 500 e 700 é de: " + str(quantidade))
