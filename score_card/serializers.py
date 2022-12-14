import django
from django.core.exceptions import ObjectDoesNotExist

from rest_framework import serializers
from student_accounts.models import Subject, Score, Student
from student_accounts.serializers import StudentDeatilSerializer


class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = "__all__"


class ScoreSerializer(serializers.ModelSerializer):
    student = StudentDeatilSerializer(read_only=True)
    subject = SubjectSerializer()

    class Meta:
        model = Score
        fields = "__all__"

    def create(self, validated_data):
        user = self.context['request'].user
        score = validated_data['score']

        try:
            student = Student.objects.get(user=user)
        except ObjectDoesNotExist:
            raise serializers.ValidationError("Student does'nt exists.")

        student.total_score += score
        student.save()

        subject, is_created = Subject.objects.get_or_create(
            name=validated_data['subject']['name']
        )

        if student.subject.count() >= 5:
            student.uploaded_all_subjects = True
            student.save()

        try:
            return Score.objects.create(
                student=student, subject=subject, score=score
            )
        except django.db.utils.IntegrityError:
            raise serializers.ValidationError(
                "Student subject combination should be unique"
            )
