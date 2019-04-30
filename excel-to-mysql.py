import xlrd
import MySQLdb

# Open the workbook
book = xlrd.open_workbook("excel-file-name/location.xls")

# Establish a MySQL connection
database = MySQLdb.connect (host="host", user = "user", 
                                passwd = "password", db = "db name")

# Get the cursor
cursor = database.cursor()

# Change table char set encoding to utf-8

# Create the INSERT INTO sql query
query = """INSERT INTO table_name (column1, colum2, column3) VALUES (%s, %s, %s)"""

# Create a For loop to iterate through each sheet in the XLS file
for i in range(0,4):
    sheet = book.sheet_by_index(i)

    # Create a For loop to iterate through each row in the XLS file
    for r in range(0, sheet.nrows):
        column1_value = sheet.cell(r, 0).value
        column2_value = sheet.cell(r,1).value
        column3_value = sheet.cell(r, 2).value

        # Assign values from each row
        values = (column1_value, column2_value, column3_value)
        # Execute sql Query
        cursor.execute(query,values)

# Close the cursor
cursor.close()

# Commit the transaction
database.commit()

# Close the database connection
database.close()