# About Pear-d

# Pear-d Initial Setup
To setup the project manually, first git clone the repo using the HTTPS link provided on the GitHub page, then open the folder in your IDE. After the folder is opened, follow these steps:

## Setup Steps
1. Run the command ```python -m venv venv``` to create your virtual environment.
2. Run ```.\venv\Scripts\activate``` on Windows or ```source venv/bin/activate``` on Linux to start the virtual environment.
4. Once in the (venv), run ```pip install -r requirements.txt``` to install all dependencies for the backend.
5. Download the ```credentials.zip``` from an authorized member of the team and unzip it.
6. Place the ```credentials``` folder in the parent directory of the project, where the frontend and backend folders are.
7. Next, ```cd .\pear_d_frontend\``` to get into the frontend, then do ```npm install``` to install the ```package.json``` for the frontend.
8. Do ```npm run build``` to make the build file for React. 
9. Now your repo should be ready to go. ```cd``` into the ```pear_d_backend``` folder and do a ```python manage.py runserver``` to start up the server.

# Git Stuff
## Commands
- ```git checkout -b "ENTER BRANCH NAME HERE"``` to checkout a new branch with chosen name. The convention we are going with is the JIRA ticket code followed by a short description of the branch. For example: ```git checkout -b "PC-1-Make-A-New-Branch"```.

- ```git checkout "BRANCH NAME HERE"``` will let you switch to an existing branch to work on it.

- ```git pull``` is used to pull in any changes made by others on the same branch so that you can stay updated with any new code one of us adds to the branch/repo.

- ```git add .``` will stage all of your current changes so that they are ready to be committed to the repo. You have to run this or ```git add INSERT_FILE_HERE``` before committing.

- ```git commit -m "INSERT MESSAGE HERE"``` will make a new commit with that commit message.

- ```git push origin BRANCH_NAME``` will push your commits to your branch and it should prompt you to make a PULL REQUEST to have the changes merged into main. 
## Practices
- Before you commit/push your changes run the command ```pip freeze > requirements.txt``` if you have made any changes to the dependencies used by the backend so that it updates the requirements.txt file accordinly.
- Unless your change is minor try to have someone else look at your PR before merging it into the main branch.


## Page Routing
### Pages Folder
- Right click the pages folder and press new folder and name it the name of the page. In that folder create two files: Name.js and Name.css where Name is the name of the page as well.
- Next go to the index.js file and copy what the previous lines have but change the names to the name of you folder.
### App.js
- In this file, you will see where the imports are and that the page names are there in one line. Add the new page name.
-Lower in the app you will see routes. Copy and paste the home one and change the word Home with the name of your file and same with the file path so it should be '/pagename' and <PageName/>.
- Now when you create buttons to other pages there will be no issue cause we have a route.
### Navigate with button
- In the page you have your buttons do this at the top with the other imports:
import { use Navigate } from 'react-router-dom'

-Then before the return inside the big function create this function:

const navigate - useNavigate();

-Now create a button like normal and add the onclick function with the navigate function:

<button onClick={() => navigate('/pagename')}>Next Page</button>

- This means when you click it goes to that page. And now you're all set!
