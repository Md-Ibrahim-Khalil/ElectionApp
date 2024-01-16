from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Voter, PollingCenter
from .serializers import VoterSerializer, PollingCenterSerializer

class CreateVoterView(APIView):
    def post(self, request):
        serializer = VoterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddPollingCenterView(APIView):
    def post(self, request):
        serializer = PollingCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateDataView(APIView):
    def put(self, request, nid):
        try:
            voter = Voter.objects.get(nid=nid)
        except Voter.DoesNotExist:
            return Response({'error': 'Voter not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = VoterSerializer(voter, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ListVotersView(APIView):
    def get(self, request, polling_center_id):
        voters = Voter.objects.filter(pollingcenter_id=polling_center_id)
        serializer = VoterSerializer(voters, many=True)
        return Response(serializer.data)

class GetPollingCenterView(APIView):
    def get(self, request, nid):
        try:
            voter = Voter.objects.get(nid=nid)
        except Voter.DoesNotExist:
            return Response({'error': 'Voter not found'}, status=status.HTTP_404_NOT_FOUND)

        polling_center = PollingCenter.objects.get(voter=voter)
        serializer = PollingCenterSerializer(polling_center)
        return Response(serializer.data)