import pandas
import openpyxl

def excel_divider(filepath, num_files):
    """
    splits an excel file into a specified number of files.

    Args:
        filepath: Path to the Excel file.
        num_files: The desired number of output files.

    Returns:
        files divided from the original Excel file.
    """

    # read the Excel file
    df = pandas.read_excel(filepath)

    # Header
    header = df.columns.values

    # get the number of rows in the excel file and divide by the number of files
    chunk_size = len(df) // num_files

    # get the remainder of the division
    left_over = chunk_size % num_files

    # Iterate through the number of files
    

excel_divider("test_file.xlsx", 5)