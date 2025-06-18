from functools import wraps
import datetime

def log_level(level):
    def decorator(func):
        @wraps(func)
        def wrappers(*args, **kwargs):
            print(f"[{level}] {datetime.datetime.now()}: {func.__name__}")
            return func(*args, **kwargs)
        return wrappers
    return decorator

@log_level("INFO")
def process():
    return "Processed"

print(process()) # [INFO] 2025-06-18 15:52:53.389381: process

# Processed

# Logs with custom level

