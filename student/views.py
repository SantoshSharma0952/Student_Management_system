from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from student.models import Student, Subject, Marks, Process
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


#Subject

class SubjectlistCreate(APIView):

    @staticmethod
    def post(request):
        sub_name = request.data.get('sub_name')
        max_marks = request.data.get('max_marks')
        min_marks = request.data.get('min_marks')
        books = request.data.get('books')
        if type(max_marks)!= int or type(min_marks)!=int:
            return Response({"Error":"Object Not Found"}, status=status.HTTP_400_BAD_REQUEST)
        newsubject=Subject.objects.create(
            sub_name=sub_name,
            max_marks=max_marks,
            min_marks=min_marks,
            books=books,
        )
        response = {"Id":newsubject.id,"sub_name":newsubject.sub_name,"max_marks":newsubject.max_marks}
        return Response(response, status=status.HTTP_201_CREATED)

    @staticmethod
    def get(request):
        subjects=Subject.objects.all()
        response=[]
        for subject in subjects:
            subject_response = {"Id":subject.id,"sub_name":subject.sub_name,"max_marks":subject.max_marks}
            response.append(subject_response)
        return Response(response, status=status.HTTP_200_OK)


class SubjectDetail(APIView):

    @staticmethod
    def get(request,subject_id):
        subjects=Subject.objects.filter(id=subject_id)
        if not subjects:
            return Response({"Error":"Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        subject=subjects.first()
        response = {"Id": subject.id, "sub_name": subject.sub_name, "max_marks": subject.max_marks}
        return Response(response, status=status.HTTP_200_OK)

    @staticmethod
    def patch(request, subject_id):
        subjects = Subject.objects.filter(id=subject_id)
        if not subjects:
            return Response({"Error": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        subject = subjects.first()
        request_payload = request.data
        if "max_marks" in request_payload and type(request_payload.get("max_marks"))!=int:
            return Response({"Error":"Object Not Found"}, status=status.HTTP_400_BAD_REQUEST)

        if not request_payload:
            return Response({"Error": "No Attribute mentioned"}, status=status.HTTP_400_BAD_REQUEST)

        for attr, val in request_payload.items():
            if hasattr(subject, attr) and getattr(subject, attr)!=val:
                setattr(subject, attr, val)
        subject.save()
        response = {"Id": subject.id, "sub_name": subject.sub_name, "max_marks": subject.max_marks,
                    "books":subject.books}
        return Response(response, status=status.HTTP_200_OK)

    @staticmethod
    def delete(request,subject_id):
        subjects = Subject.objects.filter(id=subject_id)
        if not subjects:
            return Response({"Error": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        subject = subjects.first()
        subject.delete()
        response={"Status":"Successfully Deleted"}
        return Response(response, status=status.HTTP_200_OK)

#Marks

class Markslist(APIView):

    @staticmethod
    def post(request):
        student_id = request.data.get('student_id')
        subject_id = request.data.get('subject_id')
        marks = request.data.get('marks')
        attempt = request.data.get('attempt')
        students = Student.objects.filter(id=student_id)
        if not students:
            return Response({"Error": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        subjects = Subject.objects.filter(id=subject_id)
        if not subjects:
            return Response({"Error": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        newmarks=Marks.objects.create(
            student_id=student_id,
            subject_id=subject_id,
            marks=marks,
            attempt=attempt
        )
        response = {"Id":newmarks.id,"student":newmarks.student.first_name,"subject":newmarks.subject.sub_name,
                    "marks":newmarks.marks,"attempt":newmarks.attempt}
        return Response(response, status=status.HTTP_201_CREATED)

    @staticmethod
    def get(request):
        marks=Marks.objects.all()
        response=[]
        for mark in marks:
            marks_response = {"Id":mark.id,"student":mark.student.first_name,"subject":mark.subject.sub_name,
                              "marks":mark.marks}
            response.append(marks_response)
        return Response(response, status=status.HTTP_200_OK)

class StudentMark(APIView):

    @staticmethod
    def get(request,student_id):
        student=Student.objects.filter(id=student_id)
        if not student:
            return Response({"Error":"Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        student=student.first()
        marks = Marks.objects.filter(student_id=student_id)
        response = []
        for mark in marks:
            marks_response = {"Id": mark.id, "student": mark.student.first_name, "subject": mark.subject.sub_name,
                              "marks": mark.marks}
            response.append(marks_response)
        return Response(response, status=status.HTTP_200_OK)

class ReportGen(APIView):

    @staticmethod
    def post(request,student_id):
        student=Student.objects.filter(id=student_id)
        if not student:
            return Response({"Error":"Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        student=student.first()
        newprocess=Process.objects.create(student=student,status="created",completion=0)
        return Response ({"status":True,"process_id":newprocess.id}, status=status.HTTP_201_CREATED)

    @staticmethod
    def get(request, process_id):
        processes = Process.objects.filter(id=process_id)
        if not processes:
            return Response({"Error": "Object Not Found"}, status=status.HTTP_404_NOT_FOUND)
        process = processes.first()
        response = {"Id": process.id, "status": process.status}
        return Response(response, status=status.HTTP_200_OK)