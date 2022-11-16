![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Work in progress

## User Stories and Epics

- View post list: As a `Site User` I want be able to `view a list of posts` so that `I can select one to read`
- Open a post: As a `Site User` I want be able to `click on a post` so that `I can read the full text`

- View comments: As a `Site User / Admin` I want be able to `view comments on an individual post` so that `I can read the conversation`
- Comment on a post: As a `Site User` I want be able to `leave comments on a post` so that `I can be involved in the conversation`
- Update a comment: As a `Site User` I want be able to `update a comment I made` so that `I can make changes or delete a comment`

- Account registration: As a `Site User` I want be able to `register an account` so that `I can create, comment and like`
- Social account sign in : As a `Site User` I want be able to `Sign In with my social account` so that `Sign In quicker`
- Profile picture: As a `Site User` I want be able to `upload a profile picture` so that `I can see it  when I comment on a post`
- Manage posts: As a `Site User / Admin` given that `Ì am registered` I want be able to `create, read, update and delete posts` so that `I can manage my posts`

- Create a post: As a `Site User / Admin` given that `I am registered` I want be able to `create a post` so that `I can add content to the blog`
- Update a post: As a `Site User / Admin` I want be able to `update a post I created` so that `I can make changes or delete a post`
- Delete a post: As a `Site User / Admin` I want be able to `update a post I created` so that `I can make changes or delete a post` 
- Create drafts: As a `Site User / Admin` I want be able to `create draft posts` so that `I can finish writing the content later`
- Add picture to post: As as `Site User` I want be able to `upload a picture` so that `I can add a visual representation of my post`

- View likes: As a `Site User / Admin` I want be able to `view the number of likes on each post` so that `I can see which is the most popular or viral`
- Like / Unlike: As a `Site User` I want be able to `like or unlike a post` so that `I can interact with the content`
- Vote posts: As a `Site User` I want be able to `up/downvote a post` so that `I can interact with the content`

- Approve comments: As a `Site Admin` I want be able to `approve or disapprove comments` so that `I can filter out objectionable comments`
- Create drafts: As a `Site Admin` I want be able to `create draft posts` so that `I can finish writing the content later`

## Technologies Used

### Languages Used:

- HTML5
- CSS3
- JavaScript
- Python

### Frameworks and Libraries Used:

- [Bootstrap:](https://getbootstrap.com/) Bootstrap CSS Framework used for styling and to build responsive web pages.
- [Cloudinary:](https://cloudinary.com/) Used to store all blog images and uploaded images.
<!-- - [Coverage:](https://coverage.readthedocs.io/en/latest/index.html) Used for measuring code coverage of Python test files. -->
- [Django:](https://www.djangoproject.com/) Main Python framework used in the development.
- [Django Allauth:](https://django-allauth.readthedocs.io/en/latest/index.html) Used for authentication and account registration.
- [Django Crispy Forms:](https://django-crispy-forms.readthedocs.io/en/latest/) Used to simplify the rendering of Django forms.
- [dj_database_url:](https://pypi.org/project/dj-database-url/) Used to allow database urls to connect to the postgres database.
- [Gunicorn:](https://gunicorn.org/) Green Unicorn, used as the Web Server to run Django on Heroku.
<!-- - [Jest:](https://jestjs.io/) A delightful JavaScript Testing Framework, used for automated tests. -->
- [psycopg2:](https://pypi.org/project/psycopg2/) Used PostgreSQL database adapter.
- [Summernote:](https://github.com/summernote/django-summernote) To provide a WYSIWYG editor for customizing new blog content and add images.

### Software and Web Applications Used:

- [Am I Responsive:](http://ami.responsivedesign.is) Checking the responsive.
- [Balsamiq:](https://balsamiq.com/) Used to create the wireframes.
- [Chrome DevTools:](https://developer.chrome.com/docs/devtools/) Used to test the response on different screen sizes, debugging and to generate a Lighthouse report to analyze page load.
- [Font Awesome:](https://fontawesome.com/) Used throughout the site to add icons for aesthetic and UX purposes.
<!-- - [Gauger:](https://gauger.io/fonticon/) To create the favicon, create beautiful favicon with ease. -->
- [Git:](https://git-scm.com/) Git open source software for distributed version control.
- [GitHub:](https://github.com/) Internet hosting service for software development and version control using Git.
- [Google Fonts:](https://fonts.google.com/) To import font family ’Cabin Sketch’ which is used throughout the site. Added fallback font sans-serif.
<!-- - [Google Maps:](https://mapsplatform.google.com/) Google Maps Embed API used in footer section -->
- [Heroku:](https://www.heroku.com/) For deployment and hosting of the application.
- [Heroku PostgreSQL:](https://www.heroku.com/postgres) The database used for this application.
- [HTML Validator:](https://validator.w3.org/) Check your code for HTML validation.
- [JSHint:](https://jshint.com/) Check code for JavaScript validation.
- [Lucidchart:](https://www.lucidchart.com/pages/) Used to create the site map.
<!-- - [Materialize Colors:](https://materializecss.com/color.html) Used to create the main colour palette. -->
<!-- - [SVG Backgrounds:](https://svgbackgrounds.com/) Scalable Vector Graphic used in the featurette section. Should the background image fail there is a fallback background colour set so the page still functions. -->
<!-- - [SVG Wave Generator:](https://softr.io/tools/svg-wave-generator/) Used to generate a gradient SVG wave used in the hero section. -->
- [Tiny PNG:](https://tinypng.com/) Compressing images to smaller sizes.
- [Unsplash:](https://unsplash.com/photos/NtkCemIfaiU) Hero image, Man fishing on river at daytime, Chris Sarsgard.
- [W3 CSS Validator:](https://jigsaw.w3.org/css-validator/) Check your code for CSS validation.
<!-- - [Writer:](https://writer.com/grammar-checker/) Free Grammar Check. -->

## DEPLOY TO HEROKU

- On Heroku create an account and log in.
- Click `new` and `create new app`.
- Choose a unique name for your app, select region and click on `Create App`
- Located in the `Resources` Tab, Add-ons, search and add  e.g. `Heroku PostgresSql` and select the `Hobby Dev - Free`.
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

## Clone the repository

- Open your termninal and enter this command:

      git clone <url> <where to clone>

## DEBUGING

- problem: Heroku couldn't find static files.
  - solution: pip3 install `whitenoise` and add to settings.py

---

Happy coding!
