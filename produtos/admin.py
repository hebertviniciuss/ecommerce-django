from django.contrib import admin
from .models import Marca, Categoria, Produto
# Register your models here.

@admin.register(Marca)
class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome_produto','preco', 'descricao', 'imagem_produto')