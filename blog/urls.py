from django.urls import path, include
from blog.views import communication



urlpatterns = [    
    path('communication', communication),
]
