# Project-03-Code-Institute CCTV & SAT TV ordering system

![Landing Page](readme-assets/landing-page.png)

--------------------------------------

## Table of Contents

--------------------------------------


- [Description](#description)
- [Theme](#theme)
- [User Experience](#user-experience)
- [Features](#features)
    - [Future Features](#future-features)
- [Testing](#testing-and-issues-encountered)
- [Technologies](#technologies-used)
- [Deployment](#deployment-to-heroku)
- [Credits](#credits)

----------------------------------------

## Description
----------------------------------------

As I was working in past with similar equipment, I wanted to create an ordering system that allow user to buy it in easy way without any unnecesery details. The live site can be found [here](https://cctv-and-tv-ordering-sys.herokuapp.com/?fbclid=IwAR3jjU2Z52_L418t-HViQGT0uDmrBUHPOKPhCnkGTyKiT4vwA1epErqU6D0).

----------------------------------------

## Theme

----------------------------------------
Despite the project being entirely text-based, I implemented a few little things to make it more appealing to the user. When the user enters the site, he will be greeted with a big heading and the name of ‘SAT & CCTV’. I also added emojis throughout the entire programme when I felt it would be beneficial for various reasons like bad input type etc.

![SAT-CCTV](readme-assets/)


----------------------------------------
## User Experience
----------------------------------------

### User Stories
----------------------------------------
As a first time visitor:

- I want to know which shop I entered and then decide if I want to have a look around or leave the shop 
- I want clear instructions on what I need to enter if I have been asked to do so

As a returning visitor:

- I want to be able to order more 

----------------------------------------

### Python Logic
----------------------------------------

Firstly I imagine the way shop should work like but than I realize that it's much easier with flowchart.
So I created a flowchart so I knew the structure of my programme and would be able to look at it for guidance during the process.

![Flowchart](readme-assets/)

[Back to the Top](#table-of-contents)

----------------------------------------
## Features
----------------------------------------

### Start/first decision

At first program showing information taht it's not real shop and all data provided should be fake.

The user is greeted with the LOGO together with a welcome message. Here he can decide if he wishes to continue or leave the shop instead. The option is to enter either Y/N Yes/No. The inputYesNo validating answers throughout the entire programme including user accidentally enters a space before/after the input,leave it blank or use any other key that is not accepted.
  

![Enter or Leave Shop](readme-assets/)

----------------------------------------
#### Leave Shop 

If the user changes his mind, he can leave the shop by entering N/No/n/no.

![Leave Shop](readme-assets/)

----------------------------------------

### Invalid Input

If the user enters a invalid input an error message shows up and he will be asked to enter either Y or N

![Invalid Input](readme-assets/)

----------------------------------------
### See Selection/second decision

If the user decides to have a look, a list of books will be printed and displayed. To create a little bit of anticipation the .sleep() function has been implemented with a delay of 1 second to display all titles.

![Book List](readme-assets/book-list.png)

----------------------------------------
#### Leave Shop 

If the user decides to not go ahead and order a book, he can enter any other key but the numbers between 1 and 8 to leave the shop.

![Second Choice - Leave Shop](readme-assets/second-choice-exit.png)

----------------------------------------
### Ordering

If the user wants to order a book, he is asked to enter a number between 1 and 8 to choose the desired title. A couple of examples are being mentioned for guidance.

![Second Choice - Select Title](readme-assets/second-choice-continue.png)

----------------------------------------
### User Information

As this project has been linked to a Google Sheet, I added a small paragraph to inform the user that the data will be added to this sheet but confirm that it will be collected solely for the purpose of this project and only be seen by me. I added a 5 second delay to allow the user enough time to read this message before the programme continues. To highlight it is not part of the programme itself, this text has been put between emojis.

![User Information](readme-assets/)

----------------------------------------
### Enter details

The user is now asked to enter their first and surname, IE mobile number and address.

![Details](readme-assets/)

----------------------------------------

### Invalid Input - Name

If the user enters a invalid input he will be asked to start again from the top.

![Invalid Input2](readme-assets/)

![Invalid Input3](readme-assets/)

----------------------------------------

### Enter Details - Invalid Number

If the user doesn't enter a valid 10-digit IE number with start 08 or is not a number, a message pops up and informs him that it is incorrect. He can then enter the details again. Until the user enters correct number, the programme keeps looping until a valid number has been entered. 

![Wrong mobile number](readme-assets/)

----------------------------------------

### Confirm Or Correct Details

After entering all his details, the user can then read over them again and either confirm the details by entering the digit 1, or enter the number 2 if he wishes to correct something. He will then be asked to enter all his details again from the top.

![Confirm Details - No](readme-assets/confirm-details-no.png)

If he confirms his choice, a message appears letting the user that the order can now be finished up.

![Confirm Details - Yes](readme-assets/confirm-details-yes.png)

----------------------------------------

### Invalid Input

If the user enters an invalid input, an error message appears and it loops back to the start and he will be asked to enter his details again.

![Invalid Input4](readme-assets/invalid-input4.png)


----------------------------------------


## Confirmed Details & Google Sheet

Once the user has confirmed his details, they are simultaneously added to the Google Sheet.

![Update Google Sheet](readme-assets/confirm-details-add-to-sheet.png)


### Thank you & Receipt

At this stage, the user is being thanked for supporting his local bookshop, and a small receipt will be printed. Another delay of 2 seconds has been added before the receipt has been 'printed'. On this receipt, the user will find the address of the shop, the title and price of the book he ordered, and the date and time.

![Thanks & Receipt](readme-assets/receipt.png)

## Last choice

The user is now being asked if he wishes to place another order or leave the shop. If he wishes to place another order, he is asked to enter 1 and if he wants to leave he should press any other key.

![Leave Shop](readme-assets/last-choice-exit.png)


If he enters 1 the programme starts again from the beginning.

![Order another book](readme-assets/last-choice-new-start.png)

[Back to the Top](#table-of-contents)

## Future Features
----------------------------------------

- To migrate the booklist to a Google sheet and pull out the titles from there for a wider selection
- To give the user the option to enter an email address instead of or addition to a phone number
- To allow the user to order multiple books at the same time

At the moment, I am taking the user's data in one function and updating my Google Sheet once the user confirms that all the data is correct. In the future, I might look into dividing this into three smaller functions so that the user doesn't have to enter all the data again from the top and can also select a specific section he made a mistake in and jump to this specific function/input.

----------------------------------------
## Technologies Used 
----------------------------------------

- Python, to write my code
- Heroku, to deploy my site

----------------------------------------

## Python Libraries/Modules
----------------------------------------

- Time - to add the .sleep() function and delay my code in the terminal
- [Datetime](https://www.programiz.com/python-programming/datetime/strftime) - to print the current date and time on the receipt
- [Sys](https://www.hashbangcode.com/article/stopping-code-execution-python) - to exit the programme
- [Pyfiglet](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) - to create a header
- Emoji - to add some graphical content
- Pyinputplus - to validate some inputs  
- Gspread - as API for my Google Sheet

--------------------------------------
## Testing And Issues Encountered
--------------------------------------

The site has been tested by me thoroughly during its creation to ensure that the programme runs as it should and errors are being caught. Friends also tested it on a variation of laptops and with different browsers without any issues.

I had a lot of fun creating my little bookshop and enjoyed it very much. I did, however, run into a few issues:

1) At first I only had one break statement in my order_book() function, so every time I ran the programme it jumped back to the beginning instead of going ahead to the user_data() function. I had it working before, but discovered that it was only because I entered (by chance) the only number that had the break statement included. After having posted my question in the Slack Channel, I saw my issue a couple of minutes later and entered a break statement after each choice. This fixed my problem.

2) When printing the receipt, I wanted to display the choice the user made together with a few extra pieces of information but kept running into error messages. After reading over the Code Institute material over and over again, I found a simple solution and made my select_book variable a global variable. This allowed me to show the title the user had selected on the receipt successfully.

3) My biggest issue, however, was adding the customer's details to my Google Sheet. I tried endless variations and looked at the love sandwich project for guidance as well as other similar projects. Unfortunately, none of them helped me find the answer, because unlike them, I wanted to add three variables (fname, lname and mnumber) from one function at the same time (the decision to add the title to the Google Sheet as well came later). At first I thought I might be able to add it with a simple append_row statement within my user_data() function, but it wasn't as easy as that. 

I tried turning these variables into global variables and using them, but this turned out to be unsuccessful too. I then came up with a solution and, on paper, it should have worked, but I kept getting error message after error message. So I contacted Tutor Support, who helped me and pointed out that the add_data.append_row (name1, name2, number) in my update_sheet() function was missing square brackets, converting it to a list rather than a string. After changing this, the entered details finally showed up in my Google Sheet.

[Back to the Top](#table-of-contents)

## Unfixed Bugs

At the moment, street and city not accepting white spaces.


### Validators Testing
--------------------------------------

The code has been tested by running it through the PeP8. Almost all of the errors that have been encountered were due to trailing whitespaces or either too many or not enough blank lines.

No errors were found during the final check.

![PEP8]()

--------------------------------------

### Browser Testing
--------------------------------------

The programme has been tested on Google Chrome, Firefox. Due to the nature of the programme, it is not suitable for mobile phones and smaller devices.

--------------------------------------
### Deployment to Heroku
--------------------------------------

The website was deployed by following the steps below: 

1. Log in [Heroku](https://id.heroku.com/login). 

2. Click 'New' and select 'Create new app'

3. Choose a name for the app, region and click on 'Create app'

4. Only 'Deploy' and 'Settings' are relevant from the menu section. Starting with the 'Settings' first.

5. Now Buildpacks need to be added. They install future dependencies that are needed outside of the requirements file. The first is Python and the second is node.js. Python needs to be selected first and then node.js. Save this selection.

6. Now the 'Deploy' section needs to be selected from the menu and connect it to github.

7. Enter the name of the repository we want to connect it with and click 'Connect'

8. The choice appears now to either deploy using automatic deploys or manual deployment, which deploys the current state of the branch.

9. Click deploy branch. 
    

## Credits 
--------------------------------------

- [Stackoverflow](https://stackoverflow.com) - to clarify some possibilities
- [MakeUseOf](https://www.makeuseof.com/how-to-include-emojis-in-your-python-code/) - for the syntax to add emojis
- [GeeksForGeeks](https://www.geeksforgeeks.org/python-ascii-art-using-pyfiglet-module/) - help on which module to import and how to create my header
- [W3 School](https://www.w3schools.com/howto/howto_css_fixed_footer.asp)
- Love Sandwiches - for general guidance and how to set up my API

The text for this programme has been written by myself.

--------------------------------------
## Acknowledgments
--------------------------------------

My thanks goes to the Code Institute.

A special thanks also to my amazing Mentor Andre who helped me coming up with this idea.


[Back to the Top](#table-of-contents)
