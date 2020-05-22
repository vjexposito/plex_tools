# Plex tools
A script to extract all poster / fanart  images of a plex library

# Instructions

## Requirements

First, download all necessary libraries to run the script. 
Be aware you have to run it as Administrator or sudo.  

`
pip install -r requirements.txt
`

## Plex Config

plexapi gets the credentials from the file: config.ini, which is usually located at: 
`C:\Users\username\.config\plexapi`

Run the file `find_config.py` to know where the config file should be located. 

The `config.ini` file of this repository can be used as a template in case it is not still created. 
`config.ini` common variables at: [plexapi.CONFIG](http://python-plexapi.readthedocs.io/en/latest/configuration.html)

To get the variable `server_token`, go to a movie / episode and click on the three dots.
 
![Get token 01](images/get_token_01.png?raw=true)

Then, go to the `View XML`

![Get token 02](images/get_token_02.png?raw=true)

Once the file is loaded, the url includes the toke within the parameter: `X-Plex-Token`

![Get token 03](images/get_token_03.png?raw=true)

Finally, copy this token in the `config.ini` file. 

## Start Script

Change the ``library_name`` with the name of your libraries and `root_path` to set where the images will be saved. 
Then, run the python file.

`python .\get_plex_poster_fanart.py`

# Donate

<link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/vjexposito"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>

