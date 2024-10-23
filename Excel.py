##LEER HOJA DE EXCEL

import pandas as pd
import openpyxl

archivo ='C:/Users/manel/Desktop/Numeros_primitiva.xlsx'
df=pd.read_excel(archivo, sheet_name='Hoja1')
print(df)

df2=pd.to_excel('pandas_to_excel_no_index_header.xlsx', index=True, header=True)
df2 = df[['a', 'c']]
print(df2)
