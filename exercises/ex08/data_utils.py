"""Dictionary related utility functions."""

__author__ = "730484794"

# Define your functions below
from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    file_handle = open(filename, "r", encoding="utf8")

    csv_reader = DictReader(file_handle)

    for row in csv_reader:
        result.append(row)
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
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


def head(col_table: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Produce a new col-oriented table with first n rows."""
    result: dict[str, list[str]] = {}
    for cols in col_table:
        new_list: list[str] = []
        for item in col_table:
            new_list.append(item)
    return result


def select(table: dict[str, list[str]], col_names: list[str]) -> dict[str, list[str]]:
    """Select function."""
    result: dict[str, list[str]] = {}
    for item in col_names:
        result[item] = table[item]
    return result


def concat(table1: dict[str, list[str]], table2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Concatenate two tables."""
    result: dict[str, list[str]] = {}
    for key in table1:
        result[key] = table1[key]
    for key in table2:
        if key in result:
            result[key] += table2[key]
        else:
            result[key] = table2[key]
    return result


def count(list: list[str]) -> dict[str, int]:
    """Count the number of times each value appears in a list."""
    result: dict[str, int] = {}
    for item in list:
        if item in result:
            result[item] += 1
        else:
            result[item] = 1
    return result
