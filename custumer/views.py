from rest_framework.decorators import api_view
from rest_framework.response import Response

from custumer.api.serializers import CustumerSerializer
from .models import Custumer


# FUNCTION THAT GET ALL ROUTES
@api_view(['GET'])
def getRoutes(request):
    # DEFINING API ROUTES
    routes = [
        {
            'Endpoint': '/custumers/',
            'method': 'GET',
            # 'body':None,
            "name": None,
            "city": None,
            "neighborhood": None,
            "street": None,
            "cellPhone": None,
            'description': 'return a array of custumers'
        },
        {
            'Endpoint': '/custumers/id',
            'method': 'GET',
            "name": None,
            "city": None,
            "neighborhood": None,
            "street": None,
            "cellPhone": None,
            'description': 'return a single custumer object'
        }, 
        {
            'Endpoint': '/custumers/create',
            'method': 'POST',
            "name": None,
            "city": None,
            "neighborhood": None,
            "street": None,
            "cellPhone": None,
            'description': 'Creates new custumer with data sent in post required body'
        }, 
        {
            'Endpoint': '/custumers/id/update',
            'method': 'PUT',
            "name": {'name':''},
            "city": {'city':''},
            "neighborhood": {'neighborhood':''},
            "street": {'street':''},
            "cellPhone": {'cellPhone':''},
            'description': 'Creates an existing custumers with data sent in'
        },
        {
            'Endpoint': '/custumers/id/delete',
            'method': 'DELETE',
            "name": None,
            "city": None,
            "neighborhood": None,
            "street": None,
            "cellPhone": None,
            'description': 'Deletes an existing custumer'
        },
    ]
    return Response(routes)

# FUNCTION THAT GET ALL CUSTUMERS


@api_view(['GET'])
def getCustumers(request):
    custumers = Custumer.objects.all()
    serializer = CustumerSerializer(custumers, many=True)
    return Response(serializer.data)

# FUNCTION THAT GETS A SINGLE custumer


@api_view(['GET'])
def getCustumer(request, pk):
    custumer = Custumer.objects.get(id=pk)
    serializer = CustumerSerializer(custumer, many=False)
    return Response(serializer.data)

# FUNCTION THAT CREATES A NEW custumer


@api_view(['POST'])
def createCustumer(request):
    data = request.data
    custumer = Custumer.objects.create(
        # "city","neighborhood","street", "cellPhone"
        name=data["name"],
        city=data["city"],
        neighborhood=data["neighborhood"],
        street=data["street"],
        cellPhone=data["cellPhone"],
    )
    serializer = CustumerSerializer(custumer, many=False)
    return Response(serializer.data)

# FUNCTION THAT UPDATES AN EXISTING custumer


@api_view(['PUT'])
def updateCustumer(request, pk):
    data = request.data

    custumer = Custumer.objects.get(id=pk)
    serializer = CustumerSerializer(custumer, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

# FUNCTION THAT DELETES AN EXISTING custumer


@api_view(['DELETE'])
def deleteCustumer(request, pk):
    custumer = Custumer.objects.get(id=pk)
    custumer.delete()
    return Response('Custumer deleted successfully')

# {
# "name": "Lucas Diniz",
# "city": "São Luís",
# "neighborhood": "Bequimão",
# "street": "Rua sem nome",
# "cellPhone": "545454545"
# }