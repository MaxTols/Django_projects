from django.views.generic import ListView
from django.shortcuts import render

from .models import Student


def students_list(request):
    ordering = 'group'
    template = 'school/students_list.html'
    students = Student.objects.order_by(ordering).prefetch_related('teachers')
    context = {'students': students}
    return render(request, template, context)
