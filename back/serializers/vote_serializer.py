from rest_framework import serializers

from ..models.vote_model import Vote


class VoteSerializer(serializers.Serializer):
    class Meta:
        model = Vote
        fields = ["movie", "user", "is_upvote"]
