from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from drf_yasg.utils import swagger_auto_schema
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from .serializers import StudentInfoSerializers
from .models import StudentInfo
from django.utils import timezone





@swagger_auto_schema(methods=['POST'], request_body=StudentInfoSerializers()) #include swagger doc.
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])

@api_view(['GET', 'POST'])
def StudentInfo_all(request):
    if request.method == 'GET':
        objs = StudentInfo.objects.all() #get all the studentinfo in the table
        serializer =StudentInfoSerializers (objs, many=True) #specify many as true to get all the item in the list.
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        serializer =  StudentInfoSerializers(data=request.data)

        if serializer.is_valid():#checking to know if the entries in the serializer .is_valid()

            object = StudentInfo.objects.create(**serializer.validated_data, StudentId=request.user)#here we are using unpaking to create data. using key word arguments
            #in creating a new todo, its supposed to be user=request.user, activity= cooking. using **serializer.validorated_data would create a bunch of key -word

            serializer = StudentInfoSerializers(object)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            #argument.i.e it would
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['PUT', 'DELETE'], request_body=StudentInfoSerializers())
#@authentication_classes([BasicAuthentication])
#@permission_classes([IsAuthenticated])
@api_view(['GET', 'PUT', 'DELETE'])
def StudentInfo_detail(request, StudentId):
    """
    Takes in a student id and returns the http response depending on the http method.
    Args:
    student_id:integer


    Allowed methods:
    GET- get the detail of a single student
    PUT- allows students details to be edited
    DELETE: this logic
"""

    try:
        obj = StudentInfo.objects.get(id = StudentId)# this would return a querry set.Not only a querry set, it would return the id of a particular user
    except StudentInfo.DoesNotExist:
            error ={
                 "message": "failed",
                 "error":f"StudentInfo with id{StudentId} does not exist"
            }
            return  Response(error, status=status.HTTP_400_BAD_REQUEST) 
 

    if request.method == 'GET':
        serializer = StudentInfoSerializers(obj)#serializing the objects fetched


        data = {
            "message":"sucess",
            "data":serializer.data
            #prepare the response
        }
        return Response(data, status= status.HTTP_200_OK)#send the response
    elif request.method =="PUT":
        serializer = StudentInfoSerializers(obj, data = request.data, partial = True)#here we are trying to convert the querry set to jason by passing it into the erializer class
        

        if serializer.is_valid():
                  
            serializer.save()
            
            data = {
                "message":"success",
                "data":serializer.data
            }
            return Response(data, status = status.HTTP_202_ACCEPTED)
        else:
            error = {
                "message":"failes",
                "errors":serializer.errors
            }
            return Response(error, status = status.HTTP_400_BAD_REQUEST)

    elif request.method=="DELETE":
        obj.delete()
        return Response({"message":"success"}, status= status.HTTP_204_NO_CONTENT)



@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def StudentInfo_range(request):
    if request.method == 'GET':
        today_date = timezone.now().date()
        objects = StudentInfo.objects.filter(studentCourse='Big Data Analytics')
        
        serializer = StudentInfoSerializers(objects, many=True)
        data = {
            'status'  : True,
            'message' : "Successful",
            'data' : serializer.data,
        }

        return Response(data, status = status.HTTP_200_OK)