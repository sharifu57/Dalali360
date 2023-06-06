from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('properties', views.PropertyView.as_view()),
    path('upload_property', views.UploadPropertyView.as_view()),
    path('properties/<int:pk>', views.PropertyDetailsView.as_view()),
    path('wards', views.WardView.as_view()),
    path('wards/<int:pk>', views.WardDetailsView.as_view()),
    path('users', views.UserView.as_view()), 
    path('users/<int:pk>', views.UserDetails.as_view()),
    path('register', views.RegisterView.as_view()),
    path('login', csrf_exempt(views.UserLoginView.as_view())),
    path('categories', views.CategoryView.as_view()),
    path('categories/<int:pk>', views.CategoryDetailsView.as_view()), 
    path('properties_by_userId/<int:pk>', views.ProprtiesByUserId.as_view()), 
    path('featureds', views.FeaturedView.as_view()),
    path('images', views.ImageView.as_view()),
    path('images_by_property_id/<int:pk>', views.ImageDetailsView.as_view()),
    path('profile/<user_id>', views.ProfileAPIView.as_view()),
    path('profiles_by_ward_id/<int:pk>', views.ProfilesByWardIdView.as_view()),
    path('general_search', views.GeneralSearchView.as_view()),
    path('update_profile/<int:pk>', csrf_exempt(views.UpdateUserProfile.as_view())),
    path('user_requests', views.UserRequestsView.as_view()),
    path('create_request', views.CreateUserRequest.as_view()),
    path('customers_by_user_id/<int:pk>', views.CustomerAPIView.as_view()),

]
