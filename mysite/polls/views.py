from django.http import HttpResponse


def index(request):
    return HttpResponse("You're at the polls index. How it's going bro?")

