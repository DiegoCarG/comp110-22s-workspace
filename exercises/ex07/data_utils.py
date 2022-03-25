"""Some helpfuly utility functions for working with CSV files."""

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []
    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")
    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    # Read each row of CSV line by line
    for row in csv_reader:
        result.append(row)
    # Close the file when we're done, to free its resources
    file_handle.close()

    return result


def column_values(tablee: list[dict[str, str]], column: str) -> list[str]:  
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in tablee:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


"""Dictionary related utility functions."""

__author__ = "730427471"

# Define your functions below


def head(orig: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Make column based table with only first n rows of each column."""
    result: dict[str, list[str]] = {}
    
    for key in orig:
        i = 0
        if len(orig[key]) < n:
            n = len(orig[key])
        values: list[str] = []
        while i < n:
            values.append(orig[key][i])
            i += 1
        result[key] = values

    return result


def select(orig: dict[str, list[str]], cols: list[str]) -> dict[str, list[str]]:
    """Return table but only with specified columns."""
    result: dict[str, list[str]] = {}
    for column in cols:
        result[column] = orig[column]

    return result
                

def concat(table_1: dict[str, list[str]], table_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Takes two tables and creates one table."""
    result: dict[str, list[str]] = {}
    
    for key in table_1:
        result[key] = table_1[key]

    for key in table_2:
        if key in result:
            result[key] += table_2[key]
        else:
            result[key] = table_2[key]

    return result


def count(a_list: list[str]) -> dict[str, int]:
    """Create dictionary where the key is an element of the list and the value is the amount of times it shows up in the list."""
    mydict: dict[str, int] = {}

    for item in a_list:
        if item in mydict:
            mydict[item] += 1
        else:
            mydict[item] = 1

    return mydict

        

        

            

            



    
        
