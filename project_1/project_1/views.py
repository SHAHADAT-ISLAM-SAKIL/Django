from django.http import HttpResponse

def home (request):
    return HttpResponse("this is Home Page")
def contact(request):
    return HttpResponse("this is contact page")