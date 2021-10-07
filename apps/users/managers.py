from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email: str, name: str, password: str = None):
        user = self.model(email=self.normalize_email(email), name=name)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email: str, name: str, password: str = None):
        user = self.create_user(email, name, password=password)
        user.is_admin = True
        user.save()
        return user
