from django.contrib import admin

# Register your models here.
from student.models import Student, Subject, Marks, Process, ReportCard


class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student, StudentAdmin)

class SubjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Subject, SubjectAdmin)

class MarksAdmin(admin.ModelAdmin):
    pass
admin.site.register(Marks, MarksAdmin)

class ProcessAdmin(admin.ModelAdmin):
    pass
admin.site.register(Process, ProcessAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    pass
admin.site.register(ReportCard, ReportCardAdmin)