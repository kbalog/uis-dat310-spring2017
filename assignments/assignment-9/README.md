# Assignment 9 - Webshop admin

*DRAFT*

Your task is to develop an admin back-end for the webshop using a combination of technologies (Flask, MySQL, Bootstrap).

There are no starter files provided for this assignment.
You need to use Flask with templating, Bootstrap, and MySQL for implementing the functionality below. It is allowed to use any external Python package/module and Bootstrap component, plugin, or add-on.

  * Login
    - All the functionality described below should be available only to logged in admin users. Login is based on a username and password combination.
    - There is no need to implement front-end functionality for adding new admin users. But you need to add a test user to your database dump that we can use for testing, username: "test" password: "dat310A9". You need to store passwords in a secure way in the database (i.e., no raw password strings).
  * Product management
    - The user needs to be able to list, add, delete, and edit products.
    - On the product edit/add form, check that
        - Product name is not empty
        - Price and bonus price are not empty and are numbers
        - Bonus price cannot be higher than the normal price
        - Photo is provided
    - If an error appears, then show an alert and remember the form values already filled in.
    - Note that it is part of the task to be able to modify product photos. New products can only uploaded if a photo is provided.
  * Order management
    - The admin user can list all the orders that have been registered.
    - Upon clicking on an order, show the order details, with links to the product pages.
    - Your database should contain at least 20 orders (You can generate "fake orders" with a script.)
  * Statistics
    - Provide a plot which shows the number of orders over time. I.e., for each day, show the number of orders that were registered on that day.
    - Provide a list of the "most popular products", i.e., products that have been ordered the most. Show the product ID, product name, and the total order quantity for that product.
  * General
    - When listing products or orders, show at most 10 products on a page and let the user paginate between pages.
    - All forms and alert/success messages must also be styled using Bootstrap.

It is up to you how you organize this functionality on the admin user interface (i.e., what menu points you have, etc.).
*Some example screenshots will be made available later, but these do not need to be strictly followed.*

Commit and push files to GitHub. You also need to submit a dump of your database in a `database.sql` file.  Executing this file should create all the tables that are needed for your application and should insert product and order data.


# Øving 9 - Webshop admin

*Norsk oversettelse kommer snart.*
