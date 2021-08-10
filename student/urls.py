from django.urls import path

from student import views

urlpatterns = [
    path("students/", views.StudentlistCreate.as_view(), name="member_create"),
    path("students/detail/<int:student_id>/", views.StudentDetail.as_view(), name="member_create"),
    path("students/update/<int:student_id>/", views.StudentDetail.as_view(), name="member_create"),
    path("students/delete/<int:student_id>/", views.StudentDetail.as_view(), name="member_create"),
    path("subjects/", views.SubjectlistCreate.as_view(), name="member_create"),
    path("subjects/detail/<int:subject_id>/", views.SubjectDetail.as_view(), name="member_create"),
    path("subjects/update/<int:subject_id>/", views.SubjectDetail.as_view(), name="member_create"),
    path("subjects/delete/<int:subject_id>/", views.SubjectDetail.as_view(), name="member_create"),
    path("marks/", views.Markslist.as_view(), name="member_create"),
    path("marks/detail/<int:subject_id>/", views.SubjectDetail.as_view(), name="member_create"),
    path("marks/update/<int:subject_id>/", views.SubjectDetail.as_view(), name="member_create"),
    path("marks/delete/<int:subject_id>/", views.SubjectDetail.as_view(), name="member_create"),
    path("students/<int:student_id>/marks/", views.StudentMark.as_view(), name="member_create"),
    path("students/<int:student_id>/generate_report_card/", views.ReportGen.as_view(), name="member_create"),
    path("processes/<int:process_id>/detail/", views.ReportGen.as_view(), name="member_create")
]