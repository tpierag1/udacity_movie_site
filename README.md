<h1>Avante Garde and Experimental Film Gallery</h1>


The Avante Garde and Experimental Film Gallery is a reporisoty that constructs
data classes and functions to create an html film gallery site.

The site displays the name of the film, the description of the film,
the movie poster and the ciomplete film in an iframe.

The repository contains three files.

`freshtomatoes.py`:

A script which sets the html framework and determines the jquery injection
points for variables set in the data class definition of the movie object.

It contains the required Bootstrap and Jquery calls, the CSS for display and the
HTML skeleton of the page itself.  

The function `open_movie_page()` generates the page.

To customize the look and action of the page customizations will be made in
this file.

`media.py`:

This file contains the class definitions for the object Movie, sets the
requires values for the class and defines the `show_trailer()` function.

This function opens the webbrowser and displays the trailer or full
film from the YouTube link set within the constructed nistances of `Movie()` in
`site.py`.

`site.py`:

This script imports the `freshtomatoes.py` and `media.py` files and plays two roles.

The first role is to store the instances of the class `Movie()` that are created.

The second role is to take the instances of this class, store them as a list,
`movies[]`, and call the function `freshtomatoes.open_movies_page()` with `movies[]`
as the variable.

To change the movies being displayed one must engage in the following steps:

- Delete the instances of `Movie()` that one wants to eliminate from the page.

- Construct new instances of the class `Movie()`.  This requires knowing
the title of the movie, the short description of the movie and having links to
the movie poster the trailer.

For example:

`film = media.Movie("Title", "Description", "Link_To_Poster", "Link_To_Trailer")`

- Insert the movie variable name into the `movies[]` list and delete all movies
that one does not want on the page.

- Save the file and run it to display the new selection of movies.


<h3>Generating the Page</h3>

To generate the page open a Terminal window and run the following:
```
python3 site.py
```
If using a REPL or trying to load the program in Windows open the file `site.py` and select "Run Script".
This will generate the page and open the browser to the page for viewing.
