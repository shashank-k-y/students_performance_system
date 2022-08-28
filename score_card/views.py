from rest_framework import viewsets

from student_accounts.models import Score
from score_card.serializers import ScoreSerializer


class ScoreView(viewsets.ModelViewSet):

    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
