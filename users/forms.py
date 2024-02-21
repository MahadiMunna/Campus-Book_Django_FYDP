from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount

GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    university = forms.CharField(max_length=200)
    department = forms.CharField(max_length=100)
    student_id = forms.CharField(max_length=20)
    contact_number = forms.CharField(max_length=15)
    present_address = forms.CharField(max_length=200)
    premanent_address = forms.CharField(max_length=200)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','gender', 'university','department','student_id', 'contact_number','present_address','premanent_address','password1', 'password2' ]
    
    def save(self, commit=True):
        account_user = super().save(commit=False)
        if commit == True:
            account_user.save()
            gender = self.cleaned_data.get('gender')
            university = self.cleaned_data.get('university')
            department = self.cleaned_data.get('department')
            student_id = self.cleaned_data.get('student_id')
            contact_number = self.cleaned_data.get('contact_number')
            present_address = self.cleaned_data.get('present_address')
            premanent_address = self.cleaned_data.get('premanent_address')
        
        UserAccount.objects.create(
            user = account_user,
            gender = gender,
            university = university,
            department = department,
            student_id = student_id,
            contact_number = contact_number,
            present_address = present_address,
            premanent_address = premanent_address,
        )
    
        return account_user
         