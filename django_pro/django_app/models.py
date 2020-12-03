from django.db import models
from django import forms

# Create your models here.
class model_form(models.Model):
    """docstring for model_form."""
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    subject = models.CharField(max_length = 20)
    comment = models.TextField(max_length = 20)
    def __str_(self):
        return self.name

class form_form(forms.ModelForm):
    class Meta():
        model = model_form
        fields = ('name','email','subject','comment')
        widgets ={
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email' : forms.TextInput(attrs={'class':'form-control'}),
            'subject' : forms.TextInput(attrs={'class':'form-control'}),
            'comment' : forms.Textarea(attrs={'rows':2,'class':'form-control'}),

        }
