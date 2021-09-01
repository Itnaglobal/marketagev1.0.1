from django.urls import path, include
from ChatApp import views


urlpatterns = [
    path("test_home/", views.home_page, name="home_page"),
    path("user_details/<int:id>/", views.user_details, name="user_details"),
    path("chatroom/<int:id>/", views.chatRoomView, name="chatroom"),
    # path("view_profile/<int:id>/", views.user_details, name="user_details"),
    # # path("form_validation/", views.form_validation, name="form_validation"),
    # path("room/", views.room, name="room"),
    # path("chatting/<int:id>", views.continue_chat, name="continueChat")
]
