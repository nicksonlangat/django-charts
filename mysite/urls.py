from django.contrib import admin
from django.urls import path
from core.views import HomeView,  ChartData
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view()),
    path('api/', ChartData.as_view(), name='api-data'),
]
