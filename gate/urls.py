from django.urls import path
from . import views
from .views import home, process_agent_command, voice_ui

urlpatterns = [
    path("", home),
    path("agent/process/", process_agent_command),
    path("voice/", views.voice_ui, name="voice"),
    path("delivery/", views.delivery_ui, name="delivery"),
    path("delivery/", views.delivery_home),
    path("delivery/phone/", views.delivery_phone),
    path("delivery/otp/", views.delivery_otp),
    path("delivery/scan/", views.delivery_scan),

    path("delivery/send-otp/", views.send_otp),
    path("delivery/verify-otp/", views.verify_otp),
]
