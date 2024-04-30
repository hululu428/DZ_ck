from django.http import HttpResponse
from django.urls import reverse

def index(request):
    BugReport_URL = reverse(bug_list)
    FeatureRequest_URL = reverse (feature_list)
    html = f"<h1>Страница контроля качества</h1><a href='{BugReport_URL}'>Список всех багов </a><a href='{FeatureRequest_URL}'>Запросы на улучшение</a>"
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse("Список отчетов об ошибках")

def bug_detail(request, id):
    return HttpResponse(f'Детали бага {id}')

def feature_list(request):
    return HttpResponse("Список запросов на улучшение")

def feature_detail(request, id):
    return HttpResponse(f'Детали бага {id}')
