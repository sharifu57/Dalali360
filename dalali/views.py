from django.shortcuts import render
from dalali.filter_property import FilterData
from rest_framework import permissions
from rest_framework.decorators import  permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status
from dalali.models import Category, Image, Profile, Property, Ward
from dalali.serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.auth import login
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication 
from django.db.models.query_utils import Q

# NORMAL API'S=======================

# Create your views here.
@permission_classes((permissions.AllowAny,))
class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({'data': serializer.data})
    
    def post(self, request, format=None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    
@permission_classes((permissions.AllowAny,))
class UserLoginView(APIView):
    # authentication_classes = (CsrfExemptSessionAuthentication)
    def post(self, request, format=None):
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        password = request.data.get('password', None)
        
        print("****user details****")
        print(username)
        print(password)
        print("****password details****")

        if User.objects.filter(Q(username=username)|Q(email=username)).exists():
            user_obj = User.objects.filter(Q(username=username) | Q(email=username) | Q(email=email)).first()
            user = authenticate(username = user_obj.username, password = password)
            print("user is authenticated")
            print(user)
            if user is not None:
                if user.is_active:
                    serializer = UserSerializer(user, many=False)
                    token, created = Token.objects.get_or_create(user=user)
                    return Response(
                        {
                            'status': status.HTTP_200_OK,
                            "token": token.key,
                            "user": serializer.data
                        }
                    )
                else:
                    return Response(
                        {
                            'status': status.HTTP_404_NOT_FOUND,
                            'message': 'Failed to login (not activated)'
                        }
                    )
            else:
                print("user=====", user)
                return Response(
                    {
                        'status': status.HTTP_404_NOT_FOUND,
                        'message': 'Incorrect username or password'
                    }
                )
        else:
            return Response(
                {
                    'status': status.HTTP_404_NOT_FOUND,
                    'message': 'User does not exist'
                }
            )

            
    
class UserDetails(APIView):
    def get_object(self, pk):
        try:
            user = User.objects.get(pk=pk)
            return user
        except User.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)
            
            
@permission_classes((permissions.AllowAny,))
class PropertyView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get(self, request):
        properties = Property.objects.all()
        if len(properties) >= 0:
            serializer = PropertySerializer(properties, many=True)
            return Response({'data' : serializer.data})
        else:
            serializer = PropertySerializer(properties, many=True)
            return Response({'data' : serializer.data})
        
    


@permission_classes((permissions.AllowAny,))
class UploadPropertyView(APIView):
    def post(self, request, format=None):
        serializer = UpLoadSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            # category = Category.objects.filter(id=request.data['category']).first()
            # ward = Ward.objects.filter(id=request.data['ward']).first()
            # user = User.objects.get(id=request.data['user'])
            # serializer.save(ward = ward, category = category, user = user)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class ProprtiesByUserId(APIView):
    def get(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
            properties = Property.objects.filter(user=user)
            serializer = PropertySerializer(properties, many=True)
            return Response({'data' : serializer.data})
        except User.DoesNotExist:
            raise Http404

@permission_classes((permissions.AllowAny,))
class PropertyDetailsView(APIView):
    def get_property_id(self, pk):
        try:
            property = Property.objects.get(pk=pk)
            return property
        except Property.DoesNotExist:
            raise Http404
        
    def get(self, request, pk, format=None):
        property = self.get_property_id(pk)
        serializer = PropertySerializer(property)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        property = self.get_object(pk)
        serializer = PropertySerializer(property, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        snippet = self.get_object(pk)
        snippet.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@permission_classes((permissions.AllowAny,))
class WardView(APIView):
    def get(self, request):
        wards = Ward.objects.filter(is_active=True, is_deleted = False).order_by('name')
        serializer = WardSerializer(wards, many=True)
        return Response({'data': serializer.data})
    

@permission_classes((permissions.AllowAny,))
class WardDetailsView(APIView):
    def get(self, request, pk):
        try:
            ward = Ward.objects.get(pk=pk)
            properties = Property.objects.filter(ward = ward,is_active=True, is_deleted=False)
            serializer = PropertySerializer(properties, many=True)
            return Response({'data': serializer.data})
        except Ward.DoesNotExist:
            raise Http404
        
@permission_classes((permissions.AllowAny,))
class CategoryView(APIView):
    def get(self, request):
        categories = Category.objects.filter(is_active=True, is_deleted=False)
        serializer = CategorySerializer(categories, many=True)
        return Response({'data': serializer.data})
    

@permission_classes((permissions.AllowAny,))
class CategoryDetailsView(APIView):
    def get(self, request, pk):
        try:
            category = Category.objects.get(pk=pk)
            properties = Property.objects.filter(category = category, is_active=True, is_deleted=False)
            serializer = PropertySerializer(properties, many=True)
            return Response({'data': serializer.data})
        except Category.DoesNotExist:
            raise Http404
        
@permission_classes((permissions.AllowAny,))
class FeaturedView(APIView):
    def get(self, request):
        featureds = Property.objects.all().order_by('-created')[:4]
        serializer = PropertySerializer(featureds, many=True)
        return Response({'data': serializer.data})

@permission_classes((permissions.AllowAny,))
class ImageView(APIView):
    def get(self, request):
        images = Image.objects.filter(is_active=True, is_deleted = False)
        serializer = ImageSerializer(images, many=True)
        return Response({'data': serializer.data})
    

@permission_classes((permissions.AllowAny,))
class ImageDetailsView(APIView):        
     def get(self, request, pk):
        try:
            property_id = Property.objects.get(pk=pk)
            images = Image.objects.filter(property = property_id, is_active=True, is_deleted=False)
            serializer = ImageSerializer(images, many=True)
            return Response({'data': serializer.data})
        except Ward.DoesNotExist:
            raise Http404


@permission_classes((permissions.AllowAny,))
class ProfileAPIView(APIView):
    def get(self, request, *args, **kwargs):
        user = get_object_or_404(User, pk=kwargs['user_id'])
        profile_serializer = ProfileSerializer(user.profile)
        return Response({'data': profile_serializer.data})


@permission_classes((permissions.AllowAny,))
class ProfilesByWardIdView(APIView):
    def get(self, request, pk):
        try:
            ward_id = Ward.objects.get(pk=pk)
            profiles = Profile.objects.filter(ward = ward_id, is_active=True, is_deleted=False)
            serializer = ProfileSerializer(profiles, many=True)
            return Response({'data': serializer.data})
        except Profile.DoesNotExist:
            raise Http404


@permission_classes((permissions.AllowAny,))
class GeneralSearchView(APIView):
    def get(self, request,*args, **kwargs):
        property_price = None
        category_obj = Category.objects.filter(is_active=True, is_deleted=False).first()
        ward_obj = Ward.objects.filter(is_active=True, is_deleted=False).first()
        property_obj = Property.objects.filter(is_active=True, is_deleted=False).first()
        properties = FilterData().general_filter(
            price=property_obj.price, 
            category=category_obj.name,
            ward=ward_obj.name 
        )
        serializer = PropertySerializer(properties, many=True)
        return Response({'data': serializer.data})



@permission_classes((permissions.AllowAny,))
class UpdateUserProfile(APIView):
    def get_user_id(self, user_id):
        try:
            user = User.objects.get(id=user_id)
            return user
        except User.DoesNotExist:
            raise Http404 
    def put(self, request, pk, format=None):
        user = self.get_user_id(pk)
        return Response(user)
        # print("++++++user")
        # print(user)
        # serializer = ProfileSerializer(user, data=request.data)
        # print("_______-serializer")
        # if serializer.is_valid():
        #     print("_____is valid profile")
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_200_OK)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@permission_classes((permissions.AllowAny,))
class UserRequestsView(APIView):
    def get(self, request):
        requests = UserRequest.objects.all()
        serializer = UserRequestSerializer(requests, many=True)
        return Response({'data': serializer.data})

@permission_classes((permissions.AllowAny,))
class CreateUserRequest(APIView):
    def post(self, request):
        serializer = UserRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'status': 200,
                'message': "your request have Suceessfully sent",
                'data': serializer.data
            }
            return Response(data, status=status.HTTP_201_CREATED)
        data = {
            'status': 400,
            'message': "Failed to submit (something is not right)",
            'data': serializer.errors
        }
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


@permission_classes((permissions.AllowAny,))
class CustomerAPIView(APIView):
    def get(self, request, pk):
        try:
            user_id = User.objects.get(pk=pk)
            customers = Customer.objects.filter(dalali = user_id).all()
            serializers = CustomerSerializer(customers, many=True)
            return Response({'data': serializers.data})
        except Customer.DoesNotExist:
            print("Customers does not exist-======")
            raise Http404
        return Response()



       



