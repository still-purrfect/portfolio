from django.http import HttpResponse

def home(request):
    return HttpResponse("Render is working")

def about(request):
    return render(request, 'about.html')

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    return render(request, 'contact.html')
