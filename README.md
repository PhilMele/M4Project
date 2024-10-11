

Django setup on local:
* Create `M4Project`
* Open to `M4Project` folder from terminal
* Create a virtual environment: in terminal enter the following command: `python -m venv env`.
* Activate the virtual environment: `venv/scripts/activate`
* Install Django : `pip install django`.
* Create a new Django project: `django-admin startproject M4Project`
* Run the development server: `python manage.py runserver`

GIt ignore setup credits: https://djangowaves.com/tips-tricks/gitignore-for-a-django-project/

#Stripe
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


Problem encountered: the Procfile generated with command line from documentation echo web: gunicorn app:app > Procfile created an issue relating to encoding. The encoding defaulted to UTF-16 instead of UTF-8.

To solve this problem: create a new Procfile through a Notepad, selected encoding UTF-8 and called it Procfile.txt in the same location as the actual Procfile. I then deleted the previous Procfile and renamed Procfile.txt to Procfile.

Useful Link:

Credits: https://stackoverflow.com/questions/19846342/unable-to-parse-procfile