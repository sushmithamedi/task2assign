from django.urls import path,include
from myapp import views

urlpatterns = [
    path( 'welcome',views.home),
    path('signin',views.signin),

]