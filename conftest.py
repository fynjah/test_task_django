import os

os.environ.setdefault("SECRET_KEY", "test-secret-key")
os.environ.setdefault("DEBUG", "True")
os.environ.setdefault("ENVIRONMENT", "test")
os.environ.setdefault("ALLOWED_HOSTS", "localhost")
