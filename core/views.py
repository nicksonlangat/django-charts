from django.shortcuts import render
from .models import *
from rest_framework.views import APIView
from  rest_framework.response import Response
from django.views.generic import View
# Create your views here.
class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', {"customers": 10})
class ChartData(APIView):
    students=Student.objects.all().count()
    teachers=Teacher.objects.all().count()
    cooks=Cook.objects.all().count()
    parents=Parent.objects.all().count()
    others=Staff.objects.all().count()

    def get(self, request, format=None):
        labels = ["Students", "Teachers", "Parents", "Staff", "Cooks"]
        default_items = [self.students, self.teachers, self.parents, self.others,self.cooks]
        data = {
                "labels": labels,
                "default": default_items,
        }
        return Response(data)


