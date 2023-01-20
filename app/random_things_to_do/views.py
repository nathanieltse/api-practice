from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

import requests
import json

class RandomThingsToDoView(mixins.ListModelMixin,viewsets.GenericViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        result = request.get('http://www.boredapi.com/api/activity/')
        status = result.status_code

        if status == 200:
            data = json.loads(result.json)
            response['status'] = 200
            response['message'] = 'suucess'
            response['things_to_do'] = data['activity']
        else:
            response['status'] = status
            response['message'] = 'error'
            response['things_to_do'] = {}
        
        return Response(response)
