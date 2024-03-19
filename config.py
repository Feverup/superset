import os

ENABLE_PROXY_FIX = True
FEATURE_FLAGS = {
    "DYNAMIC_PLUGINS": True,
    "ENABLE_TEMPLATE_PROCESSING": True,
    "EMBEDDED_SUPERSET": True,
    "HORIZONTAL_FILTER_BAR": True,
}
PREFERRED_DATABASES = [
    "Snowflake",
    "PostgreSQL",
    "ClickHouse Connect (Superset)",
]
LANGUAGES = {
    "en": {"flag": "us", "name": "English"},
    "es": {"flag": "es", "name": "Spanish"},
    "fr": {"flag": "fr", "name": "French"},
    "de": {"flag": "de", "name": "German"},
}
SECRET_KEY = os.environ.get("SECRET_KEY", "-")
MAPBOX_API_KEY = os.environ.get("MAPBOX_API_KEY", "-")

if os.environ["ENV"] == "local":
    SESSION_COOKIE_SAMESITE = "None"
    HTTP_HEADERS = {"X-Frame-Options": "ALLOWALL"}
    CORS_OPTIONS = {"supports_credentials": True, "allow_headers": ["*"], "resources": ["*"], "origins": ["*"]}
    GUEST_ROLE_NAME = "Gamma"
else:
    TALISMAN_ENABLED = False
