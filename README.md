# About Pear-d

# Pear-d Initial Setup
To setup the project manually, first git clone the repo using the HTTPS link provided on the GitHub page, then open the folder in your IDE. After the folder is opened, follow these steps:

## Setup Steps
1. Run the command ```python -m venv venv``` to create your virtual environment.
2. Run ```.\venv\Scripts\activate``` on Windows or ```source venv/bin/activate``` on Linux to start the virtual environment.
3. Once in the (venv), run ```pip install -r requirements.txt``` to install all dependencies for the backend.
4. Next, ```cd .\pear_d_frontend\``` to get into the frontend, then do ```npm install``` to install the ```package.json``` for the frontend.
5. Do ```npm run build``` to make the build file for React. 
6. Will Add the last couple of steps here once I figure them out with Brianna.

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