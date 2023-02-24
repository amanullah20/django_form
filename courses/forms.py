from django import forms 
from django.core import validators



class StudentRegistration(forms.Form):
    first_name = forms.CharField(label_suffix='$',initial='Aiquest',max_length=20,required=False)
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Enter your last name'}))
    email = forms.EmailField()
    batch = forms.IntegerField(help_text='Must fill the area', min_value=15)
    password = forms.CharField(widget=forms.PasswordInput(),max_length=4,min_length=2)
    re_password= forms.CharField(widget=forms.PasswordInput(),max_length=4,min_length=2)
    text = forms.CharField(widget=forms.Textarea(attrs={'row':10,'cols':15}),error_messages={'required':'please inter proper tes'})
    payments= forms.DecimalField(min_value=500,max_value=5000,max_digits=6,decimal_places=2)
    django=forms.BooleanField()
     

    def clean(self):
        cleaned_data= super().clean()
        password = self.cleaned_data['password']
        re_password= self.cleaned_data['re_password']
        if password != re_password:
            return forms.ValidationError('please enter correct password')