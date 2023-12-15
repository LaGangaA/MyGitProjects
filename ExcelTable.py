##############################################################################
#
# An example of adding a dataframe to an worksheet table in an xlsx file
# using Pandas and XlsxWriter.
#
# Tables in Excel are used to group rows and columns of data into a single
# structure that can be referenced in a formula or formatted collectively.
#
# SPDX-License-Identifier: BSD-2-Clause
# Copyright 2013-2023, John McNamara, jmcnamara@cpan.org
#

import pandas as pd
import xlsxwriter as xl
# define the startig row and column
r=1
c=2

# Create a Pandas dataframe from some data.
df = pd.DataFrame(
    {
        "Country": ["China", "India", "United States", "Italia","Spagna","Cile"],
        "Population": [1404338840, 1366938189, 330267887, 269603400,2222,9996660],
        "Rank": [1, 2, 3, 4, 5, 6],
    },
)
# Order the columns if necessary.
df = df[["Rank", "Country", "Population"]]

# Create a Pandas Excel writer using XlsxWriter as the engine.
writer = pd.ExcelWriter("pandas_table.xlsx", engine="xlsxwriter")

# Write the dataframe data to XlsxWriter. Turn off the default header and
# index and skip one row to allow us to insert a user defined header.
df.to_excel(writer, sheet_name="Prova", startrow=r+1, startcol=c, header=False, index=False)

# Get the xlsxwriter workbook and worksheet objects.
workbook = writer.book
worksheet = writer.sheets["Prova"]

# Get the dimensions of the dataframe.
(max_row, max_col) = df.shape

# Create a list of column headers, to use in add_table().
column_settings = [{"header": column} for column in df.columns]

# Add the Excel table structure. Pandas will add the data.
worksheet.add_table(r, c, max_row+r, max_col+c - 1, {"columns": column_settings})

# Make the columns wider for clarity.
worksheet.set_column(r, max_col+c - 1, 12)

# Close the Pandas Excel writer and output the Excel file.

# Create a new workbook and add a worksheet
worksheet = workbook.add_worksheet('Calcoli')
bold_format = workbook.add_format({'bold': True})
blue_format = workbook.add_format({'font_color': 'blue'})
red_format = workbook.add_format({'bg_color': 'red'})
green_format = workbook.add_format({'bg_color': 'green'})

# Write some test data.
worksheet.write("B1", 500,bold_format)
worksheet.write("B2", 10,blue_format)
worksheet.write("B5", 1,red_format)
worksheet.write("B6", 2,green_format)
worksheet.write("B7", 3)
worksheet.write("C1", 300)
worksheet.write("C2", 15)
worksheet.write("C5", 20234)
worksheet.write("C6", 21003)
worksheet.write("C7", 10000)


# Write an array formula that returns a single value
worksheet.write_formula("A1", "{=SUM(B1:C1*B2:C2)}")
# Same as above but more verbose.
worksheet.write_array_formula("A2:A2", "{=SUM(B1:C1*B2:C2)}")

# Write an array formula that returns a range of values
worksheet.write_array_formula("A5:A7", "{=TREND(C5:C7,B5:B7)}")

workbook.close()
writer.close()