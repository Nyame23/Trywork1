from django.urls import path
from .views import hi, home, about

urlpatterns = [
    path('hi/', hi, name='hi'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('', home, name='default_home'),  # This should come last
]
