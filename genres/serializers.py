from rest_framework import serializers
from genres.models import Genre

# Semelhante aos Forms do Django os Serializers podem ser feitos manualmente ou utilizando um ModelSerializer quando o objetivo é serializar de maneira padrão todo um Model

# Serializador manual
# class GenreSerializer(serializers.Serializer): # Classe de serialização para o modelo Genre
#     id = serializers.IntegerField(read_only=True) # Define o campo ID como somente leitura
#     name = serializers.CharField(max_length=100) # Define o campo name com no máximo 100 caracteres
#     ... # Outros campos do modelo

# Serializador utilizando ModelSerializer
class GenreSerializer(serializers.ModelSerializer): # Classe de serialização para o modelo Genre
    class Meta:
        model = Genre # Define o Modelo a ser serializado
        fields = '__all__' # Define que todos os campos do modelo devem ser serializados
        # fields = ['id', 'name'] # Define quais campos do modelo devem ser serializados caso não queira todos