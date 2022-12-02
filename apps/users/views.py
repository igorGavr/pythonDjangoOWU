from django.forms import model_to_dict
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import UserModel
from .serializers import UserSerializer


class UserListCreateView(APIView):

    def get(self, *args, **kwargs):
        users = UserModel.objects.all()
        # #конвертуємо екземпляри класу в dict
        serializer = UserSerializer(instance=users, many=True)
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, *args, **kwargs):
        # user = UserModel(name='max', age=14, status=True)
        # user.save()
        # UserModel.objects.create(name='kira', age=14, status=True)
        data = self.request.data
        # валідуємо
        serializer = UserSerializer(data=data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
        # #записуємо в базу даних вже з Айдішкою
        # user = UserModel.objects.create(**serializer.data)
        # #конвертуємо екземпляр класу в dict
        # serializer2 = UserSerializer(instance=user)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)

class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)

        user = UserModel.objects.get(pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        user = UserModel.objects.get(pk=pk)
        serializer = UserSerializer(user, data)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, *args, **kwargs):
        pk = kwargs.get('pk')
        data = self.request.data
        exists = UserModel.objects.filter(pk=pk).exists()
        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)
        user = UserModel.objects.get(pk=pk)
        serializer = UserSerializer(user, data, partial=True)

        if not serializer.is_valid():
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        exists = UserModel.objects.filter(pk=pk).exists()

        if not exists:
            return Response('Not found', status.HTTP_404_NOT_FOUND)

        user = UserModel.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)