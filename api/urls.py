from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

router.register("users", views.UserModelViewSet, basename="users")
router.register("blogs", views.BlogsModelViewSet, basename="blogs")
router.register("blogs-like", views.BlogsLikeModelViewSet, basename="blogs-like")

app_name = "api"

urlpatterns = [
    path("", include(router.urls)),
]
