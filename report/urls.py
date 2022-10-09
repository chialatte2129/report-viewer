from django.urls import path
from report.views.home import home
from . import views


app_name = "report"
urlpatterns = [
    path('', home, name='home'),
]