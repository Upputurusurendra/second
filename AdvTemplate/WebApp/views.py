from django.shortcuts import render
# Create your views here.
def base_views(request):
    return render(request,'MyApp/base.html')
def home_views(request):
    return render(request,'MyApp/home.html')
def courses_views(request):
    return render(request,"MyApp/courses.html")
def news_views(request):
    return render(request,"MyApp/news.html")
def sports_views(request):
    return render(request,"MyApp/sports.html")