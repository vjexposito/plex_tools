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

<style>.bmc-button img{height: 34px !important;width: 35px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{padding: 7px 15px 7px 10px !important;line-height: 35px !important;height:51px !important;text-decoration: none !important;display:inline-flex !important;color:#FFFFFF !important;background-color:#FF813F !important;border-radius: 5px !important;border: 1px solid transparent !important;padding: 7px 15px 7px 10px !important;font-size: 28px !important;letter-spacing:0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#FFFFFF !important;}</style><link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet"><a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/vjexposito"><img src="https://cdn.buymeacoffee.com/buttons/bmc-new-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px;font-size:28px !important;">Buy me a coffee</span></a>

