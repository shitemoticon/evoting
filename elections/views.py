from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Election,Candidate,Vote
from .serializers import ElectionSerializer
from .serializers import CandidateSerializer
from .serializers import VoteSerializer


class Elections(APIView):
    def get(self,request):
        elections = Election.objects.all()
        serializer = ElectionSerializer(elections,many=True)
        return Response(serializer.data,status=202)

class Candidates(APIView):
    def get(self,request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates,many=True)
        return Response(serializer.data,status=202)

class Votes(APIView):
    def get(self,request):
        votes = Vote.objects.all()
        serializer = VoteSerializer(votes,many=True)
        return Response(serializer.data,status=202)

