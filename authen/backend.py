from django.contrib.auth import get_user_model


class EmailBackend(object):
    @staticmethod
    def authenticate(username=None, password=None, **kwargs):
        user_model = get_user_model()
        try:
            user = user_model.objects.get(username=username)
        except user_model.DoesNotExist:
            try:
                user = user_model.objects.get(email=username)
            except user_model.DoesNotExist:
                return None
        if user.is_active and user.check_password(password):
            # user.backend = EmailBackend
            return user
        return None

    @staticmethod
    def get_user(user_id):
        """retrieve a username.
        kwargs could be:
        username, email, first_name, last_name

        if username is provided, kwargs will be ignored
        only first value of kwargs will be used
        """
        user_model = get_user_model()
        try:
            return user_model.objects.get(pk=user_id)
        except user_model.DoesNotExist:
            return None
