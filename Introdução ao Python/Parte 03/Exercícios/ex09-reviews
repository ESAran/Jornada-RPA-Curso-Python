import pandas as pd
from IPython.display import display

df = pd.read_csv("https://alinedecampos.pro.br/etc/datasets/airbnb.csv") # caminho

df.info()

dataframe_novo = pd.DataFrame(df, columns=["id", "neighbourhood", "number_of_reviews", "last_review"])

display(dfn.sort_values("number_of_reviews", ascending=False).drop_duplicates("neighbourhood").head(10).filter(["id","last_review"]))
