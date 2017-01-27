# Assignment 3 - Webshop prototype

In this assignment you need to create a prototype for a webshop using HTML and CSS. The prototype consists of three HTML pages (main page, product page, and shopping cart) and a single stylesheet file (style.css).

Under the `3/samples/` folder of your your GitHub repository you will find screenshots that serve as examples of what you need to create. You don't have to produce the exact same output that is shown on the samples, you can deviate from it in any way you want (especially in the content) as long as you follow the instructions given below.


### All pages

  *	Include the same header and footer
    -	The header shows the name of the webshop (you can also add a logo)
    -	The main menu is part of the header and is horizontally aligned. It has to be an unordered list inside a <nav> element
    -	The footer always stays at the bottom of the page, but "scrolls away" (i.e., when the page is long, you need to scroll down to see the footer)
        -	Hint: http://mystrd.at/modern-clean-css-sticky-footer/
    -	The footer contains contact information (tel, email) and icons of (at least) three social media platforms
  *	There must be (at least) *10px* padding on the left between the window and the content (backgrounds do not count as content and they should use 100% width of the window)
  *	Use the following HTML5 elements: `<header>`, `<footer>`, `<main>`, `<nav>`, `<article>`
  * Fonts:
    - Sans-serif font family.
    - All headings are typeset *Montserrat*, all other text is typeset *Raleway*.
        - http://fonts.googleapis.com/css?family=Montserrat
        - http://fonts.googleapis.com/css?family=Raleway
    - Font sizes are controlled by the browser; all font sizes need to be set relative, using *em*
  * The page background color is *white*
  *	Images must have alt attributes
  *	Design for normal (desktop) screen sizes (we are not developing for small screens now)
  *	Use Font Awesome icons by linking the Bootstrap CDN CSS file
    -	Paste the following code into the `<head>` section of your pages
`<link rel="stylesheet" href="http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css">`
  *	Using Bootstrap (or any other CSS framework), except the above include, is not allowed!
  * The layout has to be achieved using CSS; tables can only be used for the contents of the shopping cart!


### Main page (index.html)

  *	Contains a full-page-width banner with special deals
    -	Size: *806x240px*
    -	The banner may contain images, but the text has to be put on using CSS
  *	Lists (at least) 6 different products
    -	Put each product inside an `<article>` element
    -	Three products per row
    -	Product box is *260x370px* (excluding borders), with *10px* spacing between the product boxes
    -	Image size is *250x250px*
    -	Product name is in `<h3>`
    -	Price is shown in the bottom right corner
        -	Strike out the old price and show the new price in a different color if the item is on sale
    -	Change the appearance of the product box on mouseover (for example, change the background or borders)
  *	Special deals are shown in the top right corner of the product boxes
    -	Use a *60x40px* box that overlays the product image (set `z-index: 1`)
    -	The text in the box has to be *center-aligned* both horizontally and vertically


### Product page (product.html)

  *	Show the product image in *350x350px* size with a border around it
  *	Display the special deal the same way as on the main page
    -	*60x40px* box that overlays the image, text is *center-aligned* both horizontally and vertically
  *	Show the product's name and description on the right side of the image
  *	Display an "Add to cart" button and the product's price on the same row


### Shopping cart (cart.html)

  *	Display a "Shopping cart" heading in `<h2>`
  *	Present a table with the contents of the shopping cart
    -	The table contains at least 2 different items
    -	For each item, show the thumbnail (in *50x50px*), product name, item price, quantity and price
    -	The numerical fields (price, quantity, price) have to be aligned to the right
    -	Display edit and delete icons next to the quantities
    -	Include a summary row with the total amount
    -	The cells with the items have borders, the header and total rows do not have borders
  *	Show a checkout button

Commit and push the files you created (`index.html`, `product.html`, `cart.html`, and `style.css`) to GitHub.



# Øving 3 - Webshop prototype

I denne oppgaven skal du lage en prototype for en nettbutikk med hjelp av HTML og CSS. Prototypen skal inneha 3 HTML sider (Hovedsiden, Produktsiden og Betalingssiden (check-out/shopping cart)). Disse skal "styles" med en CSS fil (style.css)

Under `3/samples/` mappen av startfilene finner du skjermbilder som skal fungere som eksempel av hva du skal lage. Du trenge ikke å lage en eksakt kopi av bildene, og så lenge du følger instruksjonene under kan du forandre på dem som du ønsker (spesielt i innhold).


### På alle sider:

  *	Skal ha samme header og footer
    -	Header skal vise nettstedets navn (du kan også inkludere en logo)
    -	Hovedmeny er en del av header og skal orienteres vannrett. Det må være en unordered list inni et `<nav>` element
    -	Footer skal alltid være på bunnen av siden. Den skal ha slik karakter at hvis siden er lang,så må man skrolle nedover til bunnen av siden for å see den.
        -	Hint: http://mystrd.at/modern-clean-css-sticky-footer/
    -	Footer skal vise kontakt info (tel, email) og ikoner med (minst) 3 social media platforms
  *	Det skal være minst *10px* padding mellom skjerm og sideinnhold. Bakgrunnen regnes ikke som innhold, den skal dekke 100% av skjermens bredde.
  *	Følgende  HTML5 elementer skal brukes: `<header>`, `<footer>`, `<main>`, `<nav>`, `<article>`
  * Font:
    - Sans-serif font familie
    - Alle headings er av typen *Montserrat*, all annen tekst av typen *Raleway*
        - http://fonts.googleapis.com/css?family=Montserrat
        - http://fonts.googleapis.com/css?family=Raleway
    - Font størrelse er kontrollert av nettleser; ergo må de alle være relative, med bruk av *em*
  *	Bakgrunnsfargen skal være *hvit*
  *	Dimensjonsmessig skal siden designes for vanlige dataskjermer. Ikke tenk på mindre dimensjoner nå.
  *	Fonten "Awesome" skal anvendes ved å linke til Bootstrap CDN CSS fil
    -	Paste følgende kode in i `<head>` seksjonen på sidene: `<link rel=”stylesheet” href=”http://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css”>`
  *	Med unntaket i forige punkt, er det ikke lov å anvende Bootstrap (eller andre CSS framework)
  * Layout må være oppnådd ved hjelp av CSS; tabeller kan brukes kun til innholdet i handlekurven!


### Hovedside (index.html)

  *	Inneholder en banner som strekker seg over hele skjermens brede. Denne skal vise tilbud og kampanjer som butikken fronter.
    -	Størrelse: *806x240px*
    -	Banneret kan inneholde bilder, men tekst skal settes på med bruk av CSS
  *	Skal liste opp (minst) 6 forskjellige produkter
    -	Hvert produkt skal være inni et `<article>` element
    -	Det skal være 3 produkter på hver rekke (row)
    -	Produkt boksene skal ha dimensjonene *260x370px* (ikke inkludert i dette er borders). Det skal være *10px* mellomrom mellom disse produkt boksene.
    -	Bilde størrelsene skal være *250x250px*
    -	Produktets navn skal være i overskriften `<h3>`
    -	Prisen skal stå i hjørnet, nederst til høyre
        -	Hvis produktet er på salg, skal den gammle prisen være strekt-ut og den nye tilbuds prisen skal stå ved siden av I en annen farge
    -	Produkt boksen skal få annerledes utseende ved mouseover (for eksempel, annerledes bakgrunn eller border)
  *	Tilbudspris skal stå øverst til høyre i produktboksene
    -	Anvend en *60x40px* som overlapper produktbilde (set `z-index: 1`)
    -	Teksten i boksen skal være sentrert vannrett og loddrett


### Produktside (product.html)

  *	Vis produktbilde med *350x350px* størrelse, det skal og være en border rundt
  *	Tilbudspris skal vises på samme måtte som beskrevet i Hovedside (index.html)
    -	*60x40px* boks som skal overlapped bildet, teksten i boksen skal være sentrert vannrett og loddrett
  *	Vis produktets navn og en beskrivelse til høyre for bildet
  *	Vis ”Add to cart” ikon på samme linje som prisen


### Shopping cart (cart.html)

  *	Vis overskriften "Shopping cart" i `<h2>`
  *	Vis en tabell som viser innholdet i shopping cart
    -	Tabellen skal inneholde minst 2 forskjellige produkter
    -	For hvert produkt, vi en thumbnail (i *50x50px*), produktnavn, pris, antall og sum (pris*antallet)
    -	De numeriske feltene pris, antall og sum skal justeres til høyre i feltene
    -	Vi edit og delete ikoner ved siden av antallet
    -	Det skal og være en totalsum rad nederst
    -	Cellene med produkter skal ha border. Header og totalsum radene skal ikke ha border.
  *	Vis en "checkout" knapp

Commit og push filene du har lagt (`index.html`, `product.html`, `cart.html` og `style.css`) til GitHub.
