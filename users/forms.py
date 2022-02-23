from django import forms
from . import models


class SignUpForm(forms.Form):

    first_name = forms.CharField(max_length=80, label="성")
    last_name = forms.CharField(max_length=80, label="이름")
    username = forms.CharField(max_length=15, label="아이디")
    email = forms.EmailField(label="이메일")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    password1 = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        try:
            models.User.objects.get(email=email)
            raise forms.ValidationError("이미 사용되고 있는 이메일입니다.")
        except models.User.DoesNotExist:
            return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            models.User.objects.get(username=username)
            raise forms.ValidationError("유저가 이미 존재합니다.")
        except models.User.DoesNotExist:
            return username

    def clean_password1(self):
        password = self.cleaned_data.get("password")
        password1 = self.cleaned_data.get("password1")
        if password != password1:
            raise forms.ValidationError("패스워드가 서로 맞지 않습니다.")
        else:
            return password

    def save(self):
        first_name = self.cleaned_data.get("first_name")
        last_name = self.cleaned_data.get("last_name")
        username = self.cleaned_data.get("username")
        email = self.cleaned_data.get("email")
        password = self.cleaned_data.get("password")
        user = models.User.objects.create_user(username, email, password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()


class LoginForm(forms.Form):

    username = forms.CharField(max_length=10, required=True, label="아이디")
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")

    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        try:
            user = models.User.objects.get(username=username)
            if user.check_password(password):
                return self.cleaned_data
            else:
                self.add_error("password", forms.ValidationError("패스워드가 다릅니다"))
        except models.User.DoesNotExist:
            self.add_error("username", forms.ValidationError("유저가 존재하지 않습니다."))
