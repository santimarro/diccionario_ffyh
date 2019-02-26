from django.urls import path

from . import views

app_name = 'search'
urlpatterns = [
    path('', views.index, name='searchindex'),
    path('results/', views.search, name='search'),
    path('results_letter/', views.search_letter, name='search_letter'),
    path('<int:word_id>/', views.detail, name='detail'),
    path('new/', views.new_word, name='post_new')

]
