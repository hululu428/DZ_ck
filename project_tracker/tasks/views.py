from django.http import HttpResponse
from django.urls import reverse
from quality_control.views import index as main_page

def index(request):
    another_page_url = reverse(main_page)
    html = f"<h1>Страница приложения tasks</h1><a href='{another_page_url}'>Перейти на главную страницу</a>"
    return HttpResponse(html)
