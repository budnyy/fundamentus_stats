import pandas as pd

file_name = 'acoes-09-05.csv'

#Importação de dados
df = pd.read_csv(file_name, sep=";", index_col = "Papel", decimal = ",") 

#Retirada de indicadores não utilizados
df.drop(df.columns[[3,5,6,7,8,9,10,11,12,13,14,15,18]], axis = 1, inplace = True)

#Formatação de dados
df = df.replace(to_replace="%", value= '', regex = True)
df = df.replace(to_replace="\\.", value= '', regex = True)
df = df.replace(to_replace=",", value= '.', regex = True)

df = df.apply(pd.to_numeric, errors = "coerce")

df["Div.Yield"] = df["Div.Yield"].map(lambda x: x / 100)
df["ROE"] = df["ROE"].map(lambda x: x / 100)
df["Cresc. Rec.5a"] = df["Cresc. Rec.5a"].map(lambda x: x / 100)

# #Criar coluna ranking
df.insert(loc=8, column="Ranking", value=0) 

#Função para atribuir pontuação 
def compararIndicadores(row : pd.Series):
    if row["P/L"] > 3.0 and row["P/L"] < 10.0:
        row["Ranking"] += 1
    if row["P/VP"] > 0.5 and row["P/VP"] < 2.0:
        row["Ranking"] += 1
    if row["Div.Yield"] > 0.07 and row["Div.Yield"] < 0.14:
        row["Ranking"] += 1
    if row["ROE"] > 0.15 and row["ROE"] < 0.3:
        row["Ranking"] += 1
    if row["Liq.2meses"] > 1000000.0:
        row["Ranking"] += 1
    if row["Cresc. Rec.5a"] > 0.1:
        row["Ranking"] += 1
    return row["Ranking"]

df["Ranking"] = df.apply(lambda row: compararIndicadores(row), axis=1)

###

print("Ações com pontuação 6")
print(df[df["Ranking"] == 6])
print("Ações com pontuação 5")
print(df[df["Ranking"] == 5])