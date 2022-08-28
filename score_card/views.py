from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from student_accounts.models import Score
from score_card.serializers import ScoreSerializer


class ScoreView(viewsets.ModelViewSet):

    queryset = Score.objects.all()
    serializer_class = ScoreSerializer


class IndividualPerformance(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request, subject):
        username = request.user.username
        scores_in_subject = Score.objects.filter(subject__name=subject)
        if not scores_in_subject.exists():
            return Response(
                "No entries of score found for this subject. please add.",
                status=status.HTTP_404_NOT_FOUND
            )

        individual_score = scores_in_subject.filter(
            student__user__username=username,
        )
        if not individual_score.exists():
            return Response(
                "score does not exist for the student. please add.",
                status=status.HTTP_404_NOT_FOUND
            )

        top_scorer = scores_in_subject.order_by('-score').first()
        result_dict = {
            "subject": subject,
            "individual_score": individual_score.last().score,
            "top_score": top_scorer.score,
            "top_scorer": top_scorer.student.user.username
        }
        return Response(data=result_dict, status=status.HTTP_200_OK)
