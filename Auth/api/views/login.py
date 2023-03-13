from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(username=username, password=password)
    if user:
        if user.isESP:
            print('esp logined')
        # Bir oturum açma anahtarı oluşturun ve döndürün
        return Response({'token': 'TOKEN'})
    else:
        return Response({'error': 'Invalid username/password'})