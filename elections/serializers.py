from rest_framework import serializers
from account.serializers import RegisterSerializer
from .models import Election
from .models import Candidate
from .models import Vote


class CandidateSerializer(serializers.ModelSerializer):
    info = RegisterSerializer(many=False)

    class Meta:
        model = Candidate
        fields = [
            'candidate_id',
            'info',
            'message'
        ]


class ElectionSerializer(serializers.ModelSerializer):
    candidates = CandidateSerializer(many=True)

    class Meta:
        model = Election
        fields = [
            'election_id',
            'title',
            'candidates',
            'started',
            'start_date',
            'end_date',
        ]


class VoteSerializer(serializers.ModelSerializer):
    voter = RegisterSerializer(many=False)
    election = ElectionSerializer(many=False)
    candidate = CandidateSerializer(many=False)

    class Meta:
        model = Vote
        fields = [
            'id',
            'voter',
            'election',
            'candidate',
            'date_voted'
        ]
