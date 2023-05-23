from django import forms
from main.validators import validateName, validUsername


class passwordChangeForm(forms.Form):
    user = None
    current = forms.CharField(
        required=True,
        label="Current", validators=[],
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Current password'}),
    )

    new = forms.CharField(
        required=True,
        label="New", validators=[],
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New password'}),
    )

    re_new = forms.CharField(
        required=True,
        label="Confirm", validators=[],
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm password'}),
    )

    def __init__(self, user, *args, **kwargs):
        super(passwordChangeForm, self).__init__(*args, **kwargs)
        self.user = user

    def clean(self, *args, **kwargs):
        current = self.cleaned_data.get('current')
        new = self.cleaned_data.get('new')
        re_new = self.cleaned_data.get('re_new')
        if not self.user.check_password(raw_password=current):
            raise forms.ValidationError("Incorrect current password.")
        if len(new) < 6 or len(re_new) < 6:
            raise forms.ValidationError('Too short password.')
        if new != re_new:
            raise forms.ValidationError("Password didn't match.")
        else:
            print(self.user.check_password(raw_password=current))
        return super(passwordChangeForm, self).clean(*args, **kwargs)


class UpdateForm(forms.Form):
    photo      = forms.ImageField(label='', required=False)
    first_name = forms.CharField(
        required=True,
        label="First Name", validators=[],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First name'}),
    )
    last_name = forms.CharField(
        required=True,
        label="Last Name", validators=[],
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last name'}),
    )

    about_me = forms.CharField(
        required=False,
        label="About me", validators=[],
        widget=forms.Textarea(
            attrs={
                'class': 'form-control', 'placeholder': 'Write about you...',
                'style': 'height:180px',
            }
        ),
    )
    photo.widget.attrs['style'] = "display:none"
    photo.widget.attrs['id'] = "inPhoto"
    def __init__(self, account, *args, **kwargs):
        super(UpdateForm, self).__init__(*args, **kwargs)
        self.initial['first_name'] = account.user.first_name
        self.initial['last_name'] = account.user.last_name
        self.initial['about_me'] = account.about_me

    def clean(self, *args, **kwargs):
        first_name = self.cleaned_data.get('first_name')
        last_name  = self.cleaned_data.get('last_name')
        if validateName(first_name) != '' or validateName(last_name) != '':
            msg = validateName(first_name)
            raise forms.ValidationError('<li>Name contains invalid character.</li><li>Name is too short.</li>')
        return super(UpdateForm, self).clean(*args, **kwargs)