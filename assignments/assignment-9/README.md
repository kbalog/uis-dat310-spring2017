# Assignment 9 - Webshop admin

## Updates

  * File upload example has been added [under the flask examples](/examples/python/flask/8_file_upload). See also the [Flask documentation](http://flask.pocoo.org/docs/0.12/patterns/fileuploads/).
  * For plotting, you may use a JavaScript library, e.g., [D3.js](https://d3js.org/) or [Chart.js](http://www.chartjs.org/).
    - E.g., [bar chart in D3.js](http://bl.ocks.org/d3noob/8952219) or [line chart in Chart.js](http://www.chartjs.org/docs/#line-chart-introduction).

## Task

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

Din oppgave er å utvikle en admin back-end for webshop-siden ved bruk av en kombinasjon av teknologier (Flask, MySQL, Bootstrap).

Det finnes ingen startfiler for denne oppgaven.
Du må bruke Flask for tamplating, Bootstrap og MySQL for implementering av funksjonaliteten beskrevet under. Det er tillat å bruke eksterne Python packages/modules og Bootstrap components, plugins eller add-ons.

  * Login
    - All funksjonalitet beskrevet under skal bare være tilgjengelig for brukere logget inn som admin. Innlogging er basert på kombinasjon av brukernavn og passord.
    - Det er ikke nødvendig å implementere en front-end funsjonalitet for å legge til nye admin-brukere. Men du må legge til en testbruker i din databasedump som vi kan bruke til testing, username: "test", password:"dat310A9". Du må lagre passord på en sikker måte i databasen (ergo, ingen raw passord strings).
  * Product management
    - Brukeren må ha muligheten til å liste opp, legge til, slette og endre produkter.
    - På produkt edit/add formen, sjekk at
        - Produktnavn ikke er tomt
        - Pris og tilbudspris ikke er tom og at det er tall
        - Tilbudspris kan ikke være høyere enn normalpris
        - Bilde er gitt
    - Hvis en feil oppstår skal det vises en alert og formverdiene som allerede er tastet inn skal huskes.
    - Vær oppmerksom på at det er en del av oppgaven å kunne modifisere produktbilde. Nye produkter kan bare legges til om et bilde er gitt.
  * Order management
    - Admin-brukeren kan liste opp alle ordre som er registrert.
    - Når man klikker inn på en ordre skal det vises ordredetaljer med link til produktsidene.
    - Din database skal inneholde minst 20 ordre (du kan generere "fake ordre" med et skript).
  * Statistics
    - Gi et plott som viser antall ordre over tid. Dvs. for hver dag, vis antall ordre registrert den dagen.
    - Gi en liste av de mest populære produktene, dvs. produkter det har blitt bestilt mest av. Vis produkt-id, produktnavn og totalt antall bestillinger av produktet.
  * General
    - Når produkter eller ordre listes opp, vis maks 10 produkter per side og la brukeren bla mellom sider.
    - Alle former og alert/success messages skal også styles ved hjelp av Bootstrap

Det er opp til deg hvordan du organiserer funksjonaliteten på admin-brukergrensesnittet (dvs. hvilke menypunkter du har med, etc.).

Commit og push filene til GitHub. Du må også submitte en dump av databasen din i en `database.sql` fil. Kjøring av denne filen skal lage alle nødvendige tabeller for å kunne bruke din applikasjon og den skal sette inn produkt- og ordredata.
