
from django.urls import path
from .views import home, success

urlpatterns = [http://127.0.0.1:8000/
    path('', home, name='home'),
     path('success' , success , name='success')
]
