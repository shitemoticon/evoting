from django.urls import path
from .views import GetElections,GetVotes,GetCandidates,HasVoted

urlpatterns = [
    # Route for getting all elections
    path("elections",GetElections.as_view()),

    # Route for getting a particular elections
    path("elections/<election_id>",GetElections.as_view()),

    # Route for getting all candidates
    path("candidates",GetCandidates.as_view()),

    #Route for getting all votes 
    path("votes",GetVotes.as_view()), 

    #Route for getting votes for one election. pass the election id in the url
    path("votes/<election_id>",GetVotes.as_view()), 

    #Route for getting votes for one candidate in a particular election. pass the election_id and candidate_id in the url
    path("votes/<election_id>/<candidate_id>",GetVotes.as_view()), 

    #Route for checking whether a user has already voted in a particular election (prevent double voting)
    path("has-voted/<election_id>/<user_id>",HasVoted.as_view()) 
]
