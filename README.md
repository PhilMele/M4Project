TODO:
add that if the transaction is not paid, button leave should still show.
Problem: Once a transaction was made and paid. Somehow the user got loggedout during payment and the model didnt get updated with `paid = true`

Django setup on local:
* Create `m4project`
* Open to `m4project` folder from terminal
* Create a virtual environment: in terminal enter the following command: `python -m venv env`.
* Activate the virtual environment: `venv/scripts/activate`
* Install Django : `pip install django`.
* Create a new Django project: `django-admin startproject m4project`
* Run the development server: `python manage.py runserver`

GIt ignore setup credits: https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

## Stripe (credit #payment logic: credits: https://www.youtube.com/watch?v=hZYWtK2k1P8&t=1s)

The tutorial provided by the course material wasnt adapted to what I was looking for. Instead I followed the tutorial from this video (https://www.youtube.com/watch?v=hZYWtK2k1P8&t=1s) and made a number of changes to suit my project.

Improvement: I would like payment to be made without the user having to enter their bank details everytime. I initially wanted to code these in the database, but stripe advises against this. As I wantedt o focus on the geofencing element, I accepted this and left the action for future improvements.

Steps:

* Install Stripe `pip install stripe`
* install Stripe CLI `winget install Stripe.StripeCLI` (for VS Code)
* Get Stripe secret key + public key : create profile on stripe and find them on dashboard + add to .env file
* Get `STRIPE_WEBHOOK_SECRET_TEST`: 
    * Login to stripe form command line: `stripe login`
    * Enter in command line: `stripe listen --forward-to localhost:8000/stripe_webhook`
    * Copy paste key in `STRIPE_WEBHOOK_SECRET_TEST: []` in .env file.

    @login_required 
    def payment(request,applicable_fee, stay_id):
        stripe.api_key = settings
        if request.method == 'POST':
            checkout_session = stripe.checkout.Session.create(
                payment_method_types = ['cards'],
                line_items =[
                    {
                        'price':applicable_fee,
                        'quantity':1,

                    },
                ],
                mode = 'payment',
                customer_creation = 'always',
                succesful_url = settings.REDIRECT_DOMAIN + '/payment_successful?session_id={CHECKOUT_SESSION_ID}',
                cancel_url = settings.REDIRECT_DOMAIN + '/payment_cancelled',
            )
            print(f'checkout_session = {checkout_session}')
            return redirect(checkout_session.url, code=303)

* Add secret keys to .env file

    STRIPE_PUBLIC_KEY_TEST = [the_key_here]
    STRIPE_SECRET_KEY_TEST= [the_key_here]
    STRIPE_WEBHOOK_SECRET = [the_key_here]

* Add to settings .py:
    from dotenv import load_dotenv
    load_dotenv()

    STRIPE_PUBLIC_KEY_TEST = os.getenv('STRIPE_SECRET_KEY')
    STRIPE_WEBHOOK_SECRET = os.getenv('STRIPE_WEBHOOK_SECRET')
    REDIRECT_DOMAIN = os.getenv('REDIRECT_DOMAIN', 'http://localhost:8000')


Errors encountered:
"Error in payment process:No API key provided."
This was fixed by adding initialising the API key at the begining of the logic:
    @login_required
    def payment(request,applicable_fee,stay_id):
        try:
            #set API key the begining to avoid 
            #"Error in payment process:No API key provided."
            stripe.api_key = settings.STRIPE_SECRET_KEY_TEST

Problem make transaction automatic without having to enter card details everytime: 

Error: `Customer instance has invalid ID: None`
Add Stripe cutsomer ID in profile model:

    customer = stripe.Customer.create(
            email=request.user.email
            # Additional customer fields can be added here if needed
        )
        request.user.userprofile.stripe_customer_id = customer.id
        request.user.userprofile.save()

Pass id in logic: 
    customer=request.user.userprofile.stripe_customer_id,

Keep track of payment:
* When user is about to pay, stripe transaction is recorded

    @login_required
    def payment(request,applicable_fee,stay_id):
        ...

            #update stay model field with strip checkout id
            stay = Stay.objects.get(id=stay_id)
            stay.stripe_checkout_id = checkout_session.id
            stay.save()

* When user paid: stripe transaction is marked as true:

    @login_required
    def payment_successful(request):
        stripe.api_key = stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
        checkout_session_id = request.GET.get('session_id', None)
        session = stripe.checkout.Session.retrieve(checkout_session_id)
        customer = stripe.Customer.retrieve(session.customer)
        
        #mark stay payment as successful (bool to Tue)
        stay = Stay.objects.get(stripe_checkout_id=checkout_session_id)
        stay.paid = True
        stay.save()
        print("Payment sucessful!")

## user authentication
Leverage existing template provided by Django All-auth:

In views.py:
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login

    def register(request):
        if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                return redirect('home')
        else:
            form = UserCreationForm()
        return render(request, 'account/signup.html', {'form': form})


## setup PostGres on local:
Setup - PostgreSQL

Instal postgres on local: https://www.postgresql.org/download/

Normal practice:

To set up of PostGres on Local run : pip install psycopg2 (Documentation: https://medium.com/@shahrukhshl0/building-a-flask-crud-application-with-psycopg2-58de201e3c14)
Issues encountered and solution:

This may have been specific to my local setup, but I had to use : pip install psycopg2-binary (Documentation: https://pypi.org/project/psycopg2-binary/). My requirements.txt file lists : psycopg2-binary==2.9.9

In settings.py, edit `DATABASES` variables to the following to point to the new local postgres database:

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'm4project',
            'USER': '[yourusername]',
            'PASSWORD': '[yourpassword]',
            'HOST': 'localhost',
            'PORT': '5432', 
        }
    }

**Note:** You will need to run your migration again (`python manage.py migrate`) and recreate a new superuser. All data will be lost.

Once this is done, you will want your data stored in a your .env file, to avoid secret keys being publicly available when pushing the project to github and adapting the variables to their environement (local, staging, production...). To do this, do the following:
* enter `pip install python-decouple`
* modify your settings.py to look like this:

    from decouple import config

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': config('DB_NAME'),
            'USER': config('DB_USER'),
            'PASSWORD': config('DB_PASSWORD'),
            'HOST': config('DB_HOST', default='localhost'),
            'PORT': config('DB_PORT', default='5432'),
        }
    }

* Add valuest to variables to .env file. Note these dont need to be in string format, as they are considered strings by default:

    DB_NAME=m4project # your project name
    DB_USER=username # your username
    DB_PASSWORD=password # your password
    DB_HOST=localhost
    DB_PORT=5432

## static files

* Install packages: `pip install django-storages boto3`
Add to settings.py:

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/5.1/howto/static-files/

        STATIC_URL = 'static/'
        STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static'),
        ]

        MEDIA_URL = '/media/'
        MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

        STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

* Add to urls.py (project level):
    from django.conf import settings
    from django.conf.urls.static import static

    urlpatterns = [
    ...
    ]

    # Serve media files during development
    if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

## Heroku Setup (Production)
* Log into heorku : `heroku login`
* Add heroku remote : `git remote add heroku [Heroku Git URL]` (can be found in Heroku Settings)
* Push code to Heroku: `git push heroku master`
* Run first migration: `heroku run python manage.py migrate`

Problem encountered: the Procfile generated with command line from documentation echo web: gunicorn app:app > Procfile created an issue relating to encoding. The encoding defaulted to UTF-16 instead of UTF-8.

To solve this problem: create a new Procfile through a Notepad, selected encoding UTF-8 and called it Procfile.txt in the same location as the actual Procfile. I then deleted the previous Procfile and renamed Procfile.txt to Procfile.

Useful Link:

Credits: https://stackoverflow.com/questions/19846342/unable-to-parse-procfile

## geolocation

Credits: https://www.w3schools.com/html/html5_geolocation.asp


In geolocation.js add:
    const x = document.getElementById("userLocation");

    function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else { 
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
    }

    function showPosition(position) {
    x.innerHTML = "Latitude: " + position.coords.latitude + 
    "<br>Longitude: " + position.coords.longitude;
    }

add to base.html:

    {% block postloadjs %}
        <script src="{% static 'js/geolocation.js' %}"></script>
    {% endblock %}

**Error encountered**: `Uncaught TypeError: Cannot set properties of null (setting 'innerHTML')`. This as a result of the script being uploaded at the begining of the template, before the element exists.

This problem was solved by moving this specific script to the bottom of the body of the template.

* add to index.html:

    <button onclick="getLocation()">Try It</button>
    <p id="userLocation"></p>

Once this has proven to work. We can proceed by incorporating the user location in the logic of `enter()`.

We add a few more variables to `getlocation()`, which will be used to feed some `hidden` input field in the Enter form in enter.html.

* add to geolocation.js:

    document.addEventListener('DOMContentLoaded', function(){
    
    const latitudeField = document.getElementById("userLatitude") # new
    const longitudeField = document.getElementById("userLongitude") # new

    function getLocation() {
        if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition); 
        } else { 
        alert("Geolocation is not supported by this browser.");
        }
    }

    function showPosition(position) {

        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;

        // adds value to hidden inputs in index.html
        latitudeField.value = latitude; # new
        longitudeField.value = longitude; # new

    }
    getLocation() # new
    })

* add to enter.html the hidden inputs:

    <form method="post">
        {% csrf_token %}
        <input type="hidden" id="userLatitude" name="latitude" value="">
        <input type="hidden" id="userLongitude" name="longitude" value="">
        {{stayform}}
        <input type="submit" onclick="getLocation()" value="OK">
    </form>

* in views.py  in `enter()`:

    @login_required
    def enter(request):
    
        if request.method == "POST":
            # capture user current location
            latitude = request.POST.get('latitude')
            longitude = request.POST.get('longitude')
            print(f'{request.user.username}: latitude = {latitude} + longitude = {longitude}')

Geolocation radius (
* credits: https://stackoverflow.com/questions/42686300/how-to-check-if-coordinate-inside-certain-area-python
* https://geopy.readthedocs.io/en/stable/#module-geopy.distance)

* Install Geopy: `pip install geopy`
* import geopy in views.py (parking_activity app):

    from parking_management.models import Parking

* add distance calculation logic between user and parkings `enter()`:

    @login_required
    def enter(request):
    
        if request.method == "POST":
            ...

            # set user location in tuple
            user_location = [{'lat': {user_latitude}, 'lng': {user_longitude}}]
            user_location_tuple = (float(user_latitude), float(user_longitude))
          
            # match current user location to parking radius (if any)
            parkings = Parking.objects.all()
            
            # create for loop of parkings
            for parking in parkings:

                parking_radius = float(parking.radius)
                
                # set parking location in tuple
                parking_location_tuple = (float(parking.latitude), float(parking.longitude))

                #measure distance between user location and parking location
                locations_distance = distance.distance(
                    user_location_tuple,
                    parking_location_tuple).meters
                
                print("Distance: {}".format(locations_distance))

                if locations_distance <= parking_radius:
                    print(f'You are in {parking.name}')
                else:
                    print(f'You are not in {parking.name}')


**Error encountered** `TypeError: float() argument must be a string or a real number, not 'set'`: following Igor-S answer on stackoverflow, I encountered this error.

This is because of the use of `({})`, which in Python define a set, rather than parentheses `()`.

To fix this error by converting the values into `float`:
    
    user_location = (float(user_latitude), float(user_longitude))

**Error encountered** `TypeError: '<=' not supported between instances of 'float' and 'str'`: following the above mentioned example provided on stackoverflow.

This error happened because `parking.radius` is a string and `locations_distance` is a float.

    if locations_distance <= parking_radius:
        print(f'You are in {parking.name}')
    else:
        print(f'You are not in {parking.name}')

Both values need to be in the same format:

    parking_radius = float(parking.radius)

Useful links:
* https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
* https://stackoverflow.com/questions/42686300/how-to-check-if-coordinate-inside-certain-area-python
* https://geopy.readthedocs.io/en/stable/#module-geopy.distance