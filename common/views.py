from django.shortcuts import render

def home_page(request):
    return render(request, 'common/home-page.html')


def about_page(request):
    return render(request, 'common/about-page.html')