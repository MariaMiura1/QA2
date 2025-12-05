import time
from typing import Dict


def handle_intent(intent: str) -> Dict[str, str]:
    """
    Simulated virtual assistant intent handler.

    Returns a dictionary with:
    - intent: the recognized intent
    - message: the response message
    """

    intent = intent.lower().strip()

    if intent in ("hi", "hello", "hola"):
        return {
            "intent": "greeting",
            "message": "Hello! How can I help you today?"
        }

    if "time" in intent or "hora" in intent:
        current_time = time.strftime("%H:%M")
        return {
            "intent": "time_request",
            "message": f"The current time is {current_time}."
        }

    if "help" in intent or "ayuda" in intent:
        return {
            "intent": "help",
            "message": "You can ask me about the time or say hello."
        }

    # Fallback
    return {
        "intent": "unknown",
        "message": "Sorry, I didn't understand that. Could you rephrase?"
    }
