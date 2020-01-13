from django import forms
class ContactForm(forms.Form):
    name= forms.CharField(
        label="Enter Your Name",
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Your Name',
                'class': 'form-control'
            }
        )
    )
    salary= forms.IntegerField(
        label= "Enter Your Salary",
        widget= forms.NumberInput(
            attrs={
                'placeholder': 'Your Salary',
                'class': 'form-control'
            }
        )
    )
    email= forms.EmailField(
        label= "Enter your Emailid",
        widget= forms.EmailInput(
            attrs={
                'placeholder': 'Your Emailid',
                'class': 'form-control'

            }
        )
    )
    mobile= forms.IntegerField(
        label= "Enter your mobile number",
        widget= forms.NumberInput(
            attrs={
                'placeholder': 'Your mobile number',
                'class': 'form-control'
            }
        )
    )
    location= forms.CharField(
        label= "Enter your location",
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Your location',
                'class': 'form-control'
            }
        )
    )