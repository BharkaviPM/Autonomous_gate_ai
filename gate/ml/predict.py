def ai_predict(visit_hour, frequency_7d):
    # Intent logic
    if visit_hour >= 22 and frequency_7d > 3:
        intent = "Suspicious"
    elif frequency_7d >= 5:
        intent = "Delivery"
    else:
        intent = "Guest"

    # Approval probability
    approval_probability = max(0.1, 1 - (frequency_7d * 0.1))
    if intent == "Suspicious":
        approval_probability = 0.2

    # Anomaly score (0 = normal, 1 = risky)
    anomaly_score = min(1.0, (frequency_7d / 10))
    if visit_hour >= 23:
        anomaly_score += 0.2

    return intent, round(approval_probability, 2), round(anomaly_score, 2)
