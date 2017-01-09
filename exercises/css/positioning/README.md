# CSS exercises, Part III. (positioning)

## Exercise #1: Hiding from a list

Make an unordered list with numbers ranging from 1 to 10 and assign a unique ID to each list element.
Then, implement the requirements below using page-level CSS.

  - Display all list elements next to each other.
  - Move the list to the left side of the page (by setting left padding to 0 on the list itself).
  - Style the list elements as follows: 
    * Set some border and background color for the boxes around the list elements.
    * Set the text center-aligned within the boxes.
    * Set the width of the boxes to 3em.
  - Make all odd list elements hidden, so that they don't take up space.
  - Make the prime elements invisible, so that their space is left empty.

![Exercise1](images/exercise1.png)


## Exercise #2: Positioning

The HTML files are given for each exercise. You are not allowed to edit the HTML structure (nor to add IDs or classes), only the CSS parts, inside `<style>`.

**#2a)** [Starter file](exercise2a.html)

Move the even boxes 10px up and the odd boxes 10px down with respect to their original position.

![Exercise2a](images/exercise2a.png)


**#2b)** [Starter file](exercise2b.html)

Create a border offset of 10px by the document. Make it entirely fluid (i.e., fill the browser window) as the document resizes (using absolute positioning).

![Exercise2b](images/exercise2b.png)


**#2c)** [Starter file](exercise2c.html)

Make the div with id `banner` appear in the top right corner of the page, 20px from the top and right sides of the window. Set the dimensions of the box to 120x480 and apply a 1px solid border around it. Display the image _images/banner_120x480.gif_ (by setting it as background to the div). The banner should stay at the same position even when the user scrolls the page.

![Exercise2c](images/exercise2c.png)


## Exercise #3: Floating articles

[Starter file](exercise3.html)

  - Set the article dimensions to 200x100px and set some background.
  - Make the articles float next to each other with 10px space in between them.  
  - The text should not overflow the boxes.
  - The article with the `promo` class should take an entire line on its own. Further,
    * the content should be typeset in bold and made scrollable;
    * change the height of this box to half of the regular (i.e., to 50px);
    * inherit the background color from the body;
    * separate it from the other content by red horizontal lines (achieve this by setting top and bottom padding and borders).


![Exercise3](images/exercise3.png)


## Exercise #4: Webshop

Complete the missing CSS parts in [exercise4.html](exercise4.html) such that it is displayed exactly as on the screenshot below. You don't need to edit the HTML structure.

  - Three products per row, with 10px spacing between the product boxes.
  - Product box is 260x370px (excluding borders); the images are 250x250px.
  - Price is shown in the bottom right corner. 
  - Special deals are shown in the top right corner of the product boxes
    * Use a 60x40px box that overlays the product image (use z-index).
    * The text in the box has to be center-aligned both horizontally and vertically.


![Exercise4](images/exercise4.png)
