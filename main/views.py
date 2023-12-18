from django.shortcuts import render
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework import generics
from .serilaizers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.utils import timezone

# Create your views here.
class BathHouseView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    """ Добавление новости жк """
    serializer_class = BathHouseModelPostSerilizer

    def get(self,request):
        
        queryset = self.get_queryset()
        serializer = BathHouseModelSerilizer(queryset, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def get_queryset(self):

        return BathHouseModel.objects.all()

    def post(self,request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        end_time = timezone.now() + timezone.timedelta(hours= int(request.data['hours']))
        create = BathHouseModel.objects.create(number_key = request.data['number_key'],
                                    first_name = request.data['first_name'],
                                    number_phone = request.data['number_phone'],
                                    my_type = request.data['my_type'],
                                    hours = request.data['hours'],
                                    end_time = end_time
                                      )
     
        return Response(BathHouseModelSerilizer(create).data, status=status.HTTP_200_OK)



class BathHouseDeleteView(generics.GenericAPIView):

    """Удаление поста"""
    permission_classes = (AllowAny,)
    def delete(self, request,pk, *args, **kwargs):
        try:
            post=BathHouseModel.objects.get(id=pk)
        except ObjectDoesNotExist:
            data={"error":f"not found {pk}"}
            return Response(data,status=status.HTTP_404_NOT_FOUND)
        post.delete()
        return Response({'success': True},status=status.HTTP_200_OK)

class BathHouseUpdateView(generics.GenericAPIView):
    """Обновление """
    serializer_class = BathHouseModelUpdateSerilizer
    permission_classes = (AllowAny,)

    def post(self, request,pk, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            
            data = BathHouseModel.objects.get(id=pk)
            queryset = BathHouseModel.objects.exclude(id=pk)
            if not queryset.filter(number_key=request.data['number_key']).exists():
                end_time = timezone.now() + timezone.timedelta(hours= int(request.data['hours']))
                data.number_key = request.data['number_key']  
                data.first_name = request.data['first_name']
                data.number_phone =  request.data['number_phone']
                data.my_type = request.data['my_type']
                data.hours = request.data['hours'] 
                data.date_start = timezone.now() 
                data.end_time = end_time
            else: 
                return Response({"number_key" : "Такой номер ящика уже существует "},status=status.HTTP_400_BAD_REQUEST)
            
        except ObjectDoesNotExist:
            data={"error":f"not found {pk}"}
            return Response(data,status=status.HTTP_404_NOT_FOUND)

        data.save()
        return Response({'success': True},status=status.HTTP_200_OK)
    
class SearchBathHouse(generics.ListAPIView):
    queryset = BathHouseModel.objects.all()
    serializer_class = BathHouseModelSerilizer
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'number_phone','number_key']



class BathHouseFiltter(generics.ListAPIView):
    queryset = BathHouseModel.objects.all()
    serializer_class = BathHouseModelSerilizer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['my_type', 'hours']

