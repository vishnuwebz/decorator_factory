from functools import wraps
import time

def rate_limit(max_calls, period):
    def decorator(func):
        calls = []
        @wraps(func)
        def wrappers(*args, **kwargs):
            now = time.time()
            calls[:] = [t for t in calls if now - t < period]
            if len(calls) < max_calls:
                calls.append(now)
                return func(*args, **kwargs)
            print("Rate limit")
        return wrappers
    return decorator

@rate_limit(2, 5)
def api():
    return "API call"

print(api())
print(api())
print(api())

"""
API call
API call
Rate limit
None
"""

# limits calls within period