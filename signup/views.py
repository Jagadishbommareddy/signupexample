from django.shortcuts import render
from rest_framework import  viewsets
from .serializers import *
from rest_framework.views import APIView
import json
# class SingupViewSet(viewsets.ModelViewSet):
#     queryset = Signup.objects.all()
#     serializer_class = SingupSerializer


class ContactList(APIView):
    # def get(self, request):
    #     queryset = Signup.objects.all()
    #     serializer_class = SingupSerializer


    def post(self, request):
         data = json.loads(request.body)
         first_name = data['first_name']
         user = User.objects.get_or_create(first_name=first_name)
         email = data['email']
         sig = Signup.objects.get_or_create(user=user,email = email)
         sign.save()
