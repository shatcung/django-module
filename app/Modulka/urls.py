from django.urls import path,re_path
from . import views
from django.conf.urls import url

app_name = "Modulka"
urlpatterns = [

    # post views
    # Обработчики приложения блога.
    path('', views.post_list, name='post_list'),
    #path('', views.PostListView.as_view(), name='post_list'),
    
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
    path('tag/<slug:tag_slug>/',
         views.post_list, name='post_list_by_tag'),
]

