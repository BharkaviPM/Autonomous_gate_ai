import random
from datetime import datetime

class GateAIAgent:
    def __init__(self):
        self.history = []

    def observe(self, command):
        hour = datetime.now().hour
        freq = sum(1 for h in self.history if h == command)
        self.history.append(command)

        # Intent auto-classification
        if command == "SCAN":
            if hour >= 22 or freq > 3:
                intent = "SUSPICIOUS"
            else:
                intent = "GUEST"
        else:
            intent = command

        # Approval likelihood
        approval = max(0.1, 1 - (freq * 0.15))
        anomaly = 0.2 + (freq * 0.2)
        if hour >= 23: anomaly += 0.3

        return intent, approval, min(anomaly,1.0)

    def act(self, intent, approval, anomaly):
        if anomaly > 0.7:
            return self.response("Hold & Alert", "Entry held. Alert sent.")
        if approval > 0.5:
            return self.response("Open Gate", "Gate opening.")
        return self.response("Wait", "Waiting for resident approval.")

    def response(self, status, msg):
        return {
            "status": status,
            "en": msg,
            "hi": "कृपया प्रतीक्षा करें",
            "te": "దయచేసి వేచి ఉండండి"
        }