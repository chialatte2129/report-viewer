from django.urls import path
from report.views import home, upload, view_records


app_name = "report"
urlpatterns = [
    path('/', home.index, name='home'),
    path('/upload', upload.get, name='upload'),
    path('/view_record', view_records.get, name='view_record'),
]