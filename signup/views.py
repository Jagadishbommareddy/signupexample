from django.shortcuts import render
from rest_framework import  viewsets
from signup.models import *
from .serializers import *
from rest_framework.views import APIView


import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# class SingupViewSet(viewsets.ModelViewSet):
#     queryset = Signup.objects.all()
#     serializer_class = SingupSerializer


class ContactList(APIView):
    def get(self, request):
        si = Signup.objects.all()
        #print (si)
        members = SignupSerializer(si,many = True)
        return JsonResponse({"response": members.data, "status": "success"})
    def post(self, request):
        data = json.loads(request.body.decode('utf-8'))
        first_name = data['first_name']
        user_name = data ['user_name']
        user = User.objects.create(username=user_name,first_name = first_name)
        print (user)
        email = data['email']
        print (email)
        sig = Signup.objects.create(email = email, user = user)
        #sig.save()
        return JsonResponse({"response":"user_detail", "status": "success"})

# parser_classes = (JSONParser)
# @csrf_exempt
# def signup( request):
#     data = json.loads(request.body.decode('utf-8'))
#     first_name = data['first_name']
#     user_name = data ['user_name']
#     user = User.objects.create(username=user_name,first_name = first_name)
#     print (user)
#     email = data['email']
#     print (email)
#     sig = Signup.objects.create(email = email, user = user)
#     #sig.save()
#     return JsonResponse({"response":"user_detail", "status": "success"})

#
# def signup(request):
#     si = Signup.objects.all()
#     #print (si)
#     members = SignupSerializer(si,many = True)
#     return JsonResponse({"response": members.data, "status": "success"})
