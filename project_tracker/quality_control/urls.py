from django.urls import path
from quality_control import views 


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('bugs/', views.bug_list),
    path('bugs/<int:bug_id>/', views.BugDetailView.as_view(), name='BugDetailed'),
    path('features/', views.feature_list),
    path('features/<int:feature_id>/', views.FeatureDetailView.as_view(), name='FeatureDetailed'),
]
