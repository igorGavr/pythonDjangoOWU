import json
from rest_framework.views import APIView
from rest_framework.response import Response

from users.services import FileReadWriteService


class MyAPIView(APIView, FileReadWriteService):
    _file_name = 'users.json'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.users = self.load_users()


class UsersListCreateView(MyAPIView):
    def get(self, *args, **kwargs):
        return Response(self.users)

    def post(self, *args, **kwargs):
        data = self.request.data
        data['id'] = self.users[-1]['id'] + 1 if self.users else 1;
        self.users.append(data)
        self.save_users(self.users)
        return Response(data)


class UsersRetrieveUpdateDestroyView(MyAPIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = self._get_user_by_pk(pk)
        if user is None:
            return Response('Not Found')
        return Response(user)

    def put(self, *args, **kwargs):
        pk = kwargs.get('pk')
        user = self._get_user_by_pk(pk)

        if user is None:
            return Response('Not Found')

        data = self.request.data

        if data.get('id'):
            del data['id']

        user |= data
        self.save_users(self.users)
        return Response(user)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')
        index = next((i for i,v in enumerate(self.users) if v['id'] == pk), None)
        if index is None:
            return Response('Not Found')
        del self.users[index]
        self.save_users(self.users)
        return Response('deleted)')

    def _get_user_by_pk(self, pk):
        return next((user for user in self.users if user['id'] == pk), None)

