from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:word_id>/', views.detail, name='detail'),
    path('new/', views.new_word, name='post_new')

]