from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions, status
from .models import (
    JobPostSkillSet,
    JobType,
    JobPost,
    Company
)
from django.db.models.query_utils import Q

from .serializers import JobPostSerializer


class SkillView(APIView):

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        skills = self.request.query_params.getlist('skills', '')
        print("skills = ", end=""), print(skills)

        return Response(status=status.HTTP_200_OK)


class JobView(APIView):

    def post(self, request):

        JobPost_serializer = JobPostSerializer(data=request.data)

        if JobPost_serializer.is_valid(): # True or False
            JobPost_serializer.save()
            return Response(JobPost_serializer.data, status=status.HTTP_200_OK)
        
        return Response(JobPost_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

