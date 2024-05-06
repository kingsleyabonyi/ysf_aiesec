# 
from oauth2client.service_account import ServiceAccountCredentials
import gspread

import os


GOOGLE_OAUTH_SCOPES = [
    'https://spreadsheets.google.com/feeds',
    'https://www.googleapis.com/auth/spreadsheets',
    'https://www.googleapis.com/auth/drive.file',
    'https://www.googleapis.com/auth/drive',
  ]
GOOGLE_CREDENTIALS = os.getenv('CREDENTIALS')

# gc = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS, GOOGLE_OAUTH_SCOPES))