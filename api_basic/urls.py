from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ArticleAPIViewDetails, GenericAPIView, ArticleModalViewSet

router = DefaultRouter()
router.register('article', ArticleModalViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', article_list),
    path('article/', GenericAPIView.as_view()),
    # path('detail/<int:pk>/', article_detail)
    path('detail/<int:id>/', ArticleAPIViewDetails.as_view()),
    path('generic/article/<int:id>/', GenericAPIView.as_view())

]
