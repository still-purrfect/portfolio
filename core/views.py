from django.http import HttpResponse

def home(request):
    return HttpResponse("Django is working on Render")

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')
