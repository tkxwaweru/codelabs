import pandas as pd
#I dont like pandas, the big ones

# Path to the .xlsx file
xlsx_file = "../data/Test Files.xlsx"

df = pd.read_excel(xlsx_file)

df.info()
