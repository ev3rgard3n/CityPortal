from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    username = forms.CharField(required=True, help_text="Обязательное поле. Введите корректное имя пользователя.")
    email = forms.EmailField(required=True, help_text="Обязательное поле. Введите корректный email.")
    password1 = forms.CharField(required=True, help_text="Обязательное поле. Введите корректный пароль.")
    password2 = forms.CharField(required=True, help_text="Обязательное поле. Подтвердите пароль.")


    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
