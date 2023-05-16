from googleapiclient.http import MediaFileUpload
from Google import Create_Service
from urllib.parse import urlencode
from io import BytesIO
from googleapiclient.discovery import build
from google.oauth2 import service_account
from dotenv import load_dotenv
import pandas as pd
from redcap import Project
import os


load_dotenv()

URL = 'https://redcap.buwana.id/api/'
fields = ['record_id','kategori_suby','nama','jk','usia']

token = os.getenv('TOKEN_REDCAP_SDQ')

def extract_data(token, url):

    project_sdq = Project(url, token)

    return project_sdq.export_records(raw_or_label='label', fields=fields, format_type='df')
    

data = extract_data(token, URL)
print('Extract Data has done!')


# def getDataVaksinasiRedcap(mulai_tgl, selesai_tgl):
#     buf = BytesIO()
#     data = {
#         'token': 'your-token-redcap',
#         'content': 'record',
#         'format': 'json',
#         'type': 'flat',
#         'csvDelimiter': '',
#         'rawOrLabel': 'label',
#         'rawOrLabelHeaders': 'raw',
#         'exportCheckboxLabel': 'false',
#         'exportSurveyFields': 'false',
#         'exportDataAccessGroups': 'false',
#         'returnFormat': 'json'
#     }
#     ch = pycurl.Curl()
#     ch.setopt(ch.URL, 'https://amari.unpad.ac.id/api/')
#     #ch.setopt(ch.HTTPPOST, data.items())
#     postfields = urlencode(data)
#     ch.setopt(ch.POSTFIELDS, postfields)
#     ch.setopt(ch.WRITEFUNCTION, buf.write)
#     ch.setopt(ch.CAINFO, "cacert.pem")
#     ch.perform()
#     ch.close()
#     data = str(buf.getvalue(), 'utf-8')
#     # df = pd.read_csv(data)
#     buf.close()

#     df = pd.read_json(data)
#     vaksinasi = df[(df['tgl_vaksin'] <= selesai_tgl)
#                    & (df['tgl_vaksin'] >= mulai_tgl)]

#     return vaksinasi


# def getDataIsolasi():

#     # get credentials
#     SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#     SERVICE_ACCOUNT_FILE = 'dashboard-keys.json'

#     creds = None
#     creds = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)

#     # -----------------------credential-------------------------------------

#     # The ID and range of a sample spreadsheet.
#     SAMPLE_SPREADSHEET_ID = 'spreadsheet_id'

#     service = build('sheets', 'v4', credentials=creds)

#     # Call the Sheets API
#     sheet = service.spreadsheets()
#     result1 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                  range="Asrama PUPR!A4:U1000").execute()
#     data_asrama_pupr = result1.get('values', [])

#     result2 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                  range="Asrama Bale Wilasa 8!A1:K2000").execute()
#     data_asrama_wilasa8 = result2.get('values', [])

#     asrama_pupr = pd.DataFrame(data_asrama_pupr)
#     asrama_wilasa8 = pd.DataFrame(data_asrama_wilasa8)

#     asrama = {
#         'pupr': asrama_pupr,
#         'wilasa8': asrama_wilasa8
#     }

#     return asrama


# def getDataTreatment():
#     # get credentials
#     SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#     SERVICE_ACCOUNT_FILE = 'dashboard-keys.json'

#     creds = None
#     creds = service_account.Credentials.from_service_account_file(
#         SERVICE_ACCOUNT_FILE, scopes=SCOPES)

#     # -----------------------credential-------------------------------------

#     # The ID and range of a sample spreadsheet.
#     SAMPLE_SPREADSHEET_ID = 'spreadsheet_id'

#     service = build('sheets', 'v4', credentials=creds)

#     # Call the Sheets API
#     sheet = service.spreadsheets()
#     result1 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                  range="Asrama PUPR!A4:AP1000").execute()
#     data_asrama_pupr = result1.get('values', [])

#     result2 = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                  range="Asrama Bale Wilasa 8!A1:AP2000").execute()
#     data_asrama_wilasa8 = result2.get('values', [])

#     asrama_pupr = pd.DataFrame(data_asrama_pupr)
#     asrama_wilasa8 = pd.DataFrame(data_asrama_wilasa8)

#     asrama = {
#         'pupr': asrama_pupr,
#         'wilasa8': asrama_wilasa8
#     }

#     return asrama


# def getDataLacakKontak():
#     buf = BytesIO()
#     data = {
#         'token': 'your_redcap_token',
#         'content': 'report',
#         'format': 'json',
#         'report_id': '171',
#         'csvDelimiter': '',
#         'rawOrLabel': 'raw',
#         'rawOrLabelHeaders': 'raw',
#         'exportCheckboxLabel': 'false',
#         'returnFormat': 'json'
#     }
#     ch = pycurl.Curl()
#     ch.setopt(ch.URL, 'https://amari.unpad.ac.id/api/')
#     #ch.setopt(ch.HTTPPOST, data.items())
#     postfields = urlencode(data)
#     ch.setopt(ch.POSTFIELDS, postfields)
#     ch.setopt(ch.WRITEFUNCTION, buf.write)
#     ch.setopt(ch.CAINFO, "cacert.pem")
#     ch.perform()
#     ch.close()
#     data = str(buf.getvalue(), 'utf-8')
#     # df = pd.read_csv(data)
#     buf.close()

#     df = pd.read_json(data)

#     return df


# ''' Data Load '''
# CLIENT_SECRET_FILE = 'client_secret_file.json'
# API_NAME = 'sheets'
# API_VERSION = 'v4'
# SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


# def logbookTreatment(sheet_name):
#     service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#     # REPLACE FILE LOGBOOK TREATMENT
#     file_id_treatment = 'spreadsheet_id'

#     response = service.spreadsheets().values().batchGet(
#         spreadsheetId=file_id_treatment,
#         majorDimension='ROWS',
#         ranges=sheet_name
#     ).execute()

#     return response


# def relawanTreatment():
#     service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#     # REPLACE FILE RELAWAN TREATMENT
#     file_id_treatment = 'spreadsheet_id'

#     response = service.spreadsheets().values().get(
#         spreadsheetId=file_id_treatment,
#         majorDimension='ROWS',
#         range='LOGBOOK RELAWAN FK DAN FKEP'
#     ).execute()

#     df = pd.DataFrame(response['values'])
#     return df


# def getDataEmg():
#     service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#     # REPLACE FILE EMERGENCY
#     file_id_emg = 'spreadsheet_id'

#     valueRanges_Body = [
#         'Keluhan_CallCenter',
#         'Ambulance',
#         'Oksigen',
#     ]

#     response = service.spreadsheets().values().batchGet(
#         spreadsheetId=file_id_emg,
#         majorDimension='ROWS',
#         ranges=valueRanges_Body
#     ).execute()

#     return response


# def DataTesting(valueRanges_Body=[]):
#     service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

#     # REPLACE FILE TESTING
#     file_id_treatment = 'spreadsheet_id'

#     response = service.spreadsheets().values().batchGet(
#         spreadsheetId=file_id_treatment,
#         majorDimension='ROWS',
#         ranges=valueRanges_Body
#     ).execute()

#     return response
