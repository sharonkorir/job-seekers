from rest_framework.response import Response
from rest_framework.decorators import api_view 
from seekers.models import Comment, Pitch, Profile, Resume, Rate, RATE_CHOICES
from .serializers import RateSerializer, PitchSerializer, ProfileSerializer, CommentSerializer, ResumeSerializer
from django.http import JsonResponse

#show all endpoints
@api_view(['GET'])
def get_routes(request):
    routes = [
        '/api/token',
        '/api/token/refresh',
    ]
    return Response(routes)


@api_view(['GET'])
def get_resume(request):
    resume = Resume.objects.all()
    serializer = ResumeSerializer(resume, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_resume(request):
    serializer = ResumeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_pitch(request):
    pitch = Pitch.objects.all()
    serializer = PitchSerializer(pitch, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_pitch(request):
    serializer = PitchSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_comment(request, pk):
    comment = Comment.objects.filter(pitch=pk)
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_comment(request):
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['GET'])
def get_rating(request, pk):
    rating = Rate.objects.filter(resume=pk)
    serializer = RateSerializer(rating, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_rating(request):
    serializer = RateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

