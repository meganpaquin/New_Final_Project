from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django.forms.widgets import TextInput
from django.urls import reverse_lazy


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'image', 'phone', 'color')
        widgets = {
            'color': TextInput(attrs={'type': 'color'}),
        }
        success_url = reverse_lazy("home")