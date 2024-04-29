from django.urls import path
from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("detail/<int:question_id>", views.detail, name="detail"),
    path("results/<int:question_id>", views.results, name="results"),
    path("vote/<int:question_id>", views.vote, name="vote"),
    
    path("vote_meter/<int:choice_id>", views.vote_meter, name="vote_meter"),
    
    path("test", views.test_htmx, name="test")
]
