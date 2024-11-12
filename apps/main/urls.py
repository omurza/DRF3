from rest_framework.routers import DefaultRouter
from django.urls import path 

from .views import BookAPI



router=DefaultRouter()
router.register("", BookAPI, basename="api_book")
urlpatterns = [

]
urlpatterns+=router.urls