import pandas as pd
from IPython.display import display

df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv") # caminho

df.info()

dataframe_novo = pd.DataFrame(df, columns=["id", "neighbourhood", "number_of_reviews", "last_review"])

display(df[(df["neighbourhood"] == 'Lagoa')].sort_values("last_review", ascending=False).head(5).filter(["name","neighbourhood","last_review"]))

