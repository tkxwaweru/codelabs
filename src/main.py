import pandas as pd

# Path to the .xlsx file .
# Trial run
xlsx_file = "data\Test Files.xlsx"

df = pd.read_excel(xlsx_file)

df.info()
