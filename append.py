import pandas as pd
df_full = pd.read_csv(r"dati-comuni/izsam-covid19-ita-comuni.csv")
df_last = pd.read_csv(r"dati-comuni/izsam-covid19-ita-comuni-20200321.csv")
complete_df = df_full.append(df_last)
complete_df.sort_values(by='data', ascending=False)
complete_df.to_csv(r'dati-comuni/izsam-covid19-ita-comuni.csv',index=False)
