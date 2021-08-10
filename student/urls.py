from django.urls import path

from student import views

urlpatterns = [
    path("", views.StudentlistCreate.as_view(), name="member_create"),
    path("detail/<int:student_id>/", views.StudentDetail.as_view(), name="member_create"),
    path("update/<int:student_id>/", views.StudentDetail.as_view(), name="member_create"),
    path("delete/<int:student_id>/", views.StudentDetail.as_view(), name="member_create")]