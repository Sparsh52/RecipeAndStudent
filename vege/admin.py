from django.contrib import admin
from django.db.models import Sum

# Register your models here.
from .models import *
admin.site.register(Recepie)
admin.site.register(StudentID)
admin.site.register(Student)
admin.site.register(Department)
admin.site.register(Subject)


class SubjectMarkAdmin(admin.ModelAdmin):
    list_display = ['student','subject','marks']

admin.site.register(SubjectMarks,SubjectMarkAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display = ['student','student_rank','total_marks','date_of_report_card_generation']
    ordering=['student_rank']
    def total_marks(self, obj):
        subject_marks = SubjectMarks.objects.filter(student=obj.student)
        marks = subject_marks.aggregate(total_marks=Sum('marks'))
        
        # Access the total sum of marks
        total_sum = marks['total_marks']
        print(f"Total Marks: {total_sum}")
        
        return total_sum if total_sum is not None else 0



admin.site.register(ReportCard,ReportCardAdmin)

