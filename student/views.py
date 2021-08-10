from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student
from rest_framework import generics


class StudentlistCreate(APIView):

    @staticmethod
    def post(request):
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        address = request.data.get('address')
        mobile_no = request.data.get('mobile_no')
        newstudent=Student.objects.create(
            first_name=first_name,
            last_name=last_name,
            address=address,
            mobile_no=mobile_no,
        )
        response = {"Id":newstudent.id,"first_name":newstudent.first_name,"last_name":newstudent.last_name}
        return Response(response, status=status.HTTP_201_CREATED)

    @staticmethod
    def get(request):
        students=Student.objects.all()
        response=[]
        for student in students:
            student_response = {"Id":student.id,"first_name":student.first_name,"last_name":student.last_name}
            response.append(student_response)
        return Response(response, status=status.HTTP_200_OK)

class StudentDetail(APIView):

    @staticmethod
    def get(request,student_id):
        students=Student.objects.filter(id=student_id)
        if not students:
            return Response({"Error":"Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        student=students.first()
        response = {"Id": student.id, "first_name": student.first_name, "last_name": student.last_name}
        return Response(response, status=status.HTTP_200_OK)

    @staticmethod
    def patch(request, student_id):
        students = Student.objects.filter(id=student_id)
        if not students:
            return Response({"Error": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        student = students.first()
        request_payload = request.data
        if not request_payload:
            return Response({"Error": "No Attribute mentioned"}, status=status.HTTP_400_BAD_REQUEST)

        for attr, val in request_payload.items():
            if hasattr(student, attr) and getattr(student, attr)!=val:
                setattr(student, attr, val)
        student.save()
        response = {"Id": student.id, "first_name": student.first_name, "last_name": student.last_name,
                    "address":student.address,"mobile_no":student.mobile_no}
        return Response(response, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request,student_id):
        students = Student.objects.filter(id=student_id)
        if not students:
            return Response({"Error": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        student = students.first()
        student.delete()
        response={"Status":"Successfully Deleted"}
        return Response(response, status=status.HTTP_200_OK)


