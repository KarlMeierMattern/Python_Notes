import tabula

# set the input and output file paths
pdf_file_path = 'C:/Users/kmeiermatt001/Desktop/Arixcel_Invoice_58864.pdf'
excel_file_path = 'C:/Users/kmeiermatt001/Desktop/Book2.xlsx'

# extract the data from the PDF and convert to a DataFrame
df = tabula.read_pdf(pdf_file_path, pages='all')

# save the DataFrame as an Excel file
df.to_excel(excel_file_path, index=False)

print(10+5)