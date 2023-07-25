from django.shortcuts import render, get_object_or_404,redirect
from .models import Produto, Marca, Categoria
from .forms import ProdutoForm, MarcaForm, CategoriaForm
# Create your views here.
def produto_editar(request,id):
    produto = get_object_or_404(Produto,id=id)
   
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES,instance=produto)
        if form.is_valid():
            form.save()
            return redirect('admin_produtos')
    else:
        form = ProdutoForm(instance=Produto)

    return render(request,'admin/editarproduto.html',{'form':form})

def produto_remover(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('lista_produtos') 

def produto_detalhar(request,id):
    produto = get_object_or_404(Produto, id=id)
    context ={
        'produto':produto
    }
    return render(request, "produtos/detalharproduto.html",context)

def criar_produto(request):
    
    if request.method == 'POST':
        form = ProdutoForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            form = ProdutoForm()
    else:
        form = ProdutoForm()
    
    return render(request,"admin/adicionarproduto.html", {'form':form})

def produto_listar(request):
    produtos = Produto.objects.all()
    context ={
        'produtos':produtos
    }
    return render(request, "produtos/produto.html",context)

def admin_produtos(request):
    produtos = Produto.objects.all()
    context ={
        'produtos':produtos
    }
    return render(request, "produtos/form.html",context)

def criar_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = CategoriaForm()
    else:
        form = CategoriaForm()
    
    return render(request,"admin/adicionarcategoria.html", {'form':form})

def criar_marca(request):
    if request.method == 'POST':
        form = MarcaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = MarcaForm()
    else:
        form = MarcaForm()
    
    return render(request,"admin/adicionarmarca.html", {'form':form})

# Create your views here.
