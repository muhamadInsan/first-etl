from googleapiclient.http import MediaFileUpload
from Google import Create_Service


''' Data Load '''
CLIENT_SECRET_FILE = 'client_secret_file.json'
API_NAME = 'drive'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/drive']

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

# REPLACE FILE VAKSINASI
file_id_vaksinasi = 'spreadsheet_id'
file_name_vaksinasi = 'data-vaksinasi.xlsx'
mime_type = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'

media_vaksinasi = MediaFileUpload(
    'dataset-dashboard/{0}'.format(file_name_vaksinasi), mimetype=mime_type)

service.files().update(
    fileId=file_id_vaksinasi,
    media_body=media_vaksinasi
).execute()


# REPLACE FILE ISOLASI
file_id_isolasi_pupr = 'spreadsheet_id'
file_name_isolasi_pupr = 'data-isolasi.xlsx'

media_isolasi_pupr = MediaFileUpload(
    'dataset-dashboard/{0}'.format(file_name_isolasi_pupr), mimetype=mime_type)

service.files().update(
    fileId=file_id_isolasi_pupr,
    media_body=media_isolasi_pupr
).execute()

# REPLACE FILE TREATMENT
file_id_treatment = 'spreadsheet_id'
file_name_treatment = 'dataset-treatment.xlsx'

media_treatment = MediaFileUpload(
    'dataset-dashboard/{0}'.format(file_name_treatment), mimetype=mime_type)

service.files().update(
    fileId=file_id_treatment,
    media_body=media_treatment
).execute()

# REPLACE FILE LACAK KONTAK
file_id_lacakkontak = 'spreadsheet_id'
file_name_lacakkontak = 'dataset-lacakkontak.xlsx'

media_lacakkontak = MediaFileUpload(
    'dataset-dashboard/{0}'.format(file_name_lacakkontak), mimetype=mime_type)

service.files().update(
    fileId=file_id_lacakkontak,
    media_body=media_lacakkontak
).execute()

# REPLACE FILE LOGBOOK TREATMENT
file_id_logbook_treatment = 'spreadsheet_id'
file_name_logbook_treatment = 'dataset-logbook-treatment.xlsx'

media_logbook_treatment = MediaFileUpload(
    'dataset-dashboard/{0}'.format(file_name_logbook_treatment), mimetype=mime_type)

service.files().update(fileId=file_id_logbook_treatment,
                       media_body=media_logbook_treatment).execute()


# REPLACE FILE BOR
file_id_bor = 'spreadsheet_id'
file_name_bor = 'dataset-isolasi-bor.xlsx'

media_bor = MediaFileUpload(
    'dataset-dashboard/{0}'.format(file_name_bor), mimetype=mime_type)
service.files().update(fileId=file_id_bor, media_body=media_bor).execute()


# REPLACE FILE EMG
file_id_emg = 'spreadsheet_id'
file_name_emg = 'dataset-emergency.xlsx'

media_emg = MediaFileUpload(
    'dataset-dashboard/{0}'.format(file_name_emg), mimetype=mime_type)
service.files().update(fileId=file_id_emg, media_body=media_emg).execute()

# REPLACE FILE EMG
file_id_testing = 'spreadsheet_id'
file_name_testing = 'dataset-testing.xlsx'

media_testing = MediaFileUpload(
    'dataset-dashboard/{0}'.format(file_name_testing), mimetype=mime_type)
service.files().update(fileId=file_id_testing, media_body=media_testing).execute()
