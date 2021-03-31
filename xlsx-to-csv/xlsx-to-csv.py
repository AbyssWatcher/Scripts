import sys
import os
import time
import pandas as pd
import openpyxl
"""
- Converts a .xlsx file to a .csv file.
- Only works with Unix filepaths.
- The .xlsx file must be in the same directory as the script.
- The converted .csv file is formed in the current working directory.

https://realpython.com/openpyxl-excel-spreadsheets-python
https://www.studytonight.com/post/converting-xlsx-file-to-csv-file-using-python
https://openpyxl.readthedocs.io/en/stable/pandas.html
https://realpython.com/python-command-line-arguments

https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
https://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python
https://stackoverflow.com/questions/16923281/writing-a-pandas-dataframe-to-csv-file
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html
https://stackoverflow.com/questions/39399712/delete-pandas-column-with-no-name/39399747
https://stackoverflow.com/questions/49551336/pandas-trim-leading-trailing-white-space-in-a-dataframe
https://stackoverflow.com/questions/46081177/save-data-frame-as-csv-text-file-in-pandas-without-line-numbering

https://stackoverflow.com/questions/65250207/pandas-cannot-open-an-excel-xlsx-file
- Your version of xlrd is 2.0.1. In xlrd >= 2.0, only the xls format is supported. Install openpyxl instead.
"""
def main():
	if len(sys.argv) < 1:
		print("ERROR: No arguments given.")
	try:
		for file_name in sys.argv[1:]:
			start_time = time.time()
			xlsx_df = pd.read_excel(file_name, engine='openpyxl') # Uses openpyxl to work with .xlsx files.
			xlsx_df = xlsx_df.applymap(lambda x: x.strip() if isinstance(x, str) else x) # Deletes trailing whitespace.
			tail = os.path.split(file_name)[1] # Splits the path into path_head and path_tail (filename and extension).
			xlsx_df.to_csv(os.getcwd() + "/" + os.path.splitext(tail)[0] + ".csv", index=None) # Writes to a new .csv file.
			execution_time = (time.time() - start_time)
			print(f"Converting {file_name} took: {str(execution_time)} seconds.") # Prints the how long the conversion takes.
	except:
		print("ERROR: An error occured.")
if __name__ == "__main__":
	main()