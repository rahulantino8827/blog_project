from django.urls import path
from .views import BlogApiView

urlpatterns = [
    path("",BlogApiView.as_view(), name="blog")
]
