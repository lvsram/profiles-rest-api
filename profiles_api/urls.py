from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    # api view
    path('hello-view/', views.HelloApiView.as_view()),
    # view set
    path('', include(router.urls)),
]
