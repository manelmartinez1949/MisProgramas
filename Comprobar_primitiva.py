##Comprobar Primitiva
from openpyxl import Workbook
from openpyxl.styles import Font

book=Workbook()
sheet=book.active
sheet  ['A1']=6
sheet  ['B1']=19
sheet  ['C1']=30
sheet  ['D1']=32
sheet  ['E1']=34
sheet  ['F1']=42

book.save('Numeros_primitiva.xlsx')
