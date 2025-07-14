from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        label="Имя пользователя",
        help_text="Обязательное поле. До 150 символов. Только буквы, цифры и символы @/./+/-/_"
    )
    # FIXME rename field
    password1 = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        help_text=(
            "Пароль должен быть не слишком похож на другие ваши данные. "
            "Минимум 8 символов. Не может быть слишком простым или состоять только из цифр."
        )
    )
    # FIXME rename field
    password2 = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
        help_text="Введите тот же пароль ещё раз."
    )

    class Meta:
        model = User
        fields = ("username",)


class RegisterForm(UserCreationForm):
    ...
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'border'
