from django import forms
from .models import Produto, Marca, Categoria

class ProdutoForm(forms.ModelForm):
    
    class Meta:
        model = Produto
        fields = '__all__'
        widgets = {
            'nome_produto' : forms.TextInput(attrs={'class': 'form-control'}),
            'preco': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao' : forms.TextInput(attrs={'class': 'form-control'}),
            'imagem_produto': forms.FileInput(attrs={'class': 'form-control'}),
            'marca': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'})
        }

class MarcaForm(forms.ModelForm):

    class Meta:
        model = Marca
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control'}),
        }

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'
        widgets = {
            'nome' : forms.TextInput(attrs={'class': 'form-control'}),
        }