import os
import sys
import re

# Añadir la carpeta raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from app.assistant import handle_intent

import re
from app.assistant import handle_intent


def test_greeting_intent_english():
    response = handle_intent("hello")
    assert response["intent"] == "greeting"
    assert "hello" in response["message"].lower()


def test_greeting_intent_spanish():
    response = handle_intent("hola")
    assert response["intent"] == "greeting"


def test_time_intent_contains_time_pattern():
    response = handle_intent("what time is it?")
    assert response["intent"] == "time_request"
    # Check there is something that looks like HH:MM
    assert re.search(r"\b\d{2}:\d{2}\b", response["message"]) is not None


def test_help_intent():
    response = handle_intent("help")
    assert response["intent"] == "help"
    # Should guide the user somehow
    assert "ask me" in response["message"].lower()


def test_unknown_intent():
    response = handle_intent("this is a random sentence")
    assert response["intent"] == "unknown"
    assert "didn't understand" in response["message"].lower()
