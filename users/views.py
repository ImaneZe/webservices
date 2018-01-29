# -*- coding: utf-8 -*-
from rest_framework import views, mixins, permissions, exceptions
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets
from rest_framework import parsers, renderers

from users.serializers import *
from users.models import *
from users.authentication import TokenAuthentication

class ObtainAuthToken(views.APIView):
    throttle_classes = ()
    permission_classes = ()
    authentication_classes = (TokenAuthentication, )
    # parser_classes = (parsers.FormParser, parsers.MultiPartParser, parsers.JSONParser,)
    # renderer_classes = (renderers.JSONRenderer,)
    serializer_class = AuthTokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})


obtain_auth_token = ObtainAuthToken.as_view()