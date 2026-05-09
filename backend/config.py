import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
DOTENV_PATH = BASE_DIR / '.env'

if DOTENV_PATH.exists():
    try:
        from dotenv import load_dotenv
        load_dotenv(dotenv_path=DOTENV_PATH)
    except ImportError:
        pass

class Config:
    BACKEND_API_KEY = os.getenv('BACKEND_API_KEY', '').strip()
    RAILWAY_API_KEY = os.getenv('RAILWAY_API_KEY', '').strip()
    EXTERNAL_SERVICE_KEY = os.getenv('EXTERNAL_SERVICE_KEY', '').strip()
    REQUIRE_API_KEY = os.getenv('REQUIRE_API_KEY', 'true').strip().lower() in ('1', 'true', 'yes')
