  

# M4Project - GeoPay

<p align="center" width="100%">
   <img width="200" src="https://geopay-app.s3.eu-north-1.amazonaws.com/images/logo/geopay-logo.webp">
</p>

View the live site: <a href="https://geopay-12a0f6ced11c.herokuapp.com/" target="_blank">Click Here</a>

## Getting Started

This is two sided platform for users and parking managers.

On the user side, the project is meant to be used with a mobile phone., as one of the core feature requires accurate geolocation, on the customer side. This is achieved by leveraging embedded GPS.

Once you have setup a parking under the desired geolocation, as parking manager, please scan the QR code to access the deployed project from your mobile phone for a full experience.

Although a plus, the project does not require a mobile phone to be tested.

<p align="center" width="100%">
   <img width="200" src="static\images\readme_images\geopay_qr_code\geopay-qr-code-edited.png">
</p>


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
    - [Back Button](#back-button)
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

There is a parking where I park once a month, and it rains all the time. If it does not rain, there is some strong wind. Or it's just very cold outside.

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
* As a parking user, I want to be able to edit and delete my account details.
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
* As a platform I want to enable payment through a third party platform like Stripe

**Parking Manager**
* As a parking manager, I want to have a dedicated space to manage my parking from the account I have created.
* As a parking manager, I want to set and adjust the hourly fee for my parking lots.
* As a parking manager, I want to see a live list of all car registrations that have registered their arrival in my parking.
* As a parking manager, I want to be able to physically walk through my parking and inspect if car with registrations that are not marked are parked.
* As a parking manager, I want to keep records of those illegally parked cars, for future penatly process.

## 2. Design <a name="design"></a>

### 2.1 Colours <a name="colours"></a>

The main colours used for this project are the following:

![rendering](static/images/readme_images/colour_scheme/colour-scheme.png)

### 2.2 Typography <a name="typography"></a>

The project uses Albert Sans, to create a modern and accessible font.

The font is sourced from Google.

![rendering](static/images/readme_images/typography/typography.png)

### 2.3 Icons & Images <a name="icons-images"></a>

Icons and images are hosted on S3 Bucket:

* Logo was generated using MidJourney;
* Icons used are mostly coming from FontAwesome;
* Other icons, in particular those used in emails are sourced from Icons8;
* There is other image, as it did not add any value to the purpose of the product.

As users do not need to upload any image, and in order to reduce devevlopment times, it was therefore decided to upload media assets directly on S3 Buckets (see S3 Bucket Section for process).

### 2.4 Wireframes <a name="wireframes"></a>

Wireframes initially designer for the project are available below.

<details>
    <summary style="color: white; background: black; padding: 5px;">Click to see wireframes</summary>
    <p align="center">>
        <kbd><img style="background:grey; padding:10px" src="static/images/readme_images/wireframes/wireframes.png" alt="wireframes" /></kbd>
    </p>
</details>

### 2.5 Databases <a name="databases"></a>

<details>
    <summary style="color: white; background: black; padding: 5px;">Click to see ER Diargram</summary>
    <p>
        <kbd><img src="static/images/readme_images/erd.png" alt="erd" /></kbd>
    </p>
</details>

<details>
<summary style="color: white; background: black; padding: 5px;">Click to ER Diargram dependency installation process</summary>
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
<summary style="color: white; background: black; padding: 5px;">Click to see `user_management` app models</summary>
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
<summary style="color: white; background: black; padding: 5px;">Click to see `parking_management` app models</summary>
<p>

| **Model**     | **Field Name**      | **Field Type**       | **Description**                                                   |
|---------------|---------------------|-----------------------|-------------------------------------------------------------------|
| **Parking**   | `name`              | CharField             | Name of the parking object.                                         |
|               | `user`              | ForeignKey            | Links to the `UserProfile` of the parking manager.               |
|               | `phone_number`      | CharField             | Contact phone number.                                            |
|               | `street_address1`   | CharField             | First line of the parking's address.                            |
|               | `street_address2`   | CharField             | Second line of the parking's address.                           |
|               | `city`              | CharField             | City name.                                                       |
|               | `county`            | CharField             | County name.                                                     |
|               | `postcode`          | CharField             | Postal code.                                                     |
|               | `country`           | CountryField          | Country of the parking location (default: GB).                   |
|               | `max_capacity`      | IntegerField          | Maximum capacity of the parking object (default: 50).               |
|               | `latitude`          | CharField             | GPS latitude for geolocation.                                    |
|               | `longitude`         | CharField             | GPS longitude for geolocation.                                   |
|               | `radius`            | CharField             | Effective radius for geofencing.                                 |
|               | `active`            | BooleanField          | Whether the parking object is active.                               |

| **Model**     | **Field Name**      | **Field Type**       | **Description**                                                   |
|---------------|---------------------|-----------------------|-------------------------------------------------------------------|
| **Rate**      | `rate_name`         | CharField             | Name of the rate plan.                                           |
|               | `user`              | ForeignKey            | Links to the `UserProfile` of the parking manager.               |
|               | `parking_name`      | ForeignKey            | Links to the related `Parking` obejct.                              |
|               | `hour_range`        | IntegerField          | Duration in hours for which the rate applies.                    |
|               | `rate`              | DecimalField          | Fee for the specified hour range.                                |
|               | `timestamp_leave`   | DateTimeField         | Timestamp when the rate was applied.                             |

| **Model**           | **Field Name**      | **Field Type**       | **Description**                                                   |
|---------------------|---------------------|-----------------------|-------------------------------------------------------------------|
| **IllegalParking**  | `inspector`        | ForeignKey            | Links to the inspecting `UserProfile`.                           |
|                     | `parking_name`     | ForeignKey            | Links to the `Parking` object.          |
|                     | `car_reg`          | CharField             | Car registration of the offending vehicle.                       |

</p>
</details>

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see `parking_activity` app models</summary>
<p>

| **Model**         | **Field Name**           | **Field Type**       | **Description**                                                   |
|--------------------|--------------------------|-----------------------|-------------------------------------------------------------------|
| **Stay**          | `user`                  | ForeignKey            | Links to the `UserProfile` of the parking user.                  |
|                   | `parking_name`          | ForeignKey            | Links to the `Parking` object.                                      |
|                   | `calculated_fee`        | DecimalField          | Fee calculated based on the stay duration.                       |
|                   | `stripe_checkout_id`    | CharField             | Stripe checkout session ID for the payment.                      |
|                   | `paid`                  | BooleanField          | Whether the payment has been made.                               |

| **Model**         | **Field Name**           | **Field Type**       | **Description**                                                   |
|--------------------|--------------------------|-----------------------|-------------------------------------------------------------------|
| **EnterParking**  | `user`                  | ForeignKey            | Links to the `UserProfile` of the parking user.                  |
|                   | `parking_name`          | ForeignKey            | Links to the `Parking` object.                                      |
|                   | `stay`                  | ForeignKey            | Links to the associated `Stay` record.                           |
|                   | `timestamp_enter`       | DateTimeField         | Timestamp of entry.                                              |

| **Model**         | **Field Name**           | **Field Type**       | **Description**                                                   |
|--------------------|--------------------------|-----------------------|-------------------------------------------------------------------|
| **LeaveParking**  | `user`                  | ForeignKey            | Links to the `UserProfile` of the parking user.                  |
|                   | `parking_name`          | ForeignKey            | Links to the `Parking` object.                                      |
|                   | `stay`                  | ForeignKey            | Links to the associated `Stay` record.                           |
|                   | `timestamp_leave`       | DateTimeField         | Timestamp of departure.                                          |

</p>
</details>


## 3. Features <a name="features"></a>

### 3.1 Authentication <a name="auth"></a>

The project uses django allauth for authentication.

The original templates were modfied for styling purposes. This impacted the initial allauth logic and the template's ability to display messages in some cases.

As a result, a custom register view has been written up in order to display alert messages and login user after registering an account.

This process is managed in user_management app through `CustomSignupView()`.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see `CustomSignupView()`</summary>
<p>

```python
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
```

</p>
</details>

In order to install allauth, the following dependencies need to be installed by running:`pip install django-allauth` 

In your the project files, the following changes need to be made:

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see `settings.py` content</summary>
<p>

```python
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
```
</p>
</details>



<details>
<summary style="color: white; background: black; padding: 5px;">urls.py (app level)</summary>
<p>

```python
    # allauth view paths
    from .views import CustomSignupView

    urlpatterns = [
        ...
        path('accounts/signup/', CustomSignupView.as_view(), name='account_signup'),
    ]
```
</p>
</details>  

<details>
<summary style="color: white; background: black; padding: 5px;">urls.py (project level)</summary>
<p>

```python
    urlpatterns = [
       
        # Allauth package
        path('accounts/', include('allauth.urls')),
        
    ]
```

</p>
</details>

A migration will be required at the end.

> [!NOTE]
> Credits - Documentation : https://docs.allauth.org/en/latest/installation/quickstart.html


### 3.2 Password Reset Via Email <a name="password-reset"></a>

User can request a new password, from the `login.html` template (path: templates/allauth/account/login.html).

The reset password process take advantage of allauth already implemented logic and provided templates.

For this project, the logic remained untouched, but the templates were edited for styling.

In order to reset their password, users are sent an email with a token generated by django.

In order to enable emails sending, a gmail address was created and the credentials of this address were added to `.env` for security purposes.

Some changes were needed in settings.py, which are detailed below.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see changes in settings.py</summary>
<p>

```python
    # Email
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
    EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
    ACCOUNT_DEFAULT_HTTP_PROTOCOL = 'https' 
    DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
```

</p>
</details>

Finally as django provides an email template in plain text, this template was overwritten with `password_reset_key_message.html` (in path: `templates\allauth\account\email\password_reset_key_message.html`)

Django will by default look for an html file before retouring the the txt file.


> [!NOTE]
> Credits - This template was built using a template found on: https://tabular.email/

### 3.3 Media Files : AWS S3 Bucket <a name="media-files"></a>

Since this project primarily uses static files and only a few media files (like the logo and favicon), the AWS S3 bucket integration is minimal.

Sensitive credentials, like AWS keys, are stored securely in `.env` file or on Heroku variables.

This setup uses WhiteNoise for static file management in development and AWS S3 for production.

Install required libraries: run `pip install django-storages boto3 whitenoise`

Update settings.py to handle statics and media files.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see changes in settings.py</summary>
<p>

```python
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
```

</p>
</details>

In `urls.py` (project level) add settings to serve media files in developement.


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see changes in `urls.py`</summary>
<p>

```python
    urlpatterns = [
    ...
    ] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
```

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
    ```python
    INSTALLED_APPS = [
        #S3 bucket
        'storages',
    ]
    ```

### 3.4 User Profile <a name="user-profile"></a>

The project includes a user profile page.

This feature is managed by `user_account()` (path: `user_management\views.py`), which displays UserProfile information link to user's UserProfile model object.

This feature is also supported by `edit_user_account()` and `delete_user_account()`.

`delete_user_account()` contains validators to prevent:
* Parking User from deleting their accounts whilst checked-in (and not paying for parking)
* Parking Manager from deleting their accounts preventing user from checking out.

### 3.5 User Dashboard <a name="user-dashboard"></a>

<p align="center">
   <kbd><img width="200" src="static/images/readme_images/ui/user_dashboard/user-dashboard.png"></kbd>
</p>

The user dashbaord can be found in `user_management\templates\home\index.html` and is managed by `index()`.

The function first starts by idenifying the user type through `is_parking_customer()`.

If the user_type is Parking Manager, that user will be automatically redirected to their own dashboard, which his covered in the next section.

`index()` is arguably one of the most central function for the user.

This is from this function that the user can decide to:
* check-in at a parking
* checkout from a parking
* check their transaction history
* access their profile information

The template includes `geolocation.js`, which capture the user's geolocation to match with a potential parking's geofence. This element is discussed further in the **Check-In Parking** section.

Supported by `provide_car_reg.js`, the function also restricts users from checking in, if they havent provided their car registration:

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
car_reg = False
if request.user.userprofile.car_registration:
    car_reg= True
```
</p>
</details>



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

A validator prevents the parking manager from deactivating a parking with cars already checked-in.


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python

@require_POST
@login_required
def activate_parking(request, parking_id):
    if not is_parking_manager(request):
        return redirect('home')

    parking = get_object_or_404(Parking, id=parking_id)

    # checks the parking has rates applied
    rate_exist = Rate.objects.filter(parking_name=parking)
    print(rate_exist)
    
    if not rate_exist:
        print('rate_exist is empty')
        messages.error(request, f"Add a rate before activating parking.")
        return redirect('parking-info', parking_id=parking.id)

    has_user = parking_space_available(request, parking_id=parking_id)
    print(f'has_user = {has_user}')
    # prevents parking manager from deleting parking obj
    # when parking users are checked-in
    if has_user != 0:
        messages.error(request, "You cannot deactive parking when users are still checked-in. Contact admin.")
        return redirect('parking-info', parking_id=parking_id)

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
```
</p>
</details>


<p align="center">
   <kbd><img width="200" src="static/images/readme_images/ui/parking_manager_dashboard/parking-manager-dashboard.png"></kbd>
</p>


### 3.7 Create Parking<a name="create-parking"></a>

Creating a parking is a feature available only to user type: Parking Manager.

This feature is handled through `create_parking()`.

This feature uses a django form `ParkingForm()` which looks to populate fields defined in Parking model.

**Important Note**: it is through these field, the geofence is defined. A default radius of 50 meters is applied. This radius should be extended to at least 850 meters if a device other than a mobile phone is used.

**Validators - LatLng:**

With regards to latitude and longitude fields, the form implements a restriction with Regex patterns, and only accepts digits and `-` signs, to ensure values are properly implemented.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
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
```
</p>
</details>


> [!NOTE]
> Credits - This regex synthax is credited to Stackoverflow post: https://stackoverflow.com/questions/3518504/regular-expression-for-matching-latitude-longitude-coordinates<br>

How does Regex work:
* ^: Defines the start of the string.
* -?: Matches an optional minus sign.
* \d+: Matches one or more digits.
* (\.\d+)?: Optionally matches a decimal point (.) followed by one or more digits.
* $: Defines the end of the string.


**Validators - Mandatory Field:** This form sets all fields as mandatory, in forms.py, with the exception of street_address2 field:


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set all fields as required by default
        for field_name, field in self.fields.items():
            field.required = True

        # make  street_address2 not required
        self.fields['street_address2'].required = False
```

</p>
</details>

Upon success of the form being saved, the user is redirect to the parking_object page managed by `parking_info()`.


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

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    @require_POST
    @login_required
    def activate_parking(request, parking_id):
        if not is_parking_manager(request):
            return redirect('home')

        parking = get_object_or_404(Parking, id=parking_id)

        # checks the parking has rates applied
        rate_exist = Rate.objects.filter(parking_name=parking)
        print(rate_exist)
        
        if not rate_exist:
            print('rate_exist is empty')
            messages.error(request, f"Add a rate before activating parking.")
            return redirect('parking-info', parking_id=parking.id)

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
```

</p>
</details>

The button that triggers this function on the template under :



<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    <div class="col">
        <a class="btn button-2 full-width" href="{% url 'parking-info' parking_id=item.parking.id %}">Info</a>
    </div>
```

</p>
</details>


> [!IMPORTANT]
> Parking objects cannot be activated unless they are provided at least with 1 applicable rate. This rule is set in force in both backend, where the logic will check if an existing rate has been attached to this `parking_id` and display an error message, and in the front end by hiding the "Activate" button.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    if not rate_exist:
        print('rate_exist is empty')
        messages.error(request, f"Add a rate before activating parking.")
        return redirect('parking-info', parking_id=parking.id)
```

</p>
</details>



**Parking Spaces Available**

Parking spaces available are calculated with the user of `parking_space_available()`, taking `parking_id` as a parameter.

This function counts the number of `Stay` objects, relating to `parking_id` parameter, that have not been marked as paid.

The function returns this value through var `stay_objects_count` to `parking_info()`. 

This variable is then returned on the template in `parking_info.html`, via `parking_info_block.html`.



<details>
<summary style="color: white; background: black; padding: 5px;">Click to see parking_info.html</summary>
<p>

```html
    {% block parking_info_block %}
        {% include 'parking_info/parking_info_blocks/parking_info_block.html' %}
    {% endblock %}
```

</p>
</details>


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see parking_info_block.html</summary>
<p>

```html
    <div class="row d-flex align-items-center justify-content-center">
        <span>
            {{stay_objects_count}}/{{parking.max_capacity}}
        </span>
    </div>
 ```
 
</p>
</details>


**Parking Inspector & Rates**

This feature is covered in a later section.

**Edit and Delete Parking Object**

`edit_parking()` allows parking manager to edit the `parking_id` object by passing the object into `ParkingForm` as an instance to retrieve existing data and edit them.

`delete_parking()`, taking `parkinf_id` as a parameter will allow a parking manager to delete a parking object.

Upon deletion, object associated to parking_id object <b>will not be deleted</b>, as child models are set to `on_delete=models.SET_NULL`.

This is set in place, in order to avoid losing history of transactional data done previously, in particular how rates are calculated, and also illegally parked cars.

Validators were setup in each functions views to prevent parking manager deleting parking objects when users are checked-in.


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
@login_required
def delete_parking(request, parking_id):
    if not is_parking_manager(request):
        return redirect('home')

    parking = get_object_or_404(Parking, id=parking_id, user=request.user.userprofile)
    
    has_user = parking_space_available(request, parking_id=parking.id)
    print(f'has_user = {has_user}')
    # prevents parking manager from deleting parking obj
    # when parking users are checked-in
    if has_user != 0:
        messages.error(request, "You cannot delete a parking when users are still checked-in.")
        return redirect('parking-info', parking_id=parking.id)

    parking.delete()
    messages.success(request, "Parking deleted.")
    return redirect('parking-manager-dashboard')
```

</p>
</details>
    


**Rates**

Parking Info page displays all applicables rates to selected `parking_id` object.

These rates are created and edited by the parking manager.

### 3.9 Create Parking Rates <a name="create-parking-rates"></a>

Creating parking rates is enabled by `add_rate()`.

Using `RateForm`,(defined in: `parking_management/forms.py`) , it creates a rate object.

The form contains validators ensuring:
* all fields are populated
* rate value is above 0.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see parking_info_block.html</summary>
<p>

```python
    class RateForm(ModelForm):

        rate_name = forms.CharField(
            required=True, 
            label='', 
            widget=forms.TextInput(attrs={'placeholder': 'Enter rate title'})
        )
        hour_range = forms.IntegerField(
            required=True, 
            label='', 
            widget=forms.NumberInput(attrs={'placeholder': 'Maximum hour until which rate is applicable'}),
            validators=[MinValueValidator(1)]
        )
        rate = forms.DecimalField(
            required=True, 
            label='', 
            widget=forms.TextInput(attrs={'placeholder': 'Enter applicable rate'}),
            validators=[MinValueValidator(0.01)]  # prevents user to under values under or equal to 0 
        )

 ```

</p>
</details>
  

**Note for future development:** It would make sense to allow for the rate to be equal to 0, as some parkings offer free stay during an initial hour range. The current code will need to be modified. Currently, without this validator, stripe will not consider a fee of "0" value as payment. This is probably an easy fix.

The template also contain some javascript, providing a tutorial on how the hourly rate works. 

This logic is further explained in <a name="check-out"> Check-Out Parking </a>

### 3.10 Read, Edit & Delete Parking Rates <a name="read-edit-delete-parking-rates"></a>

Parking rate details are displayed by `parking_info()` through its template.

Editing and deleting an specific `rate_id` is managed by respectively:
* `edit_parking()` (path: `parking_management/views.py`)
* `delete_parking()` (path: `parking_management/views.py`)

Validators were setup in each functions views to prevent parking manager deleting parking objects when users are checked-in.


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
@login_required
def delete_rate(request, parking_id, rate_id):
    if not is_parking_manager(request):
        return redirect('home')

    has_user = parking_space_available(request, parking_id=parking_id)
    print(f'has_user = {has_user}')
    # prevents parking manager from deleting parking obj
    # when parking users are checked-in
    if has_user != 0:
        messages.error(request, "You cannot edit rate when users are still checked-in. Contact admin.")
        return redirect('parking-info', parking_id=parking_id)
        
    rate = get_object_or_404(Rate, id=rate_id)
    rate.delete()
    messages.success(request, "Rate deleted.")
    return redirect('parking-info', parking_id=parking_id)
 ```

</p>
</details>



<p align="center">
   <kbd><img width="200" src="static/images/readme_images/ui/parking_info/parking-info-rates.png"></kbd>
</p>

### 3.11 Check-In Parking : Geolocation <a name="check-in"></a>

This section is managed by parking_activity app.

The check-in process starts from the user dashboard.

The function first checks if the user has provided their car registration number. If not, it will prompt the user to do so, before moving any further.

From this point, the check-in process can be divided into 3 phases:

**Phase 1 - Capturing User Geolocation**

If the user profile has a car registration number, the user will be able to access the "Check-In" button. By clicking the button `getLocation()` triggers which will populate 2 hidden inputs. `getLocation()` is a javascript function managed by `geolocation.js` (path: static/js/geolocation.js)


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see parking_info_block.html</summary>
<p>

```python
    <div class="col-12 col-md-4 mt-3 mt-md-0">
        <form action="{% url 'get_parking_location' %}" class="w-100" method="POST">
            {% csrf_token %}
            <input type="hidden" id="userLatitude" name="latitude" value="">
            <input type="hidden" id="userLongitude" name="longitude" value="">
            <button type="submit" class="btn button-1 w-100" onclick="getLocation()">
                <span>Check-In</span>
            </button>
        </form>
    </div>
```

</p>
</details>


These two hidden inputs will capture the user's latitude and longitude.

Once captured, the templates form logic will trigger `get_parking_location()`.

The role of `get_parking_location()` is to look for a matching geolocation between the user, and a potential parking.

In order to do so, `get_parking_location()` collects the values in `user_latitude` and `user_longitude` variables which are fed by the hidden input fields populate by the javascript function.

```python
    if request.method == "POST":
        # capture user current location
        user_latitude = request.POST.get('latitude')
        user_longitude = request.POST.get('longitude')
        print(f'user_latitude = {user_latitude}')
        print(f'user_longitude = {user_longitude}')
```

> [!NOTE]
>Credits -  `getLocation()` is a copy of `HTML Geolocation API` from W3Schools (https://www.w3schools.com/html/html5_geolocation.asp
)

**Phase 2 - Capturing Matching Parking Geolocation**

If these two variables have values against them, the function will then proceed to: 
* set the user location in a tuple
* list all activate parking objects and look for matching geolocation, taking into account their respective radius value, defined in each parking object.

At the end of this process, the logic will either return a `parking_id` or nothing. 

The `parking_id` is then passed as a parameter in `enter()`.

In the event, no parking_id could be returned, `parking_id` is set as None by default in `enter()`.

**views.py:**

```python
    @login_required
    def enter(request, parking_id=None):
        ...
```

**urls.py:**

```python
    path('enter/', views.enter, name='enter'),
    path('enter/<int:parking_id>/', views.enter, name='enter_with_parking_id'),
```

> [!NOTE]
> Credits - HTML Geolocation API: https://www.w3schools.com/html/html5_geolocation.asp

> [!TIP]
> `Uncaught TypeError: Cannot set properties of null (setting 'innerHTML')`. This occurs when the script is loaded at the beginning of the template, before the element exists.
>
> This problem was solved by moving the JS file to the bottom of the `<body>` in the `index.html` template:
>
> ```html
> {% block content %}
>     ...
> {% endblock %}
>
> {% block postloadjs %}
>     <script src="{% static 'js/geolocation.js' %}"></script>
> {% endblock %}
> ```


> [!TIP]
> `TypeError: float() argument must be a string or a real number, not 'set'`: following Igor-S answer on stackoverflow, I encountered this error.
> This is because of the use of `({})`, which in Python define a set, rather than parentheses `()`.
> To fix this error by converting the values into `float`:
> ```python   
>    user_location = (float(user_latitude), float(user_longitude))
>```

> [!TIP]
>`TypeError: '<=' not supported between instances of 'float' and 'str'`: following the above mentioned example provided on stackoverflow.
>This error happened because `parking.radius` is a string and `locations_distance` is a float.
>```python
>    if locations_distance <= parking_radius:
>        print(f'You are in {parking.name}')
>    else:
>        print(f'You are not in {parking.name}')
>```

Set values in the same format:

```python
    parking_radius = float(parking.radius)
```

> [!TIP]
>`TypeError: User geolocation innacuracy: unless a mobile phone is used for testing, the accuracy of the geolocation varies between 3m to 888m. I found that from my laptop a range of 900m was comfortable to capture a nearby geofence.
> For mobile phone, I had 100% success with a radius set at 50 meters.

**Phase 3 - Validating User Consent to Check-In**

This is the last phase of the check-in process and is managed by both a python and javascript functions. Respectively:
* `enter()`
* `fetchRates()`

If a `parking_id` was provided as a parameter, `enter()` will prompt the user to:
* confirm they are happy to check-in at the identified parking. 
* automatically display the applicable rate to said `parking_id`.

As it had to be generated dynamically, taking into account that no `parking_id` parameters could be passed, the task of displaying applicable rates was assigned to `parking_fee.js`.

Through `parking_fee.js`, `fetchRates()` collects dynamically applicables rates from selected parking form the database, by using `get_parking_rates()` (views.py).


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see `get_parking_rates()`</summary>
<p>

```python
    def get_parking_rates(request, parking_id):
        print(f'get_parking_rates parking id = {get_parking_rates}')
        rates = Rate.objects.filter(parking_name_id = parking_id).values(
            'rate_name',
            'hour_range',
            'rate',
        )
        return JsonResponse(list(rates), safe=False)
```

</p>
</details>
    

`get_parking_rates()`is an API that collects Rate model objects relevant to the `parking_id` the user is checking-in from.

These objects are then returned back to `fetchRates()` in json format, before being rendererd in a table through `renderRatesTable()`.

<p align="center">
   <kbd><img width="200" src="static/images/readme_images/ui/check_in/check-in.png"></kbd>
</p>


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see `renderRatesTable()`</summary>
<p>

```python
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
                    <td>£${rate.rate}</td>
                </tr>
                `;
                tbody.appendChild(tableRow);
            });
        }else{
            table.style.display = "none"
        }
    }

```

</p>
</details>
    

> [!TIP]
> The initial code was returning an error. It seems that Json expects a dictionaryy by default. To correct this problem `safe` is set to `False` (`safe = False`), which allows to return a list instead.


**What happens if `parking_id` is None as a parameter?**

As mentioned at the end of the previous Phase, `enter()` can expect a `parking_id` parameter, but this is not mandatory.

This last section covers the possibility that geolocation might fail, or the user simply did not enable it on their phone. 

In this case we still want the user to be able to check-in through a manual step.

If `parking_id` is not provided as a parameter, the user is offered to select the parking they are looking to check-in from through a drop down menu.

This drop down menu is generated in the template:


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see template form</summary>
<p>

```python
    <form method="post">
        {% csrf_token %}
        <div class="enter-form center">
            <label for="parking-select">Select Parking:</label><br>
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
        </div>
        <hr>
        <div class="enter-submit-button center">
            <input class="button-1 btn " type="submit" value="Check-In">
        </div>
    </form>
```

</p>
</details> 

Upon selection by the user the `parking_id` is captured by an event listener, which will return the parking rates against the selected `parking_id`, using `get_parking_rates()` and the process previously mentioned.


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see script</summary>
<p>

```python
    // look for changes if the user has selected a parking manually
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

    }
```

</p>
</details>

**Phase 4 Check-in Form**

This final phase is managed by `enter()` which handles both scenarios of having the `parking_id` provided as a parameter, or provided later on upon manual selection by the user.

**Suggestion for future improvement**: there is one scenario that this project does not cover, is the pssibility of the user being geolocated within an incorrect parking, especially if 2 parking radiuses are overlaping. It would make sense to add a possibility for the user to override the `parking_id` parameter through manual selection.

> [!IMPORTANT]
> The check-in process was by far the most challenging part of the project. A big acknowledgment to Gareth McGirr and Stackoverflow for the help.

> [!NOTE]
> Credits - Gareth Mc Girr (mentor) who guided through this process<br>
> Credits - Stackoverflow: https://dev.to/chryzcode/django-json-response-safe-false-4f9i

### 3.12 Check-Out Parking <a name="check-out"></a>

Similarly to the check-in process, the check-out process starts from index template (index.html).

After checking-in, the user is redirect to `index.html`, with a slight change to the previous screen.

Instead of displaying "Check-In" button, the user is now presented with "Check-out" button instead.

The display management of these two buttons is hanlded in `index()` through var `existing_stay_obj`:
* the variable returns the latest Stay model object created with an empty Leave field.


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    #look up if user has already an existing Stay object
    #and exclude objects that is matched with a LeaveParking object 
    existing_stay_obj = Stay.objects.filter(user=request.user.userprofile).exclude(
        id__in=LeaveParking.objects.values_list('stay_id', flat=True)
    )
```

</p>
</details>

If var `existing_stay_obj` exists, the template will return a button redirecting the user to `leave()` (checkout) with `stay_id` as parameter. 

Otherwise a button leading to `enter()`(check-in) is displayed.

This entire section is managed by `leave()`, which handles the relationships between other functions.

**Phase 1 - User Stay Duration Calculation**

Using the `stay_id` parameter, it creates a LeaveParking objects, child to its Stay model object.


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    # Retrieve the existing Stay object
    try:
        stay = Stay.objects.get(id=stay_id, user=request.user.userprofile)
        print(f'stay id = {stay}')
        # Create a LeaveParking entry
        leave_parking = LeaveParking.objects.create(
            user=request.user.userprofile,
            parking_name=stay.parking_name,
            stay=stay,
        )
```

</p>
</details>

The newly created object also contained a timestamp field, which is automatically populated upon creation.

Following successful creation of the leave object, `leave()` proceeds to collect both timestamp from EnterParking and LeaveParking childs objects to `stay_id`.

The function will then compare both timestamps to extract the user's stay duration in var `total_stay_time_hours`.


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    #retrieve enter timestamp
    enter_time = EnterParking.objects.get(stay=stay_id)
    print(f'enter_time = {enter_time.timestamp_enter}')

    #retrieve leave timestamp
    exit_time = LeaveParking.objects.get(stay=stay_id)
    print(f'exit_time = {exit_time.timestamp_leave}')

    #difference between enter and leave time
    total_stay_time = exit_time.timestamp_leave - enter_time.timestamp_enter
    print(f'total_stay_time = {total_stay_time}')

    # Convert total_stay_time to hours
    total_stay_time_hours = Decimal(total_stay_time.total_seconds()) / Decimal(3600)
    print(f'total_stay_time in hours = {total_stay_time_hours}')
```

</p>
</details>

Var `total_stay_time_hours` is then used to calculte the applicable fee.

```python
    applicable_fee = calculate_user_fee(stay, total_stay_time_hours)
```

**Phase 2 - User Fee calculation**

This phase is managed by `calculate_user_fee()`.

It takes both the `stay` model object and `total_stay_time_hours` as parameters, from `leave()`.

The function starts by rounding up `total_stay_time_hours` to next hour : if a user stayed 1.5 hour, `total_stay_time_hours` will be equal to 2.

Following this steps, the applicable rates to relevant parking objects are identified.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    #look for applicate rate for parking ID and total stay again rate.hour_range
        rate_available = Rate.objects.filter(parking_name=stay.parking_name).order_by('hour_range')
        print(f'rate_available = {rate_available}')
```

</p>
</details>

Once these rates are identified, the functions proceeds to match the appropriate hourly rate to `total_stay_time_hours`, and return the value into variable `closest_rate`.


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    #return applicable fee
    #create variable to attach closest rate to it during loop
    closest_rate = None
    for rate in rate_available:
        print(f'rate_available = Hour range:{rate.hour_range}; Rate:{rate.rate}')
        if total_stay_time_hours <= Decimal(rate.hour_range):
            closest_rate = rate
            break 
    
    #if the user stayed longer than longest rate
    #apply the latest rate on the list
    if closest_rate is None and rate_available.exists():
        closest_rate = rate_available.last()
```

</p>
</details>

Once `closest_rate` is defined, the applicable fee can be calculated and returned to `leave()` under variable: `applicable_fee`.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    if closest_rate:
        print(f'closest rate is {closest_rate}')
        applicable_fee = closest_rate.rate * roundedup_total_stay_time_hours
        print(f'applicable_fee = {applicable_fee}')
        return (applicable_fee)
    else:
        print('Looks like there is a problem!')
        return None
```

</p>
</details>

**Phase 3 - Fee Form**

This phase is handled by `fee_form()` and managed by `leave()`, passing `applicable_fee` and `stay_id` as parameters. 

<details>
<summary style="color: white; background: black; padding: 5px;">Click see to leave() code section redirecting to fee_form()</summary>
<p>

```python
    if applicable_fee:
        print(f'applicable_fee is {applicable_fee}')
        fee_form(request, applicable_fee, stay_id)
        return payment(request,applicable_fee, stay_id)
    else:
        print(f'no applicable fee')
```

</p>
</details>

The role of this function is retrieve the stay object id, and add the calculated fee to it, before redirecting the user back to `leave()` for payment handling.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to fee_form() code</summary>
<p>

```python
    # add Fee value to stay_id
    @login_required     
    def fee_form(request, applicable_fee,stay_id ):
        try:
            stay = Stay.objects.get(id=stay_id)
            stay.calculated_fee = applicable_fee
            stay.save()
            print(f"Stay object {stay_id} updated with calculated_fee: {stay.calculated_fee}")
        except Stay.DoesNotExist:
            print('Stay object does not exist')  
```

</p>
</details>


### 3.13 Stripe Payment Integration <a name="stripe"></a>

**Phase 1 - Payment**

Following succesful completion of `fee_form()`, the user is returned to `leave()` for payment handling.

Payment handling is managed through a Stripe integration, which is detailed below.

The Payment handling process starts from `payment()`, taking `applicable_fee`, `stay_id` as parameters.

The function will start by collecting the `STRIPE_SECRET_KEY_TEST` from .env file, and set `applicable_fee` from pence to pounds. 


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    #set API key the begining to avoid 
    #"Error in payment process:No API key provided."
        stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
        amount_int = int(applicable_fee*100)
```

</p>
</details>

The function looks for existing stripe ID, in the UserProfile model object.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    #check if userprofile already has a stripe id
    # Create a customer if not already created
        if not request.user.userprofile.stripe_customer_id:
            customer = stripe.Customer.create(
                email=request.user.email
            )
            request.user.userprofile.stripe_customer_id = customer.id
            request.user.userprofile.save()
 ```

</p>
</details>

A local variable `price_object` is defined. The role of this variable is to create object in Stripe for future use.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    #create a price object in stripe
        price_object = stripe.Price.create(
            unit_amount=amount_int,
            currency="gbp",
            product_data={
                "name":"Parking Fee"
            }
        )
```

</p>
</details>

Following the successful completion of `fee_form()`, the user is returned to `leave()` for payment handling.

Payment handling is managed through a Stripe integration, detailed below.

The process starts with the `payment()` function, which takes `applicable_fee` and `stay_id` as parameters. This function begins by retrieving the `STRIPE_SECRET_KEY_TEST` from the `.env` file and converting the `applicable_fee` from pounds to pence (as required by Stripe). 

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    # Set API key to avoid "No API key provided" error
    stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    amount_int = int(applicable_fee * 100)  # Convert pounds to pence
```
</p> </details>

The function checks if the user has an existing Stripe customer ID in their profile (UserProfile model). If not, it creates a new customer on Stripe and saves the ID to the user's profile.

<details> <summary style="color: white; background: black; padding: 5px;">Click to see code</summary> <p>

```python
    if not request.user.userprofile.stripe_customer_id:
        customer = stripe.Customer.create(
            email=request.user.email
        )
        request.user.userprofile.stripe_customer_id = customer.id
        request.user.userprofile.save()
```
</p> </details>

A price_object is created to represent the payment amount and currency on Stripe. This object is essential for generating the checkout session.

<details> <summary style="color: white; background: black; padding: 5px;">Click to see code</summary> <p>

```python
    price_object = stripe.Price.create(
        unit_amount=amount_int,  # Amount in pence
        currency="gbp",          # British Pounds
        product_data={
            "name": "Parking Fee"
        }
    )
```
</p> </details>

After creating the price_object, a Stripe checkout session is initialized. The session includes the price details, payment method options, and success or cancellation URLs. Stripe returns the user to these URLs based on payment status.

<details><summary style="color: white; background: black; padding: 5px;">Click to see code</summary> <p>

```python
    checkout_session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': price_object.id,
            'quantity': 1,
        }],
        mode='payment',
        customer=request.user.userprofile.stripe_customer_id,
        success_url=settings.REDIRECT_DOMAIN + 'parking_activity/payment_successful?session_id={CHECKOUT_SESSION_ID}',
        cancel_url=settings.REDIRECT_DOMAIN + 'parking_activity/payment_cancelled',
    )
```
</p> </details>

Finally, the stay_id model object is updated with the Stripe checkout session ID for tracking, and the user is redirected to the Stripe-hosted checkout page.

<details> <summary style="color: white; background: black; padding: 5px;">Click to see code</summary> <p>

```python
    stay = Stay.objects.get(id=stay_id)
    stay.stripe_checkout_id = checkout_session.id
    stay.save()

    return redirect(checkout_session.url)
```
</p> </details>


**Phase 2 - Payment Confirmation (Stripe Webhook)**

Following successful payment, the user recieves an email confirmation.

This process is managed by `stripe_webhook()`.

After successful payment, Stripe will send a query back to the server and starts with a few validation.


<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    @csrf_exempt
    def stripe_webhook(request):

        print("enter webhook")
        stripe.api_key = settings.STRIPE_SECRET_KEY_TEST
    
        payload = request.body
        signature_header = request.META.get('HTTP_STRIPE_SIGNATURE')
        webhook_secret = settings.STRIPE_WEBHOOK_SECRET_TEST
        event = None
        try:
            event = stripe.Webhook.construct_event(
                payload, signature_header, webhook_secret
            )
        except ValueError as e:
            print(f"Invalid payload: {str(e)}")  # Log the error for debugging
            return HttpResponse(status=400)
        except stripe.error.SignatureVerificationError as e:
            print(f"Signature verification failed: {str(e)}")  # Log the error for debugging
            return HttpResponse(status=400)
        ...
```

</p>
</details>


Following successful validation, Stripe will look to push payment confirmation to the server, updating the `stay_id` object from False to True.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    # retrieve user payment record
    stay = Stay.objects.get(stripe_checkout_id=session_id)
    line_items = stripe.checkout.Session.list_line_items(session_id,limit=1)
    stay.paid = True
    stay.save()
```

</p>
</details>



Successful confirmation will eventually trigger an payment confirmation email being sent to the user.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code</summary>
<p>

```python
    subject = "Payment Confirmation"
                context = {
                    'username': stay.user.user.username,
                    'stripe_checkout_id': stay.stripe_checkout_id,
                    'transaction_id': stay.id,
                    'amount_paid': stay.calculated_fee,
                    'parking_name': stay.parking_name.name,
                }

                # prepare email
                message = render_to_string('email/payment_confirmation_email.html', context)
                email_reciever = stay.user.user.email

                # send email
                try:
                    send_mail(
                        subject,
                        message,
                        settings.DEFAULT_FROM_EMAIL,
                        [email_reciever],
                        html_message=message,
                        fail_silently=False,
                    )
                    logger.info('Email sent successfully')
                except Exception as e:
                    logger.error('Error sending email: %s', str(e))
                print('email is sent')
 ```

</p>
</details>

<p align="center">
   <kbd><img width="200" src="static/images/readme_images/ui/payment_confirmation_email/payment-confirmation-email.png"></kbd>
</p>


> [!TIP]
>`TypeError: stripe_webhook not found`. As the webhook view in not included in my main app, the console logs were showing a failed attempt at retrieving `stripe_webhook` path. The issue was solved by adding the name to the webhook path in the Stripe platform: `https://[domain-name]/parking_activity/stripe_webhook/`. 

> [!NOTE]
> Overall Stripe Integration: The tutorial provided by the course material wasnt adapted to what I was looking for. Instead I followed the tutorial from this video (https://www.youtube.com/watch?v=hZYWtK2k1P8&t=1s) and made a number of changes to suit the project.<br>
> `stripe_webhook not found`: The solution was brough to me by RyanM on Stackoverflow after I posted my question: https://stackoverflow.com/questions/79256457/django-stripe-webhook-not-found/79256537#79256537 <br>


### 3.14 Crispy Forms <a name="cripsy"></a>

To improve the layout of the forms, the project includes the use of crispy forms.

**Implementation steps**:
* Run `pip install django-crispy-forms`
* Run `pip install crispy-bootstrap5`


* In Installed_apps (**Settings.py**) add:

    ```python
    INSTALLED_APPS = [
        'django.contrib.admin',
        ...
        #crispy form packages
        'crispy_forms',
        'crispy_bootstrap5',

    ]
    ```
* In Settings.py, add:

```python
    CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

* add to template:

```html
    {% load crispy_forms_tags %}
```

* add to form fields:

```html
    {{ variable|as_crispy_field }}
```

> [!NOTE]
> Credits - Documentation: https://django-crispy-forms.readthedocs.io/en/latest/


### 3.15 Decorators <a name="decorators"></a>

The project makes a thorough of of the login_required decorator.

It allows to force a user to be authenticated before accessing a specific function and related template.

With the exception of login and register templates, all other function have a decorator.

```python
    from django.contrib.auth.decorators import login_required

        @login_required
        def index(request):
        ...
```

Other decorators in use: 
* `@csrf_exempt` - to remove the need for CSRF token in Stripe callback
* `@require_POST` - restricts a view to only accept POST methods 

> [!NOTE]
> Credits - Documentation: https://docs.djangoproject.com/en/5.1/topics/http/decorators/


### 3.16 Custom Error Handlers <a name="error-handler"></a>

The project implements custom error handlers, allowing to gracefully handle potential error communicated by the browser to the user.

Custom templates list:
* 404 error
* 500 error
* 403 error
* 400 error

Templates are located in: `user_management\templates\errors`

![rendering](static/images/readme_images/ui/custom_error_handler/404-custom-error-handler.png)

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code for urls.py (project level)</summary>
<p>

```python
    from django.conf.urls import handler404, handler500, handler403, handler400

    urlpatterns = [....
    ] 

    handler404 = 'user_management.views.handler404'
    handler500 = 'user_management.views.handler500'
    handler403 = 'user_management.views.handler403'
    handler400 = 'user_management.views.handler400'
 ```

</p>
</details>

<details>  
<summary style="color: white; background: black; padding: 5px;">Click to see code for views.py (app level)</summary>
<p>

```python
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
  ```

</p>
</details>

### 3.17 Parking Inspector <a name="parking-inspector"></a>

This feature is mostly managed through `parking_inspector()` and allows the parking manager to see the state of their parkings and check if all vehicles in the parking have check-in the app.

For those that are not checked-in, the parking manager has an option to record the registration plate of the illegally parked car.

The list can then be used to send Parking Charge Notices from a different system.

Currently the parking manager can:
* See checked-in cars
* Add illegally parked cars
* Delete illegally parked cars (`delete_car_reg()`)


![rendering](static/images/readme_images/ui/parking_inspector/parking-inspector.png)

**Future improvements:**

* This feature could benefit from immediate improvement such as the possibility to take a picture of the car and upload on the S3 Bucket for proof. This feature is not implemented yet.
* Another feature could be to accelerate the detection of illegally parked cars by integration Optical Character Recognition (Optical Character Recognition). This feature could be implemented by using django progressive web app extension. This would allow the parking manager to simply scan each car registration and let the GeoPay look in the database if the parked as checked-in. 

### 3.17 Back Button <a name="back-button"></a>

The project includes a back button, in `base.html`.

This back button has two features:
* It redirects the user back to the previous page using the user history :`onClick="javascript:history.go(-1)`
* It is hidden on index and parking_manager_dashboard pages using `request.path`
* It also redirects to a different page on certain cases when the previous page is likely to be a form.

<details>
<summary style="color: white; background: black; padding: 5px;">Click to see code details</summary>
<p>

```python
    {% block base_navigation_block %}
        <div class="navigation">
        <!-- If user is on user account, redirects home -->
        {% if request.resolver_match.url_name == 'user-account' %}
            <a href="{% url 'home' %}">
                <i class="fa fa-arrow-left" aria-hidden="true"></i> Back
            </a> 
        <!-- Back buttons is index after succesful payment -->
        {% elif request.resolver_match.url_name == 'payment-successful'%}
            <a href="{% url 'home' %}">
                <i class="fa fa-arrow-left" aria-hidden="true"></i> Back
            </a> 
        {% elif request.resolver_match.url_name == 'payment-cancelled' %}
            <a href="{% url 'home' %}">
                <i class="fa fa-arrow-left" aria-hidden="true"></i> Back
            </a> 
        {% elif request.resolver_match.url_name == 'parking-info' %}
            <a href="{% url 'home' %}">
                <i class="fa fa-arrow-left" aria-hidden="true"></i> Back
            </a> 
        <!-- not the above options and not listed in path below: redict to previous page -->
        {% elif request.path != '/' and request.path != '/parking_management/parking_manager_dashboard/' %}
            <a onClick="javascript:history.go(-1)">
                <i class="fa fa-arrow-left" aria-hidden="true"></i> Back
            </a> 
        {% endif %}
        </div>
    {% endblock %}
```

</p>
</details>

The credits for this feature goe to the links listed below.

> [!NOTE]
> Credits - Back button - https://stackoverflow.com/questions/524992/how-to-implement-a-back-link-on-django-templates<br>
> Credits - Excluding pages from button display - https://stackoverflow.com/questions/41129551/django-creating-an-if-statement-based-on-the-request-path-not-working<br>
> Credits -  `request.resolver_match` : https://medium.com/@iamalisaleh/how-to-get-the-current-url-within-a-django-template-8270b977f280<br>

Suggestion for improvement: The code could improve by streamlining the series of `elif` statement into a single `if`. For some reason the below code was generating an error.

```html
    {% if request.resolver_match.url_name == 'user-account' or 
        request.resolver_match.url_name == 'payment-successful' or 
        request.resolver_match.url_name == 'payment-cancelled' or 
        request.resolver_match.url_name == 'parking-info' %}
        <a href="{% url 'home' %}">
            <i class="fa fa-arrow-left" aria-hidden="true"></i> Back
        </a>
    {% else %}
    ...
    {%endif%}
```

## 4. Technologies <a name="tech"></a>

* Django & Python are used for both backend and frontend.
* HTML : for front endrendering.
* CSS : for front endrendering.
* Bootstrap : for front endrendering.
* JavaScript : for both backend and frontend.
* PostgreSQL : for data storing.
* VSCode :  used to write and edit code.
* Git : used for version control.
* GitHub : used to host version controls online.
* Heroku : used to host PostGres database online.
* WhiteNoise : used for serving static files with Heroku.
* AWS S3 Bucket used for online media file storage.
* Stripe used payment processing.
* Gmail API used for sending emails in my application.
* Pixso used for wireframes.
* Midjourney used for logo generation.
* ICO Converter was used to compress images and convert them into .webp.
* Chrome Developer Tools used to debug, test responsiveness, and generate Lighthouse reports.
* Google Fonts was used to import fonts for the site.
* Font Awesome was used for all the site icons.
* W3C HTML Validator was used to validate the HTML code.
* W3C CSS Validator was used to validate the CSS code.
* JSHint was used to detect errors and potential problems in JavaScript code.
* Notion : for generation of tables in md format

## 5. Testing <a name="testing"></a>
### 5.1 Validator Testing <a name="val-testing"></a>
#### 5.1.1 HTML <a name="html"></a>

Click on this link to see results of JSHint tool: [Python Testing Guide](html_testing.md)

#### 5.1.3 Javascript <a name="js"></a>

Click on this link to see results of JSHint tool: [Python Testing Guide](javascript_testing.md)


#### 5.1.3 Python <a name="py"></a>

Click on this link to see results of CI Python Linter tool: [Python Testing Guide](python_testing.md)


### 5.2 Lighthouse Testing <a name="lighthouse-testing"></a>

Click on this link to see results of Lighthouse tool: [Manual Testing Guide](lighthouse_testing.md)

### 5.3 User Testing <a name="user-testing"></a>

Click on this link to see user testing steps: [Manual Testing Guide](user_testing.md)

## 6. Bugs <a name="bugs"></a>

### 6.1 Current bugs <a name="current-bugs"></a>

This sections lists errors found in the final version:
* Back Button - the logic in back button to look into history to find the previous page does not work in following scenario: user tries to reach a specific page -> user is redirected to login -> upon succesful login the user is redirect to initial page : in this case the back button will revert back to initial page.

> [!TIP]
> There might be a solution, by creating an additional exception, saying that if the history does not have have a previous page, return user to home page.

* Back button does not work after using lighthouse testing. I suspect this has something to do with the impact Lighthouse has on history. In this case the user is redirected to a blank url. To repeat the error: go to `parking-info` page, launch lighthouse -> click back button

* In development after payment is made, the user is logged out and needs to log back it to reach success page. I did not manage to reproduce the error in production. I dont think this error would affect the user experience in production, as the wehbook would still be sent by Stripe marking the the transaction as `paid = true` in the Stay model object.

* The logo image on email does not show on certain messaging system. For example, it will not be displayed on outlook for desktop desktop, but will show on outloop mobile app.

* The javascript validator in register.html are capital sensitive. It will show a warning that two email addresses do not match if one email has a capital and the other does not, but the authentictaion system will accept it.


### 6.2 Design & User Experience improvements <a name="design-improvements"></a>

* The History page could be imporved by adding filters, to allow the user to retrieve specific transaction easily
* `parking-info` template could display a live map of the parking's geolocation, for visual validation. This would ensure the parking manager enters the correct coordinates. This could be done with either google maps, or Leaflet/Folium.
* I do not like the way parking rates are presented. Leaving the parking manager the possibility to enter a parking rate title, opens too many potential misunderstandings between the parking company and their customers. I think removing the use of "parking_title" and display parking rate under a specific format could make more sense: [value] hour for [value] instead of letting parking manager give it a title
* `parking-info` could be improved in the way status information could be displayed. Too much space is taken for the first 3 sections, and all could fit into a single line header with the a second row for values.
* `parking-info` could be improved in the way rates are displayed with a simple bootstrap row, with columns folding back into 2 rows for small screens. I realised too close to project submission.
* There is only one parking manager per parking. It would make sense to change the foreign key field to a M2M field to have several managers looking after the same parking.

### 6.3 Logic improvements & Backend <a name="logic-improvements"></a>

* The process of pushing migration to heroku could be automated when pushing commits to git
* The process of collecting static could be automated when pushing commits to git
* On mobile phone, users seems to get logged out if they open another window, or after a few minutes of innactivity. This does not happen on laptops. This affects the user experience, as they need to log back in everytime they want to access the app. A few posts on Stack Overflow seem to indicate this might be due to how sessions are handled, but I could not find a solution to it. This could also be due to the SSL certicate, as it is not implemented, as this is paying feature on heroku.
* The Back buttons without `<p>` not showing a hand cursor, which confuses the user whether the element is clickable or not.
* Additional business logic could be implemented on the parking manager side reporting on money made through GeoPay
* Additional features on the user side coudl also be implemented, such a loyalty and subscription to reduce prices.
* Some repeats in codes in particular with validators preventing parking user and parking manager taking some actions on checked-in parkings. A solution would be to create a global function that could be applied to all functions that need it.
* A validator could be added to check if all parking spaces are checked-in to prevent user to do so.
* Implementing a Progressive WebApp (PWA) to implement OCR allowing the packing manager to scan car registartion to confirm whether the car registration is registered, or added to the illegally parked cars model.
* There is redundancy in some of the FK, but equally adds more visibility from admin panel:
```python
class EnterParking(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.SET_NULL, null=True, blank=True)
    parking_name = models.ForeignKey(Parking, on_delete=models.SET_NULL, null=True, blank=True)
    stay = models.ForeignKey(Stay, on_delete=models.SET_NULL, null=True, blank=True)
    timestamp_enter = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"{self.id}"
```

## 7. Deployment <a name="deployment"></a>

### 7.1 Local Deployment <a name="local-deployment"></a>
**Project Deployment - Local**

**Project Creation**: The project starts by creating a folder from VS Code name M4Project.

Once the folder is created, click on folder to start from sratch.

**Local Deployment**: To copy this project, you can use git clone from your terminal.

Go to the terminal and input: git clone https://github.com/PhilMele/M4Project.git in the directory you wish to have the project folder in.

Using your code editor, such as VS Code: 
* click on open folder 
* click on the newly created folder.

**Database Deployment - PostGres**
To install PostGres on local, the following steps were followed.

To set up of PostGres on Local run : `pip install psycopg2` 

Issues encountered and solution:

This may have been specific to my local setup, but I had to use : pip install psycopg2-binary 

(Documentation: https://pypi.org/project/psycopg2-binary/). My requirements.txt file lists : psycopg2-binary==2.9.9

In settings.py, edit `DATABASES` variables to the following to point to the new local postgres database:
```python
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
```

> [!IMPORTANT] 
> You will need to run your migration again (`python manage.py migrate`) and recreate a new superuser. All data will be lost.

Once this is done, you will want your data stored in a your .env file, to avoid secret keys being publicly available when pushing the project to github and adapting the variables to their environement (local, staging, production...). To do this, do the following:
* enter `pip install python-decouple`
* modify your settings.py to look like this:

```python
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
```

* Add values to variables to .env file. Note these dont need to be in string format, as they are considered strings by default. For this project, values need to attached to the following variables:

```python
    # stripe
    STRIPE_PUBLIC_KEY_TEST = 'value'
    STRIPE_SECRET_KEY_TEST ='value'
    STRIPE_WEBHOOK_SECRET_TEST = 'value'
    # local and heroku
    DATABASE_URL= 'value'
    DJANGO_SECRET_KEY = 'value'
    # for gmail
    EMAIL_HOST_USER = 'value'
    EMAIL_HOST_PASSWORD = 'value'
```

> [!NOTE]
> Credits - Instal postgres on local: https://www.postgresql.org/download/<br>
> Credits - Extra Documentation: https://pypi.org/project/psycopg2-binary/<br>

### 5.1 Heroku Deployment <a name="heroku-deployment"></a>

**Heroku Deployment**

In order to setup django for deployment on Heroku, the following steps were followed:

* Log into heroku : `heroku login`
* Add heroku remote : `git remote add heroku [Heroku Git URL]` (can be found in Heroku Settings)
* Push code to Heroku: `git push heroku master`
* Run first migration: `heroku run python manage.py migrate`

**Problem encountered**: the Procfile generated with command line from documentation echo web: gunicorn app:app > Procfile created an issue relating to encoding. The encoding defaulted to UTF-16 instead of UTF-8.

To solve this problem: create a new Procfile through a Notepad, selected encoding UTF-8 and called it Procfile.txt in the same location as the actual Procfile. I then deleted the previous Procfile and renamed Procfile.txt to Procfile.

> [!NOTE]
> Credits - Procfile encoding solution: https://stackoverflow.com/questions/19846342/unable-to-parse-procfile<br>


**Setup production environement**

In your settings.py add:

```python
    DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
```

In your Heroku Variable add `DJANGO_DEBUG` as `False`.

By default, if this is not specified, the server will consider as a development environement.

Add whitenoise in settings.py to middleware list
```python 
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

> [!TIP]
> `MIME type ('text/html') is not a supported stylesheet MIME type, and strict MIME checking is enabled.`. Adding whitenoise corrected the error. See below for process to adding whitenoise.

> [!TIP]
> If the `.css` file is not loading in production, move `'whitenoise.middleware.WhiteNoiseMiddleware'` to the top.
> 
> ```python
> MIDDLEWARE = [
>     'django.middleware.security.SecurityMiddleware',
>     # Whitenoise package: used for production, should be set at the top
>     'whitenoise.middleware.WhiteNoiseMiddleware',
> ]
> ```

> [!IMPORTANT] 
> Everytime the static folder is changed, in particular for css, `python manage.py collectstatic` needs to be run from the console to push the changes to staticfiles.

> [!NOTE]
> Credits - https://stackoverflow.com/questions/19846342/unable-to-parse-procfile<br>
> Credits - https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment<br>


## 8. Credits <a name="credits"></a>

* `getLocation()` is a copy of `HTML Geolocation API` from W3Schools (https://www.w3schools.com/html/html5_geolocation.asp
)
* Stackoverflow: https://dev.to/chryzcode/django-json-response-safe-false-4f9i
* Overall Stripe Integration Youtube tutorial: The tutorial provided by the course material wasnt adapted to what I was looking for. Instead I followed the tutorial from this video (https://www.youtube.com/watch?v=hZYWtK2k1P8&t=1s) and made a number of changes to suit my project.
* RyanM on Stackoverflow for this answer: https://stackoverflow.com/questions/79256457/django-stripe-webhook-not-found/79256537#79256537 
* Crispy Form Documentation: https://django-crispy-forms.readthedocs.io/en/latest/
* Django Documentation: https://docs.djangoproject.com/en/5.1/topics/http/decorators/
* Gareth Mc Girr (mentor) who guided through this process
* Procfile encoding: https://stackoverflow.com/questions/19846342/unable-to-parse-procfile
* Django Deployment: https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Deployment
* Regex Synthax: https://stackoverflow.com/questions/3518504/regular-expression-for-matching-latitude-longitude-coordinates
* Back button - https://stackoverflow.com/questions/524992/how-to-implement-a-back-link-on-django-templates
* Excluding pages from button display - https://stackoverflow.com/questions/41129551/django-creating-an-if-statement-based-on-the-request-path-not-working
* `request.resolver_match` : https://medium.com/@iamalisaleh/how-to-get-the-current-url-within-a-django-template-8270b977f280

**In additon**, there is a large number of stackoverflow, reddits and github posts that I should credit but didnt take note of them as I was trying out different solutions.
