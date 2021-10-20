# from rest_framework.authentication import BasicAuthentication
from django.contrib.auth import login
from rest_framework.views import APIView
from .models import Account
from django.contrib.auth.hashers import check_password
from .serializers import RegisterSerializer

from rest_framework.authtoken.models import Token
from django.contrib.auth.models import update_last_login

from rest_framework import  status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response



class Login(APIView):

    def post(self, request):
        data = {}
        email = request.data.get('email','')
        password = request.data.get('password','')

        try:
            user =  Account.objects.get(email=email)
        except BaseException:
            data['email'] = "Unknown email address, please try again or sign up"
            return Response(data,status.HTTP_400_BAD_REQUEST)
            


    
        if  check_password(password=password,encoded=user.password):
            login(request,user)
            update_last_login(None, user)

            data['message'] = "User logged in successfully"
            data['token'] = Token.objects.get_or_create(user=user)[0].key
            data['user'] = {
                'id':user.id,
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'student_id':user.student_id,
                'staff_id':user.staff_id,
                'course':user.course,
                'department':user.department,
            }
            return Response(data,status.HTTP_200_OK)
        else:
            data['password'] = "Incorrect password, please try again"
            return Response(data,status.HTTP_400_BAD_REQUEST)




class Signup(APIView):
    authentication_classes = []
    permission_classes = [AllowAny]

    def post(self,request):
        serializer = RegisterSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            user = serializer.save()
        
            data['message'] = "User created successfully"
            data['token'] =  Token.objects.get_or_create(user=user)[0].key
            data['user'] = {
                'id':user.id,
                'email':user.email,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'student_id':user.student_id,
                'staff_id':user.staff_id,
                'course':user.course,
                'department':user.department,
            }
            return Response(data,status.HTTP_201_CREATED)
        else:
            data = serializer.errors
            return Response(data,status.HTTP_400_BAD_REQUEST)






class Logout(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        from django.contrib.auth.models import auth
        request.auth.delete()

        auth.logout(request)

        return Response('User Logged out successfully')
        

