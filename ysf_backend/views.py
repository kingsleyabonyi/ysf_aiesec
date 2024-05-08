from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny
import gspread
from oauth2client.service_account import ServiceAccountCredentials

class UserCreateView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # define the scope
            scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

            # add credentials to the account
            creds = ServiceAccountCredentials.from_json_keyfile_name('apikey.json', scope)

            # authorize the clientsheet 
            client = gspread.authorize(creds)

            # get the instance of the Spreadsheet
            sheet = client.open('Sample_sheet')

            # get the first sheet of the Spreadsheet
            sheet_instance = sheet.get_worksheet(0)

            user = list(serializer.data.values())
            sheet_instance.append_row(user)
            

            #send email
            
            # return success response
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


