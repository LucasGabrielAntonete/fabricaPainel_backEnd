from rest_framework.routers import DefaultRouter

from core.usuario import views

app_name = "core.usuario"

router = DefaultRouter()
router.register("usuarios", views.UsuarioViewSet)
