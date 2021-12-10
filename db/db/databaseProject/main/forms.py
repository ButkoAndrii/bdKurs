from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RegisterForm(UserCreationForm):
    name = forms.CharField(label='Імя',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name *'},
                                                  max_length=10))
    name = forms.CharField(label='Імя',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name *'},
                                                  max_length=10))
    name = forms.CharField(label='Імя',
                           widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name *'},
                                                  max_length=10))
    email = forms.EmailField(label='E-mail',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email *'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Your Password *'}))
    password2 = forms.CharField(label='Подтверждение пароля', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password *'}))
    is_active = False

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2', 'is_active')

    def clean(self):
        """
        По умолчанию в модели User поле email не является уникальным,
        в случае совпадения функция очищает поле и добавляет к сообщениям
        об ошибках новую строку. exists() возвращает True, если QuerySet
        содержит какие-либо результаты, и False, если нет.
        """
        cleaned_data = super().clean()
        if User.objects.filter(email=cleaned_data.get('email')).exists():
            self.add_error('email', 'такая почта уже зарегистрирована')
        return cleaned_data