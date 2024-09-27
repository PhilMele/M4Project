from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StayForm
from .models import Stay, Fee

# Create your views here.
def enter(request):
    return render(request, 'stays/enter.html', {})
# def enter(request):
#     #returns latest entry for user account:
#     user_latest_entry = Stay.objects.filter(user=request.user.userprofile).order_by('-timestamp_enter').first()
#     arrival = True
#     if user_latest_entry is not None:
#         # set marker to define if user_latest_entry is an arrival or an exit
#         if user_latest_entry.is_enter:
            
#             print("No previous stay entry found. This will be the first entry.")
#         else:
#             arrival = False
#             print(f"Previous stay entry found: {user_latest_entry}")

#     #create form that populates Stay model:user, timestamp_enter, timestamp_leave, parking_name
#     if request.method == "POST":
#         stayform = StayForm(request.POST)
#         if stayform.is_valid():
#             print("for is valid")
#             staydata = stayform.save(commit=False)
#             staydata.user = request.user.userprofile
           
#             # if the last object was an arrival
#             # then mark this object as an exit
#             if arrival:
#                 staydata.is_enter = False
#                 staydata.is_leave = True
#                 staydata.timestamp_leave = None
#             else:
#                  staydata.timestamp_enter = None

#             staydata.save()

#             messages.success(request, "Stay data saved successfully.")
#             return redirect('home')  # Replace with the appropriate URL

#         else:
#             for error in list(stayform.errors.values()):
#                 messages.error(request, error)
#     else:
#         stayform = StayForm()

#     return render(request, 'stays/enter.html', {'stayform': stayform})

def history(request):
    user_history = Stay.objects.filter(user=request.user.userprofile)
    print(user_history)
    return render(request, 'history/history.html', {'user_history':user_history})