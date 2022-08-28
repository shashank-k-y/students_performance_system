from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class Subject(models.Model):
    PHYSICS = "physics"
    CHEMISTRY = "chemistry"
    BIOLOGY = "biology"
    COMPUTER_SCIENCE = "computer_science"
    PSYCHOLOGY = "psychology"
    FINANCE = "finance"
    SUBJECT_NAMES = (
        (PHYSICS, "physics"),
        (CHEMISTRY, "chemistry"),
        (BIOLOGY, 'biology'),
        (COMPUTER_SCIENCE, 'computer_science'),
        (PSYCHOLOGY, 'psychology'),
        (FINANCE, "finance")
    )
    name = models.CharField(max_length=50, choices=SUBJECT_NAMES)

    def __str__(self) -> str:
        return f"name: {self.name}"


class Student(models.Model):
    FIRST_CLASS = 'FC'
    SECOND_CLASS = 'SC'
    FAIL = 'F'
    DISTINCTION = 'D'
    NOT_AVAILABLE = 'NA'

    DIVISION_CHOICES = (
        (FIRST_CLASS, 'First_class'),
        (SECOND_CLASS, 'Second_class'),
        (FAIL, 'fail'),
        (DISTINCTION, 'distinction'),
        (NOT_AVAILABLE, 'Not_available')
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=10)
    total_score = models.FloatField(default=0)
    division = models.CharField(
        max_length=20,
        choices=DIVISION_CHOICES,
        default=NOT_AVAILABLE
    )
    subject = models.ManyToManyField(Subject, through="Score")
    uploaded_all_subjects = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"name: {self.user.username} | roll_number: {self.roll_number}"

    @property
    def get_division(self):
        sub_count = self.subject.objects.count()
        percentage = 100 * float(self.total_score)/float(sub_count * 100)
        division = ''
        if percentage > 90:
            division = "distinction"
        elif percentage > 70:
            division = "first class"
        elif percentage > 50:
            division = "second class"
        else:
            division = "fail"
        return division



class Score(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    score = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = [['student', 'subject']]

    def __str__(self) -> str:
        return f"{self.student} | {self.subject} | score: {self.score}"
