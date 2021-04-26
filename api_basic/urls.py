from django.urls import path
from .views import GenericAPIView

urlpatterns = [
    path('article-generic/<int:id>/', GenericAPIView.as_view(),
         name='generic_article_list'),
]
