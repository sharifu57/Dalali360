import decimal
from django.db import models
import pendulum
from django.contrib.auth.models import Group, User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.conf import settings
from django.core.validators import MinLengthValidator, MaxLengthValidator
from django.core.validators import RegexValidator
from django.dispatch import receiver
from django.contrib.auth.models import Permission


# Create your models here.
class MainModel(models.Model):
    is_active = models.BooleanField(null=True, blank=True, default=True)
    is_deleted = models.BooleanField(null=True, blank=True, default=False)
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated = models.DateTimeField(auto_now=True, null=True, blank=True)
    
    def softdelete(self):
        self.is_deleted = True
        self.is_active = False
        self.updated = pendulum.now()
        self.save()

    class Meta:
        abstract = True

USER_CHOICES = (
    ("admin", "admin"),
    ("dalali", "dalali")
)

class SystemRole(MainModel):
    role = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True, related_name="system_roles")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="roles")

    def __str__(self):
        return f'{self.user.first_name}' + " - " + f'{self.role}'



class DalaliPermission(models.Model):
    class meta:
        managed = False
        permissions = [
            ("can_add_property", "Can Add Property"),
            ("can_delete_property", "Can Delete Property")
        ]
    
    def __str__(self):
        
        return f"{self.role} - {self.group}"

property_status = (
    (1, "available"),
    (2, "canceled"),
    (3, "blank"),
    (4, "New"),
    (5, "Approved"),
    (6, "Rejected")
)

LUKU = (
    (1, "single"),
    (2, "shared"),
    (3, "3 rooms share"),
    (4, "4 rooms share"),
    (5, "more than 4")
)

GENDER = (
        (1, 'Male'),
        (1, 'Female')
    )
    
TITLE = (
    (1, 'Mr'),
    (1, 'Ms')
)

ROLES = (
    (1, "New"),
    (2, "Admin"),
    (3, "Dalali")
)

MARITAL_STATUS = (
    (1, "Single"),
    (2, "married")
) 

CONTRACT_STATUS_CHOICES = (
    (1, 'Active'),
    (2, 'Inactive'),
    (3, 'Cancelled'),
    (4, 'Completed'),
    (5, 'Extended')
)

class Contract(MainModel):
    start_date = models.DateField()
    end_date = models.DateField()
    amount = models.DecimalField(null=True, max_digits=30, decimal_places=2, blank=True)
    status = models.IntegerField(choices=CONTRACT_STATUS_CHOICES, default=1, null=True, blank=True)
    paid_date = models.DateField()
    document = models.FileField(upload_to='documents/%Y/%m/%d', null=True, blank=True)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, null=True, blank=True)
    content_object = GenericForeignKey()
    

    class Meta:
        verbose_name = u'Contract'
        verbose_name_plural = u'Contracts'

    def __str__(self):
        return f"{self.start_date}"


    
class Property(MainModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    status = models.IntegerField(default=1, null=True, blank=True)
    ward = models.ForeignKey("dalali.ward", on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey("dalali.category", on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/%Y/%m/%d',null=True, blank=True)
    contract = GenericRelation(Contract, related_query_name="properties", null=True, blank=True)
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name="properties")
    
    
    class Meta:
        verbose_name = u'Property'
        verbose_name_plural = u'Properties'
        
    def __str__(self):
        
        return f"{self.name} - {self.price} - {self.status}"
    

class DalaliCommission(MainModel):
    amount = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    receipt_number = models.CharField(max_length=200, null=True, blank=True)
    is_paid = models.BooleanField(default=False, null=True, blank=True)
    property = models.OneToOneField("dalali.property", related_name="hela_ya_udalali", on_delete=models.DO_NOTHING, blank=True, null=True)
    VAT = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    
    
    def __str__(self):
        return f"{self.amount} - {self.property}"
    

class Image(MainModel):
    property= models.ForeignKey("dalali.property", on_delete=models.CASCADE, null=True, blank=True, related_name="images")
    image_path = models.ImageField(upload_to='images/%Y/%m/%d', null=True, blank=True)
    
    def __str__(self):
        
        return f"{self.property.name}"
    
class District(MainModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    code = models.CharField(max_length=100, blank=True, null=True)
    
    class Meta:
        verbose_name = u'District'
        verbose_name_plural = u'Districts'
        
    def __str__(self):
        
        return self.name
    
class Ward(MainModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    code = models.CharField(max_length=100, blank=True, null=True)
    district = models.ForeignKey("dalali.district", blank=True, null=True, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name = u'Ward'
        verbose_name_plural = u'Wards'

    def __str__(self):
        return self.name
    
class Location(MainModel):
    longitude = models.CharField(max_length=100, null=True, blank=True)
    latitude = models.CharField(max_length=100, null=True, blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
    
    class Meta:
        verbose_name = u'Location'
        verbose_name_plural = u'Locations'
        
    def __str__(self):
        return f"{self.longitude}" + f"{self.latitude}"
    

class Category(MainModel):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    icon = models.ImageField(upload_to='icons/%Y/%m/%d', null=True, blank=True)
    
    class Meta:
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'
    
    def __str__(self):
        return f"{self.name}"
   

def get_unique_id_number():
    import pendulum
    current_time = pendulum.now()
    increase = 1
    dalali_number = str(current_time.year) + "-" + str(
        current_time.month) + "-" + str(
            current_time.day) + "-" + str(User.objects.all().count() + increase)
    
    while Profile.objects.filter(dalali_number__iexact = dalali_number).exists():
        dalali_number = str(current_time.year) + "-" + str(
        current_time.month) + "-" + str(
            current_time.day) + "-" + str(User.objects.all().count() + increase)
        
        increase = increase + 1
    return dalali_number

def unique_phone_number(self, request):
    phone = request.data.get("phone_number")
    phone_number = Profile.objects.filter(phone_number__iexact = phone)

    if phone_number.exists():
        return str("phone number already exists")
    else:
        pass



class Profile(MainModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True, related_name='profile')
    about = models.TextField(null=True, blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 12 digits allowed.")
    ward = models.ForeignKey('dalali.ward', on_delete=models.DO_NOTHING, related_name="profiles", null=True, blank=True)
    dob = models.DateTimeField(null=True, blank=True)
    phone_number = models.CharField(max_length=10, null=False, blank=False, unique=False, validators=[MinLengthValidator(10), MaxLengthValidator(12), phone_regex])
    ward = models.ForeignKey(Ward, related_name="wards", null=True, blank=True, on_delete=models.SET_NULL)
    dalali_number = models.CharField(max_length=200, default=get_unique_id_number, null=True, blank=True)
    picture = models.ImageField(upload_to='picture/%Y/%m/%d', null=True, blank=True)

    
    def __str__(self):
        if self.user.username:
            return self.user.username
        return self.user.first_name + ' ' + self.user.last_name 
    
    @receiver(models.signals.post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        users_without_profile = User.objects.filter(profile__isnull=True)
        for user in users_without_profile:
            Profile.objects.create(user=user)
            
    @receiver(models.signals.post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()



class UserRequest(MainModel):
    full_name = models.CharField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=12, null=False, blank=False, unique=False)
    price_from = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    price_to = models.DecimalField(decimal_places=2, max_digits=10, null=True, blank=True)
    message = models.TextField(max_length=5000, null=False, blank=False)
    location = models.ForeignKey('dalali.Ward', null=True, blank=True, on_delete=models.SET_NULL, related_query_name="request")

    class Meta:
        verbose_name = u'UserRequest'
        verbose_name_plural = u'UserRequests'

    def __str__(self):
        return self.full_name

class Customer(MainModel):
    name = models.CharField(max_length=300, null=True, blank=False)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=10, null=False, blank=False, unique=True)
    dalali = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL, related_name="customer")
    customer = GenericRelation("dalali.Contract" , related_query_name="customer")

    class Meta:
        verbose_name = u'Customer'
        verbose_name_plural = u'Customers'

    def __str__(self):
        return f'{self.phone}'


class Activity(MainModel):
    FAVORITE = 'F'
    LIKE = 'L'
    UP_VOTE = 'U'
    DOWN_VOTE = 'D'
    ACTIVITY_TYPES = (
        (FAVORITE, 'Favorite'),
        (LIKE, 'Like'),
        (UP_VOTE, 'Up Vote'),
        (DOWN_VOTE, 'Down Vote'),
    )
    activity_type = models.CharField(max_length=1, choices=ACTIVITY_TYPES)
    date = models.DateTimeField(auto_now_add=True)
    object_id = models.PositiveIntegerField()
    content_type = models.ForeignKey(ContentType, on_delete=models.DO_NOTHING, null=True, blank=True)
    content_object = GenericForeignKey()

    def __str__(self):

        return self.date


class Post(MainModel):
    activity_post = GenericRelation(Activity, related_query_name="posts")
    name = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):

        return self.name



class Message(MainModel):
    sender = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='sent_messages', null=True, blank=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')
    subject = models.CharField(max_length=255)
    message = models.TextField()
    duration = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-duration']

    def __str__(self):
        return f'{self.sender} to {self.receiver}: {self.subject}'


class AppUser(MainModel):
    first_name = models.CharField(max_length=300, null=True, blank=True)
    last_name = models.CharField(max_length=300, null=True, blank=True)
    username = models.CharField(max_length=200, null=True, blank=True)
    customer_name = models.CharField(max_length=300, null=True, blank=False)
    customer_email = models.EmailField(max_length=100, null=True, blank=True)
    customer_phone = models.CharField(max_length=10, null=False, blank=False, unique=True)

    def __str__(self):
        
        return f'{self.customer_email} - {self.customer_name}'


class WorkFlow(MainModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    app = models.CharField(max_length=200, null=True, blank=True)
    model = models.CharField(max_length=200, null=True, blank=True)
    main_object_app = models.CharField(max_length=200, null=True, blank=True)
    main_object_model = models.CharField(max_length=200, null=True, blank=True)
    finish_path = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.code}'


class Node(MainModel):
    name = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=10, null=True, blank=True)
    view = models.CharField(max_length=500, null=True, blank=True)
    start = models.BooleanField(default=False)
    end = models.BooleanField(default=False)
    field_type = models.CharField(max_length=500, null=True, blank=True)
    flow = models.ForeignKey(WorkFlow, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.name} - {self.code}'


    
