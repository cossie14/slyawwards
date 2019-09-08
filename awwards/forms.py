from django import forms
from .models import Project,Profile


class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ['editor', 'pub_date']

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')

# class RatesForm(forms.ModelForm):
#     class Meta:
#         model =Rates
#         exclude= ['user','project']


      
class NewsProfileForm(forms.ModelForm):
     class Meta:
        model = Profile
        exclude = ['user_id']