from django.shortcuts import render

def index(request):
    user = request.user
    user_agent = request.META.get('HTTP_USER_AGENT', 'unknown')

    ip = request.META.get('REMOTE_ADDR')

    context = {'user': user, 'user_agent': user_agent, 'ip': ip, }

    return render(request, "request_ip/index.html", context)
