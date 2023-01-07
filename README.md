![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# PP4 - Blog Project - Full Stack Python + Django Framework

![am i responsive](readme_images/am-i-responsive.gif)

[Live site here](https://jg-coding-spot.herokuapp.com/)

## About

Blog Project is a web app with a home page and a navigation bar,
with a registration and login system using Django's built-in authentication views,
Registerd users are allowed to send emails to the site's owner using Django's built-in email functionality and the smtplib library.
It has implemented a database model for posts that includes fields like title, content, author, and date.
It has a form for creating and editing posts that allows users to submit their own posts or update their own posts.
It is implemented a view and template for displaying a list of all posts, with each post linking to a detail page for that post.
On the detail page for each post, display the post's content and allow users to add comments and post's likes.
Registered users are also allowed to delete or update their own posts, but not the posts of other users.

## User Experience (UX)

### Colours

- <details>
  <summary>Complementary colours palette</summary>

   Blue was chosen as the main colour to use throughout the project because it will transmit calm, reliability and trust. Orange is used as the main accent colour transmiting  energy and vitality. Green is the other accent colour meaning cleanliness and luck.

  ![complementary color palette](readme_images/complementary_color_palette.jpeg)

</details>

- <details>
  <summary>Typography colour palette</summary>

  Typography is based on the main theme colour, mix with black and with progressive decresed opacity.

  ![typography color](readme_images/typography_color_palette.jpeg)

</details>

### Typography

- <details>
  <summary>Montserrat Alternates font</summary>

  - The main font used for this project is [Montserrat alternates](https://fonts.google.com/specimen/Montserrat+Alternates). The old posters and signs in the traditional Montserrat neighborhood of Buenos Aires inspired Julieta Ulanovsky to create this font in 2010. It is a sans serif font with excellent readability.

    ![montserrat alternates](readme_images/montserrat-alternates.png)

  </details>

- <details>
  <summary>Lato font</summary>

  - For headings the font used is [Lato](https://fonts.google.com/specimen/Lato) (“Lato” means “Summer” in Polish). It is a sans serif font by Warsaw-based designer Łukasz Dziedzic.

    ![lato font](readme_images/lato-font.png)

</details>

### Wireframes

- <details>
  <summary>Blog homepage</summary>

  - ![blog index](readme_images/balsamic-blog-index.png)
  - ![blog index mobile](readme_images/balsamic-mobile-blog-index.png)

</details>

- <details>
  <summary>Blog post list page</summary>

  - ![blog posts](readme_images/balsamic-posts.png)
  - ![blog posts](readme_images/balsamic-mobile-posts.png)

</details>

- <details>
  <summary>Blog post detail page</summary>

  - ![blog post detail](readme_images/balsamic-post-detail.png)
  - ![blog mobile post detail](readme_images/balsamic-mobile-post-detail.png)

</details>

- <details>
  <summary>Blog posts management page</summary>

  - ![blog posts management](readme_images/balsamic-posts-management.png)

</details>

- <details>
  <summary>Blog user profile page</summary>

  - ![blog user profile](readme_images/balsamic-user-profile.png)

</details>

- <details>
  <summary>Blog Sign In form</summary>

  - ![blog Sign In form](readme_images/balsamic-sign-in.png)

</details>

- <details>
  <summary>Blog Sign Up form</summary>

  - ![blog Sign Up form](readme_images/balsamic-sign-up.png)

</details>

### Project Diagram

- <details>
  <summary>Project Diagram</summary>

  - ![Project Diagram](readme_images/Blog-diagram.png)

</details>

### Database relationships diagram

- <details>
  <summary>Post relationship</summary>

  - ![Post relationship](readme_images/post-relationships.png)

  </details>

- <details>
  <summary>Comment relationship</summary>

  - ![Comment relationship](readme_images/comment-relationships.png)

  </details>

- <details>
  <summary>Category relationship</summary>

  - ![Category relationship](readme_images/category-relationships.png)

  </details>

- <details>
  <summary>User Profile relationship</summary>

  - ![User Profile relationship](readme_images/user-profile-relationships.png)

  </details>
  
## Epics and User Stories

### Epics

- <details>
  <summary>Manage Posts</summary>

  - [US #10](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/10)
    - Create a post: As a `Site User / Admin` given that `I am registered` I want be able to `create a post` so that `I can add content to the blog`
  - [US #1](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/1)
    - View post list: As a `Site User` I want be able to `view a list of posts` so that `I can select one to read`
  - [US #2](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/2)
    - Open a post: As a `Site User` I want be able to `click on a post` so that `I can read the full text`
  - [US #12](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/12)
    - Update and Delete a post: As a `Site User / Admin` I want be able to `update a post I created` so that `I can make changes or delete a post`
  - [US #11](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/11)
    - Create drafts: As a `Site User / Admin` I want be able to `create draft posts` so that `I can finish writing the content later`
  - [US #14](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/14)
    - View likes: As a `Site User / Admin` I want be able to `view the number of likes on each post` so that `I can see which is the most popular or viral`
  - [US #13](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/13)
    - Like / Unlike: As a `Site User` I want be able to `like or unlike a post` so that `I can interact with the content`
  - [US #32](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/32)
    - Add picture to post: As as `Site User` I want be able to `upload a picture` so that `I can add a visual representation of my post`
  - Vote posts: As a `Site User` I want be able to `up/downvote a post` so that `I can interact with the content`
  - [US #33](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/33)
    - Custom error pages: As a `Site Admin/ User` I want be able to `have custom error pages with a return button` so that `I can return to the homepage if an error occurred`
  - [US #34](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/34)
    - As a `Site User` I want be able to `send emails` so that `I can ask questions and make suggestions`
  - [US #35](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/35)
    - As a `User / Admin` I want to be able to `Search for post` so that `I can find what I am looking for`

</details>

- <details>
    <summary>Manage Comments</summary>

  - [US #4](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/4)
    - Comment on a post: As a `Site User` I want be able to `leave comments on a post` so that `I can be involved in the conversation`
  - [US #3](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/3)
    - View comments: As a `Site User / Admin` I want be able to `view comments on an individual post` so that `I can read the conversation`
  - [US #16](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/16)
    - Approve comments: As a `Site Admin` I want be able to `approve or disapprove comments` so that `I can filter out objectionable comments`
  - Update a comment: As a `Site User` I want be able to `update a comment I made` so that `I can make changes or delete a comment`
  - Profile picture to comments: As a `Site User` I want be able to `upload a profile picture` so that `I can see it  when I comment on a post`

</details>

- <details>
  <summary>Account Registration</summary>

  - [US #6](https://github.com/JoseMGuerra/ci-pp4-django-fsf/issues/6)
    - Account registration: As a `Site User` I want be able to `register an account` so that `I can create, comment and like`
  - Social account sign in : As a `Site User` I want be able to `Sign In with my social account` so that `Sign In quicker`

</details>

## Technologies

- <details>
    <summary>Languages</summary>

  - HTML5
  - CSS3
  - JavaScript
  - Python

</details>

- <details>
    <summary>Frameworks and Libraries</summary>

  - [Django:](https://www.djangoproject.com/) Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.
  - [Bootstrap:](https://getbootstrap.com/) The world’s most popular framework for building responsive, mobile-first sites.
  - [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html) Integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication
  - [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) Crispy Forms let you control the rendering behavior of your Django forms in a very elegant and DRY way.
  - [psycopg2:](https://pypi.org/project/psycopg2/) Psycopg is the most popular PostgreSQL database adapter for the Python programming language.
  - [dj_database_url:](https://pypi.org/project/dj-database-url/) This simple Django utility allows you to utilize the [12factor](https://www.12factor.net/backing-services) inspired DATABASE_URL environment variable to configure your Django application..
  - [Gunicorn:](https://gunicorn.org/) Green Unicorn, used as the Web Server to run Django on Heroku.
  - [Cloudinary:](https://cloudinary.com/) Used to store all blog images and uploaded images.
  - [Summernote:](https://github.com/summernote/django-summernote) To provide a WYSIWYG editor for customizing new blog content and add images.
  - [Pillow:](https://pillow.readthedocs.io/en/stable/) The Python Imaging Library adds image processing capabilities to your Python interpreter.
  - [Coverage:](https://coverage.readthedocs.io/en/latest/index.html) Used for measuring code coverage of Python test files. -->
  - [Jest:](https://jestjs.io/) A delightful JavaScript Testing Framework, used for automated tests.

</details>

- <details>
    <summary>Software and Web Applications</summary>

  - [Am I Responsive:](http://ami.responsivedesign.is) Checking the responsiveness.
  - [Code Beautify:](https://codebeautify.org/) Used to beautify html code.
  - [Balsamiq:](https://balsamiq.com/) Used to create the wireframes.
  - [Chrome DevTools:](https://developer.chrome.com/docs/devtools/) Used to test the response on different screen sizes, debugging and to generate a Lighthouse report to analyze page load.
  - [Font Awesome:](https://fontawesome.com/) Used throughout the site to add icons for aesthetic and UX purposes.
  - [Git:](https://git-scm.com/) Git open source software for distributed version control.
  - [GitHub:](https://github.com/) Internet hosting service for software development and version control using Git.
  - [Google Fonts:](https://fonts.google.com/) Used to import fonts family [Montserrat](https://fonts.google.com/specimen/Montserrat+Alternates) which is used as main font throughout the site and [Lato](https://fonts.google.com/specimen/Lato) font used for headings.
  - [Heroku:](https://www.heroku.com/) For deployment and hosting of the application.
  - [Elephant PostgreSQL:](https://www.elephantsql.com/) The database used for this application.
  - [HTML Validator:](https://validator.w3.org/) Check your code for HTML validation.
  - [JSHint:](https://jshint.com/) Check code for JavaScript validation.
  - [CI Python Linter](https://pep8ci.herokuapp.com/) Check code for python pep8 validation.
  - [Tiny PNG:](https://tinypng.com/) Compressing images to smaller sizes.
  - [Unsplash:](https://unsplash.com/photos/NtkCemIfaiU) Stock images.
  - [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/) Check your code for CSS validation.
  - [Gauger:](https://gauger.io/fonticon/) Used to create the favicon Logo, create beautiful favicon with ease.
  - [Lucidchart:](https://www.lucidchart.com/pages/) Used to create the site map.
  - [Contrast Checker](https://webaim.org/resources/contrastchecker/) Tool to check the contrast ratio.

</details>

## Testing

- [Testing](TESTING.md)

### Running automated tests

- <details>
    <summary>JavaScript automated tests</summary>

  - The automated javascript test can be executed using Jest as follows:

  - If Jest is not installed then run the command:

          npm install --save-dev jest

  - Jest-environment-jsdom is used as testing environment for Jest allowing to test code that interacts with the DOM using a virtual DOM powered by jsdom.
  - Jest-environment-jsdom, need to be it installed in your project. This can be done using npm by running the following command:

          npm install --save-dev jest-environment-jsdom

  - Run the js test file using the command :

          npm test

</details>

- <details>
    <summary>Unit test automated tests</summary>

  - The automated django/python tests are executed using unittest.
  - Test run using sqlite3 as Db, set DEBUG  to `True` before running tests.
  - Run the python tests using the command:

          python3 manage.py test

</details>

- <details>
    <summary>Coverage automated tests</summary>

  - Test coverage for the django/python tests can be reviewed using the coverage tool:

  - If coverage is not installed then run the command:

            pip3 install coverage
  - Test run using sqlite3 as Db, set DEBUG  to `True` before running tests.
  - Run the following series of commands to determine test coverage:

          coverage run --source=blog manage.py test
          coverage report
          coverage html
          python3 -m http.server 
          (coverage results can be viewed in the browser in the htmlcov directory)

  - To exclude certain files or directories from running or from the coverage report, you can use the --omit option in the coverage command:

        coverage run --omit="myapp/migrations/*" manage.py test

  - Alternatively create a .coveragerc folder and add the following:

        [run]
        omit=
            *staticfiles*
            *migrations*
            *env*
            *manage.py*
            *settings.py*

        [report]
        omit =
            *staticfiles*
            *migrations*
            *env*
            *manage.py*
            *settings.py*

</details>

## Deployment to Heroku

- <details>
    <summary>Process</summary>

  - On Heroku create an account and log in.
  - Click `new` and `create new app`.
  - Choose a unique name for your app, select region and click on `Create App`
  - Create an account and set up a database with [Elephantsql](https://www.elephantsql.com/docs/index.html)
  - Under the `Settings` click `Reveal Config Vars` and set IP to 0.0.0.0 and the PORT to 8000
  - In the terminal if you haven't do so:
    - Pip install dependencies.
    - Create `requirements.txt` ($ pip3 freeze --local > requirements.txt)
    - Create a `Procfile` (`$ echo web: gunicorn <app_name>.wsgi > Procfile`)
    - Create an evn.py file and add all your environment variables.
    - Create a .gitignore file and add your env.py files
  - In the Heroku app dashboard, under `Settings` click on `Reveal Config Vars`:
    - Set "DATABASE_URL", CLOUDINARY_URL", "HEROKU_HOSTNAME" and "SECRET_KEY"
  - Back in Gitpod push you changes to Github.
  - In Heroku `Deploy` Tab, the `deployment method` select Github,
    scroll down to Manual deploy and deploy branch.
  - Once the build is complete, go back to Heroku and click on `Open App`

</details>

## Set up ElephantSQL as Database for this application

- <details>
    <summary>Process</summary>

  - Go to the ElephantSQL website (https://www.elephantsql.com/) and create an account.

  - After creating an account, you will be able to create a new PostgreSQL database. Choose the plan that best fits your needs and click "Create new instance".

  - Give your database a name and select a region. You can also choose a database version if you have a specific version in mind.

  - Once the database is created, you will see the database details page. Here, you can find the connection details for your database, including the hostname, port, database name, and username.

  - To connect to the database, you will need a PostgreSQL client. There are many different clients available, such as pgAdmin and psql. Choose a client and follow the instructions to connect to your database using the connection details provided.

  - Once you are connected to the database, you can start creating tables and inserting data. You can also use SQL commands to manage and query the data in your database.

</details>

## Set Up Cloudinary to host images used by the application

- <details>
    <summary>Process</summary>

  - Sign up for a Cloudinary account at https://cloudinary.com/users/register/free.

  - After you have signed up, you will be taken to the dashboard. In the dashboard, click on the "Settings" tab and then click on the "Security" tab.

  - In the "Security" tab, you will see your "Cloud Name", "API Key", and "API Secret". These will be needed later to authenticate your Django application with Cloudinary.

  - Install the Cloudinary Python library by running the following command:

        pip install cloudinary

  - Add the following code to your Django settings file to configure the Cloudinary library with your account credentials:

        CLOUDINARY_CLOUD_NAME = "your_cloud_name"
        CLOUDINARY_API_KEY = "your_api_key"
        CLOUDINARY_API_SECRET = "your_api_secret"

  - Log in to Heroku and go to the Application Configuration page for the application. Click on Settings and click on the "Reveal Config Vars" button and add the following:
  
        KEY: CLOUDINARY_URL
        VALUE: cloudinary://CLOUDINARY_API_KEY:CLOUDINARY_API_SECRET@CLOUDINARY_CLOUD_NAME

  - Add the Cloudinary library to your Django project by adding 'cloudinary' to the INSTALLED_APPS list in your Django settings file:

        INSTALLED_APPS = [    ...    'cloudinary',]

  - Run the following command to apply the changes to your Django project:

        python manage.py migrate

  - You are now ready to use Cloudinary in your Django project. To use Cloudinary to manage and serve your  media files, you can use the CloudinaryField field in your Django models.

  - For example, to create a model with a Cloudinary image field, you can do the following:

        from django.db import models
        from cloudinary.models import CloudinaryField

        class MyModel(models.Model):

        name = models.CharField(max_length=255)
        image = CloudinaryField('image')

  - You can then use the image field just like any other Django field to store and retrieve images from Cloudinary.

</details>

## Set Up Gmail in Django

- <details>
    <summary>Process</summary>

  - Install the django-email-backend package by running the following command:

          pip install django-email-backend

  - In your Django settings file (typically settings.py), add the following lines to configure the email backend:

          EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
          EMAIL_HOST = 'smtp.gmail.com'
          EMAIL_PORT = 587
          EMAIL_USE_TLS = True
          EMAIL_HOST_USER = 'your-gmail-username@gmail.com'
          EMAIL_HOST_PASSWORD = 'your-gmail-password'

  - Make sure that you have enabled "Less secure app access" in your Gmail account settings. To do this, go to your Google Account settings, click on "Security" and then scroll down to "Third-party apps with account access." Make sure that "Allow less secure apps" is turned on.

  - Test the email backend by sending a test email from your Django application. You can do this by using Django's built-in send_mail function, like this:

          from django.core.mail import send_mail

          send_mail(
          'Subject here',
          'Here is the message.',
          'from@example.com',
          ['to@example.com'],
          fail_silently=False,
          )

  - If everything is set up correctly, this should send a test email to the specified address using your Gmail account as the email backend.

</details>

## Clone a Github repository

- <details>
    <summary>Process</summary>

  - To clone a repository from GitHub, you will need to have Git installed on your computer. If you don't already have Git installed, you can download it from the official website (https://git-scm.com/).

  - Once you have Git installed, open a terminal window and navigate to the location where you want to store the repository on your local machine. Then, use the following command to clone the repository:

        git clone https://github.com/USERNAME/REPOSITORY.git

  - Replace "USERNAME" with the GitHub username of the owner of the repository, and replace "REPOSITORY" with the name of the repository you want to clone.

  - For example, if you want to clone this repository the command would be:

        git clone https://github.com/JoseMGuerra/ci-pp4-django-fsf <where to clone>

  - This will create a new directory on your local machine with the same name as the repository, and download all the files from the repository into that directory.

  - You can also use a graphical Git client, such as GitHub Desktop, to clone a repository from GitHub. With GitHub Desktop, you can simply enter the URL of the repository and choose a local directory to clone the repository to.

</details>

## DEBUGING

- <details>
    <summary>Modal error</summary>

        TypeError: $(...).modal is not a function
        solution: place bootstrap script in base.html head tag.

    ![jquery error](readme_images/modal-error.png)

</details>

## Known Bugs

- Currently no known bugs

## Resources / Credits / Inspiration

- Python documentation
- Django project documentation
- Code with Stein
- Corey Schafer
- Free code camp
- Stack over flow
- I Think Therefore I Blog walk-through project

## Acknowledgments

Thank you to my mentor Brian Macharia for his help and invaluable feedback.

---

Happy coding!
