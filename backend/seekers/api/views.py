from rest_framework.response import Response
from rest_framework.decorators import api_view 
from seekers.models import Comment, User, Resume, Rate, RATE_CHOICES
from .serializers import RateSerializer, CommentSerializer, ResumeSerializer
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.views import APIView
from rest_framework.exceptions import AuthenticationFailed

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['username'] = user.username
        # ...

        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
           raise AuthenticationFailed('Incorrect password')

        return Response({
          "message": "success"
        })

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

# @api_view(['GET'])
# def get_pitch(request):
#     pitch = Pitch.objects.all()
#     serializer = PitchSerializer(pitch, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# def add_pitch(request):
#     serializer = PitchSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)

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

