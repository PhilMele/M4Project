TODO:
add that if the transaction is not paid, button leave should still show.
Problem: Once a transaction was made and paid. Somehow the user got loggedout during payment and the model didnt get updated with `paid = true`. Only seem to happen on local after I havent connected in a while.
Error: when I click on Enter, the console shows a brief error message and then disapear
javascript error on index page due to geolocation
Correct 500 error when normal user clicks on parking manager dashboard : if user doesnt have permission, redirect to home
user cannot enter parking if car registration is not populated + userprofile as a whole
Add back button to all pages
create filtr that only shows activated parkings to user
create a button to tell the parking managert o activate parking
parking can only be activiated with rates have been populated and cannot be 0.
add footer
fix check-out siccess message at Noneafter selecting manually what parking userchecks in
fix logout problem when scanning qr code. Might be SSL certificate realted problem.
Check validators for sign up
check validators for login when email or password is wrong
check all code meets indentions standard and spaces
add validator to make sure parking is null 0 or negative
change navbar for manager to remove uneeded elements
imrpoevemt: parking insepctor can be imporved with OCR and connecting to a CRM to issue PCR
add labels to form fields
add check to prevent activating parking if no rate is available
add autamtaed email when order is paid
add placeholders on user dashboard if no parking is available
add placeholders on parking manager dashboard if no parking is available
add email verification
fix error that says you echekc in Parking None if selected manually
fix success message on payment
check if its ok to have the venv file avilable on github
add tutorial on how to add long and lat from google maps to parking latlng
remove commentedout text in dahsboard blocks if layout is good

# M4Project - GeoPay

View the live site: <a href="https://geopay-12a0f6ced11c.herokuapp.com/" target="_blank">Click Here</a>

# Table of Contents

1. [User Experience](#ux)
   - [Project Goals](#project-goals)
   - [User Stories](#ux-subsection)
2. [Design](#design)
   - [Colours](#colours)
   - [Typography](#typography)
   - [Icons & Images](#icons-images)
   - [Wireframes](#wireframes)
   - [Databases](#databases)
3. [Features](#features)
    - [Authentication](#auth)
    - [Password Reset Via Email](#password-reset)
    - [Media Files : AWS S3 Bucket](#media-files)
    - [User Profile](#user-profile)
    - [User Dashboard](#user-dashboard)
    - [Parking Manager Dashboard](#parking-manager-dashboard)
    - [Create Parking](#create-parking)
    - [Read, Edit & Delete Parking](#read-edit-delete-parking)
    - [Create Parking Rates](#create-parking-rates)
    - [Read, Edit & Delete Parking Rates](#read-edit-delete-parking-rates)
    - [Check-In Parking : Geolocation](#check-in)
    - [Check-Out Parking](#check-out)
    - [Stripe Payment Integration](#stripe)
    - [Crispy Forms](#cripsy)
    - [Decorators](#decorators)
    - [Custom Error Handlers](#error-handler)
    - [Parking Inspector](#parking-inspector)
4. [Technologies](#tech)
5. [Testing](#testing)
   - [Validator Testing](#val-testing)
     * [HTML](#html)
     * [CSS](#css)
     * [Javascript](#js)
     * [Python](#py)
   - [Lighthouse Testing](#lighthouse-testing)
   - [User Testing](#user-testing)
6. [Bugs](#bugs)
   - [Current bugs](#current-bugs)
   - [Design & User Experience improvements](#design-improvements)
   - [Logic improvements & Backend](#logic-improvements)    
7. [Deployment](#deployment)
   - [Local Deployment](#local-deployment)
   - [Heroku Deployment](#heroku-deployment)
8. [Credits](#credits)


## 1. User Experience <a name="ux"></a>

### 1.1 Project Goals <a name="project-goals"></a>

As a potential user, I built this project to address a recurring problem I face.

There is a parking where I park once a month, and it rains all the time. If it does rain, there is some strong wind, or it's very cold outside.

Sometimes, all three together.

For me to register my car for parking, I need to walk to the machine, wait for it to connect to some internet, enter my registration and wait even longer for a ticket to be printed, so I can take this ticket to my wind screen.

Some parkings have app. This one does not. But even if it had an app, I probably wouldn't download it.

I want to park and pay, with no inbetween.

This is what this project aims to achieve: a parking payment system based on geolocation, with a webapp.

As a user, I want to check-in by opening the app. Using my phone's GPS, the app will capture my geolocation and check me in automatically.

As I leave, I reopen the app to mark my departure and pay.

No time spent in the outside cold.

### 1.2 User Stories <a name="user-stories"></a>

**User Management**
* As a user, I want to create an account.
* As a parking user, I want to be able to register my car registration number against my account.
* As a parking user, I want to be able to edit my account details.
* As a parking user, I want to be able to mark myself as a user of the parking by clicking on a button to show what time I arrived.
* As a parking user, I want to automatically mark my entry and exit using geofencing to reduce manual effort.
* As a parking user, I want to select my parking should geolocation fails.
* As a parking user, I want to be able to pay for parking without walking to a machine.
* As a parking user, I want to be automatically charged based on my entry and exit times, with no additional steps.
* As a parking user, I want to be able to check my past transaction.

**Platform Functionality**
* As a platform, I want to record the time the user has registered their arrival and departure at a parking location.
* As a platform, I want to charge the customer based on the time difference between their arrival and departure, multiplied by the hourly fee.
* As a platform, I want to validate the user's location to ensure they are within the parking zone when they mark their arrival or departure.
* As a platform, I want to securely store and process users' sensitive information, like payment details.

**Parking Manager**
* As a parking manager, I want to have a dedicated space to manage my parking from the account I have created.
* As a parking manager, I want to set and adjust the hourly fee for my parking lots.
* As a parking manager, I want to see a live list of all car registrations that have registered their arrival in my parking.
* As a parking manager, I want to be able to physically walk through my parking and inspect if car with registrations that are not marked are parked.
* As a parking manager, I want to keep records of those illegally parked cars, for future penatly process.

## 2. Design <a name="design"></a>

### 2.1 Colours <a name="colours"></a>
### 2.1 Typography <a name="typography"></a>
### 2.1 Icons & Images <a name="icons-images"></a>

Icons and images are hosted on S3 Bucket:

* Logo was generated using MidJourney;
* Icons used are mostly coming from FontAwesome;
* Other icons, in particular those used in email find are sourced from Icons8;
* There is no actual images, as it did not add any value to the purpose of the product

### 2.1 Wireframes <a name="wireframes"></a>
### 2.1 Databases <a name="databases"></a>

<details>
    <summary>Click to see ER Diargram</summary>
    <p>
        <img src="static/images/readme_images/erd.png" alt="erd" />
    </p>
</details>

<details>
<summary>Click to ER Diargram dependency installation process</summary>
<p>
ERD was generated using django extension `Graphviz`.

To install `Graphviz` these steps were followed:
    * run: `pip install django-extensions`
    * run: `winget install Graphviz`
    * add:

        INSTALLED_APPS = [
        ...
        'django_extensions'
        ]

    * run: `pip install pydotplus`
    * run: `python manage.py graph_models -a -o erd.png`
</p>
</details>

The databases are split across 3 diffrent apps: 
* `user_management`
* `parking_activity`
* `parking_management`.

<details>
<summary>Click to see `user_management` app models</summary>
<p>

| **Model**         | **Field Name**           | **Field Type**       | **Description**                                                   |
|--------------------|--------------------------|-----------------------|-------------------------------------------------------------------|
| **UserProfile**    | `user`                  | OneToOneField         | Links to the Django `User` model.                                |
|                    | `user_type`             | IntegerField          | Type of user (1: User, 2: Parking Manager).                      |
|                    | `phone_number`          | CharField             | Optional phone number.                                           |
|                    | `street_address1`       | CharField             | First line of the user's street address.                         |
|                    | `street_address2`       | CharField             | Second line of the user's street address.                        |
|                    | `city`                  | CharField             | City name.                                                       |
|                    | `county`                | CharField             | County name.                                                     |
|                    | `postcode`              | CharField             | Postal code.                                                     |
|                    | `country`               | CountryField          | Country of residence.                                            |
|                    | `car_registration`      | CharField             | Optional car registration number.                                |
|                    | `stripe_customer_id`    | CharField             | Stripe customer ID for payment processing.                       |

</p>
</details>

<details>
<summary>Click to see `parking_management` app models</summary>
<p>

| **Model**     | **Field Name**      | **Field Type**       | **Description**                                                   |
|---------------|---------------------|-----------------------|-------------------------------------------------------------------|
| **Parking**   | `name`              | CharField             | Name of the parking lot.                                         |
|               | `user`              | ForeignKey            | Links to the `UserProfile` of the parking manager.               |
|               | `phone_number`      | CharField             | Contact phone number.                                            |
|               | `street_address1`   | CharField             | First line of the parking's address.                            |
|               | `street_address2`   | CharField             | Second line of the parking's address.                           |
|               | `city`              | CharField             | City name.                                                       |
|               | `county`            | CharField             | County name.                                                     |
|               | `postcode`          | CharField             | Postal code.                                                     |
|               | `country`           | CountryField          | Country of the parking location (default: GB).                   |
|               | `max_capacity`      | IntegerField          | Maximum capacity of the parking lot (default: 50).               |
|               | `latitude`          | CharField             | GPS latitude for geolocation.                                    |
|               | `longitude`         | CharField             | GPS longitude for geolocation.                                   |
|               | `radius`            | CharField             | Effective radius for geofencing.                                 |
|               | `active`            | BooleanField          | Whether the parking lot is active.                               |

| **Model**     | **Field Name**      | **Field Type**       | **Description**                                                   |
|---------------|---------------------|-----------------------|-------------------------------------------------------------------|
| **Rate**      | `rate_name`         | CharField             | Name of the rate plan.                                           |
|               | `user`              | ForeignKey            | Links to the `UserProfile` of the parking manager.               |
|               | `parking_name`      | ForeignKey            | Links to the related `Parking` lot.                              |
|               | `hour_range`        | IntegerField          | Duration in hours for which the rate applies.                    |
|               | `rate`              | DecimalField          | Fee for the specified hour range.                                |
|               | `timestamp_leave`   | DateTimeField         | Timestamp when the rate was applied.                             |

| **Model**           | **Field Name**      | **Field Type**       | **Description**                                                   |
|---------------------|---------------------|-----------------------|-------------------------------------------------------------------|
| **IllegalParking**  | `inspector`        | ForeignKey            | Links to the inspecting `UserProfile`.                           |
|                     | `parking_name`     | ForeignKey            | Links to the `Parking` lot where the incident occurred.          |
|                     | `car_reg`          | CharField             | Car registration of the offending vehicle.                       |

</p>
</details>

<details>
<summary>Click to see `parking_activity` app models</summary>
<p>

| **Model**         | **Field Name**           | **Field Type**       | **Description**                                                   |
|--------------------|--------------------------|-----------------------|-------------------------------------------------------------------|
| **Stay**          | `user`                  | ForeignKey            | Links to the `UserProfile` of the parking user.                  |
|                   | `parking_name`          | ForeignKey            | Links to the `Parking` lot.                                      |
|                   | `calculated_fee`        | DecimalField          | Fee calculated based on the stay duration.                       |
|                   | `stripe_checkout_id`    | CharField             | Stripe checkout session ID for the payment.                      |
|                   | `paid`                  | BooleanField          | Whether the payment has been made.                               |

| **Model**         | **Field Name**           | **Field Type**       | **Description**                                                   |
|--------------------|--------------------------|-----------------------|-------------------------------------------------------------------|
| **EnterParking**  | `user`                  | ForeignKey            | Links to the `UserProfile` of the parking user.                  |
|                   | `parking_name`          | ForeignKey            | Links to the `Parking` lot.                                      |
|                   | `stay`                  | ForeignKey            | Links to the associated `Stay` record.                           |
|                   | `timestamp_enter`       | DateTimeField         | Timestamp of entry.                                              |

| **Model**         | **Field Name**           | **Field Type**       | **Description**                                                   |
|--------------------|--------------------------|-----------------------|-------------------------------------------------------------------|
| **LeaveParking**  | `user`                  | ForeignKey            | Links to the `UserProfile` of the parking user.                  |
|                   | `parking_name`          | ForeignKey            | Links to the `Parking` lot.                                      |
|                   | `stay`                  | ForeignKey            | Links to the associated `Stay` record.                           |
|                   | `timestamp_leave`       | DateTimeField         | Timestamp of departure.                                          |

</p>
</details>


## 3. Features <a name="features"></a>

### 3.1 Authentication <a name="auth"></a>

The project uses django allauth for authentication.

The original templates were modfied for styling purposes, impacting the initial logic and the templates ability to display alter messages in some cases.

As a result, a custom register view has been written up in order to display alert messages and login user after registering an account.

This process is managed in user_management app through `CustomSignupView()`.

<details>
<summary>Click to see `CustomSignupView()`</summary>
<p>
    from django.contrib.auth.forms import UserCreationForm
    from django.contrib.auth import login
    from allauth.account.views import SignupView

    class CustomSignupView(SignupView):
    def form_valid(self, form):
        # Save the user
        user = form.save()

        # Authenticate the user for login
        user = authenticate(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1']
        )
        if user is not None:
            login(self.request, user)
            return redirect('home')
        return super().form_valid(form)
</p>
</details>

In order to install allauth, the following dependencies need to be installed by running:`pip install django-allauth` 

Your the project files, the following changes need to be made:

<details>
<summary>Click to see `settings.py` content</summary>
<p>

   TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                os.path.join(BASE_DIR, 'templates'),
            
                os.path.join(BASE_DIR, 'templates', 'allauth'),

            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    ...
                    # needed for allauth package
                    'django.template.context_processors.request',
                ],
            },
        },
    ]   

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        ...
        # all auth package:
        'django.contrib.sites',
        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.google',

        ...

    ]

    AUTHENTICATION_BACKENDS = [
        # Needed to login by username in Django admin, regardless of `allauth`
        'django.contrib.auth.backends.ModelBackend',

        # `allauth` specific authentication methods, such as login by email
        'allauth.account.auth_backends.AuthenticationBackend',

    ]

    MIDDLEWARE = [
        ...
        #All auth package:
        'allauth.account.middleware.AccountMiddleware',
    
    ]

    # Allauth settings
    ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
    ACCOUNT_EMAIL_REQUIRED = True
    ACCOUNT_EMAIL_VERIFICATION = 'none'
    ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
    ACCOUNT_USERNAME_MIN_LENGTH = 4
    LOGIN_URL = '/accounts/login/'
    LOGIN_REDIRECT_URL = '/'
</p>
</details>



<details>
<summary>urls.py (app level)</summary>
<p>

    # allauth view paths
    from .views import CustomSignupView

    urlpatterns = [
        ...
        path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    ]
</p>
</details>  

<details>
<summary>urls.py (project level)</summary>
<p>

    urlpatterns = [
       
        # Allauth package
        path('accounts/', include('allauth.urls')),
        
    ]
</p>
</details>

A migration will be required at the end.

Usefull link:

* Documentation : https://docs.allauth.org/en/latest/installation/quickstart.html


### 3.2 Password Reset Via Email <a name="password-reset"></a>

User can request a new password, from the `login.html` template (path: templates/allauth/account/login.html).

The reset password process take advantage of allauth already implemented logic and provided templates.

For this project, the logic remained untouched, but the templates were edited for styling.

In order reset their password, users are sent an email with a token generated by django.

In order to enable emails sending, a gmail address was created and the credentials of this address were added to `.env` for security purposes.

Some changes were needed in settings.py, which are detailed below.

<details>
<summary>Click to see changes in settings.py</summary>
<p>

    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https' 
    DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')

</p>
</details>

Finally as django provides an email template in plain text, this template was overwritten with `password_reset_key_message.html` (in path: `templates\allauth\account\email\password_reset_key_message.html`)

Django will by default look for an html file before retouring the the txt file.

This template was built using a template found on: https://tabular.email/

Useful links:
* Email templates: https://tabular.email/

### 3.3 Media Files : AWS S3 Bucket <a name="media-files"></a>

Since this project primarily uses static files and only a few media files (like the logo and favicon), the AWS S3 bucket integration is minimal.

Sensitive credentials, like AWS keys, are stored securely in `.env` file or on Heroku variables.

This setup uses WhiteNoise for static file management in development and AWS S3 for production.

Install required libraries: run `pip install django-storages boto3 whitenoise`

Update settings.py to handle statics and media files.

<details>
<summary>Click to see changes in settings.py</summary>
<p>

    import os
    from pathlib import Path

    BASE_DIR = Path(__file__).resolve().parent.parent

    # Static files settings
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

    
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    # Static file storage for production
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

</p>
</details>

In `urls.py` (project level) add settings to serve media files in developement.


<details>
<summary>Click to see changes in `urls.py`</summary>
<p>

    urlpatterns = [
    ...
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

</p>
</details>
    

To set up AWS S3 bucket, the following steps need to be followed:
* Create an account
* Create an S3 Bucket (untick `Block all public access`)
* Click on newly created bucket and go to Permissions
* write JSON bucket policy:
* Click `Policy Generator` and entert he following: 
    Type:`S3 Bucket Policy`
    Select `Allow`
    Principal: `*`
    Actions: `GetObject`
    ARN: `[enter ARN number from Properties tab]/*`
* Copy/Paste policy generated into the policy bucket.
* In terminal run:
    `pip install django-storages`
    `pip install boto3`
* In setting.py:

    INSTALLED_APPS = [
    
        #S3 bucket
        'storages',
    ]

### 3.4 User Profile <a name="user-profile"></a>

TO BE COMPELTED

### 3.5 User Dashboard <a name="user-dashboard"></a>

![rendering](static/images/readme_images/ui/user_dashboard/user-dashboard.png)


The user dashbaord can be found in `user_management\templates\home\index.html` and is managed by `index()`.

The function first starts by idenifying the user type through `is_parking_customer()`.

If the user_type is Parking Manager, that user will be automatically redirected to their own dashboard, whic his covered in the next section.

`index()` is arguably one of the most central function for the user.

This is from this function that the user can decide to:
* check-in at a parking
* checkout from a parking
* check their transaction history
* access their profile information

The template includes `geolocation.js`, which capture the user's geolocation to match with a potential parking's geofence. This element is discussed further in the **Check-In Parking** section.

Supported by `provide_car_reg.js`, the function also restricts users from checking in, if they havent provided their car registration:

    car_reg = False
    if request.user.userprofile.car_registration:
        car_reg= True

### 3.6 Parking Manager Dashboard <a name="parking-manager-dashboard"></a>

The parking manager dashboard provides a dashboard to user_type: Parking Manager.

It is handled by `parking_manager_dashboard()` and can be found on the following path: `parking_management/views.py`.

Similarly to the User Dashboard, the function checks if the user is a parking manager, through `is_parking_manager()`. Failing this test, will redirect the user to User Dashboard.

The dashboard allows the parking manager to have an overview of the `parking_id` that are associated to their account.

From this dashboard, the parking manager can:
* create a new parking object
* check existing parking status
* access each dedicate parking details page

At the bottom of the template, `activate_parking_helper.js` provides a reminder to activate the parking, and how to do it.

![rendering](static/images/readme_images/ui/parking_manager_dashboard/parking-manager-dashboard.png)

### 3.7 Create Parking<a name="create-parking"></a>

Creating a parking is a feature available only to user type: Parking Manager.

This feature is handled through `create_parking()`.

This feature uses a django for: `ParkingForm()` which looks to populate fields defined in Parking model.

**Important Note**: it is through these field, the geofence is defined. A default radius of 50 meters is applied. This radius should be extended to at least 850 meters if a device other than a mobile phone is used.

**Validators**

**LatLng:** With regards to latitude and longitude fields, the form implements a restriction with Regex patterns, and only accepts digits and `-` signs, to ensure values are properly implemented.

    class ParkingForm(forms.ModelForm):

        # restricts values in lat lng fields to didgits only
        latitude = forms.CharField(
            validators=[
                RegexValidator(
                    regex=r'^([+-]?)((90(\.0{1,9})?)|([1-8]?[0-9])(\.\d{1,9})?)$',  # Allows latitude with up to 9 decimals
                    message="Latitude must be a valid number (e.g., -90.0 to 90.0 and up to 9 decimals)."
                )
            ],
            widget=forms.TextInput(attrs={'aria-label': 'Latitude', 'placeholder': 'Enter latitude'})
        )

        longitude = forms.CharField(
            validators=[
                RegexValidator(
                    regex=r'^([+-]?)((180(\.0{1,9})?)|((1[0-7][0-9])|([1-9]?[0-9]))(\.\d{1,9})?)$',  # Allows longitude with up to 9 decimals
                    message="Longitude must be a valid number (e.g., -180.0 to 180.0 and up to 9 decimals)."
                )
            ],
            widget=forms.TextInput(attrs={'aria-label': 'Longitude', 'placeholder': 'Enter longitude'})
        )

**Note**: this regex synthax need to be credited to Stackoverflow post here: https://stackoverflow.com/questions/3518504/regular-expression-for-matching-latitude-longitude-coordinates

How does Regex work:
* ^: Defines the start of the string.
* -?: Matches an optional minus sign.
* \d+: Matches one or more digits.
* (\.\d+)?: Optionally matches a decimal point (.) followed by one or more digits.
* $: Defines the end of the string.


**Mandatory fields:** This form sets all fields as mandatory, in forms.py, with the exception of street_address2 field:

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set all fields as required by default
        for field_name, field in self.fields.items():
            field.required = True

        # make  street_address2 not required
        self.fields['street_address2'].required = False

Upon success of the form being saved, the user is redirect to the parking_object page managed by `parking_info()`.

Useful links:
* Stackover post on Regex for LatLng values: https://stackoverflow.com/questions/3518504/regular-expression-for-matching-latitude-longitude-coordinates


### 3.8 Read, Edit & Delete Parking <a name="read-edit-delete-parking"></a>

`parking_info()` handles the management of parking information and takes as a parameter`parking_id`.

This function enables the display of:
* parking status
* number of parking spaces used
* access to Parking Inspector feature
* parking information details and the option to add or edit them 
* rates applicable and the option to add or edit them

**Parking Status**

Parking status advises whether, the `parkind_id` is active or innactive.

For a user to check-in a parking, the parking needs to be `activate`.

Activating and deactivating parking is enabled with `activate_parking()`. Taking `parking_id` as a parameter, it either switch the parking on and off.

    @require_POST
    @login_required
    def activate_parking(request, parking_id):
        if not is_parking_manager(request):
            return redirect('home')

        parking = get_object_or_404(Parking, id=parking_id)

        # if actiate is true turn it off
        if parking.active:
            parking.active = False
            parking.save()
        # if activate is off turn it on
        else:
            parking.active = True
            parking.save()

        messages.success(request, f"{parking.name} has been {'activated' if parking.active else 'deactivated'}.")
        return redirect('parking-info', parking_id=parking_id)

The button that triggers this function on the template under :

    <div class="col">
        <a class="btn button-2 full-width" href="{% url 'parking-info' parking_id=item.parking.id %}">Info</a>
    </div>

**Parking Spaces Available**

Parking spaces available are calculated with the user of `parking_space_available()`, taking `parking_id` as a parameter.

This function counts the number of `Stay` objects, relating to `parking_id` parameter, that have not been marked as paid.

The function returns this value through var `stay_objects_count` to `parking_info()`. 

This variable is then returned on the template in `parking_info.html`, via `parking_info_block.html`.


parking_info.html

    {% block parking_info_block %}
        {% include 'parking_info/parking_info_blocks/parking_info_block.html' %}
    {% endblock %}

parking_info_block.html

    <div class="row d-flex align-items-center justify-content-center">
        <span>
            {{stay_objects_count}}/{{parking.max_capacity}}
        </span>
    </div>

**Parking Inspector & Rates**

This feature is covered in a later section.

**Edit and Delete Parking Object**

`edit_parking()` allows parking manager to edit the `parking_id` object by passing the object into `ParkingForm` as an instance to retrieve existing data and edit them.

`delete_parking()`, taking `parkinf_id` as a parameter will allow a parking manager to delete a parking object.

Upon deletion, object associated to parking_id object <b>will not be deleted</b>, as child models are set to `on_delete=models.SET_NULL`.

This is set in place, in order to avoid losing history of transactional data done previously, in particular how rates are calculated, and also illegally parked cars.

**Rates**

Parking Info page displays all applicables rates to selected `parking_id` object.

These rates are created and edited by the parking manager.

### 3.9 Create Parking Rates <a name="create-parking-rates"></a>

Creating parking rates is enabled by `add_rate()`.

Using `RateForm`,(defined in: `parking_management/forms.py`) , it creates a rate object.

The form contains validators ensuring:
* all fields are populated
* rate value is above 0.

**Note for future development:** It would make sense to allow for the rate to be equal to 0, as some parkings offer free stay during an initial hour range. The current code will need to be modified. Currently, without this validator, stripe will not consider a fee of "0" value as payment. This is probably an easy fix.

The template also contain some javascript, providing a tutorial on how the hourly rate works. 

This logic is further explained in <a name="check-out"> Check-Out Parking </a>

### 3.10 Read, Edit & Delete Parking Rates <a name="read-edit-delete-parking-rates"></a>
### 3.11 Check-In Parking : Geolocation <a name="check-in"></a>
### 3.12 Check-Out Parking <a name="check-out"></a>
### 3.13 Stripe Payment Integration <a name="stripe"></a>
### 3.14 Crispy Forms <a name="cripsy"></a>
### 3.15 Decorators <a name="decorators"></a>
### 3.16 Custom Error Handlers <a name="error-handler"></a>
### 3.17 Parking Inspector <a name="parking-inspector"></a>

## 4. Technologies <a name="tech"></a>

## 5. Testing <a name="testing"></a>
### 5.1 Validator Testing <a name="val-testing"></a>
#### 5.1.1 HTML <a name="html"></a>
#### 5.1.2 CSS <a name="css"></a>
#### 5.1.3 Javascript <a name="js"></a>
#### 5.1.3 Python <a name="py"></a>
### 5.2 Lighthouse Testing <a name="lighthouse-testing"></a>
### 5.3 User Testing <a name="user-testing"></a>

<!-- Click on this link to see manual testing steps: [Manual Testing Guide](MANUAL_TESTING.md) -->

## 6. Bugs <a name="bugs"></a>

### 6.1 Current bugs <a name="current-bugs"></a>

### 6.2 Design & User Experience improvements <a name="design-improvements"></a>

### 6.3 Logic improvements & Backend <a name="logic-improvements"></a>

## 7. Deployment <a name="deployment"></a>

### 7.1 Local Deployment <a name="local-deployment"></a>

To install PostGres on local, the following steps were followed.

To set up of PostGres on Local run : `pip install psycopg2` 

Issues encountered and solution:

This may have been specific to my local setup, but I had to use : pip install psycopg2-binary 

(Documentation: https://pypi.org/project/psycopg2-binary/). My requirements.txt file lists : psycopg2-binary==2.9.9

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

Useful links:
* Instal postgres on local: https://www.postgresql.org/download/
* Extra Documentation: https://pypi.org/project/psycopg2-binary/

### 5.1 Heroku Deployment <a name="heroku-deployment"></a>

## 8. Credits <a name="credits"></a>

# colour palette


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

## Setup AWS S3 Bucket
The project does not have any media files, with the exception of the logo and favicon.

As a result, it felt that time should not be invested into a full integration of the S3 bucket.

The steps below cover the initial steps followed to setup an AWS account and host the logo file on S3.
* Create an account
* Create an S3 Bucket (untick `Block all public access`)
* Click on newly created bucket and go to Permissions
* write JSON bucket policy:
* Click `Policy Generator` and entert he following: 
    Type:`S3 Bucket Policy`
    Select `Allow`
    Principal: `*`
    Actions: `GetObject`
    ARN: `[enter ARN number from Properties tab]/*`
* Copy/Paste policy generated into the policy bucket.
* In terminal run:
    `pip install django-storages`
    `pip install boto3`
* In setting.py:

    INSTALLED_APPS = [
    
        #S3 bucket
        'storages',
    ]



## Heroku Setup (Production)
* Log into heorku : `heroku login`
* Add heroku remote : `git remote add heroku [Heroku Git URL]` (can be found in Heroku Settings)
* Push code to Heroku: `git push heroku master`
* Run first migration: `heroku run python manage.py migrate`

Problem encountered: the Procfile generated with command line from documentation echo web: gunicorn app:app > Procfile created an issue relating to encoding. The encoding defaulted to UTF-16 instead of UTF-8.

To solve this problem: create a new Procfile through a Notepad, selected encoding UTF-8 and called it Procfile.txt in the same location as the actual Procfile. I then deleted the previous Procfile and renamed Procfile.txt to Procfile.

### 

setup Debug = False
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
crdiits: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment

Add whitenoise in settings.py to middleware list

    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

**Error encountered**: `MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled.`. whitenoise wasnot installed. Adding whitenoise corrected the error.

**Error encountered**: css file not loading in production. This problem was solved by moving `'whitenoise.middleware.WhiteNoiseMiddleware',` to the top.

    MIDDLEWARE = [
        'django.middleware.security.SecurityMiddleware',
        #whitenoise package : used for production to be set at the top
        'whitenoise.middleware.WhiteNoiseMiddleware',    
    ]

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

                    ...

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

**Error encountered** User geolocation innacuracy: in order to deal with lack of accuracy of the user location (which seems to be between 3m to 888m range based on various test), the minimum parking radius has been set to 1km (1000m).

In future development, this radius could be drastically reduced by using GPS location. This would require using native features of the phone. Either through a mobile app, or using Django's progressive web app.

* handle redirect to identified parking_id or not

Due to potential innacuracy in geolocation, `get_parking_location()` might not return a parking ID.

Depending on the scenario, `get_parking_location()` will redirect the user with out without the `parking id` as a parameter:

    return redirect('enter_with_parking_id', parking_id=parking_name.id)

    or

    return redirect('enter') 

To handle these two scenarios, two paths leading to the same view were made available:

    path('enter/', views.enter, name='enter'),
    path('enter/<int:parking_id>/', views.enter, name='enter_with_parking_id'),

The parameter is then returned in `enter()` and is given a default value of `None`:

    def enter(request, parking_id=None):

* StayForm() handling and submission

This part is handled by `enter()` and considers two scenarios through a form:
* if parking_id is provided as an argument, the user is asked to confirm they are happy to be marked as having entered `parking_id`
* if parking_id is None, the user is asked to select the parking name from a drop down menu.

Upon submission of the form, a Stay object is created, together with an Enter Object, both are linked via a foreign Key.

* rendering of parking fees (javascript)

Within the javascript document, the following logic is applied:

First implement a logic that collects the `parking_id`:

If provided as a parameter, the logic picks up the parking_id from the url

    // sets parking id as null by default
    let parkingId = "null";
    // captures parameter from url (if any)
    const path = window.location.pathname;
    const match = path.match(/\/enter\/(\d+)\//);
    const parkingIdFromParam = match ? match[1] : null;
    console.log(`parking id is ${parkingIdFromParam}`);

If not provided as parameter, a drop down menu needs to be added to the html template looping over the different parking names available.

    <!-- If parking ID is None -->
    <form method="post">
        {% csrf_token %}
        <label for="parking-select">Select Parking:</label>
        <select id="parking-select" name="parking_name">
            <option value="">Select parking</option>
            {% for parking in parking_list %}
                <option value="{{ parking.id }}" 
                    {% if parking_id == parking.id %}
                        selected
                    {% endif %}>
                    {{ parking.name }}
                </option>
            {% endfor %}
        </select>
        <input type="submit" value="Submit the form">
    </form>

Once a parking name is selected, variable `manuallySelectedParking` collects the chosen parking name, which in turn give `parkingId` the id of the parking selected.

    const manuallySelectedParking = document.getElementById('parking-select');
        console.log("manuallySelectedParking=", manuallySelectedParking);

    if(manuallySelectedParking){
        manuallySelectedParking.addEventListener('change', function(){
            console.log("this is getting accessed")
            parkingId = this.value || "null";
            console.log(`Updated parking id is ${parkingId}`);
            // only trigger fetchRates() if parking_id is not null
            // to avoid 404 error in console
            if (parkingId !== "null"){
                fetchRates();
            }
                
            })


Once `parking_id` is retrieved, the logic calls `get_parking_rates()` to return the parking rates. The function dynamically returns parking fees based on the parking selected.

    #used to get parking rates through API (dynamically generated with js)
    #note: safe = False allows to return a list instead of a dictonnary
    # this is because Json expect a dict by default (add error to log of errors encourntered)
    # credits: https://dev.to/chryzcode/django-json-response-safe-false-4f9i
    def get_parking_rates(request, parking_id):
        print(f'get_parking_rates parking id = {get_parking_rates}')
        rates = Rate.objects.filter(parking_name_id = parking_id).values(
            'rate_name',
            'hour_range',
            'rate',
        )
        return JsonResponse(list(rates), safe=False)

`get_parking_rates()` is called from parking_fee.js at the bottom of template : `enter.html`
    
**enter.html**

    {% block postloadjs %}
    <script src="{% static 'js/parking_fee.js' %}"></script>
    {% endblock %}

**parking_fee.js**

Create function `fetchRates()` to dynamically collect applicables rates from selected parking form the database.

    function fetchRates(){
        console.log(`ParkindId in fetchRates= ${parkingId}`);
        if(parkingId){
            fetch(`/parking_activity/get_parking_rates/${parkingId}/`)
            .then(response => response.json())
            .then(data =>{
                console.log("Fetched rates", data);
                renderRatesTable(data);
            })
            .catch(error => console.error("theres an error when getting the rates", error))
        }   
    }

Once the data is collected, it can then be rendered in `enter.html` template with `renderRatesTable()`.

    function renderRatesTable(data){

        // get the body of the table
        const table = document.getElementById("ratesTable");
        const tbody = document.querySelector("table tbody")
        tbody.innerHTML = "";

        if(data.length>0){
            
            // shows table
            table.style.display ="table"
            // Adds data to table rwos

            data.forEach(rate=>{
                const tableRow = document.createElement('tr');
                tableRow.innerHTML = `
                <tr>
                    <td>${rate.rate_name}</td>
                    <td>${rate.hour_range}</td>
                    <td>${rate.rate}</td>
                </tr>
                `;
                tbody.appendChild(tableRow);
            });
        }else{
            table.style.display = "none"
        }
    }

    <table>
        <thead>
            <tr>
                <th>Rate Name</th>
                <th>Hour Range</th>
                <th>Rate</th>
            </tr>
        </thead>
        <tbody></tbody>
    </table>

Problem encountered: error generated in the console `404 Page Not Found` when parkingId is null. To cover this, `fetchRates()` in wrapped within an if statement that checks if parkingId is null before triggering `fetchRates()`

    if (parkingId !== "null"){
        fetchRates()
    }

Useful links:
* https://developer.mozilla.org/en-US/docs/Web/API/Geolocation_API
* https://stackoverflow.com/questions/42686300/how-to-check-if-coordinate-inside-certain-area-python
* https://geopy.readthedocs.io/en/stable/#module-geopy.distance

# Parking Management App

## Parking Manager Dashboard

## Create New Parking (form)

This feature is managed by `create_parking()`. 

To enable this `ParkingForm` is created in forms.py, allowing to create Parking model objects.

Upon successful submission, the newly created object passes its id, as a parameter to redirect the user to `parking_info()`

Use Crispy Forms:
* Run `pip install django-crispy-forms`
* Run `pip install crispy-bootstrap5`
* Run `pip install django-countries`

* In Installed_apps (Settings.py) add:

    INSTALLED_APPS = [
        'django.contrib.admin',
        ...
        #crispy form packages
        'crispy_forms',
        'crispy_bootstrap5',

    ]
* In Settings.py, add:

    CRISPY_TEMPLATE_PACK = 'bootstrap5'

## See Parking Details (CRUD)

# Parking Rates (CRUD)

# Parking Inspector (see registration, take note of those not registered)

## JS Validators on signup

## django logging to see logs in production

import os

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
            },
        },
        "root": {
            "handlers": ["console"],
            "level": "WARNING",
        },
        "loggers": {
            "django": {
                "handlers": ["console"],
                "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
                "propagate": False,
            },
        },
    }

ciredits: https://docs.djangoproject.com/en/5.1/topics/logging/

## is_parking_customer()

## is_parking_manager()
Used to prevent non `parking_manager` user types to access parking_management app functions.

    class UserProfile(models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        user_type = models.IntegerField(choices=USER_TYPE, default = 1)
    

    def is_parking_manager(request):
        print(f'request.user.userprofile.user_type: {request.user.userprofile.user_type}')
        if request.user.userprofile.user_type != 2:
            return False
        return True

        @login_required
    def parking_manager_dashboard(request):
        if not is_parking_manager(request):
            return redirect('home')
        
        ...

If the user_type is not '2' (parking manager), return user to home page.

## decorators
from django.views.decorators.http import require_POST
@login_required

from django.contrib.auth.decorators import login_required
login_required


## error handlers
urls.py (project level):

    from django.conf.urls import handler404, handler500, handler403, handler400

    urlpatterns = [....
    ] 

    handler404 = 'user_management.views.handler404'
    handler500 = 'user_management.views.handler500'
    handler403 = 'user_management.views.handler403'
    handler400 = 'user_management.views.handler400'

In views.py (app level):

    def handler404(request, exception):
        """ Handle 404 errors and render the custom 404 error page """
        return render(request, 'errors/404.html', status=404)


    def handler500(request):
        """ Handle 500 errors and render the custom 500 error page """
        return render(request, 'errors/500.html', status=500)


    def handler403(request, exception):
        """ Handle 403 errors and render the custom 403 error page """
        return render(request, 'errors/403.html', status=403)


    def handler400(request, exception):
        """ Handle 400 errors and render the custom 400 error page """
        return render(request, 'errors/400.html', status=400)


    def test_500_error(request: HttpRequest):
        """ Raise a test exception for the 500 error handler """
        raise Exception("Test 500 error")


    def test_403_error(request):
        """ Raise a test exception for the 403 error handler """
        raise PermissionDenied("Test 403 error")


    def test_400_error(request):
        """ Raise a test exception for the 400 error handler """
        raise SuspiciousOperation("Test 400 error")

Add templates in: `app_name/templates/errors/template_name`

## Problem encountered - user getting logged out on mobile phone 
when opening new borwser window when scanning QR code

To solve this problem, add to settings.py:

    # Prevent sessions from being reset
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True 
    SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
    SESSION_COOKIE_DOMAIN = '.geopay-12a0f6ced11c.herokuapp.com'
    CSRF_TRUSTED_ORIGINS=['https://*.geopay-12a0f6ced11c.herokuapp.com']

credits: https://stackoverflow.com/questions/3976498/why-doesnt-session-expire-at-browser-close-true-log-the-user-out-when-the-bro

This has improve the result. However, the problem still persist. This could be due to the fact I havent deployed the SSL certificate on the site, as this is a paying feature.



Credits:
Validation for login : https://stackoverflow.com/questions/74245576/the-problem-of-not-displaying-validation-messages-in-allauth-after-overriding-al

## sites used
https://cdnjs.com/ : for cdn links
https://tabular.email/: for email template
https://icons8.com/ : icons on email
