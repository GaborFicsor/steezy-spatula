# Steezy Spatula - cooking made less overwhelming

Steezy Spatula is a responsive web application aiming to help people who are struggling with the idea of cooking in general, by providing recipes that are easy to follow and without any unnecessary or additional information. Agile methodology was used to pland and design throughout development. A data model was implemented to make features like managing, querying and manipulating data possible for the users of this website who are able to access these features through authorisation. Registering to the website will give people permission to handle CRUD functionalities such as, create, read, update and delete. For version control GitHub was used. The repository can be found here: [GitHub repository](https://github.com/GaborFicsor/steezy-spatula)

For the admin panel the default django admin dashboard was used, where the admin is able to perform CRUD functionalities related to every model and object.

![image of the amiresponsive testing](static/images/amiresponsive.png)

The live website can be viewed here: [Steezy Spatula - cooking made less overwhelming](https://steezy-spatula.herokuapp.com/)

## CONTENTS

* [User Experience](#user-experience)
  * [Client Goals](#client-goals)
  * [User Stories](#user-stories)

* [Design](#design)
  * [Design Thinking](#design-thinking)
  * [Colour Scheme](#colour-scheme)
  * [Typography](#typography)
  * [Imagery](#imagery)
  * [Wireframes](#wireframes)

* [Features](#features)
  * [General Features on Each Page](#general-features-on-each-page)
  * [Future Implementations](#future-implementations)
  * [Accessibility](#accessibility)

* [Technologies Used](#technologies-used)
  * [Languages Used](#languages-used)
  * [Frameworks, Libraries & Programs Used](#frameworks-libraries--programs-used)

* [Deployment & Local Development](#deployment--local-development)
  * [Deployment](#deployment)
  * [Local Development](#local-development)
    * [How to Fork](#how-to-fork)
    * [How to Clone](#how-to-clone)

* [Testing](#testing)

* [Credits](#credits)
  * [Code Used](#code-used)
  * [Content](#content)
  * [Media](#media)
  * [Acknowledgments](#acknowledgments)


## User Experience

The main goal of this website is to give its users the ability to gain more confidence in the kitchen by providing simple recipes. The whole project aims to make the experience the least overwhelming possible. People should not be discouraged by excess information and should only be told the most important things to get started.

People can register on the website which gives them access to features like adding the recipes that they feel are worth sharing in the sense that it would be beneficial to their peers. Registered users can edit or delte their own uploaded recipes to the site. If people don't have any idea to share yet, they are welcome to browse the existing list of recipes that can be found in the recipes section from which they can save recipes to their list that can be viewed anytime under the "My Stuff" tab. Furthermore, users of the site can comment under any recipe and share their thoughts and be a part of a conversation. Comments can also be deleted or updated by the users.


### Client Goals

<hr>

* To have an immediate understanding of what the website's purpose is.
* To be able to view the site on a range of device sizes, without any distortions that would lower the quality or usability of the website.
* To be able to navigate through the website effortlessly and gain feedback on the actions undertaken to avoid confusion.
* To give users the ability to create, read, edit and delete their recipes and comments.

### User Stories

<hr>

As a site User

* I want to be able to register on the website to gain access to the full experience provided by the application.
* I want to be able to create and share my recipe.
* I want to have the ability to edit the recipes I have created if needed.
* I want to have the ability to delete the recipes I have created if needed.
* I want to have the ability to view other users' shared recipes.
* I want to have the ability to save and 'unsave' the recipes I like, to access them faster and easier anytime.
* I want to have the ability to engage in conversations regarding a recipe.
* I want to be able to view my recipes in one place to manage them faster and easier.
* I want to be reinforced by the actions I undertake during my time on the website.
* I want to search and filter recipes to cater for my own needs.

## Design

### Design thinking

<hr>

I was excited to come up with this idea for my project because it is definitely something I could see myself using. I have a bad relationship with cooking so it was easy to have a viewpoint of an end-user of the website. I think the most important thing about the design was to make the whole webpage have the least clutter possible. 

Whenever I look for recipes online there are several websites out there on the web, but I have not found any that is truly focusing on people with depression and anxiety, at least not in regard to cooking. Even if I find an easy recipe on one of these websites I have to scroll down a lot to get to the actual details and information which just further discourages me to look for recipes like this. It is tedious and for people who really need guidance -like me-, it is not a solution. My website however cuts straight to the point with recipes. No description, and no scrolling down, only the relevant and most important information is presented.

One of my proudest accomplishments in designing this website was the idea I had to make the progress bars differently coloured based on a recipe's difficulty, so people can easily judge if they have the mental capacity to follow through, or give it a try another day. There are 4 levels of difficulties, which are easy, moderate, intermediate, and challenging. I had further ideas to make this even better. One of them was to not use discouraging colours like red on the challenging difficulty for example because it might give people the impression that the recipe can be a bit too difficult to handle. The other one was, to not fill the bar all the way up even for the hardest difficulty because that can also be discouraging to people, which I don't want. I would like to further improve this website, maybe research what features the potential users would truly find useful. I think this is a good project idea and I did spend my time polishing the design.

### Colour Scheme 

<hr>

For the main colour of the design I picked tomato red which goes well with black and white colours, while also making the overall look of the website engaging and visually pleasing. I aimed to make the visitors have a good experience, so they would consider coming back more often.

<details>
  <summary>Colour Palette</summary>

![images of the website's color palette using coolors.co](static/images/colour_palette.png)

</details>

### Typography

<hr>

For the font styles I used the default Arial font provided and for the header elements I picked [Paytone One](https://fonts.google.com/specimen/Paytone+One?query=Paytone)

<details>
  <summary>Paytone One font from Google Fonts</summary>

![image of the Paytone One font style](static/images/paytone_one.png)

</details>

### Imagery 

<hr>

For the images on the website I used stock images from [pexels](https://www.pexels.com/)
<details>
  <summary>background image</summary>

![background image of the website](static/images/header.jpg)

</details>

<details>
  <summary>placeholder image for the recipe card</summary>

![placeholder image of the recipe card](static/images/placeholder.jpg)

</details>


### Wireframes

<hr>

During the early stages of development, I tried using [figma](https://www.figma.com/), where I came up with the idea for the landing page. However, due to my neurodivergent brain I found it hard and overwhelming to come up with a rough mock-up for a complete design.

<details>
  <summary>image of the landing page</summary>

![images of an early mock-up](static/images/early_mockup.png)

</details>

### Database

<hr>

For creating a relational database diagram, I used [figma](https://www.figma.com/). For this project I created 2 models, one for the recipes and one for the comments. There is also a model for the users which was generated by django-allauth.

<details>
  <summary>image of the relational database</summary>

![image of the relational database](static/images/models.png)

</details>

## Features

The main pages of the website are a landing page, a recipes page and a profile page. Further pages for features include: creating and editing forms, authorization pages provided by django-allauth, custom error pages for 400, 403, 404 and 500 errors, and a confirmation page with the purpose of defensive design.

All pages on the website are responsive, have a favicon and a unique title displaying in the browser tab. Every page shares a common navbar and a footer section.
### Landing Page

<hr>

The landing page is what users see the first time they visit my website, so I wanted to make it eye-catching by having a site logo with a slogan on display, and a short explanation as to who this site is dedicated to. The landing page also features a call to action button for registering. This buttin is only present when the user is not logged in. Further down a short description can be found about me, where I explain the purpose and the targeted audience.

<details>
  <summary>image of the landing page when the user is not logged in</summary>

![image of the landing page](static/images/landing_page.png)

</details>

After a registered user logs in to the website the call to action button disappears, and the navbar changes. The user now has access to the 'My Stuff' tab which will be mentioned further down the features.

<details>
  <summary>image of the landing page when the user is logged in</summary>

![image of the landing page if the user is logged in](static/images/landing_page_logged_user.png)

</details>

If the current user of the website is logged in as the admin(superuser), then the navbar displays a tab called 'Admin' which will take the user to the default django admin panel where they can perform crud functions on every single object within the database.

<details>
  <summary>image of the landing page when the superuser(admin) is logged in</summary>

![image of the landing page if the admin is logged in](static/images/landing_page_admin.png)

</details>

### Recipes Page

<hr>
The recipes page give the users a well structured and designed view of the uploaded recipes. A filter form placed at the top gives people the ability to search and filter for recipes by narrowing down their needs. Users can filter by looking up words, select a  difficulty, type or strictly vegan recipes, It is also possible to combine these filters to get the best result possible.

The recipes page also changes based on user authentication. If the user is not logged in, then they don't have access to all crud functionalities of the website. They can only filter, search and view the existing recipes.

<details>
  <summary>image of the recipes page</summary>

![image of the recipes page](static/images/recipes_page.png)

If the current user is logged in to the website, a hyperlink appears below the filter form that says "+add your own".

</details>

<details>
  <summary>image of the recipes page when the user is logged in</summary>

![image of the recipes page when the user is logged in](static/images/recipes_page_logged_user.png)

</details>

Every user has access to the filter form, where they can search for recipes.

<details>
  <summary>image of the recipe filter</summary>

![image of the recipe filter](static/images/filter.png)

</details>

The recipes are presented in a form of a card where -to my judgement- the utmost important details are presented, which are an image, a title, the cooking time and a progress bar which gives a visual representation of how difficult the task could be. All of this combined can give people the ability to judge if they can tackle it, or decide that they look further. There is also a green leaf icon as a small indicator at the top left corner of a recipe if it's vegan-friendly, so people who only eat vegan food can find these recipes more easily.

<details>
  <summary>image of a recipe card</summary>

![image of a recipe card](static/images/recipe_card.png)

</details>

The page can hold 9 entries of recipes at once, any more results will create a pagination, where people can browse by looking at different pages. Recipes shown are ordered by their date of creation, with the most recent showing up first. 
<details>
  <summary>image of pagination</summary>

![image of the pagination](static/images/pagination.png)

</details>

If the user tried looking up or filtering down to a recipe that does not exist in the database, they will be informed by a sentence.

<details>
  <summary>image of no results</summary>

![image of no results after filtering](static/images/recipes_page_no_result.png)

</details>

### My Stuff

<hr>

When the user clicks on the 'My Stuff' tab in the navigation bar, they are directed to their profile page that displays their username and the date they registered on the website. In addition, the page includes two tables that allow the user to view their shared and saved recipes, providing a convenient and accessible way to keep track of their recipes.

On the 'My Stuff' page, there is a table dedicated to displaying all the recipes they have uploaded to the website, titled "My Recipes." At the top of the table, there is a plus sign that serves as a link to the recipe creation form. The table consists of three columns. The first column displays the name of each recipe and serves as a hyperlink to the detailed page for that recipe. The second column features a pencil icon, which allows the user to edit the corresponding recipe. Clicking the pencil icon takes the user to the recipe's editing form. Finally, the third column contains a trash-can icon, which provides the user with the option to delete the corresponding recipe. Upon clicking the icon, the user is redirected to a confirmation page, where they can confirm their intention to delete the recipe.

If the user has not created any recipes yet, instead of a table a text is shown saying, 'Looks like you haven't added anything just yet! Share your recipes with us here', the word 'here' at the end serves as a hyperlink to the recipe creation form.

The second table holds entries that have been saved by the user. Three table columns hold information about the recipe's name, which is also a hyperlink to the corresponding recipe's detailed page, the recipe's author, and a button to 'unsave' or 'delete' recipes from this list. Any recipe on the website can be saved, and it only takes one click to add them to this list. If, however, the user has not saved any recipes yet, instead of a table a text is present, saying 'Any recipe you fancy will be saved here for You', the word 'recipe' serves as a hyperlink to the recipes page.

<details>
  <summary>image of the currently empty 'My Stuff' page of a user</summary>

![image of the my stuff page](static/images/my_stuff.png)

</details>

<details>
  <summary>image of the filled 'My Stuff' page of a user</summary>

![image of the my stuff page filled with data](static/images/my_stuff_added.png)

</details>

### Recipe detail page

<hr>

At this point, the users have more ways to access a detailed page of a recipe, but the most straightforward way is to access them via the recipes page. Clicking on a recipe card will take the user to the detailed page of the recipe, where they can see the title, the author, and the date of creation of the recipe they clicked on. There is also a button that shows up for registered users which is the 'save' button. Clicking this button will 'save' this recipe to the user's 'my saved recipes' table mentioned earlier. If a recipe is not 'saved' an empty flag icon is present. After clicking this button the icon changes to a solid flag and an alert message pops up saying that the current recipe the user is viewing has been successfully saved to their list. Clicking again this button replaces the icon to its original form and an alert message pops up saying that the current recipe the user is viewing has been removed from their saved recipes list. This process can also be done on the 'My Stuff' page.

If the user is viewing the detailed page of a recipe that they created, there are also two icons present next to the 'save' button. These are the pencil icon for editing and trash can icon for deleting of the current recipe.

The first row of the detail section shows an image of the recipe, which is either a placeholder image or an image of the actual recipe if it was provided by the author. Next to the image, A short details section gives information about the recipe's type, preparation and cooking time, the calories and serving size and difficulty.

<details>
  <summary>image of page details section</summary>

![image of recipe detail page's details section](static/images/recipe_details.png)

</details>

The next section is the ingredients and method sections which hold information regarding the ingredients and the steps to follow.

<details>
  <summary>image of ingredients and method section</summary>

![image of recipe detail page's ingredients and method section](static/images/ingredients_and_method.png)

</details>

At the bottom of the recipe detail page, a comment section can be found which is only available to the registered users of the website. If there are no comments yet under a recipe, a text is shown saying 'Be the first to comment!' with the comment form next to it. The comment form is a text area where people can write and submit a comment with the button below. Doing so will display the newly submitted comment and make an alert pop-up that the comment has been added. The current username is also reflected on the form. If there are comments under a recipe, they are listed below each other with the most recent comment at the top. Each comment has information about the author and the date of creation. If the current user is the author of a comment, a pencil icon for editing and a trash can icon for deleting the comment is shown. The pencil icon takes the user to the comment editing form where they can update and resubmit their comment. Doing so will make an alert pop-up saying that the comment has been updated successfully. Clicking on the trash-can icon will take the user to a confirmation page, where they need to affirm their intentions.

<details>
  <summary>image of comments</summary>

![image of the recipe detail page's comment section](static/images/comments.png)

</details>

<details>
  <summary>image of an empty comment section</summary>

![image of an empty comment section](static/images/comments_empty.png)

</details>

### Authorization pages

#### Register

If a user decides to register to the website, they can do so by clicking either on the 'Register' button in the navbar or by clicking the call to action button on the landing page. Both actions will take the user to the sign-up form, where they need to choose a unique username and password. The E-mail address is set to optional. If the user has already registered to the website, there is a link at the top that will take them to the login form if clicked.

<details>
  <summary>image of register page</summary>

![image of the registering form](static/images/register.png)

</details>

#### Login

If a user wants to log in after returning to the website they can do so, by clicking on the login button in the navbar. Here they need to type in their username and password and they can make the website remember them, so they don't have to log in every time they visit the website. If the user is not registered yet and therefore can not use the login form to enter the website, a link is present at the top that will take them to the signup form. If the user filled out the login form and pressed the sign in button they are then taken back to the landing page with an alert message saying that they have successfully logged in.

<details>
  <summary>image of login page</summary>

![image of the login form](static/images/login.png)

</details>

#### Logout

If a user wants to sign out, they can do so by clicking on the Logout link on the navigation bar. This action will take the user to the Sign Out page where they can choose to click on 'Sign Out' or 'Back to recipes' buttons. Clicking on 'Sign Out' will take the user back to the landing page with a message saying they have successfully signed out.

<details>
  <summary>image of logout page</summary>

![image of the logout form](static/images/logout.png)

</details>

### Forms

#### Creating a recipe

Navigating to the creating form of a recipe can be done more than one way at this point. The form has a Recipe name field, a type field, a checkbox for marking the vecipe as vegan, an ingredients and method field, preparation time and cooking time, serving size, calories and difficulty. Lastly, the user can provide an image for the recipe but it's not mandatory. If the user doesn't provide an image, a placeholder image will be shown instead on the recipe card and the recipe's detailed page as well. Submitting the form will take the user back to the recipes page and an alert message pops up saying the recipe has been added successfully. 

<details>
  <summary>Adding a recipe</summary>

![image of the recipe form](static/images/recipe_create.png)

</details>


Reaching the editing page of a recipe can be done more than one way at this point. This form is very similar to the creating form except all the fields are pre-populated with the existing data, and the user is able to manipulate every field and submit their updated version. The form also tells the user when the recipe was added, and when was it last updated. If the user submits the updated recipe an alert message will pop up saying that the update was successful.

<details>
  <summary>image of editing form</summary>

![image of the recipe editing form](static/images/recipe_edit.png)

</details>

The comment editing form can only be accessed through the recipe detail page where the comment the user wants to edit is present. There he can click on the pencil icon mentioned earlier which takes them to the comment editing form page where they can edit and resubmit their comment. Doing so will take them back to the recipes page and an alert message will pop up saying the comment was updated successfully.

<details>
  <summary>image of comment edidting form</summary>

![image of the comment editing form](static/images/comment_edit.png)

</details>

Deleting either a recipe or a comment can be done by finding a trash-can icon of the recipe or the comment the user wants to delete. Clicking the trash-can icon will take them to a page where they need to confirm their action. Deleting an item will take them back to the recipes page with an alert saying the request for deletion was successful, and the item no longer exists.

Before a delete request can be processed, the user needs to confirm this with a form. Confirming the deletion will take the user back to the recipes page and an alert will pop up saying that the deleting was successful.

<details>
  <summary>image of delete form</summary>

![image of the delete form](static/images/confirm_delete.png)

</details>

As mentioned earlier, there are four custom error pages provided to the website. The most common is the 404 which is shown to the user if they navigate to a page that does not exist, for example if they are trying to reach a recipe that has been deleted.

<details>
  <summary>image of error 404 page</summary>

![image of the error 404 page](static/images/error404.png)

</details>

## Defensive design

### Recipe form

Default form validations of the recipe form provided by django
* The recipe has to be unique, so if the user tries to add a recipe with the same name more than one time they will be informed that a recipe with the same name already exists.
* The form can not be submitted without specifing the recipe's type
* The form can not be submitted with an empty ingredients field
* The form can not be submitted with an empty method field
* The form can not be submitted without selecting the preparation time
* The form can not be submitted without selecting the cooking time
* The form can not be submitted without selecting a difficulty

The following custom validations have been added to the recipe form
* The maximum character count for the ingredients is capped at 1500 characters, the form can not be submitted with more characters than 1500 characters in the ingredients field
* The maximum character count for the method is capped at 4000 characters, the form can not be submitted with more characters than 4000 characters in the ingredients field
* The serving size can not be 0
* The serving size can not be more than 99, as it should be a realistic number
* The amount of calories per serving can not be less than 50
* The amount of calories per serving can not be over 5000, as it should be a realistic number

### Comment form

Default form validations of the comment form provided by django
* The comment form can not be empty

Custom validation for the comment form
* The length of the comment text can not be more than 300 characters

## Future Implementations

### Ideas for later

<hr>

 * A complete profile page with a profile picture that shows up on the user's profile, by their added recipes, and by their comments
 * The ability to like a recipe
 * The ability to rate a recipe by the users, get general feedback and emphasize the best recipes
 * Give users the ability to send private messages to other members
 * Give users the ability to view other members' profile pages where their added recipes are listed
 * A blog page where the admin can suggest recipe books to the users and give them advice regarding handy devices and tools for cooking

### Things did not get implemented at this stage

<hr>

 * Design a visually more pleasing recipe detail page.
 * Make the Django Summernote text field strip the styling of the text if a user is trying to paste it from an external source.
 * Prevent the page from reloading when the save/unsave button is pressed.

### Accessibility

<hr>

* With keeping accessibility in mind, I provided aria-label texts to hyperlinks as well as to buttons. Also, descriptions of the images can be found throughout the website.

* I tried using colours that are visually appealing while also maintaining a good contrast so that every text is easily readable.

* The current page the user is viewing is reflected in the navigation bar by highligting


![image of the lighthouse extension's report](static/images/ligthhouse_report.png)

### Validation with external tools

#### W3C HTML validator

![image of the w3c html validator's result](static/images/)

### W3c CSS validator

![image of the w3c css validator's result](static/images/)

### JSHint JavaScript validator

![image of the JSHint JavaScript validator's result](static/images/)

### Code Institute's Python Linter

![image of Code Institute's Python Linter's result](static/images/)

## Technologies Used

<hr>

### Languages Used

<hr>

* HTML
* CSS
* JavaScript
* Python

### Frameworks, libraries and other external tools

<hr>

* [Cloudinary](https://cloudinary.com) - for storing images
* [Django Framework](https://www.djangoproject.com/) - for rapid development and maintaining the database of the website
* [Django-Crispy-Forms](https://django-crispy-forms.readthedocs.io/) - for rendering forms
* [Django-Allauth](https://django-allauth.readthedocs.io) - for authorization
* [Django-Filter](https://django-filter.readthedocs.io/) - for creating a filter for my Recipe model
* [Django-Summernote](https://summernote.org/) - for rendering textfields in the forms
* [Gunicorn](https://gunicorn.org/) - for HTTP requests and to run a Python web application.
* [Psycopg2](https://pypi.org/project/psycopg2/) - for PostgreSQL engine
* [ElephantSQL](https://www.elephantsql.com/) - for storing database 
* [Bootstrap 5.3.0](https://getbootstrap.com/) - for accelerated styling and responsiveness of the website
* [One Page Wonder](https://startbootstrap.com/theme/one-page-wonder) - for navbar, header footer and a circle image styling
* [jQuery](https://jquery.com/) - for hiding alert messages automatically and set the progress bar's colors based on the difficulty
* [Git](https://git-scm.com/) - for version control
* [GitHub](https://github.com/) - for storing the project repository
* [Gitpod](https://gitpod.io/) - as an IDE for creating the code
* [Heroku](https://dashboard.heroku.com/) - for deploying the application
* [Figma](https://www.figma.com/) - for creating a mock-up landing page
* [Coolors](https://coolors.co/) - for visual representation of the colours used on the page
* [Favicon](https://favicon.io/) - for creating the favicon
* [Cssgradient](https://cssgradient.io/) - for adding an overlay to the background image
* [Picresize](https://picresize.com/) - for resizing images
* [Google Fonts](https://fonts.google.com/) - Paytone One font
* [Font Awesome](https://fontawesome.com/) - for using icons
* [Pexels](https://pexels.com/) - for the background image


### Validators

<hr>

* [W3C Markup Validation](https://validator.w3.org/)
* [W3C Jigsaw](https://jigsaw.w3.org/css-validator/)
* [JSHint](https://jshint.com/)
* [CI Python Linter](https://pep8ci.herokuapp.com/)

### Deployment

<hr>

 1. Navigate to [GitHub](https://github.com/) in the browser
 2. Open the [Code Institute Full Template](https://github.com/Code-Institute-Org/ci-full-template) provided by [Code Institute](https://codeinstitute.net/ie/)
 3. Click **'Use this Template'** button and select **'Create a new repository'**
 4. Enter a name for the project and an optional description
 5. Click the **'Create Repository from Template'** button
 6. Once the repository is created we can open a new workspace with [Gitpod](https://gitpod.io/workspaces/) 2 ways:
    * We can either install a Google [chrome extension](https://www.gitpod.io/docs/configure/user-settings/browser-extension) provided by gitpod
      1. If we added this extension to our Google Chrome browser, a green 'Gitpod' button will show up in our newly created repository
      2. Clicking this button will generate a new workspace with Gitpod's [integrated development environment](https://en.wikipedia.org/wiki/Integrated_development_environment) where we can start working on our project
    * Or we can use our GitHub repository's URL
      1. Copy the repository URL from the browser
      2. Enter gitpod.io/# in the browser and change the '#' symbol to our GitHub repository's URL

<br>

 7. When the workspace is up and running we need to set up our Django environment first, to do that:
      1. Install Django by entering the following in the terminal: ```pip3 install 'django<4'```
      2. Install [psycopg2](https://pypi.org/project/psycopg2/) PostgreSQL database adapter, by entering the following in the terminal: ```pip3 install dj3-cloudinary-storage```
      3. We need to add every supporting dependencies and libraries to a **'requirements.txt'** file by entering the following in the terminal after a dependency like **psycopg2** has been installed: ```pip3 freeze --local>requirements.txt``` (this will create a **requirements.txt file in our local repository which is important for deploying the project later)
      4. Create our project by entering the following in the terminal: ```django-admin startproject 'PROJECT_NAME' .``` (replace **'PROJECT_NAME'** with out desired name for the project, also don't forget to add the '.' at the end of the command.)
      5. Create a new App by entering the following in the terminal: ```python3 manage.py startapp APP_NAME``` (replace the **'APP_NAME'** with the desired name for the app)
      6. After the app has been created and showed up in our local directory, we need to add the app to the **INSTALLED_APPS** list in our **PROJECT_NAME** folder's **SETTINGS.py** file
      7. After our **APP_NAME** has been added to the **INSTALLED_APPS** enter the following in the terminal: ```python3 manage.py makemigrations```, followed by ```python3 manage.py migrate``` (this will create our skeleton django project)
      8. In order to see how our django skeleton project looks rendered in the browser, we need to add **'localhost'** to the **ALLOWED_HOSTS** in our **PROJECT_NAME** folder's **SETTINGS.py** file
      9. Now we can run a local server with the following entered in the terminal: ```python3 manage.py runserver```
      10. Click **Open Browser** to see the rendered application in the browser
 
<br>

 8. For deploying the website we need to set up [Heroku](https://heroku.com/) cloud platform service
      1. Create a new account on Heroku and connect it with our GitHub account
      2. Sign in to our Heroku profile
      3. Click on **'New'** and select **'Create new app'**
      4. Name the app and choose the region(select Europe)
      5. Once the app is created, navigate to the **Settings** tab and add the following Buildpack:
          * **'heroku/python'**
      6. Then add the following Config Vars:
          * **PORT** : **8000**
          * **SECRET_KEY** : **YOUR_SECRET_KEY**
          * **DISABLE_COLLECTSTATIC** : **1**
      7. Also, in **SETTINGS.py**, add ```'your-project-name-on-heroku.herokuapp.com'``` to **ALLOWED_HOSTS** list, where ```localhost``` have been already added previously

<br>

 9. Our Django database is only accessible within gitpod and is not suitable for production enviroment. The deployed project on a hosting service will not be able to access it, so we need to use [ElephantSQL](https://www.elephantsql.com/) To use this service:
      1. Create an ElephantSQL account
      2. Click on **'+Create New Instance'**
      3. Set up plan
          * Name: **'YOUR_PROJECT_NAME'**
          * Plan: **'Tiny Turtle (free)'**
      4. Select region
          * Data center: **'EU West-1 (Ireland)'** 
      5. Click on **Review**
      6. Click on **Create Instance** 
      7. In the ElephantSQL dashnoard, click on the newly added database
      8. Copy the URL with the button provided
      9. Add URL to the Heroku Config Vars
          * **DATABASE_URL** : **YOUR_DATABASE_URL_FROM_ELEPHANT_SQL** 

<br>

 10. To store our static files, we need to use [Cloudinary](https://cloudinary.com/) cloud based service. To use this service:
      1. Create a Cloudinary account
      2. Navigate to the dashboard
      3. Copy The API Environment variable with the button provided
      4. Add the following **Config Var** to  our project on**Heroku**
          * **CLOUDINARY_URL** : **YOUR_CLOUDINARY_URL**
      5. Add the following in the **SETTINGS.py** to **INSTALLED_APPS** list
          * ```'cloudinary_storage',```
          * ```'cloudinary'```
      6. Navigate to the bottom of **SETTINGS.py**
      7. Below the **STATIC_URL** variable, add:
          * ```STATICFILES_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'```
          * ```STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]```
          * ```STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')```
          * ```<empty_line>```
          * ```MEDIA_URL = '/media/'```
          * ```DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'```
      8. Navigate to the top of **SETTINGS.py** 
      9. Add the following line under the **BASE_DIR** variable
          * ```TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')```
      10. Navigate to the **TEMPLATES** variable in **SETTINGS.py** and add this to **DIRS**
          * ```[TEMPLATES_DIR]```

<br>

 11. Create a new file in our local directory and name it **env.py**
      1. Add **env.py** to the **.gitignore** file, to make sure it is not pushed to github as this file holds sensitive data
      2. at the top: 
          * ```import os```
          * ```<empty_line>```
          * ```os.environ["CLOUDINARY_URL"] = "YOUR_COPIED_CLOUDINARY_URL"```
          * ```os.environ["DATABASE_URL"] = "YOUR_DATABASE_URL_FROM_ELEPHANT_SQL"```
      3. We need to make our Django project aware of our **env.py**, in order to do this, we need to add the following at the top of **SETTINGS.py**:
          * ```import os```
          * ```import dj_database_url```
          * ```if os.path.isfile('env.py'):```
          * ```import env```
      4. Now that this is done we can add our secret key to **env.py**
          * ```os.environ["SECRET_KEY"] = "YOUR_SECRET_KEY"```
      5. Then in **SETTINGS.py** ,add:
          * ```SECRET_KEY = os.environ.get('SECRET_KEY')```
      6. Find the **DATABASES** variable in **SETTINGS.py** and comment out the url above it and the **DATABASES'**  dictionary entirely
          * The reason for doing this is because the commented out code connects our Django application to the created db.sqlite3 database within our repository. However, as we know, that database is not suitable for production.
      7. and add the following:
          * ```DATABASES = {'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))}```
      8. Finally, it's now safe to save our changes, and push it to our repository in GitHub, to do this enter the following in the terminal:
          * ```git add .```
          * ```git commit -m "Add your commit message here"```
          * ```git push```
  12. In order to push the changes to Heroku and make our initial deployment we need to create a file, called **Procfile** in our local directory, and add the following to it:
        * ```web: gunicorn steezyspatula.wsgi```
  13. On Heroku, select our project and Navigate to the Deploy tab and select GitHub as the Deployment method
  14. Click Connect to GitHub
  15. With our GitHub profile selected, search for the correct GitHub repository and click "Connect"
  16. Once the connection is done, select Enable Automatic Deploys (to make sure Heroku rebuilds the latest version after the final changes have been pushed to GitHub)
  17. Finally select Deploy Branch in Manual deploy to make the initial deployment. (Automatic deploys work only after this step.)

  18. Now that our Django environment is up and running, we can start working on our project by following Django's [MVT(Model View Template)](https://www.geeksforgeeks.org/django-project-mvt-structure/) structure
       * each time we want to create a view we need to do 3 things:
          1. Create the **view** in the **APP_NAME** directory's **views.py** file
             * here we can create functions and classes
          2. Create the **url path** for the **view** in the **APP_NAME** directory's **urls.py** file
          3. Create the **template** for the **view** to render in the specified **url path**, these are our custom html files added to our project's template folder in the root directory
  19. We can now add models to our project within our **APP_NAME** folder's **models.py** file
       * every time we create, update or alter a model, or any field within our model we need to **save**, and type the following to the terminal:
          1. ```python3 manage.py makemigrations```, this will create a migration file with the applied changes to the database model
          2. ```python3 manage.py migrate```, this will apply the changes to our database model

<hr>

## Important Notes
 * in our **PROJECT_NAME** folder's **SETTINGS.py** file, we mustn't leave **DEBUG = True** for production, before final deployment we **HAVE TO** set this variable to **False**, we can do so by:
   * Either setting ```DEBUG = False``` manually in **SETTINGS.py**
   * Or by adding the following lines in **env.py**, and in **SETTINGS.py**
      * in **env.py**: ```os.environ['DEVELOPMENT'] = "1"```
      * in **SETTINGS.py**: ```DEBUG = 'DEVELOPMENT' in os.environ```
      * this way Debug mode will only be active during development

 * If we want to see what changes will be applied to our model before migrating we can type the following in the termina:
    * ```python3 manage.py makemigrations --dry-run```
       * This will perform a 'dry run' of the migrations that would be generated by ```python3 manage.py makemigrations``` command without actually modifying the database schema
       * This allows us to preview the migrations before actually applying them and we can make sure not to cause any unintended changes

 * After we have installed any packages to our project in the terminal with the command: ```pip3 install <name_of_the_package>```
   * we must add them to our requirements.txt with the following line entered after the installation in the terminal: ```pip3 freeze --local>requirements.txt```
     * This command will create a requirements.txt in our working directory when first entered
     * the '--local' flag means that only our locally installed packages need to be added to the requirements.txt, rather than all packages installed on the system
     * the '>' symbol redirects the output of the command to the file, in this case ```requirements.txt```

 * If we are getting an error when trying to use the command: ```python3 manage.py migrate```,
   * enter the following in the terminal: ```unset PGHOSTADDR```
      * this command removes the environment variable **'PGHOSTADDR'** which is an environment variable used by PostgreSQL database to define the address of the host where the database is running.
  
 * During production we can add the **DISABLE_COLLECTSTATIC** environment variable to our project's **Config Var** on Heroku to **1**
     * The value **1** means **True** in this context
     * By setting this **key** to **True**, we are telling Django not to collect static files into the **'STATIC_ROOT'** directory
     * The reason for doing this, is to reduce the size of the deployed application and improve the performance of the deployment process
     * When we are finished developing our project we need to remove it from the **Config Vars**

### Forking

<hr>

Use forking, when you want to contribute to an existing project, by creating a copy of the original repository

1. Login to GitHub profile
2. Navigate to [this repository](https://github.com/GaborFicsor/steezy-spatula)
3. Navigate to the top right corner of the sceen, and click on the **'Fork'** button
4. Select **Create new fork**
5. Once the process is complete, you will be redirected to the newly forked repository

### Cloning

<hr>

Use cloning, when you want to work on a project locally and make changes without affecting the remote repository

1. Login to GitHub profile
2. Navigate to [this repository](https://github.com/GaborFicsor/steezy-spatula)
3. Click on the green **'Code'** button
4. Click on the clipboard icon to copy
5. In [Gitpod](https://gitpod.io/workspaces/), click on the green button **'New Workspace'**
6. Enter the following in the terminal:
   * ```git clone <repository_copied_to_clipboard>```
7. Press Enter to generate local clone.


## Testing

<hr>

## Bugs

<hr>

### Solved

<hr>

* Model relation During early development, I had issues with my models, when I was trying to connect my Recipe model with a many-to-many relationship to a model called Allergens. My lack of understanding of how a many-to-many relationship should work ended me up breaking my models beyond repair. Not even deleting the model from the models.py helped. I had to contact Code Institute Tutor Support where Jason helped me out a lot by giving instructions on how to reset my database.

* Rendering form field in template:
At a later stage in development, I was trying to render the filter form in my recipe template. At this stage, it had 3 fields to filter by, of which one was a TextInput field to look up recipes. I wanted to render every field individually to be able to style them easier, rather than using crispy forms, but my text field would not want to render. When I tried to render {{ form.recipe_name|as_crispy_field }} I got an error stating that the field that I am trying to pass is either non-existent or invalid. I had to contact Code Institute Tutor Support where Joshua pointed out that I am using the icontains lookup type the wrong way. Adding lookup_expr='icontains' to the variable inside the RecipeFilter Class solved this problem and the field was rendering as expected. 

* Pagination bug, during manual testing I found that after filtering the recipe list I was able to look through the paginated views in my recipes template, by viewing the next pages, however, when I tried to click on the previous page the filtered list was not working properly and every recipe got listed again without filtering. Replacing the correct url inside the first and previous page-links solved this problem


## Credits

<hr>

* [Django Class Based views filtering](https://gist.github.com/MikaelSantilio/3e761b325c7fd7588207cec06fdcbefb)
* [Special Hack To Style Pagination With Bootstrap](https://www.youtube.com/watch?v=wY_BNsxCEi4)
* [Display Multiple Queryset in List View](https://stackoverflow.com/questions/48872380/display-multiple-queryset-in-list-view)
* [Pagination using ListView and dynamic/filtered queryset](https://stackoverflow.com/questions/52007038/pagination-using-listview-and-a-dynamic-filtered-queryset)
* Comment model - Code Institute's I think therefore I blog walkthrough project
* Alert timeout - Code Institute's I think therefore I blog walkthrough project


### Media

<hr>

* [Background image - from pexels](https://www.pexels.com/hu-hu/foto/kenyer-elelmiszer-szendvics-egeszseges-1565982/)
* [Placeholder recipe image - from pexels](https://www.pexels.com/hu-hu/foto/egeszseges-fa-textura-asztal-349609/)
* A picture of me - represented by my favourite Teddy Bear
* [Favicon](https://favicon.io/)

  
###  Acknowledgments

<hr>

I would like to thank
 * my girlfriend, for testing the usability and user experience of the website, as well as creating a profile and uploading recipes.
 * my Mentor [Jubril Akolade](https://github.com/Jubrillionaire) for taking the time to review my project and answering my questions.
 * Code Institute Tutor staff: Joshua, Ed, and Jason for helping me out with problems I would have not be able to solve on my own.
