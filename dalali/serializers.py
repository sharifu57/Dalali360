from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from dalali.models import Category, Image, Profile, Property, Ward, Customer, UserRequest

class PropertySerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        # fields = [
        #     # 'id',
        #     'name',
        #     'price',
        #     # 'month_per_contract',
        #     # 'description',
        #     # 'luku',
        #     # 'distance',
        #     # 'user',
        #     # 'ward',
        #     # 'category',
        #     # 'image'
        #     ]
        fields = '__all__'
        depth = 3


class UpLoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Property
        fields = [
            'name', 
            'price',
            'description',
            'ward',
            'category',
            'image',
            'user'
        ]
        

class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ward
        fields = '__all__'
        depth = 2
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth = 3
        

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
        depth = 2

        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        depth = 2
        
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True,  validators=[UniqueValidator(queryset=User.objects.all())]),
    password = serializers.CharField(write_only=True, required=True, validators=[validate_password]),
    # password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')
        
        extra_kwargs = {
            'first_name': {'required': True},
            'last_name': {'required': True}
        }


        def create(self, validated_data):
            user = User.objects.create(
                username = validated_data['username'],
                email = validated_data['email'],
                first_name = validated_data['first_name'],
                last_name = validated_data['last_name']
            )

            user.set_password(validated_data['password'])
            user.save()
            return user

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class UserRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserRequest
        fields = '__all__'

        
