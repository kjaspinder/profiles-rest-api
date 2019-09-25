from django.urls import path, include
from rest_framework.routers import DefaultRouter

from profiles_api import views

"""this is how we register viewset  """
router = DefaultRouter()
router.register('hello-viewset',views.HellowViewSets, base_name = 'hello-viewset')
router.register('profile',views.UserProfileViewSet)

urlpatterns = [
    path('hello-view/',views.HelloApiView.as_view()),
    path('',include(router.urls))
]
