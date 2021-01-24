from django import forms

messages = {
    'required': 'you should fill this field',
    'invalid': 'your filled data is invalid',
    'max_length': 'please decrement your entry',
}


class UserLoginForm(forms.Form):
    username = forms.CharField(error_messages=messages, max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(error_messages=messages, max_length=40,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))


class UserRegistrationForm(forms.Form):
    username = forms.CharField(error_messages=messages, max_length=30,
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(error_messages=messages, max_length=50,
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(error_messages=messages, max_length=40,
                               widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
