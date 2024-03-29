<img width="162" alt="Home|Cooking" src="https://user-images.githubusercontent.com/92300013/179736385-24b1ef1a-050b-4510-baf6-5b7462b00cc0.png">

This is a full-stack framework project built using Django, HTML, CSS and Python. My objective is to create a functioning and responsive website, that allows users to post, comment and like or unlike recipes. This project is based around the functionallity of CRUD - Create, Read, Update, Delete. 

I wanted to build a Recipe page because I enjoy cooking and sharing recipes that I have created for my freinds and family. I wanted to create an simple platform for user to use. 
Simple but effective 

It can be hardwork trying to plan out what your next recipe will be for dinner. This site make it easy for User to find inspiration with 
Home cooked recipes at your finger tips :point_up:. Share with people, what family secrets recipe you may have out there. 

## About 

The Home|Cooking page is a website where users can view recipes, like, Comment and and also share their own recipes with other users. This page is intended for any one who enjoys cooking and is looking for some inspiration. 


Live link found here <a href="https://home-cooking.onrender.com/" alt="Live Link"> Home|Cooking </a>

#

<img width="1082" alt="Screen" src="https://user-images.githubusercontent.com/92300013/181036010-8b638a9f-af99-4571-8888-480b3b2edf6c.png">

#

# User Storys 
## Admin
- As a Site admin I can create, edit and delete recipes and comments so that i can manage the site content.
- As a Site admin I can log out of the admin panel so that i can disconnect from the website.
- As a Site admin I can access the admin panel so that i can manage the page.

## Login/Register
- As a User I can login/logout off my account if I wish so that i can connect/disconnect from the website.
- As a User I can register for an account so that i can interact with the website pages.

## User Recipes
- As a Logged-in user I can post a recipes so that other users can see them.
- As a logged-in user I can like and unlike recipes so that i can share the love with recipes I like.
- As a Logged-in user I can upload an image along with my recipe so that i can other users can see what the dish looks like.
- As a Logged-In user I can see all the recipes that I liked so that i can return to them

## User Interaction
- As a User I can delete my recipe so that i can remove any unwanted recipe.
- As a User I can edit recipes so that i can update anything on the recipes.
- As a User I can view comments on recipes so that i can see other user's thoughts on the recipe.
- As a User I can view the number of likes on recipes so that i can see which recipe is most favourite

## Navigation
- As a User I can easily navigate through the site so that i can view content.
- As a User I can search the desirable recipe by keyword so that i can find the recipe I want faster.
- As a User I can see the most recent recipes so that i can keep up to date with the latest recipes.
- As a user I can see the most loved recipes so that i can quickly find inspiration and see which recipes are most liked

#

# Features 
## Home Page
### Navigation Bar
- This featured appears throughout the page,it allows users to easily navigate through the site.
- The Navigation bar has a number of links for 'Home', 'Recipes' and 'Login/Register', more links appear when user is logged in. 
- The Navigation bar alos includes a search bar, where users can search for recipes. 
- A Message will appear when you have logged in. 

<img width="1432" alt="Nav bar" src="https://user-images.githubusercontent.com/92300013/179953899-f76f03ae-fdb1-4a3b-b0db-8cdcd24988a9.png">

#

### Hero Image
- The hero image is welcoming and has a homnely feel to it. A message is displayed giving users an insight into the website. 
- The Login / Register button will redirect user to the login page / Resgister page if user don't have a account. 

<img width="1368" alt="Hero Image" src="https://user-images.githubusercontent.com/92300013/179966563-821f217c-2e79-49c1-9c58-bfb88b35bf2e.png">

#

### Inspiration Recipes
- Inspiration Recipes shows the most recently Added recipe, if anyone needs a quick inspiration. 
- This section showing 4 recipe cards is fully responsive.
- Each recipe shows who craeted it with a number of other details. 

<img width="1384" alt="Inspiration Recipes" src="https://user-images.githubusercontent.com/92300013/179969013-4f091d81-561b-4d6b-94ee-52daee1b9232.png">

#

### Footer
- Appears throughout the pages and contains social links.
- Links are opened in a new tab, so they can easily revert back to Home|Cooking.

<img width="1422" alt="Footer" src="https://user-images.githubusercontent.com/92300013/179976168-2e81d242-2175-421e-9e8d-c4d7b911f14e.png">

#

### Recipe Page 
- The Recipe pages shows all the Recipes avavilable, each recipe shows the craetor of the dish.
- Starting with most recent to oldest recipes - The site will paginate all recipe cards to display 6 to a page.
- Each Card shows a number of features from an image, name,  date posted and number of likes. 
- Each recipe card takes users to the recipe details page

<img width="1432" alt="All recipes" src="https://user-images.githubusercontent.com/92300013/179976467-c2bb6e42-e867-4a27-8874-2134af41e26f.png">

#

### Login / Register
- The login / Register buttons redirect Users to the login page where they can either signin or follow the link to the Register page where they can signup and create an account with use.

<img width="1417" alt="Sign-in page" src="https://user-images.githubusercontent.com/92300013/179980101-40a6b7d9-7993-406b-bc68-2d40275f08bd.png">

#

<img width="1398" alt="Sign-up Page" src="https://user-images.githubusercontent.com/92300013/179981039-b07670d4-6668-435c-9194-3b2720dd540a.png">

#

### Favourite Recipes Page
- The Favourite Recipes page can only be viewed when the User is loggin, this page shows all recipes that the user liked.

<img width="1429" alt="Favourite Recipe" src="https://user-images.githubusercontent.com/92300013/179989872-7beff406-3220-4c28-b0ea-2f8b8ecd2996.png">

#

### Your Recipes Page
- This pages shows all recipes that the user has uploaded & created.
- The user can Add recipe with a click of a button found at the top of page.
- Recipes can be Edited and Deleted with a click of a button.

<img width="1429" alt="Edit/delete" src="https://user-images.githubusercontent.com/92300013/180599738-268be264-2ac8-46fb-96b9-07410ea0fc61.png">

#

### Recipes Detail page 
- The page shows all the infromation about the recipe and include  Recipes name, author name, date posted and image.
- The body of the page contains short description of the recipe, ingredients and preparation steps
- Number of likes and comments are displayed after the preparation steps
- Only logged in users can leave a comment

<img width="1424" alt="Recipe detail" src="https://user-images.githubusercontent.com/92300013/180602836-1eae18b0-a564-41c7-bfe8-3ac460e56613.png">

#

### Add Recipes
- Ounce the User is logged In, they can add recipes. 
- A form must be filled out in order to publish recipes. 
- All fields must be complated, a default image is provided. 

<img width="1423" alt="Add recipe" src="https://user-images.githubusercontent.com/92300013/180754475-0995859f-583e-4056-b4a2-c8d7daab02d0.png">

#

# Design 
## Color
- Color palette from <a href="https://coolors.co/" alt="Coolors">Coolors</a>

![Recipe](https://user-images.githubusercontent.com/92300013/180755515-3b77621d-481b-4ecf-b06e-62d60822c818.png)

#

## Font
- 'Lobster Two'
- 'Shadows Into Light'
- 'Yanone Kaffeesatz'

#

# Technologies Used

## Languages
- <a href="https://en.wikipedia.org/wiki/HTML5" alt="HTML5">HTML5</a>
- <a href="https://en.wikipedia.org/wiki/CSS" alt="CSS3">CSS3</a>
- <a href="https://www.python.org/" alt="Python">Python</a>

#

## Frameworks, Libraries & Programs Used
GitHub / GitPod - Holds the repository of my project, GitHub connects to GitPod.

Heroku - Connected to the GitHub repository. 

Django - used to build the models, forms and views of the app.

Cloudinary - Used as free cloud storage for images uploaded to the site through the recipe forms

Bootstrap - Used to quickly add design to my website. <a href="https://startbootstrap.com/theme/freelancer" alt="Freelancer"> (Freelancer)</a>

Summernote - Used to add a text area field to the admin setup to enable a list of steps.

Google Fonts - Used fonts for the website.

Font Awesome - Used for icons.

W3C Markup Validator - was used to validate HTML

W3C CSS Validator - was used to validate CSS

#

# Wireframe

[WIREFRAME](https://lucid.app/lucidspark/8713686c-4b42-4e8c-b6c8-45bee297a24e/edit?beaconFlowId=A68660C88A866270&invitationId=inv_107efb42-5399-4ede-8047-149768ab93a8#)

#

# Database schema 
[DATABASE SCHEMA](https://lucid.app/lucidchart/cde07f32-52f8-43ef-b9cc-eddf47a621f7/edit?beaconFlowId=857755314F8C6DDA&invitationId=inv_21573bd0-7751-4a60-95fe-795c3b06be31&page=0_0#)



# Testing
## User Story 
### Admin
   - As a Site admin I can create, edit and delete recipes and comments so that i can manage the site content.
   - As a Site admin I can log out of the admin panel so that i can disconnect from the website.
   - As a Site admin I can access the admin panel so that i can manage the page.

This was tested by creating a Superuser on the Django Admin Panel where the administrator can perform all the CRUD functionalitis.

### User Interaction
   - As a User I can delete my recipe so that i can remove any unwanted recipe.
   - As a User I can edit recipes so that i can update anything on the recipes.
   - As a User I can view comments on recipes so that i can see other user's thoughts on the recipe.
   - As a User I can view the number of likes on recipes so that i can see which recipe is most favourite.

<img width="1294" alt="User Interaction" src="https://user-images.githubusercontent.com/92300013/180782553-66dc249f-6897-4c76-a215-63de8b455cef.png">

<img width="537" alt="delete recipe" src="https://user-images.githubusercontent.com/92300013/180792748-0df6c023-1364-48ea-bc79-54cd5b5a5fac.png">

### User Recipes
   - As a Logged-in user I can post a recipes so that other users can see them.
   - As a logged-in user I can like and unlike recipes so that i can share the love with recipes I like
   - As a Logged-in user I can upload an image along with my recipe so that i can let users see what the dish looks like
   - As a Logged-In user I can see all the recipes that I liked so that i can return to them

<img width="1425" alt="Add recipe" src="https://user-images.githubusercontent.com/92300013/180783433-6f2bbebf-5b04-4c65-b366-02158258a10e.png">

<img width="295" alt="Add image" src="https://user-images.githubusercontent.com/92300013/180783713-88bc03f6-466f-4e94-911e-2dfb63e20e00.png"> <img width="94" alt="Liked recipe" src="https://user-images.githubusercontent.com/92300013/180783867-aa87e378-7449-4bc2-b45e-750ee923dc83.png">

### Login / Register
   - As a User I can login/logout off my account if I wish so that i can connect/disconnect from the website
   - As a User I can register for an account so that i can interact with the website pages

<img width="1188" alt="Signin" src="https://user-images.githubusercontent.com/92300013/180794843-c57d0d04-0e09-486b-9d23-bcf1d6c212ef.png">

<img width="1184" alt="signout" src="https://user-images.githubusercontent.com/92300013/180794932-d3f6b5b8-4f28-4ec4-8599-256e9f061ce0.png">

<img width="855" alt="SignUp" src="https://user-images.githubusercontent.com/92300013/180795155-d77e971a-c00b-4ace-b84f-d72bdd32e59c.png">

<img width="569" alt="Login message" src="https://user-images.githubusercontent.com/92300013/180800244-2a0f57e2-d1dc-4376-af0b-4e1e04833ab0.png">

### Navigation
   - As a User I can easily navigate through the site so that i can view content.
   - As a User I can search the recipe by keyword so that i can find the recipe I want faster
   - As a User I can see the most recent recipes so that i can keep up to date with the latest recipes.
   - As a user I can see the most loved recipes so that i can quickly find inspiration and see which recipes are most liked

<img width="1347" alt="Navbar" src="https://user-images.githubusercontent.com/92300013/180800805-1e8c4f9b-2677-4d85-a1d8-d291b51ddad0.png">

<img width="999" alt="Searched Prawns" src="https://user-images.githubusercontent.com/92300013/180803784-ce7ff54a-f78d-42d3-a7d7-a41933db3b1e.png">

<img width="1092" alt="Liked recipes" src="https://user-images.githubusercontent.com/92300013/180804810-21ef76bd-f42e-467e-9fe0-1e5959426cba.png">

#

##  Future Features
- Down the lines you could start to add home made videos and tips on how to cook certian things. Giving User an insight on 
how you cook certain recipes. Whats the best way to cook something or learn how to cook a new ingredient.

#

## Bugs and Issues
- Favourite_recipes wasn't showing up your favourite recipes, had the code in wrong and had to change it, needed to leave a space after a line. 
- Had a problem with my comments, nothing was showing up. I need to capitalizes the C in Comments 
- Issues with my cloudiary storage, needed to change to lowercase 

#

# Deployment 

## Gitpod 

To create a new repository I took the following steps:

1. Logged into Github.
2. Click on the ‘repositories’ section.
3. Repository template - I used the code institute template.
4. Clicked the green ‘new’ button, creates new repository page.
6. Once created I opened the new repository and clicked the green ‘Gitpod’ button to create a workspace in Gitpod for editing.

## Heroku

To deploy this page to Heroku from its GitHub repository, the following steps were taken:

1. Create the Heroku App:
   - Select "Create new app" in Heroku.
   - Choose a name for your app and select the location.

2. Attach the Postgres database:
   - In the Resources tab, under add-ons, type in Postgres and select the Heroku Postgres option.

3. Prepare the environment and settings.py file:
- In the Settings tab, click on Reveal Config Vars and copy the url next to DATABASE_URL.
- In your GitPod workspace, create an env.py file in the main directory.
- Add the DATABASE_URL value and your chosen SECRET_KEY value to the env.py file.
- Add the SECRET_KEY value to the Config Vars in Heroku.
- Update the settings.py file to import the env file and add the SECRETKEY and DATABASE_URL file paths.
- Update the Config Vars with the Cloudinary url, adding into the settings.py file also.
- In settings.py add the following sections:
  * Cloudinary to the INSTALLED_APPS list
  * STATICFILE_STORAGE
  * STATICFILES_DIRS
  * STATIC_ROOT
  * MEDIA_URL
  * DEFAULT_FILE_STORAGE
  * TEMPLATES_DIR
  * Update DIRS in TEMPLATES with TEMPLATES_DIR
  * Update ALLOWED_HOSTS with ['app_name.heroku.com', 'localhost']

4. Store Static and Media files in Cloudinary and Deploy to Heroku:
- Create three directories in the main directory; media, storage and templates.
- Create a file named "Procfile" in the main directory and add the following:
web: gunicorn project-name.wsgi
- Log in to Heroku using the terminal heroku login -i.
- Then run the following command: heroku git:remote -a your_app_name_here and replace your_app_name_here with the name of your Heroku app. This will link the app to your Gitpod terminal.
- After linking your app to your workspace, you can then deploy new versions of the app by running the command git push heroku main and your app will be deployed to Heroku.

#

# Credits
- <a href="https://codeinstitute.net/ie/">Code Institute</a> - The Project 'I think therefore I blog' helped me alot with setting up the page and gave me a template to work off
- <a href="https://summernote.org/">Summernote</a> - I learn how to inport a summernote toolbar. 
- <a href="https://www.djangoproject.com/">Django documentation</a> - also helped me other problems
- <a href="https://www.youtube.com/watch?v=AGtae4L5BbI">Search bar</a> - This video on YouTube help me create a searchbar 
- <a href="https://startbootstrap.com/theme/freelancer" alt="Freelancer"> Bootstrap </a> - A free template Freelancer
