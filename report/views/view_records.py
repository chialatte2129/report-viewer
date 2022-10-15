
from django.views import View
from django.db.models import F
from django.shortcuts import redirect, render
from report.forms import  SearchForm
from report.models import DoorRecord
NUM_OF_ITEMS = 5


class DoorRecordView(View):
    """_summary_

    """

    def __init__(self):
        pass
    
    def _handle_search_data(self, recorded_date, door_id):
        result_dict = {}
        filter = {
            "door_id": door_id,
            "recorded_date":recorded_date
        }
        action_record = list(
            DoorRecord.objects
            .annotate(door_id=F("door_action__door_id"), action=F("door_action__action"))
            .filter(**filter)
            .values("recorded_time", "count", "action")
            .order_by("recorded_time")
        )

        for row in action_record:
            if row["recorded_time"] not in result_dict:
                result_dict[row["recorded_time"]] = {
                    "in":0,
                    "out":0,
                    "total":0
                }
            result_dict[row["recorded_time"]][row["action"]] = row["count"]
            result_dict[row["recorded_time"]]["total"] = (
                result_dict[row["recorded_time"]]["in"]
                - result_dict[row["recorded_time"]]["out"]
            )
        # print(result_dict)
        result = []
        for k,v in result_dict.items():
            v["recorded_time"] = k
            result.append(v)
        # print(result)
        return result

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect("/login")
        form = SearchForm()
        item_list = []

        return render(
            request,
            'report/view_records.html',
            {
                'form':form,
                'item_list': item_list
            }
        )

    def post(self, request):
        if not request.user.is_authenticated:
            return redirect("/login")
        
        form = SearchForm(request.POST)
        item_list = []

        if form.is_valid():
            recorded_date = request.POST["record_date"]
            print(recorded_date)
            door_id = request.POST["door_id"]
            item_list = self._handle_search_data(recorded_date, door_id)
        return render(
            request,
            'report/view_records.html',
            {
                'form':form,
                'item_list': item_list
            }
        )   
