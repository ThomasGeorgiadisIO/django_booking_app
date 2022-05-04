from django.urls import path
from .views import *

urlpatterns = [
    path('', homepage, name='homepage'),
    path('experienceList/', ExperienceListView.as_view(), name='experienceList'),
    path("contactUs/", contactUs, name="contactUs"),
    path("aboutUs/", aboutUs, name="aboutUs"),

    path("login/", loginUser, name="loginUser"),
    path("logout/", logoutUser, name="logoutUser"),
    path("signupUser/", signupUser, name="signupUser"),
    path("signupGuide/", signupGuide, name="signupGuide"),

    path("dashboardUser/", dashboardUser, name="dashboardUser"),
    path("dashboardUser/wishList/", wishList, name="wishList"),
    path("dashboardUser/wishList/<int:id>", wishListAdd, name="wishListAdd"),
    path("<pk>/dashboardUser/wishList/delete", WishListDeleteView.as_view(), name="wishListDelete"),
    path('dashboardUser/editUser/', editUser, name='editUser'),
    path('dashboardUser/editPass/', editPass, name='editPass'),
    path('dashboardUser/orderHistory/', OrderHistoryListView.as_view(), name='orderHistory'),

    path("dashboardGuide/", dashboardGuide, name="dashboardGuide"),
    path('dashboardGuide/editGuide/', editGuide, name='editGuide'),
    path("dashboardGuide/experienceManage", experienceManage, name="experienceManage"),
    path('dashboardGuide/experienceCreate/', ExperienceCreateView.as_view(), name='experienceCreate'),
    path("<pk>/dashboardGuide/update", ExperienceUpdateView.as_view(), name="experienceUpdate"),
    path("<pk>/dashboardGuide/delete", ExperienceDeleteView.as_view(), name="experienceDelete"),

    path("experienceDetails/<int:id>", ExperienceDetails.as_view(), name="experienceDetails"),
    path('experienceDetails/success/', PaymentSuccessView.as_view(), name="success"),
    path('experienceDetails/failed/', PaymentFailedView.as_view(), name='failed'),

    #sorting paths for price
    path('experienceList/sortByPriceAscending/', sortByPriceAscending, name="sortByPriceAscending"),
    path('experienceList/sortByPriceDescending/', sortByPriceDescending, name="sortByPriceDescending"),

    #sorting paths for maximum number of people
    path('experienceList/sortByNumberOfPeopleAscending/', sortByNumberOfPeopleAscending, name="sortByNumberOfPeopleAscending"),
    path('experienceList/sortByNumberOfPeopleDescending/', sortByNumberOfPeopleDescending, name="sortByNumberOfPeopleDescending"),

    #sorting paths for maximum number of people
    path('experienceList/sortByDurationAscending/', sortByDurationAscending, name="sortByDurationAscending"),
    path('experienceList/sortByDurationDescending/', sortByDurationDescending, name="sortByDurationDescending"),

    #sorting paths for maximum number of people
    path('experienceList/sortByDateAscending/', sortByDateAscending, name="sortByDateAscending"),
    path('experienceList/sortByDateDescending/', sortByDateDescending, name="sortByDateDescending"),

    # API
    path('api/tours/', getTours, name="getTours"),
    path('api/tours/<id>/', getTour, name="getTour"),
    path('api/guides', getGuides, name="getGuides"),
    path('api/guide/<id>', getGuide, name="getGuide"),

    path('api/checkout-session/<id>/', create_checkout_session, name='api_checkout_session'),
]
