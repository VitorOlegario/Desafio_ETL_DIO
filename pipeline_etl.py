from usuarios_etl import usuarios
import pandas as pd

conta = [usuario for usuario in usuarios]

salvar = pd.DataFrame(conta)
salvar.to_csv("usuarios3.csv", index=None)