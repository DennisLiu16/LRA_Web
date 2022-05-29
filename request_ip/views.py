from django.shortcuts import render
from django.utils import timezone

from request_ip.models import ipInfo
from .forms import ipInfoForm

import ipaddress

# debug
from prettytable import PrettyTable
import socket

def index(request):
    # using Form
    user = request.user
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')
    user_ip = request.META.get('REMOTE_ADDR')

    form = ipInfoForm()

    if request.method == "POST":
        form  = ipInfoForm(request.POST)
        if form.is_valid():

            # use new form to apply connected_time and usr_ipv4 info
            # https://blog.csdn.net/qq_21570029/article/details/79728458
            new_model = form.save(commit=False)

            # check server ip valid
            try:
                ipv4 = ipaddress.ip_address(new_model.server_ipv4) # ip from user input
                if ipv4.version == 4:
                    new_model.usr_ipv4 = user_ip
                    new_model.connected_time = timezone.now()
                    new_model.save()
                    
                    # local debug
                    pt = PrettyTable()
                    pt.field_names = ['time', 'server IP', 'user IP']

                    ipInfoObjs = ipInfo.objects.all()
                    for item in ipInfoObjs:
                        pt.add_row([item.connected_time, item.server_ipv4, item.usr_ipv4])
                    
                    print(pt) # debug

            except ValueError:
                # abort save
                print('IP invalid')
                pass

    context = {
        'form': form,
        'user': user,
        'user_agent': user_agent,
        'ip': user_ip,
    }

    return render(request, "request_ip/index.html", context)