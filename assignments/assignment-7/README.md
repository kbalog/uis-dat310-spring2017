# Assignment 7 - Webshop

This exercise builds on assignment 3 from before. The static webshop prototype will now be developed into a dynamic site using Flask and MySQL.

You can work with your submission from before or can also choose to work with the reference solution; the reference solution can be downloaded from the assignments repository (https://github.com/uis-dat310-spring2017/assignments-2017/tree/master/3/solution).

  *	Use templates instead of static HTML pages
    - Pages should share the same "HTML frame" (i.e., the `<html>`, `<head>`, `<body>` elements should be present only in a single template file `layout.html`)
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
        - Name, email, telephone, and shipping address (postcode, city, street) are obligatory fields. It's not possible to go to the next step unless these are provided. You application should "remember" the values the user already filled in (i.e., in case there is an error, only the missing parts need to be completed, the rest of the values are remembered).
    - Confirmation page
  * Upon confirmation of the order, store it in a database and display the order number
      - Store the order "head" in one table (order_id, name, email, telephone, address, etc.) and the order items in another table (order_id, product_id, quantity).

The skeleton of the solution is provided, which implements the main program logic.

Commit and push files to GitHub.

You also need to submit a dump of your database in a `database.sql` file.  Executing this file should create all the tables that are needed for your application and should insert product data.


# Øving 7 - Webshop

Denne oppgaven bygger videre på øving 3 fra tidligere. Den statiske nettbutikken skal nå bli utviklet til å bli en dynamisk side, ved bruk av Flask og MySQL.

Du kan bygge videre på dine egne filer du har fra den tidligere innleveringen, eventuelt kan du bruke filene fra løsningsforslaget. Løsningsforslaget kan lastes ned fra "assignments repository" (https://github.com/uis-dat310-spring2017/assignments-2017/tree/master/3/solution).

  * Bruk maler (templates) istedenfor statiske HTML sider
    - Sider skal dele samme "HTML ramme" (`<html>`, `<head>`, `<body>` elementene skal bare være å finne i én mal-fil (template file) `layout.html`)
  * Lag en tabell for lagring av produktinformasjon
    - Lagre produktid, navn, beskrivelse, vanlig pris, bonus pris, og bilde
    - Legg til minst 6 produkter i tabellen
  * Last produktene fra databasen når de listes opp på startsiden (index page) og når de vises med detaljer på produktsiden (product page)
  * Produkter skal kunne legges til i handlekurven
    - Handlekurven må lagres i en økt (session)
  * Vis innholdet i handlekurven
    - Brukeren skal kunne fjerne produkter fra handlekurven og endre antall
  * Implementer utsjekkprosessen, som har tre steg
    - Viser innholdet i handlekurven
    - Viser ordredetaljer (navn, faktura- og sendingsadresse, etc.)
      - Name, email, telephone, og shipping address (postcode, city, street) er obligatoriske felt. Det er ikke mulig å gå til neste steg uten at disse er fylt inn. Ved feil, skal applikasjonen huske verdier som allerede er fylt inn (slik at bare deler som mangler trengs å bli fylt ut, mens resten blir husket fra tidligere)
    - Bekreftelsesside
  * Ved bekreftelse av ordre, lagre infoen i en database og vis ordrenr
      - Lag ordre "head" i en tabell (order_id, name, email, telephone, address, etc.) og ordre elementer i en annen tabell (order_id, product_id, quantity).


Du er gitt grunnkoden, som implementerer hovedfunksjonene til programmet som du ikke trenger å tenke på.

Last opp til GitHub (commit og push).

Du må også lage en dump av databasen i en `database.sql` fil. Utfører denne filen skal lage alle tabellene som er nødvendig for din applikasjon og skal sette inn produktdata.
