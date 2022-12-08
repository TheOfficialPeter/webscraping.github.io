# A Dive Into Webscraping
###### Author: P e t e r. <br/> Please note: This article assumes that you know the basic python syntax.

### Basic

1. Installing Python + libraries.
      1. Installing VsCode and configuring Python
      2. Installing libraries
2. Introduction to Requests.
3. Example of Requests.
4. Introduction to Beautiful Soup.
5. Example of Beautiful Soup.

### Advanced

6. What is lazy-loading and how to overcome it.
7. Introduction to Selenium.
8. Example of Selenium.

### Web Scraping with NodeJS

9. Getting started with NodeJS.
      1. What is NodeJS?
      2. Why use NodeJS?
      3. Installing NodeJS.
      4. Installing NodeJS modules
10. Introduction to Puppeteer.
11. Example of Puppeteer.

### Browser Automation

12. What is Browser Automation.
13. Introduction to browser automation with Selenium
14. Example of browser automation with Selenium

## Installing Python + Libraries

Installing python is really simple. Just visit [the official python web page](https://www.python.org/downloads/) and download the latest version and open the installer. During installation please make sure you have checked the box that **adds python to the PATH**. If you don't see the checkbox, add it manually. [Here](https://medium.com/@omoshalewa/why-you-should-add-python-to-path-and-how-58693c17c443) is an example. If this link is broken just google 'How to add python to PATH'.<br/>

### Installing VsCode and configuring Python

The next step for you it to grab your text editor so we can start coding some cool stuff. Personally I prefer using [Vim](https://www.vim.org) or [Vscode](https://code.visualstudio.com). I would recommend you to use VsCode since it is more beginner-friendly. After installing [Vscode](https://code.visualstudio.com) from the website, open it up and you should be greeted with a fancy looking UI. Now we are going to connect Python with Vscode otherwise we our text editor (Vscode) is useless. I will be explaining how to install the extension, but if you find it difficult to follow you can also visit the official tutorial [here](https://code.visualstudio.com/docs/languages/python). Upon being greeted with the main User Interface, navigate to the extensions tab. (Picture below of the extensions tab icon)

![image](https://user-images.githubusercontent.com/57006688/205931750-ab716e71-84f6-41e6-9bcc-a2d2c559923d.png)

Search python in the textbox then install the first one. It might take some time to install.

![image](https://user-images.githubusercontent.com/57006688/205932087-fcbac426-c45c-453e-bcf0-bd330eb8e027.png)

After installed press `ctrl+shift+p` (You can also go the the <b>View</b> tab and select <b>Open command palette</b>). A window from the top should appear, type in `Python: Select Interpreter` and press Enter or Click on that option.

![group js - Chat - Visual Studio Code 12_6_2022 10_36_50 PM](https://user-images.githubusercontent.com/57006688/206017893-3617bf8b-402a-4e85-b831-8f0d47e52d68.png)

Then select the recommended one. Great! Now we have Python installed and connected with Vscode.<br/>
We can now create python files and run them within Vscode.

### Installing libraries

By now you should know what command prompt is. We will be using it to install the required libraries. At the start of each section I will show you how you can install the required libraries. Some might not require installation, but I will state how when it does.

## Introduction to Requests

The Requests library is a pre-installed (sometimes) python library. If you don't have the module installed or just want to make sure do the following:<br/>

1. Open command prompt.
2. Type in `pip install requests`
3. Look at what the output says. It will state whether the requirements are already met (already installed) or not. Either way it should be installed.

Requests is used to make HTTP requests to web pages / ip addresses to be able to retrieve or send data.
We use this library only for basic web scraping that doesn't involve the need for extreme methods of scraping. You would also need to know how to work with strings to use this library as your main method of scraping since Requests grabs the web page's front-end code as a whole string. The string formatting has to be done manually. When we reach <b>4. Introduction to Beautiful Soup</b> you'll see how we work around this tedious problem. 

## Example of Requests

We can start of by creating a new python file in Vscode and call it something similar to <b>main.py</b> or <b>test.py</b>. Now let's open the file and firstly import the modules/libraries we need for web scraping in this case we are using Requests. The first line of code should look like this: 

![image](https://user-images.githubusercontent.com/57006688/206243471-9bb0d503-b731-41d1-b696-2f8123cffe0b.png)

We are importing the Requests module (it's basically a python script containing pre-defined functions that you can use almost anywhere).

Now we have a list of functions we can use to do some scraping. We would like to grab a web page's code first so that we can use that information for statistical purposes, marketing research etc.

![image](https://user-images.githubusercontent.com/57006688/206243759-59cfd1cb-7e01-4619-8ec0-f9e241381bdb.png)

In the above image we are using the `HTTP GET` requests using the `requests.get(url)` function to make grab the html source of the url which we are storing in a variable called `r`. If we were to print the variable `r` this is what it will return when we run the file:

![image](https://user-images.githubusercontent.com/57006688/206243942-f54a0b87-2478-4bb0-8678-abb717fea3da.png)

This is the HTML code of the website url we provided to the `GET` request, stored as a string.
Now that we have the data captured from the website we can use it. Also forgot to mention you can run python files by pressing the `run icon` top right.

![image](https://user-images.githubusercontent.com/57006688/206244165-6dd386fc-c046-45f1-a5af-6ed5d7c40e86.png)

Let's go back a few steps. Web scraping requires you to know what you want to achieve. This is my thought process when it comes to scraping.
- I have a deep look into the website and it's mechanics.
- I start to look for <b>unique, important values</b> as well as <b>repeating values</b>. Both can be used in different use cases.
<br/>
Below is my analysis of the website we are currently testing.

![image](https://user-images.githubusercontent.com/57006688/206375541-986bbc31-7338-4b6a-8e25-cd391ac35219.png)

The items circled in `red` are repeating values. The items circled in `blue` are important values. In this scenario we can use the important values to monitor the results of the books and use the repeating values to store the information about it. To be honest this scenario doesn't really have a great "important value", you will be seeing better ones as we progress to different websites to scrape.
