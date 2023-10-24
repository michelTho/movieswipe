from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.request import Request

from ..models.movie_model import Movie
from ..models.user_model import User
from ..serializers.vote_serializer import VoteSerializer
from ..models.vote_model import Vote


class VoteViewSet(views.APIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def put(self, request: Request):
        current_user = User.objects.filter(
            session_key=request.session.get("session_key")
        ).first()
        if current_user is None:
            current_user = User.objects.create(
                session_key=request.session.get("session_key")
            )
        vote_data = {**request.data, "user": current_user}
        serializer = VoteSerializer(data=vote_data)
        if serializer.is_valid():
            serializer.save()
            return Response("Vote successfully added", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
