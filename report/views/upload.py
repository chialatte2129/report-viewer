import datetime
from typing import List
from django.views import View
from django.shortcuts import redirect, render
from report.forms import UploadForm
from report.models import DoorAction, DoorRecord
from openpyxl import load_workbook
from datetime import datetime as dt
NUM_OF_ITEMS = 5

class UploadFlowData(View):
    """_summary_
        Page Action:
            init(GET): Empty Page With Upload Btn
            preview(POST): after upload, preview upload data
            submit(POST): store upload data to database
    """

    def __init__(self):
        pass

    def _handle_uploaded_file(self, record_list, col_dict, file):
        wb = load_workbook(file.file)
        ws = wb.active

        col_list = []
        col_index = 0
        for cell in list(ws.rows)[0]:
            col_list.append(col_index)
            col_dict[col_index] = cell.value
            col_index+=1

        for row in list(ws.rows)[1:]:
            val_list = []
            for cell in row:
                if isinstance(cell.value, dt):
                    cell.value = dt.strftime(cell.value, '%Y-%m-%d')
                if isinstance(cell.value, datetime.time):
                    cell.value = cell.value.strftime('%H:%M')
                val_list.append(cell.value)
            result = {k:v for k,v in zip(col_list, val_list)}
            record_list.append(result)

    def _handle_update_db(self, record_list, col_dict):
        door_action_map = DoorAction.get_map()
        for datetime_record in record_list:
            date_str = datetime_record[0]
            time_str = datetime_record[1]
            for k,v in datetime_record.items():
                if col_dict[k] not in door_action_map:
                    continue
                temp_row = {
                    "recorded_at":f"{date_str}T{time_str}:00",
                    "recorded_date":date_str,
                    "recorded_time":time_str,
                    "door_action_id":door_action_map[col_dict[k]]
                }
                door_obj, created = DoorRecord.objects.get_or_create(**temp_row)
                door_obj.count = v
                door_obj.save()

    def get(self, request, action):
        if not request.user.is_authenticated:
            return redirect("/login")
        message:str = ""
        record_list:List[dict] = []
        col_dict = {}
        form = UploadForm()
        return render(
            request,
            'report/upload.html',
            {
                "form":form,
                "action":action,
                "message":message,
                "col_dict":col_dict,
                "record_list":record_list
            }
        )

    def post(self, request, action):
        if not request.user.is_authenticated:
            return redirect("/login")
        message:str = ""
        record_list:List[dict] = []
        col_dict = {}
        form = UploadForm()

        if action == "preview":
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                self._handle_uploaded_file(record_list, col_dict, request.FILES['file'])
            else:
                message = "Form Error"

        elif action == "submit":
            print(request.POST["record_list"])
            record_list = eval(request.POST["record_list"])
            col_dict = eval(request.POST["col_dict"])
            if len(record_list):
                self._handle_update_db(record_list, col_dict)
                message = "Upload Success"

        return render(
            request,
            'report/upload.html',
            {
                "form":form,
                "action":action,
                "message":message,
                "col_dict":col_dict,
                "record_list":record_list
            }
        )
