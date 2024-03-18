from django import forms
from .models import student, teacher, leave

class AddForm(forms.ModelForm):
    class Meta:
        model = student

        fields = ('firstname','lastname','email','age','phonenumber','address','department','username','password')

        widgets ={

            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control'}),
            'department': forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            
        }

class TeacherForm(forms.ModelForm):
    class Meta:
        model = teacher
        
        fields = ('firstname','lastname','username','password','email','age','phonenumber','address','department')

        widgets ={

            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'password':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.TextInput(attrs={'class':'form-control'}),
            'age':forms.TextInput(attrs={'class':'form-control'}),
            'phonenumber':forms.TextInput(attrs={'class':'form-control'}),
            'address': forms.Textarea(attrs={'class':'form-control'}),
            'department': forms.TextInput(attrs={'class':'form-control'}),
            
        }


class LeaveForm(forms.ModelForm):
    class Meta:
        model = leave

        fields = ['reason', 'date']

        widgets ={

            'reason': forms.Textarea(attrs={'class':'form-control'}),
            'date': forms.DateInput(attrs={'class':'form-control','type':'date'}),
            
        }
