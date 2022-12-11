from googleapiclient.discovery import build
from google.oauth2 import service_account
import json

# sheet: https://docs.google.com/spreadsheets/d/1KEftBJQWb5CgXZUJUS2NJcQ-_sNieAIY9znBFghE3CU/edit#gid=0

SAMPLE_SPREADSHEET_ID = '1KEftBJQWb5CgXZUJUS2NJcQ-_sNieAIY9znBFghE3CU'

def connect():
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    SERVICE_ACCOUNT_FILE = 'key.json'
    creds = None
    creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    return sheet

def format(val):
    dic = []
    for i in range(1, len(val)):
        if len(val[i]) > 0:
                dic.append({ val[0][0] : val[i][0], val[0][1] : val[i][1]})
    return dic


def read():
    sheet = connect()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="sheet1!A1:B50").execute()
    values = result.get('values', [])
    return format(values)
    
def create(email , name):
    sheet = connect()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="sheet1!A1:B50").execute()
    values = result.get('values', [])

    for i in range(1,len(values)):
        if len(values[i]) > 0:
             if values[i][1] == email:
                     return False
    data = [[name , email ]]
    creat = sheet.values().append(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        range="sheet1!A1:B1",
        body={"values" : data},
                valueInputOption="USER_ENTERED",
                insertDataOption= "INSERT_ROWS"  
        ).execute()
    return True

def delete(email):
    sheet = connect()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="sheet1!A1:B50").execute()
    values = result.get('values', [])
    for i in range(len(values)):
            if len(values[i]) > 0:
                if values[i][1] == email:
                    request_body = {
                        "requests": [
                            {
                            "deleteDimension": {
                                "range": {
                                "sheetId": 0,
                                "dimension": "ROWS",
                                "startIndex": i,
                                "endIndex": i+1
                                }
                            }
                            }
                        ],
                    }
                    sheet.batchUpdate(
                        spreadsheetId =  SAMPLE_SPREADSHEET_ID,
                        body = request_body
                    ).execute()
                    return True
    return False


def update(email , name):
    sheet = connect()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="sheet1!A1:B50").execute()
    values = result.get('values', [])
    for i in range(len(values)):
            if len(values[i]) > 0:
                if values[i][1] == email:
                    delete(email)
                    data = [[name , email ]]
                    update = sheet.values().append(
                        spreadsheetId=SAMPLE_SPREADSHEET_ID,
                        range="sheet1!A" + str(i+1)+":B"+str(i+1),
                        body={"values" : data},
                                valueInputOption="USER_ENTERED",
                                insertDataOption= "INSERT_ROWS"  
                        ).execute()
                    return True
    return False

