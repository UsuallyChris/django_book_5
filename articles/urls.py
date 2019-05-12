""" URL definitions for articles app """
from django.urls import path

from .views import ArticleListView
from .views import ArticleUpdateView
from .views import ArticleDetailView
from .views import ArticleDeleteView
from .views import ArticleCreateView

urlpatterns = [
    path('<int:pk>/edit/',
         ArticleUpdateView.as_view(), name='article_edit'),
    path('<int:pk>/',
         ArticleDetailView.as_view(), name='article_detail'),
    path('<int:pk>/delete/',
         ArticleDeleteView.as_view(), name='article_delete'),
    path('new/', ArticleCreateView.as_view(), name='article_new'),
    path('', ArticleListView.as_view(), name='article_list'),
]
