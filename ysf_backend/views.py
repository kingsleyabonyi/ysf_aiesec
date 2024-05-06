from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from rest_framework.permissions import AllowAny

class UserCreateView(APIView):
    permission_classes = [AllowAny]
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            # user.set_password(serializer.data["password"])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


# from .utils import get_gspread_client  # Assuming helper function location

# class GoogleSheetView(APIView):
#   def get(self, request):
#     gc = get_gspread_client()  # Get authorized client
#     worksheet = gc.open_by_key('YOUR_SPREADSHEET_KEY').sheet1  # Access specific sheet
#     data = worksheet.get_all_records()  # Fetch data as a list of dictionaries

#     return Response(data)