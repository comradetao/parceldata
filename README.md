# parceldata
Land Parcel Data Assignment
Both the JSON endpoint and website are contained in this one project and are all run through Python and Flask.

# REQUIREMENTS:
Python 3.9.0

Required Python modules installed through PyPI:
xmltodict 0.12.0
flask 1.1.2
requests 2.24.0
(earlier versions of both modules and python may function, but have not been tested)

# SETUP:

Install python and necessary modules.
Download package.
Navigate to the package's root directory (where app.py is) in the command prompt window.
Enter the command "flask run".
Copy the server address provided to you in the command prompt window and enter it in your
web browser's address bar

# HOW TO USE:

Once the flask server has started, users can get access to both the JSON and HTML resources.

To access the JSON file for a given parcel ID, follow this pattern:

serverURL/json/parcelid 

where "parcelid" is the formatted 8-digit parcel ID (Ex: 123-45-678 including dashes) and
serverURL is the index address of the flask server (Ex: 127.0.0.1:5000).

To access the HTML version of the parcel data for a given parcel ID, enter
the parcel ID using the same formatting as for JSON (ex: 123-45-678 including dashes)
in the "Look Up" box in the top right corner and click "Look Up"

You may also access the pages by entering the URL in your browser's address bar following the same
pattern as the JSON endpoint, but replace "/json/" with "/page/".

# TODO:

Error checking on the user's input parcel ID.
Error pages to show what went wrong.
Validation of XML data (is it complete? real? empty?)

