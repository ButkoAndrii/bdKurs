from django.shortcuts import render
# from models import Person, QueueConscripts
from .models import Person, QueueConscripts


# Create your views here.
def index(request):
    return render(request, 'main/mainpage.html')


def current_query(request):
    base = {}
    queryset = QueueConscripts.objects.order_by("department", "week_day")
    time = [i.time for i in queryset]
    busy = [i.busy for i in queryset]
    department = [i.department for i in queryset]
    week_day = [i.week_day for i in queryset]
    base['time'] = time
    base['busy'] = busy
    base['department'] = department
    base['week_day'] = week_day
    # base = QueueConscripts.objects.all()
    # time = QueueConscripts.time
    # time = time.objects.all()

    return render(request, "main/current_query.html", {'time': time, 'busy': busy, 'department': department, 'week_day': week_day})
