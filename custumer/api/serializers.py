from rest_framework.serializers import ModelSerializer
from custumer.models import Custumer

"""
    Classe responsável por serializar os dados de um Cliente.
"""
class CustumerSerializer(ModelSerializer):
    class Meta:
        model = Custumer
        fields = '__all__'