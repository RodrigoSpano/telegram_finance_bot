import gspread
# import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path="./.env")

sheet_name = os.getenv("SHEET_NAME")
print(sheet_name)
# define the scope
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

# add credentials to the account
creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)

# authorize the clientsheet 
client = gspread.authorize(creds)

# get the instance of the Spreadsheet
sheet = client.open(sheet_name).sheet1
# sheet = client.open("nohayplata_bot").sheet1

# get the first sheet of the Spreadsheet
# row_test=["pepe","juanito",123]
# sheet.insert_row(row_test, 6)

# data => messages format [amount,item,category] 
def write_available_row(data):
    total_rows = sheet.row_count
    available_row = False

    for row in range(2, total_rows + 1):
        if len(sheet.row_values(row)) == 0:
            sheet.insert_row(data, row)
            available_row = True
            break

    if not available_row:  # Add new row if there isnt
        sheet.insert_row(data, total_rows + 1)


def clear_sheet():
    sheet.clear()