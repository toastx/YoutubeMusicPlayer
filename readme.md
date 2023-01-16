# Youtube automation using Selenium

Automating YouTube Music with Selenium in Python allows you to easily control and manipulate the playback of songs on the platform. This can be a great way to quickly and easily create a personalized listening experience without having to manually navigate through the website.

## Prerequisites:

## Modules:

 ### Selenium : Automation of browsers
 ### localStoragePy : Storing small strings permanently in JSON format

## Browsers:

### Firefox :
Since Google Chrome does not allow extensions to be used in headless mode [when the browser is running in the background], we must use a different browser such as Firefox in order to utilize extensions with Selenium.

## GeckoDriver:

In order to automate Firefox using Selenium, we must install Geckodriver.exe, which is the official browser automation engine for Selenium.

In order to stream music without ads using our webdriver, we need to enable an ad blocker extension. To do this, we will need to obtain a .xpi file for the desired ad blocker extension. The .xpi file is a type of compressed file that contains the extension and its components. You can follow the Step 1 at the linked webpage to learn how to obtain the .xpi file for your extension.


## Procedure:

To begin automating in Firefox using Selenium, we need to initialize our webdriver.
We need to set the path for our Firefox browser, and install the Geckodriver.exe in the path of this .py file
We use the "Options" class to add various properties to our webdriver for optimized performance. 


In order to stream music without ads using our webdriver, we need to enable an ad blocker extension. To do this, we will need to obtain a .xpi file for the desired ad blocker extension. The .xpi file is a type of compressed file that contains the extension and its components. You can follow the Step 1 at the linked webpage to learn how to obtain the .xpi file for your extension.
Once you download the .xpi file, copy its path and and set it as a variable, and initialize it in the webdriver


For our music player, we will be adding a function called Stream/Pause Music , Name of Track and Add/Play/Remove Playlist and Stop. This function will allow the user to search for and play a specific song on YouTube using the webdriver.
To accomplish this, we will use the webdriver to search for the song using the provided URL. The webdriver will then click on the first video in the search results by locating its element using the "Inspect Element" feature and the xpath.
Finally, we will use the URL and the xpath to navigate to and access the desired video using the webdriver."



                


https://user-images.githubusercontent.com/85751209/212715932-5f31b278-7cb2-42f6-aff5-1b637dae4981.mp4



