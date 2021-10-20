from django.urls import path
from .views import Elections,Votes,Candidates

urlpatterns = [
    path("elections/",Elections.as_view()),
    path("candidates/",Candidates.as_view()),
    path("votes/",Votes.as_view())
]
