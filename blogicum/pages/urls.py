from django.urls import path
from . import views

app_name = 'pages'

urlpatterns = [
    path('about/', views.about, name='about'),  # pages:about
    path('rules/', views.rules, name='rules'),  # pages:rules
]
