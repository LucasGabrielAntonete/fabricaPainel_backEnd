from django.core.exceptions import ValidationError
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView


class EmailAPIView(APIView):
    def post(self, request, *args, **kwargs):
        subject = request.POST.get("subject", "Nome do email")
        message = request.POST.get("message", "Conteúdo do email")
        recipient_list = ["lucasantonete@gmail.com", "lucasantonete@hotmail.com"]
        from_email = "lucasantonete.ifc@gmail.com"
        try:
            send_mail(
                subject,
                message,
                recipient_list=recipient_list,
                from_email=from_email,
            )

        except BadHeaderError:
            return HttpResponse("Invalid header found.")
        except ValidationError as e:
            return HttpResponse(str(e))
        return HttpResponse({"Email enviado com sucesso"}, status=status.HTTP_200_OK)
