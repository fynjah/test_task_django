from django.urls import re_path
from app.views import LCBookingView, LTableView, index

urlpatterns = [
    re_path("^$", index),
    re_path(r"^bookings/$", LCBookingView.as_view()),
    re_path(r"^tables/$", LTableView.as_view()),
]
