'''
fakeDB.py
Mimiking the basic functionality of a table-based database while storing all data in a text file. This is for fun and not recommended to actual use.
Unless you like text files with easily alterable data (security is horrific).
And FYI, you MUST *.save() your database when you are done processing it, otherwise it will not write to the file.
By Kai "Bring It On" Austin
October 2013
'''

import random

# ***** PARSING FUNCTIONS *****

def parsCols(string):
    '''
    RETURNS LIST
    Converting the row specifying columns to a string
        string = STRING of the file specifying what the columns are
    '''
    colist = []
    col = ''
    for char in string:
        if char != '|':
            col += char
        else:
            colist.append(col.strip())
            col = ''
    return colist

def parsRow(string, colist):
    '''
    RETURNS DICTIONARY
    Converts a row of items to a dictionary based on the col=>row pointers
        string = STRING from a file row, eg. x | y | z |
        colist = LIST with the names of the columns the table has
    '''
    rowdict = {}
    colpos = 0
    row_word = ''
    for char in string:
        if char != '|':
            row_word += char
        else:
            current_pointer = colist[colpos].strip()
            rowdict[current_pointer] = row_word.strip()
            colpos += 1
            row_word = ''
    return rowdict

def dbToRow(colist, row_dict):
    ''' 
    PARSES A ROW=>STRING
    Turns a row in the floating database into a properly formated string
    in the file database.
    Any item in the row which is not a specified column will be skipped.
        colist = LIST with the names of the columns the table has
        row_dict = DICTIONARY form of a row in the database
    '''
    fileRow = ''
    #Start by getting the right order of the columns
    for col in colist:
        if col in row_dict:
            fileRow += row_dict[col] + ' | '
        else:
            fileRow += " | "
    
    return fileRow

def dbToCol(colist):
    ''' 
    PARS A COLUMN=>STRING 
    Turns a table's columns in the floating database into a properly formated string.
        colist = LIST of a table's columns
    '''
    fileRow = ''
    for col in colist:
        fileRow += col + ' | '
    return fileRow

# ***** DATABASE AND OBJECTS *****

class DB:
    '''
    The Database Object. Of Doom.
    Basic formatting when "floating": 
    { TABLE_NAME: 
        {   
            COLUMNS: [COL1, COL2], 
            ROWS: [ {
                    COL1: VALUE1, 
                    COL2: VALUE2
                    }] } }
    '''
    def __init__(self, filename):
        ''' Initializing the database  '''
        self.tables = self.unpack(filename)
        
    def unpack(self, db_file = 'fakeDB.txt'):
        '''
        RETURNS DICTIONARY
        Unpacks database and stores it
            db_file = the name of the file where the database is stored
        '''
        database = {}
        flines = []
        f = open(db_file, 'r')
        
        onLine = 1
        workingTable = ''
        
        for line in f:
            #remove empty lines
            if line != '\n':
                line = line.replace('\n', '')
                #Check to see if table name, or line after table name
                if 'TABLE_NAME' in line:
                    #Reset everything so no overlapping data
                    if database:
                        database[workingTable].rows = flines
                        flines = []
                    #Gettign the table name and 
                    line = line.replace('TABLE_NAME: ', '')
                    database[line] = Table(line)
                    workingTable = line
                    #Next line should specify the column => Row pointers
                    onLine = 2
                elif onLine == 2:
                    #Get the names of the keys
                    database[workingTable].cols = parsCols(line)
                    onLine = 3
                elif onLine >= 3:
                    flines.append(Row(parsRow(line, database[workingTable].cols)))
                else:
                    print 'ERROR: Database not initialized'
        f.close()
        if database:
            #If the database is not empty, add everything left
            database[workingTable].rows = flines
            return database
        else:
            print 'Your Database is empty...'
            return {}
        
    def save(self, db_file = 'fakeDBdata.txt'):
        '''
        OVER-WRITES TXT FILE
        Over rights everything in the txt file with all the new information
            db_file = STRING with the name of the desired database destination
        '''
        f = open(db_file, 'w')
        
        for table in self.tables:
            #For each table in the database
            #Write the name of the table
            table_name = 'TABLE_NAME: ' + self.getTable(table).name + '\n'
            f.write(table_name)
            #Write the column names
            cols = self.getTable(table).cols
            col_names = dbToCol(cols) + '\n'
            f.write(col_names)
            #Now print all the rows
            all_rows = self.getTable(table).rows
            for row in all_rows:
                rowString = dbToRow(cols, row.data) + '\n'
                f.write(rowString)
            #Space between tables
            f.write('\n')
            
        f.close()

    
    def getTable(self, table_name):
        '''
        RETURNS DICTIONARY
        Gets the specified table from a database
            table_name = STRING, the name of a table
        '''
        return self.tables[table_name]
    
    def printTable(self, table_name):
        '''
        PRINTS table_name
        Prints out all the information in the table
            table_name = STRING the name of the table
        '''
        table = self.tables[table_name]
        print table.name
        table.printCols()
        table.printRows()
    
    def newTable(self, table_name, colist):
        '''
        MAKES A NEW TABLE IN THE DB
        Note that this is distinct from unpacking as colist (columns in the table) is known
            myDB = DICT, the database to add the table to
            table_name = STRING, the name of the new table
            colist = LIST, the list of columns to be in the table
        '''
        self.tables[table_name] = Table(table_name, colist, [])
    
    def deleteTable(self, table_name):
        ''' 
        DELETES TABLE FROM DATABASE 
            table_name = STRING of the name of the table to delete
        '''
        del self.tables[table_name]

class Table:
    '''
    The table with rows and names and glorious awesomeness
    Tables when printed look like this:
    TABLE_NAME: Awesome
    Level | Name | Special Skill |
    9001 | Kamina | Leader |
    1000 | Yoite | Kira |
    '''
    def __init__(self, name, cols = [], rows = []):
        self.name = name
        self.cols = cols
        self. rows = rows
        
    def newCol(self, col_name):
        '''
        ADDS STRING TO TABLE.COLS
        Makes a new column in the specified table
            col_name = STRING with the name of the new column
        '''
        #Update the column list
        self.cols.append(col_name)
        #Update every row to be initially empty
        for row in self.rows:
            row.data[col_name] = ''
            
    def deleteCol(self, col_name):
        ''' 
        DELETES STRING IN TABLE.COLS AND KEY IN ALL TABLE.ROW
        Removes a column from the table, including every element which
        is in that column for all respective rows
            col_name = STRING with the name of the column
        '''
        #Delete columns from a row
        for row in self.rows:
            del self.row[col_name]
        
        #Delete the column from self.cols
        self.cols.remove(col_name)
         
    
    def printCols(self):
        ''' PRINTS OUT THE LIST OF ALL COLUMNS IN A TABLE'''
        print self.cols
    def getCols(self):
        ''' RETURNS LIST OF ALL COLUMNS IN THE TABLE '''
        return self.cols

    def newRow(self, row_data):
        '''
        ADDS NEW ROW TO TABLE.ROW
        Makes a new row in the specified table
            row_data = DICTIONARY with all the data to make a row
                IF there is no value corresponding to a column, it will be skipped
                IF a key in row_data is not a column in the table, it will be skipped
        '''
        #Get all the columns to correspond to a row
        allcols = self.cols
        set_row = Row()
        for i in allcols:
            #Check to see if there is a corresponding column for a specific row section
            if i in row_data:
                set_row.data[i] = row_data[i]
            else:
                #If not specified, then set the space to empty
                set_row.data[i] = ''
        #Everything check
        self.rows.append(set_row)
    
    def deleteRow(self, key, value):
        ''' 
        DELETES ROW IN TABLE.ROW
        Removes the first row from a table that contains the key and value pair
            key = STRING with the column name
            value = STRING with the row's data corresponsing to the key
        '''
        for row in self.rows:
            if row.data[key] == value:
                self.rows.remove(row)
                break
    
    def getRows(self, key, value):
        ''' 
        RETURNS LIST OF ROWS 
        Gets a row with the specified key and value pair
            key = STRING with the column name
            value = STRING with the row's data corresponsing to the key
        '''
        retrieved = []
        for row in self.rows:
            if row.data[key] == value:
                retrieved.append(row)
        return retrieved
        
    def printRows(self):
        ''' PRINTS ALL ROWS IN TABLE.ROW '''
        for row in self.rows:
            row.printRow()

class Row:
    ''' A row. Of Doom. '''
    def __init__(self, parsed = {}):
        '''
        MAKES ROW
            parsed = DICTIONARY of previously defined data to be put in the row
        '''
        #Make a row here
        self.data = {}
        #Check if there is parsed data to add, then add it
        if len(parsed) != 0:
           for key in parsed:
               self.data[key] = parsed[key] 
               
    def printRow(self):
        ''' PRINTS ROW '''
        print self.data
        
    def update(self, key, newValue):
        ''' 
        UPDATES DATA
        Updates the data in a row corresponding to the specified column
        '''
        self.data[key] = newValue
        
        
if __name__ == '__main__':
    print 'Please use another file to create your functions.'