# from django.db.models import Max

# from rest_framework import serializers

# from score_card import models

# class SubjectScoreSerializer(serializers.ModelSerializer):
#     top_scorer = serializers.SerializerMethodField(read_only=True)

#     class Meta:
#         model = models.Subject
#         fields = "__all__"

#     def get_top_scorer(self, instance):
#         return models.Subject.objects.distinct('name').aggregate(Max('score'))
