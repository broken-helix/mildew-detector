# **Mildew Detector - Introduction**

The Mildew Detector is a project which seeks to use machine learning to teach
an alorithm to be able to make a prediction on whether a leaf is infected
with Powdery Mildew or not.

[View the live project here](link).

![Am I Responsive?](responsive-link.jpg)

<hr>

## **TABLE OF CONTENTS**

- [**Dataset Content**](#dataset-content)
  - [Sub-section](#sub-section)
- [**Business Requirements**](#business-requirements)
  - [Sub section](#sub-section)
- [**Hypothesis**](#hypothesis)
  - [Sub section](#sub-section)

- [**Testing**](#testing)
- [**Technologies Used**](#technology-used)
- [**Deployment**](#deployment)
- [**Credits**](#credits)

<hr>

## **DATASET CONTENT**

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).
We then created a fictitious user story where predictive analytics can be applied in a
real project in the workplace.

- The dataset contains +4 thousand images taken from the client's crop fields.
The images show healthy cherry leaves and cherry leaves that have powdery mildew,
a fungal disease that affects many plant species.
The cherry plantation crop is one of the finest products in their portfolio,
and the company is concerned about supplying the market with a compromised quality product.

## **BUSINESS REQUIREMENTS**

The cherry plantation crop from Farmy & Foods is facing a challenge where their
cherry plantations have been presenting powdery mildew. Currently, the process is manual
verification if a given cherry tree contains powdery mildew.
An employee spends around 30 minutes in each tree, taking a few samples of tree leaves
and verifying visually if the leaf tree is healthy or has powdery mildew.
If there is powdery mildew, the employee applies a specific compound to kill the fungus.
The time spent applying this compound is 1 minute.  
The company has thousands of cherry trees, located on multiple farms across the country.
As a result, this manual process is not scalable due to the time spent in the manual process
inspection.

To save time in this process, the IT team suggested an ML system that detects instantly,
using a leaf tree image, if it is healthy or has powdery mildew.
A similar manual process is in place for other crops for detecting pests, and if this
initiative is successful, there is a realistic chance to replicate this project for all
other crops.

The dataset is a collection of cherry leaf images provided by Farmy & Foods,
taken from their crops.

- 1 - The client is interested in conducting a study to visually differentiate a healthy
cherry leaf from one with powdery mildew.
- 2 - The client is interested in predicting if a cherry leaf is healthy or contains
powdery mildew.

## HYPOTHESES

- The project hypotheses are driven by the requirements of the client and mapped to the business requirements.

### Hypothesis 1

- The first hypothesis is that there is a visual difference between the appearance of infected and health cherry tree leaves.

- The business requirement is that the client wants to conduct a study to visually differentiate a healthy leaf from an infected one.
- The hypothesis will be tested by calculating average and variability of images and plotting the results to detect if there are differences.

### Hypothesis 2

- The second hypothesis is that it is possible to predict with >97% accuracy, if an image of a cherry tree leaf is infected with powdery mildew.

- The business case is that the client wants to predict if a cherry tree is infected or healthy, with at least 97% accuracy.
- The hypothesis will be tested by training a model on the train and test images and calculating the accuracy with a validation set.

## RATIONALE

*Map the business requirements in a User Story based format to each of the Data Visualization and ML Tasks along with the specific actions required for the enablement of each task.*

*Articulate a Business Case for each Machine Learning task which must include the aim behind the predictive analytics task, the learning method, the ideal outcome for the process, success/failure metrics, model output and its relevance for the user, and any heuristics and training data used.*

### Visualisation Task

- Displaying images

#### user stories

### ML Task

- The second business requirement requires a ML task which involves designing, training and validating the model. The client has requested a final accuray of 97% or greater. The client wishes to be able to upload an image of a leaf and recieve a result which can be downloaded.  The client will be supplied with a dashboard

### **Epics and User Stories**

Information gathering and data collection.
Data visualization, cleaning, and preparation.
Model training, optimization and validation.
Dashboard planning, designing, and development.
Dashboard deployment and release.

### Information gathering and data collection ###

- As a **user** I can **action** so that **result**

### Data visualization, cleaning, and preparation ###

- As a **user** I can **action** so that **result**

### Model training, optimization and validation ###

- As a **user** I can **action** so that **result**

### Dashboard planning, designing, and development ###

- As a **user** I can **action** so that **result**

### Dashboard deployment and release ###

- As a **user** I can **action** so that **result**

### **Agile Methodology**

An Agile Approach was followed in the planning and construction of the site.  User stories were built using GitHub Issues, grouped into Epics for different aspects of the project and organised onto a board.
Each user story has a list of tasks to tick off and an acceptance criteria.  As stories were built, they were moved to the Not Started column of the board.  Once they were started, they were moved to the In Progress Column and finally, when all tasks were complete, the story was moved to the complete column and marked closed.  Each story was listed in relevant Epic as a task and ticked off when the story was complete.

The project board can be viewed here: [Mildew Detector Project Board](link).

## **DASHBOARD**

### **Navigation**

#### **Streamlit MultiPage**

About

![Streamlit Menu](streamlit-menu.jpg)

### **Summary Page**

About

![Streamlit Summary](streamlit-summary.jpg)

### **Leaves Visualiser**

About

![Streamlit Visualiser](streamlit-visualiser.jpg)

### **Mildew Detector**

About

![Streamlit Detector](streamlit-detector.jpg)

#### **ML Performance**

About

![Streamlit ML Performance](streamlit-performance.jpg)

### **Project Hypothesis**

About

![Streamlit Hypothesis](streamlit-hypothesis.jpg)

### **Future Steps**

- Other species.
- Mobile application.

<hr>

## **TESTING**

- Manual tests were carried out throughout the process and documented in the user stories as tasks.

<hr>

## **TECHNOLOGIES USED**

- [Git](https://git-scm.com/)<br>
   Used for version control alongside GitHub.
- [GitHub](https://github.com/)<br>
   Used to store the project and utilise git version control.
- [Heroku](https://id.heroku.com)<br>
   Used to deploy project.
- [W3C - HTML](https://validator.w3.org/)<br>
   Used to validate all HTML code.
- [W3C - CSS](https://jigsaw.w3.org/css-validator/)<br>
   Used to validate all CSS code.
- [CI PEP8 Testing](https://pep8ci.herokuapp.com/)<br>
   Used to validate all Python code.
   streamlit
   jupyter notebooks

<hr>

## **DEPLOYMENT**

### **Create Github Repository**

- Log in to your Github account.
- Navigate to repositories and select 'New'.
- Select the 'Code Institute' template from the 'Repository Template' menu.
- Give your repository a name and select 'Create Repository'.
- When the repository has been created select 'Gitpod' to open a new workspace.

### **Heroku**

- Log in to your Heroku account [Heroku](https://id.heroku.com).
- From the home page select 'New', then select 'Create New App' from the drop-down.
- Provide a name for your app and selectyour regrion.
- Add 3 new keys along with your relevant value information: 'SECRET_KEY', 'DATABASE_URL' and 'ClOUDINARY_URL'.
- At the top of the page select the 'Deploy' tab.
- For the preferred deployment method select 'Github'.
- Search for your repository name and connect.
- Additionally, automatic deploys can be enabled for deployment after each push to Github.

### **Fork this project**

- Sign in to Github and go to my [repository](https://github.com/broken-helix/keep-it-tidy-london)
- At the top of the page select 'Fork'.
- The Fork will now be added to your repositories.

### **Clone this project**

- Sign in to Github and go to my [repository](https://github.com/broken-helix/keep-it-tidy-london)
- Select the green 'Code' button.
- Select from one of the cloning options HTTPS, SSH or Github CLI. Click the clipboard icon to copy the URL.
- Open git bash
- Enter ‘git clone’ into the text box and then paste the respository URL and select enter.

For more information on cloning please read the github documentation [here](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository)

<hr>

## **Credits**

- [The Code Institutes](https://codeinstitute.net/) 'Malaria Detector' walkthrough project which inspired the main functionality of the application.
- [Stack Overflow](https://stackoverflow.com/) for help with errors encountered during development.
- [W3Schools - Python](https://www.w3schools.com/python/) for reference and research.
- Mo (<https://github.com/link>) - Code Institute mentor.


In the terminal type <code>jupyter notebook --NotebookApp.token='' --NotebookApp.password=''</code> to start the jupyter server.
