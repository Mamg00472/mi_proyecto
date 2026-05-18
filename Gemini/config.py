import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
MODEL_NAME = "gemini-2.0-flash"

ENABLE_VOICE_INPUT = True
ENABLE_TEXT_INPUT = True
SCREENSHOT_DIR = "/tmp/gemini_screenshots"
LOG_FILE = "agent_log.txt"

MAX_RETRIES = 3
TIMEOUT = 30

HAS_DISPLAY = os.environ.get("DISPLAY", "") != ""
USE_VIRTUAL_DISPLAY = not HAS_DISPLAY

if not os.path.exists(SCREENSHOT_DIR):
    os.makedirs(SCREENSHOT_DIR)
