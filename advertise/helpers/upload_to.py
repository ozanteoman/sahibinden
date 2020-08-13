import os
import uuid


def upload_to_user(instance, filename):
    extension = filename.split('.')[-1]
    new_name = f"{str(uuid.uuid4())}.{extension}"
    return os.path.join('users', new_name)
