# 3 access control

from functools import wraps

def require_role(role):
    def decorator(func):
        @wraps(func)
        def wrapper(user, *args, **kwargs):
            if user.get("role") == role:
                return func(user, *args, **kwargs)
            return "Access denied"
        return wrapper
    return decorator

@require_role("admin")
def delete(user):
    return "Deleted"

user = {"role" : "admin"}
print(delete(user))

# Deleted

# Restricts access by role