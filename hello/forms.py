from django import forms

from hello.models import Friend


class HelloForm(forms.Form):
    name = forms.CharField(label='Name')
    mail = forms.EmailField(label='Email')
    gender = forms.BooleanField(label='Gender', required=False)
    age = forms.IntegerField(label='Age')
    birthday = forms.DateField(label='Birth')


class FriendForm(forms.ModelForm):
    class Meta:
        model = Friend
        fields = ['name', 'mail', 'gender', 'age', 'birthday']


class FindForm(forms.Form):
    find = forms.CharField(label='Find', required=False)


class CheckForm(forms.Form):
    str = forms.CharField(label='String')

    def clean(self):
        cleand_data = super().clean()
        str = cleand_data['str']
        if str.lower().startswith('no'):
            raise forms.ValidationError('You input "NO"!')
