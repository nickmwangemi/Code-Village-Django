from django.db import models
from students.models import Student

# Create your models here.


class Subject(models.Model):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    class Meta:
        db_table = 'tbl_subjects'

    # def __str__(self):
    #     return self.name
    
    def getGrade(self):
        if self.score >= 80 and self.score <= 100:
            return 'A'
        elif self.score >= 60 and self.score < 80:
            return 'B'
        elif self.score >= 40 and self.score < 60:
            return 'C'
        elif self.score >= 0 and self.score < 40:
            return 'D'
        else:
            'Unknown Grade'
    
    def __str__(self):
        return "{} - {}".format(self.name,self.getGrade())
    