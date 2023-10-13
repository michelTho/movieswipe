from rest_framework import serializers

from ..models.vote_model import Vote


class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ["movie", "is_upvote"]
