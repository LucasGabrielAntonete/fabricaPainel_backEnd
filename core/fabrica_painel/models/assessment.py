from django.db import models
from core.usuario.models import Usuario
from core.fabrica_painel.models.work import Work

class Assessment(models.Model):
    registration =  models.ForeignKey(Usuario,
        related_name="assessment",
        limit_choices_to={'user_type': Usuario.UserType}, 
        on_delete=models.PROTECT)
    work = models.ForeignKey(Work, on_delete=models.PROTECT)
    grade = models.FloatField()
    evaluator = models.ForeignKey(
        Usuario,
        on_delete=models.PROTECT,
        related_name="assessments_evaluator",
        limit_choices_to={'is_evaluator': True})
    date_time = models.DateTimeField()

    def __str__(self):
        return f"{self.registration} - {self.work}"