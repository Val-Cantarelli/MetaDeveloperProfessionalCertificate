from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes,throttle_classes
from .serializers import MenuItemSerializer
from django.shortcuts import get_object_or_404
from rest_framework import status
from .models import MenuItem
from django.core.paginator import Paginator,EmptyPage
from rest_framework.permissions import IsAuthenticated
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework import viewsets
from rest_framework import generics
from .serializers import MenuItemSerializer
from .throttles import TenCallsPerMinute
from rest_framework.permissions import IsAdminUser
from django.contrib.auth.models import User,Group

'''
'''
#
@api_view(['POST', 'GET'])
def menu_items(request):
    if request.method == 'GET':
        items = MenuItem.objects.select_related('category').all()
        category_name = request.query_params.get('category')
        to_price = request.query_params.get('to_price')
        search = request.query_params.get('search')
        ordering = request.query_params.get('ordering')
        perpage = request.query_params.get('perpage',default=2)
        page=request.query_params.get('page',default=1)
        
        if category_name:
            items = items.filter(category__title = category_name)
        if to_price:
            items = items.filter(price = to_price) 
            # in price__lte,"lte" means <= to a value. But we want =, so we use just 
            # price
        
        if search:
            items=items.filter(title__icontains=search)
        
        if ordering:
            # Se eu quiser criar hierarquia na ordem
            #items = items.order_by(ordering)    
            ordering_fields= ordering.split(',')
            items = items.order_by(*ordering_fields)
            
        paginator = Paginator(items,per_page=perpage)
        try:
            items=paginator.page(number=page)
        except EmptyPage:
            items=[]
                
        serialized_item = MenuItemSerializer(items,many=True)    
        return Response(serialized_item.data)
    
    if request.method =='POST':
        serialized_item = MenuItemSerializer(data=request.data)
        # Verify the data and raise an error
        serialized_item.is_valid(raise_exception=True)
        serialized_item.save()
        return Response(serialized_item.data,status.HTTP_201_CREATED)
                  
@api_view()
def single_item(request,id):
    item= get_object_or_404(MenuItem,pk=id)
    serialized_item = MenuItemSerializer(item)
    return Response(serialized_item.data)       



@api_view()
@permission_classes([IsAuthenticated])
def secret(request):
    return Response({"message": "Secreta mensagem..uauaaaaa"}) 

@api_view(['POST'])
@permission_classes([UserRateThrottle])
def manager_view(request):
    if request.user.groups.filter(name='Manager').exists():
        return Response({"message":"Only the manager should see this!"})
    else: 
        return Response({"message": "You are not authorized"},403)

# Throttling - anonymous users
@api_view()
@throttle_classes([AnonRateThrottle])
def throttle_check(request):
    return Response({"message":"Sucessfull"})

# Throttling - auth users
@api_view()
@permission_classes([IsAuthenticated])
@throttle_classes([TenCallsPerMinute])
def throttle_check_auth(request):
    return Response({"message":"message for the logged users only"})

@api_view()
@permission_classes([IsAuthenticated])
def me(request):
    return Response(request.user.email)


@api_view(['POST'])
@permission_classes([IsAdminUser])
def managers(request):
    username = request.data['username']
    if username:
        user = get_object_or_404(User, username=username)
        managers = Group.objects.get(name="Manager")
        
        if request.method == 'POST':
            managers.user_set.add(user)
        elif request.method == 'DELETE':
            managers.user_set.remove(user)
            
        return Response({"message":"ok"})
    
    return Response({"message":"error"},status.HTTP_400_BAD_REQUEST)


'''
ModelView(como RetrieveUpdateDestroyAPIView): tem um controle mais detalhado;
ModelViewSet: tem todos os CRUD aqui dentro. 

class MenuItemsViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer 
    
    def get_throttles(self):
        if self.action == 'retrieve':
            throttle_classes = [AnonRateThrottle]
            # ou passo uma classe personalizada de throtlles.py
        else:
            throttle_classes = []
            # Para todas as outras ações (como list, create, etc.), throttle_classes 
            # será uma lista vazia. Isso significa que não haverá throttling para 
            # essas ações.
        return [throttle() for throttle in throttle_classes]
    
    
'''

