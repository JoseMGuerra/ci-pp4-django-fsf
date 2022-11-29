![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Work in progress

## User Stories and Epics

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
  <!-- - [Coverage:](https://coverage.readthedocs.io/en/latest/index.html) Used for measuring code coverage of Python test files. -->
  <!-- - [Jest:](https://jestjs.io/) A delightful JavaScript Testing Framework, used for automated tests. -->

</details>

- <details>
    <summary>Software and Web Applications</summary>

  - [Am I Responsive:](http://ami.responsivedesign.is) Checking the responsiveness.
  - [Balsamiq:](https://balsamiq.com/) Used to create the wireframes.
  - [Chrome DevTools:](https://developer.chrome.com/docs/devtools/) Used to test the response on different screen sizes, debugging and to generate a Lighthouse report to analyze page load.
  - [Font Awesome:](https://fontawesome.com/) Used throughout the site to add icons for aesthetic and UX purposes.
  - [Git:](https://git-scm.com/) Git open source software for distributed version control.
  - [GitHub:](https://github.com/) Internet hosting service for software development and version control using Git.
  - [Google Fonts:](https://fonts.google.com/) Used to import fonts family [Montserrat](https://fonts.google.com/specimen/Montserrat) which is used as main font throughout the site and [Lato](https://fonts.google.com/specimen/Lato) font used for headings.
  - [Heroku:](https://www.heroku.com/) For deployment and hosting of the application.
  - [Elephant PostgreSQL:](https://www.elephantsql.com/) The database used for this application.
  - [HTML Validator:](https://validator.w3.org/) Check your code for HTML validation.
  - [JSHint:](https://jshint.com/) Check code for JavaScript validation.
  - [Lucidchart:](https://www.lucidchart.com/pages/) Used to create the site map.
  - [Tiny PNG:](https://tinypng.com/) Compressing images to smaller sizes.
  - [Unsplash:](https://unsplash.com/photos/NtkCemIfaiU) Hero image, Man fishing on river at daytime, Chris Sarsgard.
  - [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/) Check your code for CSS validation.
  <!-- - [Google Maps:](https://mapsplatform.google.com/) Google Maps Embed API used in footer section -->
  <!-- - [Gauger:](https://gauger.io/fonticon/) To create the favicon, create beautiful favicon with ease. -->
  <!-- - [Materialize Colors:](https://materializecss.com/color.html) Used to create the main colour palette. -->
  <!-- - [SVG Backgrounds:](https://svgbackgrounds.com/) Scalable Vector Graphic used in the featurette section. Should the background image fail there is a fallback background colour set so the page still functions. -->
  <!-- - [SVG Wave Generator:](https://softr.io/tools/svg-wave-generator/) Used to generate a gradient SVG wave used in the hero section. -->
  <!-- - [Writer:](https://writer.com/grammar-checker/) Free Grammar Check. -->

</details>

## Deployment

- <details>
    <summary>Deploy to Heroku</summary>

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

## Clone the repository

- Open your termninal and enter this command:

      git clone <url> <where to clone>

## DEBUGING


---

Happy coding!
