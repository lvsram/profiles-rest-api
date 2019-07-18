from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
# you don't need to mention base_name because we mentioned queeryset in serializers.py
# that's it needed to register profile view set
router.register('profiles', views.UserProfileViewSet)

urlpatterns = [
    # api view
    path('hello-view/', views.HelloApiView.as_view()),
    # view set
    path('', include(router.urls)),

]
