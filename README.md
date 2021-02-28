# MS4-DJ-ecomSite
MS4 Project E-Commerce Site

[View the deployed project here.](https://ecom-nearrocks.herokuapp.com/)

MS4 Final Project for Code Institute.
NearRocks Craft Beer Store is an online store to purchase Craft Beers mainly from Ireland but also Craft beers from USA and UK. The user can select the type and style of the beer they desire to purchase. They can login the the website account to see their purchased items.
Their is also a recent news section or posts from the website host. A user can use their own email to signup or use Github social platform to sign into the app.
The Admin can create, read, update and delete posts and Beers and Breweries in the django administration section. 
The pages are designed to be responsive with a masonary feel on the items and news post sections. A customer can easily see their added quantities in the shopping bag and checkout their items for delivery.

- Live Deployed Project on Heroku: [HERE](https://ecom-nearrocks.herokuapp.com/)
- GitHub Repo : [HERE](https://github.com/Dermomurphy/MS4-DJ-ecomSite)

# Contents

# UX
### Objectives

### User Stories

- User Stories can be seen [HERE](googledrivelink)


### Features

#### Common Base HTML
#### Home PAGE
#### Products Page
#### Product Detail Page
#### Shopping Bag
#### Posts Page
#### Post Detail Page
#### Shopping Checkout Page
#### Profile Page

### Wireframes
Desktop

Mobile

## Surface
- #### Colour Scheme
- #### Typography
- #### Images Used
- #### Icons

# Database

# Technologies Used:
1. [Bootstrap](https://getbootstrap.com)
    - Built with Bulma CSS framework. 
2. ![jQuery](https://img.shields.io/badge/jQuery-3.5.1-yellowgreen)
    - [jQuery](https://jquery.com/) - is a fast, small, and feature-rich JavaScript library. It makes things like HTML document traversal and manipulation, event handling, animation. The project uses **JQuery** to simplify DOM manipulation.
3.  [PostrgesSQL]() - Heroku app based PostgresSQL Database
4.  [Django Framework 3.1.7](https://www.djangoproject.com/) - Django Python app framework

5.  [Visual Studio Code](https://code.visualstudio.com/): Programming code editor created by Microsoft.
6.  ![Chrome Developer Tools](https://img.shields.io/badge/Chrome%20Dev%20Tools-Google%20Chrome-blue)
    - [Chrome Developer Tools](https://developers.google.com/web/tools/chrome-devtools) -  web developer tools built directly into the Google Chrome web browser.
7.  ![Git](https://img.shields.io/badge/Git-----fast--version--control-orange)
    - [Git](https://git-scm.com/) - open source distributed version control system.
8.  ![GitHub](https://img.shields.io/badge/GitHub-Git%20repository%20hosting%20service-lightgrey)
    - [GitHub](https://github.com/) - Web-based hosting service for version control using Git.
9.  [W3CMarkupValidation](https://validator.w3.org/) Tools to assess CSS and HTML validation.
10.  [GoogleFonts](https://fonts.google.com/) - font families from Google.
11. ![HTML5](https://img.shields.io/static/v1?label=HTML&message=5&color=E34F26&logo=html5&logoColor=ffffff)
    - [HTML5](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - used for Hyper text markup language.
12. ![CSS3](https://img.shields.io/static/v1?label=CSS&message=3&color=1572B6&logo=css3&logoColor=ffffff)
    - [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used for cascading stylesheets.
13. [Visual Paradigm](https://online.visual-paradigm.com/) - Schema Diagrams
14. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja - Templating language.
15. [Python V3.6.9](https://www.python.org/) - Python Programming language.

# Testing

# Deployment

## Heroku:

## AWS (Amazon Web Services):
- An AWS Account was created with and S3 Bucket instance to store our static files for hosting. IAM user group and content polocies were also generated giving us access to the secret access key ID and secret access key for retrieval of file. 

|Key|Value|
|--|--|
|AWS_ACCESS_KEY_ID|```AWS Access Key ID```|
|AWS_SECRET_ACCESS_KEY|```AWS Secret Access Key```|
|DATABASE_URL	|```Postgres Database URL```|
|AWS_STORAGE_BUCKET_NAME| ```ecom-nearrocks```|
|AWS_S3_REGION_NAME|```eu-west-1```|
|AWS_ACCESS_KEY_ID |```os.environ.get('AWS_ACCESS_KEY_ID')```|
|AWS_SECRET_ACCESS_KEY|``` os.environ.get('AWS_SECRET_ACCESS_KEY')```|
|AWS_S3_CUSTOM_DOMAIN |```f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'```|
    
    #Static and MEdia Files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


## Local Deployment:

# Credits:
- Main Text Written by Dermot Murphy
- Google Fonts for font styles; https://fonts.google.com/
- [Bootstrap Slate CSS Framework + Themes]() Bespoke Slate Theme used
- W3schools.com:[W3Schools](https://www.w3schools.com/)

# Notice of Image Use:
I do not own any of the photographs however I have been given express permission to use any photographs from the breweries shown directly. I operate Craft beer tasting sessions under [DublinBeerTasting](www.dublinbeertasting.com) and as such have a good working relationship with all showcased breweries.

# Acknowledgements:
- Mentor Adegbenga Adeye:  for site layout inspiration, constructive advice. Github : https://github.com/deye9

- Code Institute : for instructional videos and Tutoring/support slack channel. https://codeinstitute.net/
