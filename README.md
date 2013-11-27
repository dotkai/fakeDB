fakeDB.py
======

Mimiking the basic functionality of a table-based database (aka, MySQL) while storing all data in a text file. Specifically, it extracts data from a table-formated file, converts it into a dictionary format, and can be manipulated by a user. Saving the database will convert everything back to the table-formated file. 

This is for fun and not recommended to actual use. Unless you like text files with easily alterable data (Perks, you can see what you are doing). This was an experimet and I will likely do one for other languages as well.

By Kai "Bring It On" Austin

October 2013

Use
-----------

Note that the database is comprised of 3 different objects:

  * **DB** - The whole database, comprised of tables
  * **Table** - A table with specified columns and rows formated according to those columns
  * **Row** - A row in a table with data

The table formatting, if desired to be edited manually via the txt file.

  1. Name the table
  2. List the names of the desired columns, seperated by pipes
  3. The rows begin here, with each element in the row cooresponding to its respective column

```txt
TABLE_NAME: (Example)
(COLUMN-NAME-1) | (COLUMN-NAME-2) | (COLUMN-NAME-3) |
(element-a1) | (element-a2) | (element-a3) |
(element-b1) | (element-b2) | (element-b3) |
...
```

Spaces are acceptable and capitalization does not matter. However I prefer to write the column names in all caps for easy read purposes

*Note: There are no auto generated ids. If you want them, make a custom column for it.*


Opening and Saving the Database
-----------

**To MAKE a new Database, or retrieve an existing:**
```python
myDB = fakeDB.DB()
```

This requires the existence of the default text file "fakeDBdata.txt." You are welcome to remove all its default contents before continuing on (i.e. myDB.deleteTable("Example") - this will be covered later).

There is also the option to make a database with a custom file.
```python
myDB = fakeDB.DB("myCustomFile.txt")
```

**To SAVE the Database:**

To save the database to the dafault file ("fakeDBdata.txt"), then use.
```python
myDB.save()
```

To save to a custom file,
```python
myDB.save("myCustomFile.txt")
```

***FYI, you MUST *.save() your database when you are done processing it, otherwise it will not write to the file and you will loose all your changes.***

Making a Table
-----------
**To MAKE a new Table**

```python
myTable = fakeDB.Table("myTableName")
```

This will have no columns or rows. As a minimum, you must speficy the table's name.

**To make a table with specified columns**

```python
myTable = fakeDB.Table("myTableName", [ "COL-1", "COL-2", ...])
```

This will create a table with the specified columns. Column names are stored as string in an array/list. You will not be able to add rows unless there are corresponding columns.

**To make a table with predetermined rows and columns**

```python
myTable = fakeDB.Table("myTableName", [ "COL-1", "COL-2", ...], [ RowObject, RowObject, ...])
```

This will create a table with all specified columns and rows. Please note that the rows are Row objects. Do not pass in any other data type. If you wish to make a new row, keep reading.

Once again, as a reminder, this database does not make unique ids for each row. Instead, each row corresponds to the location in the table's row array/list. The first row added will have an index of 0, the next an index of 1, etc.


Making a Row
-----------

**To MAKE a new row**
```python
aRow = fakeDB.Row()
```

This will create a new empty row. When put into a table, it will adapt the columns, however all elements corresponding to the columns will be empty strings.

**To MAKE a row with existing data**
```python
rowData = {"COL-1": "myName", "COL-2": "20", ...}
aRow = fakeDB.Row(rowData)
```

Pass a dictionary with the keys corresponding to the columns of a table, and their respective values. Note, that is one of the keys does not correspond to a value in the table, it will be ignored. All unspecified keys will obtain empty values.

Documentation
-----------

Class | Function | Parameters | Description/Use |
 ------------ | :-----------: | ----------- | ----------- |
DB     |   ``` getTable(table_name)```    |  table_name = *STRING, the name of a table* | Gets the specified table from a database; *RETURNS DICTIONARY*  |
DB     |   ``` printTable(table_name)```    |  table_name = *STRING, the name of a table* | Prints out all the information in the table row by row  |
DB     |   ``` makeTable(table_name, colist)```    |  table_name = *STRING, the name of the new table*;  colist = *LIST, the list of columns to be in the table* | Prints out all the information in the table row by row  |
DB     |   ``` deleteTable(table_name)```    |  table_name = *STRING of the name of the table to delete* | Deletes a table from the database  |
Table     |   ``` newCol(col_name) ```    |  col_name = *STRING with the name of the new column* | Makes a new column in the specified table  |
Table     |   ``` removeCol(col_name) ```    |  col_name = *STRING with the name of the column to delete* |  Removes a column from the table, including every element which is in that column for all respective rows  |
Table     |   ``` printCols() ```    |  (none) |  Prints out a LIST of all the columns in a table  |
Table     |   ``` gettCols() ```    |  (none) |  Returns a LIST of all the columns in a table  |
Table     |   ``` newRow(row_data) ```    |  row_data = *DICTIONARY with all the data to make a row* |  Makes a new row in the specified table;  IF there is no value corresponding to a column, it will be skipped; IF a key in row_data is not a column in the table, it will be skipped  |
Table     |   ``` deleteRow(key, value) ```    |   key = *STRING with the column name*; value = *STRING with the row's data corresponsing to the key* |  Removes the first row from a table that contains the key and value pair  |
Table     |   ``` getRow(key, value) ```    |   key = *STRING with the column name*; value = *STRING with the row's data corresponsing to the key* |  Gets a row with the specified key and value pair  |
Table     |   ``` printRows() ```    |  (none) |  Prints all the rows in the table  |
Row     |   ``` printRow() ```    |  (none) |  Prints the specified row  |
Row     |   ``` update(key, value) ```    |  key = *STRING with the column name*; value = *STRING with the row's data corresponsing to the key* |  Updates the data in a row corresponding to the specified column  |
[documentation table]
