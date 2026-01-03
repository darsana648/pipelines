from django.http import HttpResponse

def home(request):
    return HttpResponse("CI/CD Django App Working")
