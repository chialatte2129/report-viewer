from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import redirect, render
from report.forms import UploadForm
NUM_OF_ITEMS = 5

def handle_uploaded_file(f):
    # with open('some/file/name.txt', 'wb+') as destination:
    #     for chunk in f.chunks():
    #         destination.write(chunk)
    print("Handle Process")

def get(request):
    if request.user.is_authenticated:
        record_list = []
        if request.method == 'POST':
            form = UploadForm(request.POST, request.FILES)
            if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                print("success")
                return HttpResponse("File uploaded successfuly")
        else:
            form = UploadForm()

        return render(
            request,
            'report/upload.html',
            {
                "form":form,
                "record_list":record_list
            }
        )
    else:
        return redirect("/login")
