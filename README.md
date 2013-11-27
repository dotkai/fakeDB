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


Making and using the Database
-----------

**To make a new Database:**
```python
myDB = fakeDB.DB()
```

This requires the existence of the default text file "fakeDBdata.txt." You are welcome to remove all its default contents before continuing on (i.e. myDB.deleteTable("Example") - this will be covered later).

There is also the option to make a database with a custom file.
```python
myDB = fakeDB.DB("myCustomFile.txt")
```

**To save the Database:**

To save the database to the dafault file ("fakeDBdata.txt"), then use.
```python
myDB.save()
```

To save to a custom file,
```python
myDB.save("myCustomFile.txt")
```

***FYI, you MUST *.save() your database when you are done processing it, otherwise it will not write to the file and you will loose all your changes.***

Class | Function | Parameters | Description/Use |
 ------------ | :-----------: | :-----------: | -----------: |
DB     |   Cell Bold    |         Cell |
New section   |     More      |         Data |
And more      |            And more          |
[documentation table]
