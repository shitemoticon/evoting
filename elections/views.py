from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

from .models import Election,Candidate,Vote
from .serializers import ElectionSerializer
from .serializers import CandidateSerializer


class GetElections(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request,format=None,**kwargs):
        if kwargs:
            try:
                election = Election.objects.get(election_id=kwargs['election_id'])
                serializer = ElectionSerializer(election,many=False)
                return Response(serializer.data,status.HTTP_200_OK)
            except BaseException:
                return Response({'message':'This election does not exist'},status.HTTP_404_NOT_FOUND)
        else:
            elections = Election.objects.all()
            serializer = ElectionSerializer(elections,many=True)
            return Response(serializer.data,status=202)

class GetCandidates(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        candidates = Candidate.objects.all()
        serializer = CandidateSerializer(candidates,many=True)
        return Response(serializer.data,status=202)

class GetVotes(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self,request,format=None,**kwargs):
        response = {}
        if kwargs:      
            try:
                # Get all votes in a particular election that belong to a particular candidate
                if kwargs['election_id'] and kwargs['candidate_id']:
                    try:
                        candidate_votes = Vote.objects.filter(election=kwargs['election_id'],candidate=kwargs['candidate_id'])
                        candidate = Candidate.objects.get(candidate_id=kwargs['candidate_id'])
                        serializer = CandidateSerializer(candidate,many=False)
                        response['votes'] = len(candidate_votes)
                        response['candidate'] = serializer.data
                    except BaseException:
                        return Response({'message':'This candidate or election does not exist'},status.HTTP_404_NOT_FOUND)
            except KeyError:
                # Get all votes in a particular election
                try:
                    election_votes = Vote.objects.filter(election=kwargs['election_id'])
                    election = Election.objects.get(election_id=kwargs['election_id'])
                    serializer = ElectionSerializer(election,many=False)
                    response['votes'] = len(election_votes)
                    response['election'] = serializer.data
                except BaseException:
                    return Response({'message':'This election does not exist'},status.HTTP_404_NOT_FOUND)


        else:
            # Get all available votes
            votes = Vote.objects.all()
            response['all_votes'] = len(votes)
        return Response(response,status.HTTP_200_OK)



class HasVoted(APIView):
    def get(self,request,election_id,user_id,format=None):
        try:
            vote =  Vote.objects.filter(election=election_id,voter=user_id)
            has_voted = len(vote) > 0
            return Response({"has_voted":has_voted},status.HTTP_200_OK)
        except BaseException:
             return Response({"has_voted":False},status.HTTP_200_OK)




