from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from student_accounts.models import Score, Student
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


class OverallPerformance(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            student = Student.objects.get(user=request.user)
        except ObjectDoesNotExist:
            return Response(
                "Student does not exist",
                status=status.HTTP_404_NOT_FOUND
            )
        total_score = total_score if student.uploaded_all_subjects else "please add all subjects to view total_score" # noqa

        top_student = Student.objects.filter(
            uploaded_all_subjects=True
        ).order_by('total_score')

        result_dict = {
            "total_score": total_score,
            "division": student.get_division,
            "overral_top_score": top_student.first().total_score if top_student.exists() else 'None so far', # noqa
            "overral_top_performer": top_student.first().user.username if top_student.exists() else 'None so far' # noqa
        }
        return Response(data=result_dict, status=status.HTTP_200_OK)
