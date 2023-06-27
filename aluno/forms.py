from django import forms

class ContatoForm(forms.Form):
    full_name = forms.CharField(
        label="Nome Completo", 
        max_length=100, 
        widget=forms.TextInput(attrs={
            'placeholder': 'Name', 
            'class': 'form-control'
        })
    )
    
    email = forms.EmailField(
        label="Email", 
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'nome@email.com',
            'class': 'form-control'
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'placeholder': 'Mensagem',
            'class': 'form-control'
        })
    )

    fields = ['all']