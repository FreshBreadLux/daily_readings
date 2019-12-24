# Daily Readings Terminal Configuration
Merry Christmas, Thomas! Your gift is that you need to configure your .bash_profile to run this python script on startup. We want you to close your terminal before bed and start it up every morning. The script will scrape the daily readings for that day and print them in your terminal, so you'll start off every day with the daily readings. You can also run the script from the command line if you're up late or if you forgot to close your terminal the night before.
We hope you like it!

## Setup Instructions

### Install python 3
You need python 3 installed in order to run this script. The easiest way to do that is on this website: https://www.python.org/downloads/
Download the latest version and follow the installation instructions. If you have Xcode, you can also use homebrew to install python 3. Instructions for both methods can be found here: https://www.saintlad.com/install-python-3-on-mac/

### Install `requests` and `BeautifulSoup`
The script uses these python packages, so use `pip3` to install them. Run the following commands in your terminal:
`pip3 install requests`
`pip3 install beautifulsoup4`

### Update your `.bash_profile`
An example `.bash_profile` is included in this repo. In addition to the command to execute the script, there are a few other unrelated settings you might find useful: a `bind` setting to ignore capitalization in tab auto-completion, and a number of aliases for common git tasks.

### Add the `daily_readings.py` file
Copy the `daily_readings.py` file from this repo and add it to the same directory that holds your `.bash_profile`

The script should now run on startup.

## Running manually
`python3 ./daily_readings.py`

You can also choose between the daily Gospel reading or the full set of readings. Toggle the commented lines in `daily_readings.py` to switch between the two. The default is the daily Gospel reading.
