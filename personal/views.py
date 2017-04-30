from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'personal/home.html')

def contact(request):
    return render(request, 'personal/contact.html', {'content': ['If you would like  to contact me', 'abhi.saharan@gmail.com']})

def analysis (request):
    return render(request, 'personal/analysis.html')

def apple(request):
    return render(request, 'personal/apple.html')
