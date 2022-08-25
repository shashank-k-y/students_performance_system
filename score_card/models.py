from django.db import models

from student_accounts.models import Student


class Subject(models.Model):
    PHYSICS = "PHY"
    CHEMISTRY = "CHEM"
    BIOLOGY = "BIO"
    COMPUTER_SCIENCE = "CS"
    PSYCHOLOGY = "PSY"
    FINANCE = "FIN"
    SUBJECT_NAMES = (
        (PHYSICS, "physics"),
        (CHEMISTRY, "chemistry"),
        (BIOLOGY, 'biology'),
        (COMPUTER_SCIENCE, 'computer_science'),
        (PSYCHOLOGY, 'psychology'),
        (FINANCE, "finance")
    )
    name = models.CharField(max_length=50, choices=SUBJECT_NAMES)
    score = models.FloatField(default=0)
    student = models.ManyToManyField(Student)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"name: {self.name} | score: {self.score} |" + \
            f"student: {self.student.user.username}"
