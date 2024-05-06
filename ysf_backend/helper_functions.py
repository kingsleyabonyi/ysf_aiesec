# from oauth2client.service_account import ServiceAccountCredentials
# import gspread

# def get_gspread_client():
#   """
#   Retrieves authorized gspread client for Google Sheets access.
#   """
#   try:
#       credentials = ServiceAccountCredentials.from_json_keyfile_name(GOOGLE_CREDENTIALS_PATH, GOOGLE_OAUTH_SCOPES)
#       gc = gspread.authorize(credentials)
#       return gc
#   except Exception as e:
#       raise HTTPException(f"Error authorizing Google Sheets: {e}")