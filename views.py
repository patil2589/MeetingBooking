from django.shortcuts import render,redirect
from django.views.generic import ListView, CreateView
from .models import Users,MeetingBookModel
from .forms import MeetingBookForm
from django.db.models import Q
class UserListView(ListView):
    def get_queryset(self):
        users = Users.objects.filter(meetingbookmodel__booked=True)
        if not users:
            allusers = Users.objects.all()
            return allusers
        else:
            print(users)
            filterusers = Users.objects.filter(~Q(user_name__in=users))
            return filterusers
        return users
class MeetingCreateView(CreateView):
    model = MeetingBookModel
    form_class = MeetingBookForm


def meetingSave(request):
    form = MeetingBookForm(request.POST)
    if form.is_valid:
        form.booked = True
        form.save()
    else:
        print("Not valid")

    return redirect('index')
