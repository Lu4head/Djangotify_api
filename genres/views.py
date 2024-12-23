#import json
#from django.utils.decorators import method_decorator
#from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#from django.views.generic import View
#from django.shortcuts import get_object_or_404 # É utilizada a função get_object_or_404 para obter um objeto com base no ID recebido e garantir que caso não seja encontrado seja retornado um erro 404
from rest_framework import generics 
from genres.models import Genre
from genres.serializers import GenreSerializer

# ##############################################################################################################
# |    API sem usar DRF - Apenas Padrão Django                                                                 |
# ##############################################################################################################


# @method_decorator(csrf_exempt, name='dispatch') # csrf_exempt decorator é necessário para permitir requisições POST desligando a proteção CSRF
# class genre_create_list_view(View):
#     def get(self, request): # Método GET para retornar todos os gêneros
#         genres = Genre.objects.all()
#         data = [{'id': genre.id,'name': genre.name,} for genre in genres] # Cria um dicionário com os gêneros
#         return JsonResponse(data, safe=False)
    
#     def post(self,request): # Método POST para criar um novo gênero
#         data = json.loads(request.body.decode('utf-8')) # Decodifica o corpo da requisição para um dicionário
#         new_genre = Genre.objects.create(name=data['name']) # Cria um novo objeto Genre com o nome recebido
#         new_genre.save()
#         return JsonResponse({'id': new_genre.id, 'name': new_genre.name},status=201)

# class genre_detail_update_delete_view(View):
#     def setup(self, request, *args, **kwargs): # Método setup para obter o gênero com base no ID recebido, essa função é chamada independente do método HTTP
#         super().setup(request, *args, **kwargs) # Chama o método setup da classe pai
#         #self.genre = Genre.objects.get(pk=kwargs.get('pk')) # Esse método não é utilizado pois se não encontrar o obejto com o ID recebido ele retorna um erro 500 fora do padrão de API's REST
#         self.genre = get_object_or_404(Genre, pk=kwargs.get('pk')) # Obtém o gênero com base no ID recebido, caso não seja encontrado retorna um erro 404
    
#     def get(self, request, pk): # Método GET para retornar um gênero específico
#         #self.genre = get_object_or_404(Genre, pk=kwargs.get('pk')) # No lugar do setup é possível utilizar o get_object_or_404 diretamente no método de cada requisição
#         return JsonResponse({'id': self.genre.id, 'name': self.genre.name})
            
    
#     def put(self, request, pk): # Método PUT para atualizar um gênero específico
#         data = json.loads(request.body.decode('utf-8')) # Decodifica o corpo da requisição para um dicionário
#         self.genre.name = data['name'] # Atualiza o nome do gênero
#         self.genre.save()
#         return JsonResponse({'id': self.genre.id, 'name': self.genre.name}, status=200)
        
    
#     def delete(self, request, pk): # Método DELETE para deletar um gênero específico
#         self.genre.delete() # Deleta o gênero
#         return JsonResponse({'message': f'Genre { self.genre.name } deleted successfully'}, status=204)


# ##############################################################################################################
# |    API usando DRF                                                                                          |
# ##############################################################################################################

class GenreListCreateView(generics.ListCreateAPIView): # Classe para listar e criar gêneros utilizando o ListCreateAPIView do Django Rest Framework
    queryset = Genre.objects.all() # Define a queryset para retornar todos os gêneros
    serializer_class = GenreSerializer # Define a classe de serialização para a classe GenreSerializer

class GenreDetailView(generics.RetrieveUpdateDestroyAPIView): # Classe para visualizar, atualizar e deletar um gênero utilizando o RetrieveUpdateDestroyAPIView do Django Rest Framework
    queryset = Genre.objects.all() # Define a queryset para retornar todos os gêneros
    serializer_class = GenreSerializer # Define a classe de serialização para a classe GenreSerializer
    #lookup_field = 'pk' # Define o campo de busca como o ID do gênero, não obrigatório pois o padrão é o ID
