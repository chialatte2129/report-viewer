from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render
NUM_OF_ITEMS = 5


def get(request):
    first_name = ''
    last_name = ''
    item_list = []
    items = None
    if request.user.is_authenticated:
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        first_name = user.first_name
        last_name = user.last_name

        paginator = Paginator(item_list, NUM_OF_ITEMS)  # Show NUM_OF_ITEMS posts per page
        page = request.GET.get('page')
        items = paginator.get_page(page)

    return render(
        request,
        'report/upload.html',
        {
            'items': items,
            'first_name': first_name,
            'last_name': last_name
        }
    )