<img width="162" alt="Home|Cooking" src="https://user-images.githubusercontent.com/92300013/179736385-24b1ef1a-050b-4510-baf6-5b7462b00cc0.png">

This is a full-stack framework project built using Django, HTML, CSS and Python. My objective is to create a functioning and responsive website, that allows users to post, comment and like or unlike recipes. This project is based around the functionallity of CRUD - Create, Read, Update, Delete. 

I wanted to build a Recipe page because I enjoy cooking and sharing recipes that I have created for my freinds and family. I wanted to create an simple platform for user to use. 
Simple but effective 

## About 

The Home|Cooking page is a website where users can view recipes, like, Comment and and also share their own recipes with other users. This page is intended for any one who enjoys cooking and is looking for some inspiration. 

#

# User Storys 
## Admin
- As a Site admin I can create, edit and delete recipes and comments so that i can manage the site content.
- As a Site admin I can log out of the admin panel so that i can disconnect from the website.
- As a Site admin I can access the admin panel so that i can manage recipes and comments.

## Login/Register
- As a User I can login/logout off my account if I wish so that i can connect or disconnect from the website.
- As a User I can register for an account so that i can interact with the site content.

## User Recipes
- As a Logged-in user I can post a recipes so that other users can see them.
- As a logged-in user I can like and unlike recipes so that i can mark which recipes I like.
- As a Logged-in user I can upload an image along with my recipe so that i can other users can see what the dish looks like.

## User Interaction
- As a User I can delete my recipe so that i can remove any unwanted recipes that I have made.
- As a User I can edit recipes so that i can update any changes or mistakes to my recipes.
- As a User I can see all the recipes that I liked so that i can return to them.
- As a User I can view comments on recipes so that i can read other user's opinions.
- As a User I can view the number of likes on recipes so that i can see which recipe is most popular.

## Navigation
- As a User I can easily navigate through the site so that i can view desired content.
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

<img width="1418" alt="Add Recipe" src="https://user-images.githubusercontent.com/92300013/180599153-a8056794-a158-465e-85a6-9ea002ad614d.png">

#

<img width="1429" alt="Edit/delete" src="https://user-images.githubusercontent.com/92300013/180599738-268be264-2ac8-46fb-96b9-07410ea0fc61.png">

#

## Bugs and Issues
- Favourite_recipes wasn't showing up your favourite recipes, had the code in wrong and had to change it, needed to leave a space after a line. 
- Had a problem with my comments, nothing was showing up. I need to capitalizes the C in Comments 
- Issues with my cloudiary storage, needed to change to lowercase 


# Deployment 

## Gitpod 

To create a new repository I took the following steps:

1. Logged into Github.
2. Click on the ???repositories??? section.
3. Repository template - I used the code institute template.
4. Clicked the green ???new??? button, creates new repository page.
6. Once created I opened the new repository and clicked the green ???Gitpod??? button to create a workspace in Gitpod for editing.

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