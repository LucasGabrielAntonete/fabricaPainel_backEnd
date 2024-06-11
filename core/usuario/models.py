from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
from core.fabrica_painel.models.edition import Edition
from core.fabrica_painel.models.field import Field

class Usuario(AbstractUser):
    username = None
    email = models.EmailField(_("e-mail address"), unique=True)
    registration = models.IntegerField(null=True, unique=True)
    name = models.CharField(max_length=255, null=True)
    is_advisor = models.BooleanField(default=False, null=True, blank=True)
    is_evaluator = models.BooleanField(default=False, null=True, blank=True)
    field = models.ForeignKey(Field, on_delete=models.PROTECT, null=True)
    class UserType(models.TextChoices):
        STUDENT = "STUDENT", _("Student")
        TEACHER = "TEACHER", _("Teacher")
        ADMIN = "ADMIN", _("Admin")

    user_type = models.CharField(
        max_length=10,
        choices=UserType.choices,
        default=UserType.STUDENT,
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    EMAIL_FIELD = "email"

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["-date_joined"]


class Pre_user(models.Model):
    class user_type(models.TextChoices):
        STUDENT = "STUDENT", _("Student")
        TEACHER = "TEACHER", _("Teacher")
        ADMIN = "ADMIN", _("Admin")
    email = models.EmailField(_("e-mail address"), unique=True)
    registration = models.IntegerField(null=True, unique=True)
    name = models.CharField(max_length=255, null=True)
    classroom = models.CharField(max_length=255, null=True)
    user_type = models.CharField(
        max_length=10, choices=user_type.choices, default=user_type.STUDENT
    )
    edition = models.ForeignKey(Edition, on_delete=models.PROTECT, null=True)




    