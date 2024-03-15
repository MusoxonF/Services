from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from rest_framework import status
from.models import *
from.serializers import *


class PhotoView(ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSer


class PhotoDetail(APIView):
    def get(self, request, id):
        try:
            photo = Photo.objects.get(id=id)
            serializer = PhotoSer(photo)
            return Response(serializer.data)
        except:
            return Response({'message':"bu id xato"})

    def patch(self, request, id):
        photo = Photo.objects.get(id=id)
        rasm = request.data.get('photos')
        photo.photo = rasm
        photo.save()
        return Response({'message':'successfully'})
    
    def delete(self, request, id):
        photo = Photo.objects.get(id=id)
        photo.delete()
        return Response({'message':'successfully'})


class PhotoProductView(ListCreateAPIView):
    queryset = PhotoProduct.objects.all()
    serializer_class = PhotoProductSer


class PhotoProductDetail(APIView):
    def get(self, request, id):
        try:
            photo = PhotoProduct.objects.get(id=id)
            serializer = PhotoProductSer(photo)
            return Response(serializer.data)
        except:
            return Response({'message':"bu id xato"})
    
    def patch(self, request, id):
        photo = PhotoProduct.objects.get(id=id)
        rasm = request.data.get('photos')
        photo.photo = rasm
        photo.save()
        return Response({'message':'successfully'})

    def delete(self, request, id):
        photo = PhotoProduct.objects.get(id=id)
        photo.delete()
        return Response({'message':'successfully'})


class PhotoClientView(ListCreateAPIView):
    queryset = PhotoClient.objects.all()
    serializer_class = PhotoClientSer


class PhotoClientDetail(APIView):
    def get(self, request, id):
        try:
            photo = PhotoClient.objects.get(id=id)
            serializer = PhotoClientSer(photo)
            return Response(serializer.data)
        except:
            return Response({'message':"bu id xato"})
    
    def patch(self, request, id):
        photo = PhotoClient.objects.get(id=id)
        rasm = request.data.get('photos')
        photo.photo = rasm
        photo.save()
        return Response({'message':'successfully'})
    
    def delete(self, request, id):
        photo = PhotoClient.objects.get(id=id)
        photo.delete()
        return Response({'message':'successfully'})


class ServicesView(APIView):
    def get(self, request):
        services = Services.objects.all()
        serializer = ServicesGetSer(services, many=True)
        return Response(serializer.data)

    def post(self, request):
        a = request.data.getlist('photos', [])
        serializer = ServicesSer(data=request.data)
        if serializer.is_valid():
            s = serializer.save()
            for i in a:
                n = Photo.objects.create(photo=i)
                s.photos.add(n)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ServicesDetail(APIView):
    def get(self, request, id):
        try:
            services = Services.objects.get(id=id)
            serializer = ServicesSer(services)
            return Response(serializer.data)
        except:
            return Response({'message':"bu id xato"})
    
    def patch(self, request, id):
        a = request.data.getlist('photos', [])
        services = Services.objects.get(id=id)
        serializer = ServicesSer(services, data=request.data, partial=True)
        if serializer.is_valid():
            s=serializer.save()
            if a:
                for i in a:
                    n = Photo.objects.create(photo=i)
                    s.photos.add(n)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        services = Services.objects.get(id=id)
        services.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ProductsView(APIView):
    def get(self, request):
        products = Products.objects.all()
        serializer = ProductsGetSer(products, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        a = request.data.getlist('photos', [])
        serializer = ProductsSer(data=request.data)
        if serializer.is_valid():
            s=serializer.save()
            for i in a:
                n = PhotoProduct.objects.create(photo=i)
                s.photos.add(n)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductsDetail(APIView):
    def get(self, request, id):
        try:
            products = Products.objects.get(id=id)
            serializer = ProductsSer(products)
            return Response(serializer.data)
        except:
            return Response({'message':"bu id xato"})
    
    def patch(self, request, id):
        a = request.data.getlist('photos', [])
        products = Products.objects.get(id=id)
        serializer = ProductsSer(products, data=request.data, partial=True)
        if serializer.is_valid():
            s=serializer.save()
            if a:
                for i in a:
                    n = PhotoProduct.objects.create(photo=i)
                    s.photos.add(n)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        products = Products.objects.get(id=id)
        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ClientsView(APIView):
    def get(self, request):
        clients = Clients.objects.all()
        serializer = ClientsGetSer(clients, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        a = request.data.getlist('photos', [])
        serializer = ClientsSer(data=request.data)
        if serializer.is_valid():
            s=serializer.save()
            for i in a:
                n = PhotoClient.objects.create(photo=i)
                s.photos.add(n)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ClientsDetail(APIView):
    def get(self, request, id):
        try:
            clients = Clients.objects.get(id=id)
            serializer = ClientsSer(clients)
            return Response(serializer.data)
        except:
            return Response({'message':"bu id xato"})

    def patch(self, request, id):
        a = request.data.getlist('photos', [])
        clients = Clients.objects.get(id=id)
        serializer = ClientsSer(clients, data=request.data, partial=True)
        if serializer.is_valid():
            s=serializer.save()
            if a:
                for i in a:
                    n = PhotoClient.objects.create(photo=i)
                    s.photos.add(n)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        clients = Clients.objects.get(id=id)
        clients.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SocialView(APIView):
    def get(self, request):
        social = Social.objects.all()
        serializer = SocialSer(social, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SocialSer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class SocialDetail(APIView):
    def get(self, request, id):
        try:
            social = Social.objects.get(id=id)
            serializer = SocialSer(social)
            return Response(serializer.data)
        except:
            return Response({'message':"bu id xato"})
    
    def patch(self, request, id):
        social = Social.objects.get(id=id)
        serializer = SocialSer(social, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        social = Social.objects.get(id=id)
        social.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
