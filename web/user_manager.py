from django.contrib.auth.models import User
from dalali.models import *
from django.db.models.query_utils import Q


def migrate_data():
    for user in User.objects.all():
        for customer in Customer.objects.all():
            if not AppUser.objects.filter(
                Q(first_name=user.first_name)|
                Q(last_name=user.last_name)|
                Q(username=user.username)|
                Q(customer_name=customer.name)|
                Q(customer_email=customer.email)|
                Q(customer_phone=customer.phone)
                ).exists():
                appuser = AppUser()
                appuser.first_name = user.first_name
                appuser.last_name = user.last_name
                appuser.username = user.username
                appuser.customer_name = customer.name
                appuser.customer_email = customer.email
                appuser.customer_phone = customer.phone
                print(appuser)
                appuser.save()
            else:
                print("====passs")
                pass


class UserManager:
    def get_properties(self):
        properties = Property.objects.filter(is_active=True, is_deleted=False)
        if properties.exists():
            return properties
        else:
            pass

    @staticmethod
    def show_all_users():
        all_customers = Customer.objects.all()
        all_users = User.objects.all()

        for user_obj in all_users:
            for cust_obj in all_customers: 
                appUser = AppUser(
                    first_name=user_obj.first_name,
                    last_name=user_obj.last_name,
                    username=user_obj.username,
                    customer_name = cust_obj.name,
                    customer_phone= cust_obj.phone,
                    customer_email= cust_obj.email
                )

                appUser.save()

    @staticmethod
    def get_system_users():
        users = User.objects.all()
        if users is not None:
            return users
        else:
            return 'No users available'
