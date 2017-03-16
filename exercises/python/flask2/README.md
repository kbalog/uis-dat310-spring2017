# Server Side Programming exercises (Python, Flask), Part II.

  * [Jinja documentation](http://jinja.pocoo.org/docs/2.9/templates/)


## Exercise #1: Top movies

Complete the `ex_1/templates/movies.html` template file such that information about movies is displayed in a table as seen below.  

![Exercise1](images/exercise1.png)

Specifically:

  * Sort movies by rating.
  * Show the rank in the first column.
  * The synopsis should be limited to 80 characters. If no synopsis is available display the text "No synopsis is available" in italics.
  * Make the URLs clickable links. The link should open in a new window.
  * Alternate between background colors `#ECECEC` and `#CCCCCC` for even and odd rows.

You need to run the `ex_1/app.py` python file and see the output on [http://localhost:5000/](http://localhost:5000/). Note that you will need to re-start the app each time you make changes to the template file.

**You need to complete this exercise without making any changes to the `app.py` file!**
