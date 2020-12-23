from django.urls import path
from .import views

#=========================================#
# this part takes all the urls of our app #
#=========================================#
urlpatterns = [
    path('',views.index,name='index'),
    path('filter',views.getprems,name='filter'),
]
