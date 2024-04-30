from django.http import HttpResponse
from django.urls import reverse

# def index(request):
#     BugReport_URL = reverse(bug_list)
#     FeatureRequest_URL = reverse (feature_list)
#     html = f"<h1>Страница контроля качества</h1><a href='{BugReport_URL}'>Список всех багов </a><a href='{FeatureRequest_URL}'>Запросы на улучшение</a>"
#     return HttpResponse(html)

from django.views import View
from django.views.generic import ListView
from django.views.generic import DetailView
from .models import BugReport, FeatureRequest

class IndexView(View):
    def get(self, request):
        BugReport_URL = reverse(bug_list)
        FeatureRequest_URL = reverse (feature_list)
        html = f"<h1>Страница контроля качества</h1><a href='{BugReport_URL}'>Список всех багов </a><a href='{FeatureRequest_URL}'>Запросы на улучшение</a>"
        return HttpResponse(html)

def bug_list(request):
    bugs = BugReport.objects.all()
    bugs_html = '<h1>Список багов</h1><ul>'
    for bug in bugs:
        bugs_html += f'<li><h3>{bug.title}\t{bug.status}</h3><a href="{bug.id}/">Подробнее</a></li>'
    bugs_html += '</ul>'
    return HttpResponse(bugs_html)

class BugDetailView(DetailView):
    model = BugReport
    pk_url_kwarg = 'bug_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        bug = self.object
        response_html = f'<h1>{bug.title}</h1><h2>Описание</h2><p>{bug.description}</p><p>Статус: {bug.status}</p><p>Приоритет: {bug.priority}</p><p>Проект: {bug.project}</p><p>Задача: {bug.task}</p>'
        return HttpResponse(response_html)


# def bug_detail(request, id):
#     return HttpResponse(f'Детали бага {id}')

def feature_list(request):
    features = FeatureRequest.objects.all()
    features_html = '<h1>Список доработок</h1><ul>'
    for feature in features:
        features_html += f'<li><h3>{feature.title}\t{feature.status}</h3><a href="{feature.id}/">Подробнее</a></li>'
    features_html += '</ul>'
    return HttpResponse(features_html)

class FeatureDetailView(DetailView):
    model = FeatureRequest
    pk_url_kwarg = 'feature_id'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        feature = self.object
        response_html = f'<h1>{feature.title}</h1><h2>Описание</h2><p>{feature.description}</p><p>Статус: {feature.status}</p><p>Приоритет: {feature.priority}</p><p>Проект: {feature.project}</p><p>Задача: {feature.task}</p>'
        return HttpResponse(response_html)

