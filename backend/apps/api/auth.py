import os
from pathlib import Path
import environ

env = environ.Env(DEBUG=(bool, False))
BASE_DIR = Path(__file__).resolve().parent.parent.parent
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))



KUDA_LIVE_URL       = env("KUDA_LIVE_URL")
KUDA_TEST_URL       = env("KUDA_TEST_URL")
KUDA_API_KEY        = env("KUDA_API_KEY")
SME_TOKEN           = env("SME_TOKEN")

SME_HEADERS = {
    "Accept": "application/json, text/plain, */*",
    "Accept-language": "en-GB,en-US;q=0.9,en;q=0.8",
}