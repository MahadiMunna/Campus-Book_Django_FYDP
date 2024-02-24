from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserAccount

GENDER_TYPE = (
    ('Male', 'Male'),
    ('Female', 'Female'),
)
class RegistrationForm(UserCreationForm):
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

class EditProfile(forms.ModelForm):
    gender = forms.ChoiceField(choices=GENDER_TYPE)
    university = forms.CharField(max_length=200)
    department = forms.CharField(max_length=100)
    student_id = forms.CharField(max_length=20)
    contact_number = forms.CharField(max_length=15)
    present_address = forms.CharField(max_length=200)
    premanent_address = forms.CharField(max_length=200)

    class Meta:
        model = User
        fields = ['first_name', 'last_name','email']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if self.instance:
            try:
                user_account = self.instance.account
            except UserAccount.DoesNotExist:
                user_account = None

            if user_account:
                self.fields['gender'].initial = user_account.gender
                self.fields['university'].initial = user_account.university
                self.fields['department'].initial = user_account.department
                self.fields['student_id'].initial = user_account.student_id
                self.fields['contact_number'].initial = user_account.contact_number
                self.fields['present_address'].initial = user_account.present_address
                self.fields['premanent_address'].initial = user_account.premanent_address
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()

            user_account, created = UserAccount.objects.get_or_create(user=user)

            user_account.gender = self.cleaned_data['gender']
            user_account.university = self.cleaned_data['university']
            user_account.department = self.cleaned_data['department']
            user_account.student_id = self.cleaned_data['student_id']
            user_account.contact_number = self.cleaned_data['contact_number']
            user_account.present_address = self.cleaned_data['present_address']
            user_account.premanent_address = self.cleaned_data['premanent_address']
            
            user_account.save()

        return user