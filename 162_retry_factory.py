# 1 Retry Factory

from functools import wraps
import time
def retry(n):
    def decorator(func):
        @wraps(func)
        def wrappers(*args, **kwargs):
            for attempt in range(n):
                try:
                    return func(*args, **kwargs)
                except:
                    if attempt == n - 1:
                        print("Failed")
                    time.sleep(1)
        return wrappers
    return decorator

@retry(3)
def fail():
    raise ValueError

fail()
# Failed

# Reties function with custom template


