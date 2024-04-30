from django.urls import path
from quality_control import views 


urlpatterns = [
    path('', views.index),
    path('bugs/', views.bug_list),
    path('bugs/<int:id>', views.bug_detail),
    path('features/', views.feature_list),
    path('features/<int:id>', views.feature_detail),
]
