from django.shortcuts import render

# Create your views here.
from dashboard.models import Profile, CV


def createpage(request):
    cv = CV.objects.filter(user=request.user).all()
    print(cv)
    return render(request, 'createpage/addpages.html', {'cv': cv})
