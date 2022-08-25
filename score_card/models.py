from django.db import models

from student_accounts.models import Student


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
    student = models.ManyToManyField(Student, through='Score')

    def __str__(self) -> str:
        return f"name: {self.name}"


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
