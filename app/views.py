from django.shortcuts import render
import os

pasta='app/static'
nomes_arquivos= os.listdir(pasta)


# Create your views here.
def index(request):
  return render(request, "index.html")

def outraspaginas(request, argumento):
  if argumento == "contato":
    return  render(request, "contato.html")

  elif argumento == "sobre":
    return render(request, "sobre.html")

  elif argumento == "pedidos":
    devolver = {
      'titulo_card' : "Murilo ",
      'descricao' : "Murilândia",
      'imagens' : nomes_arquivos,
    }
    return render(request, "pedidos.html", devolver)
  
  return render(request, "index.html")