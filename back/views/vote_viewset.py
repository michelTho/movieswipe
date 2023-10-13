from rest_framework import views, status
from rest_framework.request import Request
from rest_framework.response import Response

from ..serializers.vote_serializer import VoteSerializer
from ..models.vote_model import Vote


class VoteViewSet(views.APIView):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer

    def put(self, request: Request):
        print(request.data)
        try:
            vote = Vote.objects.get(movie=request.data["movie"])
        except KeyError:
            return Response(
                "Please provide a movie_id", status=status.HTTP_400_BAD_REQUEST
            )
        except Vote.DoesNotExist:
            serializer = VoteSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    "Vote successfully added", status=status.HTTP_201_CREATED
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        vote.is_upvote = request.data["is_upvote"]
        vote.save()
        return Response("Vote successfully updated", status=status.HTTP_200_OK)
