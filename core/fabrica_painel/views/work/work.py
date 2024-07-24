from rest_framework.viewsets import ModelViewSet
from drf_spectacular.utils import extend_schema
from django.utils import timezone
from django.urls import reverse


from core.fabrica_painel.models.work import Work
from core.fabrica_painel.serializers.work import (
    WorkDetailSerializer,
    WorkWriteSerializer
)

from uuid import uuid4
from core.fabrica_painel.signals.signal_work_update import data_updated
from core.fabrica_painel.signals.signal_work_advisor_update import advisor_changed



@extend_schema(tags=["work"])
class WorkViewSet(ModelViewSet):
    queryset = Work.objects.all()
    serializer_class = WorkDetailSerializer

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return WorkDetailSerializer
        return WorkWriteSerializer
    http_method_names = ["get", "post", "patch", "delete"]

    def update(self, request, *args, **kwargs):
        work = Work.objects.get(pk=self.kwargs["pk"])
        response = super().update(request, *args, **kwargs)
        old_advisor = work.advisor
        instance = self.get_object()
        new_advisor = instance.advisor

        if work.verification_token is not None and old_advisor != new_advisor:
                print(f"{old_advisor} {new_advisor} {instance}") 
                advisor_changed.send(
                    sender=Work,
                    instance=instance,
                    request=request,
                    old_advisor=old_advisor,
                    new_advisor=new_advisor
                )

        elif work.verification_token is None and work.final_submission_work_date is not None:
           
            token = str(uuid4())
            work.verification_token = token
            work.final_submission_work_date = None
            work.save()
            work.final_submission_work_date = timezone.now()
            work.save()

            accept_work_path = reverse("accept-work", kwargs={"verification_token": token})
            accept_work_link = f"http://localhost:8000{accept_work_path}"

            data_updated.send(sender=Work, instance=instance, accept_work_link=accept_work_link)

        return response

        