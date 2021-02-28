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
1. [**UX**](#ux)
 
   - [**User Stories**](#user-stories)
   - [**Admin Stories**](#admin-stories)
 
2. [**Features**](#features)
   - [**Common Base Html**](#common-base-html)
   - [**Home Page**](#home-page)
   - [**Products Page**](#products-page)
   - [**Product Detail Page**](#product-detail-page)
   - [**Shopping Bag**](#shopping-bag)
   - [**Posts Page**](#posts-page)
   - [**Post Detail Page**](#post-detail-page)
   - [**Surface**](#surface)

3. [**Database*](#database)
    - [**Products Model*](#products-model)
    - [**Brewery Model*](#brewery-model)
    - [**Posts Model*](#posts-model)

 
4. [**Technologies Used**](#technologies-used)

5. [**Testing**](#testing)
 
6. [**Deployment**](#deployment)
 
7. [**Credits**](#credits)
   - [**Content**](#content)
   - [**Media**](#media)
   - [**Acknowledgements**](#acknowledgements)

# UX
### Objectives

### User Stories:
As as User I have the ability to :
1. See Beer products of different beer styles and breweries and purchase these items.
2. I can see the latest news Posts in the news section and click into further detail about that post.
3. I can sort the Beers based on Rating , price, Beer Style and see all products.



### Admin Stories:
As an Admin I have the ability to : 
1. I Can login to the site with my super username and secure password or I can login using my GitHub social account.
2. Once logged in as an admin I can add news posts, Breweries and beers. 
3. As a logged in user I have the ability to add any new Beers.  I can select a title, Image URL and write a description using the content editor provided. I can also give this beer a star rating out of 5 stars, 5 being the highest mark. IBU, ABV brewery name can also be added. 


# Features

#### Common Base HTML
- Framework for the project working off base.html
#### Home PAGE
- a simple banner image with shop now button taking the user to all products with main nav and sub navigation. Main nav ahas logo and account login info with shopping bag icon
#### Products Page
- A masonary style layout of all products in the shop
#### Product Detail Page
- a Detail section of product description , rating, price and quantity needed a go back button and an add to bag button
#### Shopping Bag
- shopping contents section with tabular list of all items added to the bag
#### Posts Page
- Latest news from the website admin laid out in masonary style, truncated text display on each post
#### Post Detail Page
- Furthe detail on each post full banner image and description




## Surface
- #### Colour Scheme
    - Slate Grey Bootstrap css used as main css (Bootswatch)[https://bootswatch.com/slate/]
- #### Typography
    Google fonts Lato as main font
- #### Images Used
    - (unsplash)[www.unsplash.com] and various brewery websites see disclaimer/notice of image use.
- #### Icons
    - Font Awesome Icons used.(Fontawesme)[www.fontawesome.com]

# Database
 - for local deployment an sqlite3 database was used. 
 - for heroku deployment the heroku postgresSQL databse is used.

 - custom models used for posts, brewery, products.
 ### Products Model
 |id|brewery|sku|name|style|description|abv|ibu|price|rating|image_url|image|
 |--|--|--|--|--|--|--|--|--|--|--|--|
 |id (pk)|CharField (fk=>brewery)|CharField|CharField|CharField|TextField|DecimalField|IntegerField|DecimalField|DecimalField|URLField|ImageField|

 ### Brewery Model
 |id|name|friendly_name|country|
 |--|--|--|--|
 |id (pk)|CharField|CharField|CharField|

 ### Posts Model
 |id|title|body|image|created_on|
 |--|--|--|--|--|
 |id (pk)|CharField|TextField|ImageField|DateTimeField|

 
# Technologies Used:
1. [Bootstrap](https://getbootstrap.com)
    - Built with Bootstrap CSS framework. 
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
13. [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) - Jinja - Templating language.
15. [Python V3.6.9](https://www.python.org/) - Python Programming language.

# Testing
- simple Django SetUp testing was pefformed on the products and Brewery models. Running tests can be performed by type `./manage.py test` into the CLI

# Deployment
## Issues:
- As I have developed this project not on Gitpod but on a local Virtual Environment using VSCode as suggested from my last project submission I have ran into some obstacles that have caused some major issues. The main issue is that the local session variables are not being stored correctly in the session storage. This means the Cart update has not come to fruition unfortunately and it has hampered my progresss significantly. I have as of yet not found a solution even after conversing with my mentor and it is worth noting that some other students may have this issue if they are to follow the tutorials using a venv. Another main issue overcome was the gunicorn heroku deployment procfile. One must specifically define the path in the procfile in order to have a successful build otherwise Heorku cannot find the correct wsgi application module.
```web: PYTHONPATH=`pwd`/.. gunicorn ecomSite.wsgi:application```
`

- Even though the project is lacking in functionality I have managed to deploy to Heroku and setup all the AWS storage necessary. I bare full responsiblity for the unfinished nature of the project however I have been hampered in progressing due to these issues. 

## Heroku:
Deployed using Heroku accessed via the link below
 - https://ecom-nearrocks.herokuapp.com/


  ### Process
   #### 1: Created a Github account at https://github.com My account: https://github.com/Dermomurphy

   #### 2: Setup Heroku for hosting App.
   1. Create a Heroku account
   2. Create a new app [must have a unique name] and select your region

   #### 3: Synced folder on local machine to Github Repo via VsCode: https://github.com/Dermomurphy/MS4-DJ-ecomSite automatic deployment on Heroku.
   -  Synced folder on local machine to Github Repo via VsCode: https://github.com/Dermomurphy/MS4-DJ-ecomSite

   - Configure Procfile to have content ```web: PYTHONPATH=`pwd`/.. gunicorn ecomSite.wsgi:application``` in order to deploy app using python on Heroku. 

   #### 4: Set environment variables in env.py locally and on Heroku config variables.
   - Create an env.py file in the apps root directory.
   - Add the env.py file to your .gitignore file
   - In order to deploy in Heroku set Config vars located in settings. Click Reveal config vars to input these variables.


   #### 7: Pushing files to Heroku hosted. 
   1. In the terminal window type in `heroku login` and fill in your heroku credentials and password
   2. Commit all your files and type in the same terminal window `git push heroku master`. 

   #### 8: Open Deployed App in Heroku.
   1. Click on **Open app** in the Heroku account, the application will open in a new tab within the browser
  
---     

## AWS (Amazon Web Services):
- An AWS Account was created with and S3 Bucket instance to store our static files for hosting. IAM user group and content policies were also generated giving us access to the secret access key ID and secret access key for retrieval of file. 

|Key|Value|
|--|--|
|AWS_ACCESS_KEY_ID|`Custom AWS Access Key ID`|
|AWS_SECRET_ACCESS_KEY|`Custom AWS Secret Access Key`|
|DATABASE_URL	|`Postgres Database URL`|
|AWS_STORAGE_BUCKET_NAME| `ecom-nearrocks`|
|AWS_S3_REGION_NAME|`eu-west-1`|
|AWS_S3_CUSTOM_DOMAIN |`f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'`|
    
    #Static and MEdia Files
    STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'
    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'


## Local Deployment:
1. `mkdir ecomSite`
2. `cd ecomSite`
3. Create a virtualenv: `python -m virtualenv venv_name`
4. `cd venv_name`
5. Activate it: `source venv_name\bin/activate`
6. from within the venv environment use `git clone <repo-name>` and and clone this repo into it (`https://github.com/Dermomurphy/MS4-DJ-ecomSite.git`)
7. `pip install -r requirements.txt` 
8. To run the server on localhost:8000 use `python3 manage.py runserver` open a browser and point it to localhost:8000

# Credits:
## Content
- Main Text Written by Dermot Murphy
- Google Fonts for font styles; https://fonts.google.com/
- [Bootstrap Slate CSS Framework + Themes](https://bootswatch.com/slate/) Bespoke Slate Theme used
- W3schools.com:[W3Schools](https://www.w3schools.com/)

## Media
I do not own any of the photographs however I have been given express permission to use any photographs from the breweries shown directly. I operate Craft beer tasting sessions under [DublinBeerTasting](www.dublinbeertasting.com) and as such have a good working relationship with all showcased breweries.

## Acknowledgements
- Mentor Adegbenga Adeye:  for site layout inspiration, constructive advice. Github : https://github.com/deye9

- Code Institute : for instructional videos and Tutoring/support slack channel. https://codeinstitute.net/
