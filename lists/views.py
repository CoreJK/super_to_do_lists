from django.shortcuts import render

# Create your views here.


def home_page(reqeust):
    return render(reqeust, 'home.html')


