from django.shortcuts import render
from rest_framework.views import APIView
from project.models import Project
from project.serializers import ProjectSerializer
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
import requests
from datetime import datetime

# Create your views here.


class ProjectView(APIView):
    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProjectDetail(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GitubProjects(APIView):
    def get(self, request):
        repos_url = "https://api.github.com/users/RonG305/repos"

        try:
            response = requests.get(repos_url)
            if response.status_code == 200:
                repos_data = response.json()
                # Format date and time strings for each repository
                for repo in repos_data:
                    repo['created_at'] = self.format_datetime(
                        repo['created_at'])
                    repo['updated_at'] = self.format_datetime(
                        repo['updated_at'])
                    repo['pushed_at'] = self.format_datetime(repo['pushed_at'])
                return Response(repos_data)
            else:
                return Response({"message": "Failed to fetch repositories"}, status=response.status_code)
        except requests.RequestException as e:
            return Response({"message": f"Error fetching repositories: {e}"}, status=500)

    def format_datetime(self, datetime_str):
        # Parse the string to datetime object
        parsed_datetime = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%SZ")
        # Format the datetime as per your requirement
        formatted_datetime = parsed_datetime.strftime("%B %d, %Y")
        return formatted_datetime


class GitubView(APIView):
    def get(self, request, pk):  # Handle 'pk' parameter for project ID
        # Example GitHub API URL
        repos_url = f"https://api.github.com/repositories/{pk}"

        try:
            response = requests.get(repos_url)
            if response.status_code == 200:
                repo_data = response.json()
                return Response(repo_data)
            else:
                return Response({"message": "Failed to fetch repository"}, status=response.status_code)
        except requests.RequestException as e:
            return Response({"message": f"Error fetching repository: {e}"}, status=500)
