from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm


class CustomUserCreationForm(ModelForm):
    username = forms.CharField(
        label="Имя пользователя",
        help_text="Обязательное поле. До 150 символов. Только буквы, цифры и символы @/./+/-/_",
    )

    password = forms.CharField(
        label="Пароль",
        widget=forms.PasswordInput,
        help_text=(
            "Пароль должен быть не слишком похож на другие ваши данные. "
            "Минимум 8 символов. Не может быть слишком простым или состоять только из цифр."
        ),
    )

    password_confirm = forms.CharField(
        label="Подтверждение пароля",
        widget=forms.PasswordInput,
        help_text="Введите тот же пароль ещё раз.",
    )

    class Meta:
        model = User
        fields = ("username",)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Пароли не совпадают.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
