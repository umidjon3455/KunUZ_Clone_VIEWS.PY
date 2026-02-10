from django.shortcuts import render
from .models import News, Category

def home(request):
    news_list = News.objects.filter(status='PB')
    categories = Category.objects.all()
    return render(request, 'home.html', {
        'news_list': news_list,
        'categories': categories
    })
