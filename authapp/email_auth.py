from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

CustomUser = get_user_model()


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None):
        if "@" in username:
            kwargs = {"email": username}
        else:
            kwargs = {"username": username}

        try:
            user = CustomUser.objects.get(**kwargs)
            if user.check_password(password):
                return user
            else:
                return None
        except CustomUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist:
            return None
