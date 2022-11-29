from rest_framework.views import APIView
from rest_framework.response import Response

# class UsersView(APIView):
#     def get(self, *args, **kwargs):
#         return Response('Hello from GET')
#
#     def post(self, *args, **kwargs):
#         print(self.request.data)
#         print(self.request.query_params)
#         return Response('Hello from POST')
#
#     def put(self, *args, **kwargs):
#         return Response('Hello from PUT')
#
#     def patch(self, *args, **kwargs):
#         return Response('Hello from PATCH')
#
#     def delete(self, *args, **kwargs):
#         return Response('Hello from DELETE')
#
#
# class UserTestView(APIView):
#     def get(self, *args, **kwargs):
#         print(kwargs)
#         return Response('ok')

users = [
    {"name": "Max", "age": 23},
    {"name": "LI", "age": 33},
    {"name": "Pole", "age": 32},
    {"name": "Nelio", "age": 233},
]


class UserListCreateView(APIView):
    def get(self, *args, **kwargs):
        return Response(users)

    def post(self, *args, **kwargs):
        user = self.request.data
        users.append(user)
        return Response(user)


class UserRetrieveUpdateDestroyView(APIView):
    def get(self, *args, **kwargs):
        pk = kwargs.get('pk')
        try:
            user = users[pk]
        except IndexError:
            return Response('Not Found')
        return Response(user)

    def put(self, *args, **kwargs):
        new_user = self.request.data
        pk = kwargs.get('pk')

        try:
            user = users[pk]
        except IndexError:
            return Response('Not Found')
        user['name'] = new_user['name']
        user['age'] = new_user['age']
        return Response(new_user)

    def delete(self, *args, **kwargs):
        pk = kwargs.get('pk')

        try:
            del users[pk]
        except IndexError:
            return Response('Not found')
        return Response('deleted')
