from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=13)

class Subject(models.Model):
    sub_name = models.CharField(max_length=30)
    max_marks = models.IntegerField()
    min_marks = models.IntegerField()
    books = models.CharField(max_length=50)

class Marks(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE,)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE,)
    marks = models.IntegerField()
    attempt = models.IntegerField()

class Process(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE,)
    status = models.CharField(max_length=30)
    completion = models.IntegerField()

class ReportCard(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE,)
    reportmsg = models.CharField(max_length=30)