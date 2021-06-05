from django.urls import path
from .views import test, apioverview, testdetails

urlpatterns = [
    path("", apioverview, name="api-over-view "),
    path("test/", test.as_view()),
    path("test/<int:id>", testdetails.as_view()),
]
