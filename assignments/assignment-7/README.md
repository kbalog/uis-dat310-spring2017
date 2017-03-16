# Assignment 7 - Webshop

*DRAFT*

This exercise builds on assignment 3 from before. The static webshop prototype will now be developed into a dynamic site using Flask and MySQL.

You can work with your submission from before or can also choose to work with the reference solution; the reference solution can be downloaded from the assignments repository (https://github.com/uis-dat310-spring2017/assignments-2017/tree/master/3/solution).

  *	Use templates instead of static HTML pages
    - Pages should share the same "HTML frame" (i.e., the `<html>`, `<head>`, `<body>` elements should be present only in a single template file)
  *	Create a table for storing product information
    -	Store product identifier, name, description, normal price, bonus price, and photo
    -	Add at least 6 different products to the table
  *	Load products from the database when listing them on the index page and showing details on the product page
  *	Products can be added to the shopping cart
    -	The shopping cart needs to be stored in a session
  *	Display the contents of the shopping cart  
    - The user can remove products from the cart or change the quantities
  *	Implement the checkout process, which consists of three steps
    - Display the contents of the shopping cart
    - Providing order details (name, billing and shipping address, etc.)
      - *XXX, YYY, and ZZZ* are obligatory fields. It's not possible to go to the next step unless these are provided. You application should "remember" the values the user already filled in (i.e., in case there is an error, only the missing parts need to be completed, the rest of the values are remembered).
    - Confirmation page
  * Upon confirmation of the order, store it in a database and display the order number
      - Store *XXX, YYY, and ZZZ*

The skeleton of the solution is provided, which implements the main program logic.

Commit and push files to GitHub.

# Øving 7 - Webshop

*norsk oversettelse kommer snart*
