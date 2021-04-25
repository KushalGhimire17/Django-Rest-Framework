from django.urls import path
from .views import article_list, article_detail, ArticleAPIView, ArticleDetails

urlpatterns = [
    path('article/', ArticleAPIView.as_view(), name='api_article_list'),
    path('detail/<int:id>', ArticleDetails.as_view(), name='api_article_detail'),
    # path('article/', article_list, name='article_list'),
    # path('detail/<int:pk>', article_detail, name='article_detail'),
]
