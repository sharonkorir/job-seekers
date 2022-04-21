from rest_framework.response import Response
from rest_framework.decorators import api_view 
from seekers.models import Comment, Pitch, Profile, Resume, Rate, RATE_CHOICES
from .serializers import RateSerializer, PitchSerializer, ProfileSerializer, CommentSerializer, ResumeSerializer


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