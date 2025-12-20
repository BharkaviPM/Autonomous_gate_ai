import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .agent import GateAIAgent

agent = GateAIAgent()

def home(request):
    return render(request, "home.html")

agent = GateAIAgent()

def voice_ui(request):
    return render(request, "voice.html")

def delivery_ui(request):
    return render(request, "delivery.html")


@csrf_exempt
def process_agent_command(request):
    data = json.loads(request.body)
    command = data.get("command")

    intent, approval, anomaly = agent.observe(command)
    response = agent.act(intent, approval, anomaly)

    response.update({
        "intent": intent,
        "approval": round(approval*100,1),
        "anomaly": round(anomaly,2)
    })

    return JsonResponse(response)

import random
from django.shortcuts import render, redirect
from django.http import JsonResponse

# TEMP STORAGE (for demo)
SESSION_OTP = {}

def delivery_home(request):
    return render(request, "delivery_home.html")

def delivery_phone(request):
    return render(request, "delivery_phone.html")

def delivery_otp(request):
    return render(request, "delivery_otp.html")

def delivery_scan(request):
    return render(request, "delivery_scan.html")

# ---- OTP LOGIC ----

def send_otp(request):
    phone = request.POST.get("phone")
    otp = str(random.randint(100000, 999999))
    SESSION_OTP[phone] = otp

    print("OTP (demo):", otp)  # judge-friendly demo

    return JsonResponse({"status": "OTP_SENT"})

def verify_otp(request):
    phone = request.POST.get("phone")
    otp = request.POST.get("otp")

    if SESSION_OTP.get(phone) == otp:
        return JsonResponse({"status": "VERIFIED"})
    return JsonResponse({"status": "FAILED"})
