from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password, **extra_kwargs):
        # якщо Юзер передає параметри ми його активуємо
        extra_kwargs['is_active'] = True

        if not email:
            raise ValueError('The email must be set')

        email = self.normalize_email(email)
        # створюємо екземпляр класу user
        user = self.model(email=email, **extra_kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_kwargs):
        extra_kwargs.setdefault('is_staff', True)
        extra_kwargs.setdefault('is_superuser', True)
        extra_kwargs.setdefault('is_active', True)

        if not extra_kwargs.get('is_staff'):
            raise ValueError('Superuser must have is_staff=True')
        if not extra_kwargs.get('is_superuser'):
            raise ValueError('Superuser must have is_superuser=True')

        user = self.create_user(email, password, **extra_kwargs)
        return user
