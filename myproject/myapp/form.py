from django import forms
from myapp.models import Product

class productUploadForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['p_name','p_color','p_size','p_prize','p_qty','p_description','p_photo']
        
        widgets = {
            'p_name': forms.TextInput(attrs = {'class': 'form-control','value': 'hi'}),
            'p_color': forms.TextInput(attrs = {'class': 'form-control' , 'placeholder': 'hello' }),
            'p_size': forms.TextInput(attrs = {'class': 'form-control' }),
            'p_prize': forms.NumberInput(attrs = {'class': 'form-control' }),
            'p_qty': forms.NumberInput(attrs = {'class': 'form-control' }),
            'p_description': forms.Textarea(attrs = {'class': 'form-control' }),
            'p_photo': forms.ClearableFileInput(attrs = {'class': 'form-control' })

        }
        
        
class productEditForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['p_name','p_color','p_size','p_prize','p_qty','p_description','p_photo']
        
        widgets = {
            'p_name': forms.TextInput(attrs = {'class': 'form-control','value': 'hello world'}),
            'p_color': forms.TextInput(attrs = {'class': 'form-control' , 'placeholder': 'hello' }),
            'p_size': forms.TextInput(attrs = {'class': 'form-control' }),
            'p_prize': forms.NumberInput(attrs = {'class': 'form-control' }),
            'p_qty': forms.NumberInput(attrs = {'class': 'form-control' }),
            'p_description': forms.Textarea(attrs = {'class': 'form-control' }),
            'p_photo': forms.ClearableFileInput(attrs = {'class': 'form-control' })

        }