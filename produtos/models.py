from django.db import models

class Marca(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome da Marca')

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=150, verbose_name='Nome da Categoria')

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome_produto = models.CharField(max_length=150, verbose_name='Nome do Produto')
    preco = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Preço')
    descricao = models.TextField(verbose_name='Descrição')
    imagem_produto = models.ImageField(null=True, blank=True, upload_to='produtos', verbose_name='Imagem do Produto')
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, verbose_name='Marca')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name='Categoria')

    def __str__(self):
        return self.nome_produto
