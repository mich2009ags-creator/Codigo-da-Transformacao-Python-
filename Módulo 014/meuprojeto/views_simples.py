from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models_simples import Produto

# Página principal - lista de produtos
def lista_produtos(request):
    busca = request.GET.get('busca', '')
    if busca:
        produtos = Produto.objects.filter(nome__icontains=busca)
    else:
        produtos = Produto.objects.all()
    
    return render(request, 'index.html', {
        'produtos': produtos,
        'busca': busca
    })

# Cadastrar produto
def cadastrar(request):
    if request.method == 'POST':
        produto = Produto(
            nome=request.POST['nome'],
            descricao=request.POST.get('descricao', ''),
            preco=float(request.POST['preco']),
            quantidade=int(request.POST['quantidade'])
        )
        produto.save()
        return redirect('/')
    return render(request, 'form.html')

# Editar produto
def editar(request, id):
    produto = get_object_or_404(Produto, id=id)
    if request.method == 'POST':
        produto.nome = request.POST['nome']
        produto.descricao = request.POST.get('descricao', '')
        produto.preco = float(request.POST['preco'])
        produto.quantidade = int(request.POST['quantidade'])
        produto.save()
        return redirect('/')
    return render(request, 'form.html', {'produto': produto})

# Excluir produto
def excluir(request, id):
    produto = get_object_or_404(Produto, id=id)
    produto.delete()
    return redirect('/')