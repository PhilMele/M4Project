from django.shortcuts import render, redirect, get_object_or_404
from user_management.models import UserProfile
from parking_activity.models import Stay
from .models import Parking, Rate, IllegalParking
from .forms import ParkingForm, RateForm, IllegalParkingForm
from django.views.decorators.http import require_POST

from django.contrib.auth.decorators import login_required
from django.contrib import messages


def is_parking_manager(request):
    if request.user.userprofile.user_type != 2:
        return False
    return True


@login_required
def parking_manager_dashboard(request):
    if not is_parking_manager(request):
        return redirect('home')

    user_parking_list = Parking.objects.filter(
        user=request.user.userprofile
        ).order_by('name')

    # calculates parking capacity
    parking_space_data = []

    for parking in user_parking_list:
        # activate/deactivate parking
        activate = activate_parking(
            request,
            parking_id=parking.id
            )

        # return cpunt of all car registration parked in parking id
        parking_spaces_used = parking_space_available(
            request,
            parking_id=parking.id
            )

        parking_space_data.append({
            'parking': parking,
            'spaces_used': parking_spaces_used,
            'is_activate': parking.active,
        })

    return render(request, 'dashboard/parking_manager_dashboard.html', {
        'user_parking_list': user_parking_list,
        'parking_space_data': parking_space_data,
    })


@require_POST
@login_required
def activate_parking(request, parking_id):
    if not is_parking_manager(request):
        return redirect('home')

    parking = get_object_or_404(Parking, id=parking_id)

    # checks the parking has rates applied
    rate_exist = Rate.objects.filter(parking_name=parking)

    if not rate_exist:
        messages.error(request, f"Add a rate before activating parking.")
        return redirect('parking-info', parking_id=parking.id)

    has_user = parking_space_available(request, parking_id=parking_id)

    # prevents parking manager from deleting parking obj
    # when parking users are checked-in
    if has_user != 0:
        messages.error(
            request,
            "You cannot deactive parking when users are still checked-in."
            "Contact admin."
            )
        return redirect('parking-info', parking_id=parking_id)

    # if actiate is true turn it off
    if parking.active:
        parking.active = False
        parking.save()

    # if activate is off turn it on
    else:
        parking.active = True
        parking.save()

    messages.success(
        request,
        (
            f"{parking.name} has been "
            f"{'activated' if parking.active else 'deactivated'}."
        ))
    return redirect('parking-info', parking_id=parking_id)


@login_required
def parking_inspector(request, parking_id):
    if not is_parking_manager(request):
        return redirect('home')

    parking_users = Stay.objects.filter(
        parking_name=parking_id,
        paid=False,
        )

    illegal_users = IllegalParking.objects.filter(
        parking_name=parking_id,
    )

    parking = get_object_or_404(Parking, id=parking_id)

    # record list of cars illegally parked
    if request.method == "POST":
        illegalparkingform = IllegalParkingForm(request.POST)
        if illegalparkingform.is_valid():
            illegalparkingformdata = illegalparkingform.save(commit=False)
            illegalparkingformdata.inspector = request.user.userprofile
            illegalparkingformdata.parking_name = parking
            illegalparkingformdata.save()
            messages.success(request, "Illegal Registration saved.")
            return redirect('parking-inspector', parking_id=parking_id)
        else:
            messages.error(request, "Oops. Something did not work")
    else:
        illegalparkingform = IllegalParkingForm()

    return render(request, 'parking_inspector/parking_inspector.html', {
        'parking_users': parking_users,
        'illegal_users': illegal_users,
        'illegalparkingform': illegalparkingform,
        'parking': parking,
    })


@login_required
def delete_car_reg(request, illegalparking_id, parking_id):
    if not is_parking_manager(request):
        return redirect('home')

    car_reg_obj = get_object_or_404(IllegalParking, id=illegalparking_id)
    car_reg_obj.delete()
    messages.success(request, "Car reg. deleted.")
    return redirect('parking-inspector', parking_id=parking_id)


# Parking objects
@login_required
def create_parking(request):
    if not is_parking_manager(request):
        return redirect('home')

    if request.method == "POST":
        parkingform = ParkingForm(request.POST)
        if parkingform.is_valid():
            parkingdata = parkingform.save(commit=False)
            parkingdata.user = request.user.userprofile
            parkingdata.save()
            new_parking = parkingform.save()
            new_parking_id = new_parking.id
            messages.success(request, "Parking data saved successfully.")
            return redirect('parking-info', parking_id=new_parking_id)
        else:
            messages.error(request, "Oops. Something did not work")
    else:
        parkingform = ParkingForm()
    return render(request, 'parking/create_parking/create_parking.html', {
        'parkingform': parkingform
    })


@login_required
def parking_info(request, parking_id):
    if not is_parking_manager(request):
        return redirect('home')

    print({parking_id})

    stay_objects_count = parking_space_available(request, parking_id)
    parking = get_object_or_404(Parking, id=parking_id)
    rates = Rate.objects.filter(parking_name=parking)

    # prevent user from seeing activate button on frontend
    is_rate = True
    if not rates:
        is_rate = False

    return render(request, 'parking_info/parking_info.html', {
        'parking': parking,
        'rates': rates,
        'stay_objects_count': stay_objects_count,
        'is_rate': is_rate
    })


def parking_space_available(request, parking_id):
    if not is_parking_manager(request):
        return redirect('home')

    # identify parking
    parking = get_object_or_404(Parking, id=parking_id)

    # count of stay objects with paid = false
    stay_objects_count = Stay.objects.filter(
        parking_name=parking,
        paid=False).count()

    return stay_objects_count


@login_required
def edit_parking(request, parking_id):
    if not is_parking_manager(request):
        return redirect('home')

    parking = get_object_or_404(Parking, id=parking_id)
    parking_id = parking_id

    if request.method == "POST":
        editparkingform = ParkingForm(request.POST, instance=parking)
        if editparkingform.is_valid():
            editparkingform.save()
            messages.success(request, "Parking details updated successfully.")
            return redirect('parking-info', parking_id=parking.id)
        else:
            messages.error(
                request,
                "There was an issue updating the parking details."
                "Contact admin"
                )
    else:
        editparkingform = ParkingForm(instance=parking)

    return render(request, 'parking/edit_parking/edit_parking.html', {
        'editparkingform': editparkingform,
        'parking_id': parking_id
    })


@login_required
def delete_parking(request, parking_id):
    if not is_parking_manager(request):
        return redirect('home')

    parking = get_object_or_404(
        Parking,
        id=parking_id,
        user=request.user.userprofile
    )

    has_user = parking_space_available(request, parking_id=parking.id)

    # prevents parking manager from deleting parking obj
    # when parking users are checked-in
    if has_user != 0:
        messages.error(
            request,
            "You cannot delete a parking when users are still checked-in.")
        return redirect('parking-info', parking_id=parking.id)

    parking.delete()
    messages.success(request, "Parking deleted.")
    return redirect('parking-manager-dashboard')


# Rate objects
@login_required
def add_rate(request, parking_id):
    if not is_parking_manager(request):
        return redirect('home')

    parking = get_object_or_404(Parking, id=parking_id)
    parking_id = parking_id
    if request.method == "POST":
        rateform = RateForm(request.POST)
        if rateform.is_valid():
            ratedata = rateform.save(commit=False)
            ratedata.user = request.user.userprofile
            ratedata.parking_name = parking
            try:
                # check with model validator object can be saved
                ratedata.full_clean()
                ratedata.save()
                messages.success(
                    request,
                    "New rate created successfully."
                    )
                return redirect('parking-info', parking_id=parking_id)
            except ValidationError as e:
                rateform.add_error(None, e.message)
        else:
            messages.error(
                request,
                "Oops. Something did not work."
                "Read messages in the form, for more information."
                "Alternatively, it might be the hour range you have entered"
                "already exist")
    else:
        rateform = RateForm()

    return render(request, 'rate/add_rate/add_rate.html', {
        'rateform': rateform,
        'parking_id': parking_id
    })


@login_required
def edit_rate(request, parking_id, rate_id):
    if not is_parking_manager(request):
        return redirect('home')

    rate = get_object_or_404(Rate, id=rate_id)
    parking = get_object_or_404(Parking, id=parking_id)
    parking_id = parking.id

    has_user = parking_space_available(request, parking_id=parking.id)

    # prevents parking manager from deleting parking obj
    # when parking users are checked-in
    if has_user != 0:
        messages.error(
            request,
            "You cannot edit rate when users are still checked-in."
            "Contact admin."
            )
        return redirect('parking-info', parking_id=parking_id)

    if request.method == "POST":
        editrateform = RateForm(
            request.POST,
            instance=rate)
        if editrateform.is_valid():
            try:
                editrateform.full_clean()
                editrateform.save()
                messages.success(
                    request,
                    "Parking details updated successfully."
                    )
                return redirect('parking-info', parking_id=parking_id)
            except ValidationError as e:
                rateform.add_error(None, e.message)
        else:
            messages.error(
                request,
                "Oops. Something did not work."
                "Read messages in the form, for more information."
                "It might be the hour range you have entered already exist")
    else:
        editrateform = RateForm(instance=rate)

    return render(request, 'rate/edit_rate/edit_rate.html', {
        'editrateform': editrateform,
        'parking_id': parking_id
    })


@login_required
def delete_rate(request, parking_id, rate_id):
    if not is_parking_manager(request):
        return redirect('home')

    has_user = parking_space_available(request, parking_id=parking_id)

    # prevents parking manager from deleting parking obj
    # when parking users are checked-in
    if has_user != 0:
        messages.error(
            request,
            "You cannot edit rate when users are still checked-in."
            "Contact admin.")
        return redirect('parking-info', parking_id=parking_id)

    rate = get_object_or_404(Rate, id=rate_id)
    rate.delete()
    messages.success(request, "Rate deleted.")
    return redirect('parking-info', parking_id=parking_id)
