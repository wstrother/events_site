from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("detail/<int:question_id>", views.detail, name="detail"),
    path("reults/<int:question_id>", views.results, name="results"),
    path("vote/<int:question_id>", views.vote, name="vote"),
]
