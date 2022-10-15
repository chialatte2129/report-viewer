from django.urls import path
from report.views import home
from report.views.upload import UploadFlowData
from report.views.view_records import DoorRecordView

app_name = "report"
urlpatterns = [
    path('/', home.index, name='home'),
    path('/upload/<str:action>', UploadFlowData.as_view(), name='upload'),
    path('/view_record', DoorRecordView.as_view(), name='view_record'),
]