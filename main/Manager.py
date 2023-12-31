from django.contrib.auth.base_user import BaseUserManager #импортируем для создание своего менеджера клиентов



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, first_name, phone_number, password , **extra_fields):
        """Создает и сохраняет пользователя с заданным адресом электронной почты или телефоном и паролем.""" 


        if not phone_number:
            raise ValueError('Указанный номер телефона должен быть установлен')
   
        user = self.model(first_name = first_name, phone_number = phone_number, **extra_fields)
        
        user.set_password(password)
        user.save()
        return user
    #как сахронять простого пользователя
    def create_user(self,first_name,phone_number, password, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_active', True)

        return self._create_user(first_name,phone_number, password, **extra_fields)
    #как сахронять суперпользователя
    def create_superuser(self,first_name,phone_number, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)


        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(first_name,phone_number, password, **extra_fields )