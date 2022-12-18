# A Dive Into Webscraping
###### Author: P e t e r. <br/> Please note: This article assumes that you know the basic python syntax. Also the code is available [here](https://github.com/TheOfficialPeter/webscraping.github.io/blob/main/test.py).

### Basic

1. Installing Python + libraries.
      1. Installing VsCode and configuring Python
      2. Installing libraries
2. Introduction to Requests.
3. Example of Requests.
4. Introduction to Beautiful Soup.
5. Example of Beautiful Soup.
6. Displaying data on a graph using pyplot

### Advanced

7. What is lazy-loading and how to overcome it.
8. Introduction to Selenium.
9. Example of Selenium.

### Web Scraping with NodeJS

10. Getting started with NodeJS.
      1. What is NodeJS?
      2. Why use NodeJS?
      3. Installing NodeJS.
      4. Installing NodeJS modules
11. Introduction to Puppeteer.
12. Example of Puppeteer.

### Browser Automation

13. What is Browser Automation.
14. Introduction to browser automation with Selenium
15. Example of browser automation with Selenium

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

We can start of by creating a new python folder called "Python" and then create a file inside of it and then open it in Vscode and call it something similar to <b>main.py</b> or <b>test.py</b>. 

![image](https://user-images.githubusercontent.com/57006688/206842513-27afffc6-5ef5-4bc9-9a02-ab255a2d4e8d.png)

![test py - Python - Visual Studio Code 12_10_2022 11_08_15 AM](https://user-images.githubusercontent.com/57006688/206842598-d726bb0d-2c91-4ee8-bf37-a4bf206f5b1a.png)

![image](https://user-images.githubusercontent.com/57006688/206842604-ee109fed-cc06-4baf-8612-05bbe102a19d.png)

![image](https://user-images.githubusercontent.com/57006688/206842611-4794a625-d821-4513-90b1-76f85af50ca6.png)

Now let's open the file and firstly import the modules/libraries we need for web scraping in this case we are using Requests. The first line of code should look like this: 

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

The items circled in `red` are repeating values. The items circled in `blue` are important values. In this scenario we can use the important values to monitor the results of the books and use the repeating values to store the information about it. To be honest this scenario doesn't really have a great "important value", but we will use it anyways. You will be seeing better ones as we progress to different websites to scrape.

Now we will scrape the `important value` instead of the `repeating values` only becuase it's a tedious process to do a lot of complex scraping with manual string methods as I mentioned previously, but I'll do it once.

First start of by grabbing the element's tags beginning index like this:

![image](https://user-images.githubusercontent.com/57006688/206643961-d7dace65-57b6-495c-9255-9a91f7ba2af6.png)

What we do is get the number of the character where the `<strong>` element is first occured, because when you look in your browser's inspector tool (right-click, inspect element)

![image](https://user-images.githubusercontent.com/57006688/206644544-876f25ed-85f0-47e1-8ee1-5b770722aaa8.png)

You'll see that the `important value` has a tag around it called "strong" and you would also notice that it is the first occurance of the tag "strong", but if there were previous occurences of that tag then this wouldn't have worked becuase this code grabs the first occurence. Hopefully I explained it in a way you could understand.

Now we will grab the "strong" closing tag which looks like `</strong>`

![image](https://user-images.githubusercontent.com/57006688/206644713-140e28f1-1285-4b96-bc04-d3b859d16057.png)

Now we have 2 numbers. We know where the element starts and end in the whole string. Now we `cut` the text out like below.

![image](https://user-images.githubusercontent.com/57006688/206644893-db60f43c-7d29-4909-b692-b711c659b5a9.png)

And now if we print the part that we cut out of the main string we get this:

![image](https://user-images.githubusercontent.com/57006688/206644967-8c6586a7-cdee-411c-84c9-950fbf86df1d.png)

The reason I use `+len("<strong>")` is becuase it grabs the number of the starting point of the element's text so when you do it without that part like below:

`stringCut = sourceCode[begin:end]` <br/>
`print(stringCut)`


Then it will output this:

`<strong>1000`

But when you add the length of the word `<strong>` you get:

`1000`

And that's it. This is webscraping in a nutshell. You can go to <b>6. Displaying data on a graph using pylot</b> if you want to see how we use this data for research.

## Introduction to Beautiful Soup

"Beautiful Soup is a Python library for pulling data out of HTML and XML files. It works with your favorite parser to provide idiomatic ways of navigating, searching, and modifying the parse tree. It commonly saves programmers hours or days of work."

To install this library you'll have to open command prompt and type in the following `pip install beautifulsoup4` and then press `Enter`. 

## Example of Beautiful Soup

Now we will add the library to our Python script.

![image](https://user-images.githubusercontent.com/57006688/206842016-22120611-a9e3-41d2-8686-37c06c8de6f9.png)

We say `as bs` just to add our own abbreviation to the class `BeautifulSoup` so now we can just use `bs` everywhere.

Let's continue where we last left off. Since beatiful soup is used to dissasemble a website's source code, it doesn't grab the source code this means that we will still be using the requests library to grab the source code and feed it to beautiful soup. So you should have this as your code currently:

![image](https://user-images.githubusercontent.com/57006688/206841902-34204c0c-0306-458c-a618-61c3bbcf3749.png)

And now we have the variable `soureCode` which stores the code and we will read it in beautiful soup like this:

![image](https://user-images.githubusercontent.com/57006688/206842137-a705c1b0-0835-4666-b933-e9b02f6ad166.png)

Alright. Now let's grab the "repeating values" which are the book names. We will do this by using Beautiful Soup's `find_all()` function which can fetch any tag names etc. Since each name elements has a tag `h3` it will be really easy grabbing them all.

![image](https://user-images.githubusercontent.com/57006688/206853776-0293bc5d-1747-44c6-a2e6-f4136c8c77be.png)

In the image above we use the `bs.find_all()` function with the parameter set as `h3` to find all the h3 tagged elements on the web page. If you don't know how I got `h3` right-click on webpage and open the developer tools (right-click -> Inspect element) and then you will see that the name has an h3 tag. Now we have a loop that will go through all the `elements` that we found. Now we just want the text of those elements, not the element itself. so if we want to print the name of each book we will do this

![image](https://user-images.githubusercontent.com/57006688/206853892-b0ae17cf-7de0-41fc-b2ac-08b344be9eb4.png)

you have to put `.text` becuase otherwise it will print the entire element. You can change it and see the difference. And that's the basics of scraping with Beautiful Soup.

## Displaying data on a graph using pyplot

Pyplot is a library which is used to visually display information. It can be used along with machine learning to make predictions for many different scenario's.
We will install the library by opening Command Prompt and typing `pip install matplotlib`. Now in VsCode we will import the library

![image](https://user-images.githubusercontent.com/57006688/208314224-2257e54c-4288-47d0-9455-ce9d9b35f3ea.png)
