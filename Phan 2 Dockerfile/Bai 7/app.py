import os

app_env = os.getenv('APP_ENV', 'development')
print(f"Current environment: {app_env}")