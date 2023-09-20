# **Mildew Detector - Introduction**

The Mildew Detector is a project which employs machine learning to teach
an algorithm to be able to make a prediction on whether a leaf is infected
with Powdery Mildew or not.

[View the live project here](link).

![Am I Responsive?](responsive-link.jpg)

***

## **Table of Contents**

- [**Dataset Content**](#dataset-content)
- [**Business Requirements**](#business-requirements)
- [**Hypotheses**](#hypotheses)
  - [*Hypothesis 1*](#hypothesis-1)
  - [*Hypothesis 2*](#hypothesis-2)
- [**Rationale**](#rationale)
  - [*Data Visualisation*](#business-requirement-1)
  - [*Classification*](#business-requirement-2)
- [**ML Business Case**](#ml-business-case)
- [**Dashboard Design**](#dashboard-design)
  - [*Summary*](#summary)
  - [*Leaves Visualiser*](#leaves-visualiser)
  - [*Mildew Detector*](#mildew-detector)
  - [*Hypotheses and Validation*](#hypotheses-and-validation)
  - [*ML Performance*](#ml-performance)

- [**Testing**](#testing)
- [**Technologies Used**](#technology-used)
- [**Deployment**](#deployment)
- [**Credits**](#credits)

***

## **Dataset Content**

The dataset is made up of 4208 images of single cherry tree leaves, taken from healthy trees and those infected with Powdery Mildew.

The dataset is sourced from
[Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).

***

## **Business Requirements**

The business requirements for the project are as follows:
* **Business requirement 1** - *The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one infected with Powdery Mildew*.
* **Business requirement 2 -** *The client is interested in predicting if a cherry leaf is healthy or infected with Powdery Mildew*.

The fictional company, Farmy & Foods, has a number of cherry tree plantations and are experiencing problems with Powdery Mildew infections. Powdery Mildew is a disease is caused by *Podosphaera clandestina*, one of the common species of the Powdery Mildew group of fungi. The disease affects cherry trees, damages and stunts new leaf growth and can affect crop return in commercial settings. The same fungus reportedly causes Powdery Pildew in peaches, apricots, apples and pears.  

Currently, the company process to detect this infection involves manual checking of the cherry tree leaves. An employee spends around 30 minutes in each tree, taking a few samples of leaves and visually deciding if the leaf tree is healthy or has Powdery Mildew. If infection is suspected, the employee applies a chemical compound to kill the fungus. The time spent applying this compound is 1 minute.  

The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.  

To save time, the IT team have suggested a Machine Learning system that detects instantly, using an image of a leaf, if the tree is healthy or has Powdery Mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for other crops.  

The dataset is a collection of cherry leaf images, provided by the client from their plantations.  

***

## **Hypotheses**

### **Hypothesis 1**

*There is a visual difference in appearance between infected and health cherry tree leaves.*

* Business requirement 1 requires a study to visually differentiate a healthy leaf from an infected one.
* The hypothesis will be investigated with an average image study.

### **Hypothesis 2**

*It is possible to predict, with at least 97% accuracy, if an image of a cherry tree leaf is infected with powdery mildew.*

* Business requirement 2 is that the client wants to predict if a cherry tree is infected or healthy, with at least 97% accuracy.
* The hypothesis will be tested by training a model on the train and test images and calculating the accuracy with a validation set.

***

## **Rationale**

*Mapping the business requirements to the tasks. User stories can be found, along with Epics, on the project board here:*

### **Business Requirement 1**
**Data Visualisation**

*User Stories*
* As a **client** I can **visually differentiate a healthy from an infected leaf** so that **I can visually determine if leaves are infected or not**.
* As a **client** I can **view the difference between average healthy and infected leaves** so that **I can view any differences between samples**.
* As a **client** I can **display a montage of images of infected and healthy leaves** so that **I can see differences between them**.

*Tasks*
* Calculate standard deviation and mean of infected and healthy leaf images.
* Display on the Streamlit dashboard, average and average variability images for infected and healthy leaves.
* Display differences between healthy and infected leaves on the Streamlit dashboard.<br>
* Create an image montage viewer on the Streamlit dashboard to display a selection of either healthy or infected leaf images.

***

### **Business Requirement 2**
**Classification**

*User Stories*
* As a **client** I can **determine that the Machine Learning Model is accurate to at least 97%** so that **I can be sure the results are accurate**.
* As a **client** I can **upload an image of a cherry tree leaf** so that **I can get an indication of whether it is infected or healthy**.
* As a **client** I can **download a report** so that **I can view the results outside of the dashboard environment**.

*Tasks*
* Build a binary classifier.
* Validate the accuracy of the model with the validation set.
* Display the results on the Machine Learning Performance page of the Streamlit dashboard.
* Use the model to create the Mildew Detector page of the Streamlit dashboard.

***

### **ML Business Case**

* An ML model is required to predict if a leaf is infected with Powdery Mildew or not, based on the provided dataset. The problem requires a **supervised, 2-class, single-label, classification model**.
* The ideal outcome is to provide the company with a faster and more reliable detector for Powdery Mildew detection.
* The model success metrics are an **accuracy of 97% or above** on the test set.
* The model output is defined as a flag, indicating if the leaf has Powdery Mildew or not and the associated probability of being infected or not. The farmers will take a picture of a leaf and upload it to the App.
* Heuristics: The current detection method is based on a manual inspection. Visual collection and inspection is slow and it leaves room to produce inaccurate diagnostics due to human error.
* The training data to fit the model comes from the leaves database provided by Farmy & Foody company and uploaded on Kaggle. This dataset contains 4208 images of cherry leaves.

***

## **Dashboard Design**

### **Navigation**

#### **Streamlit MultiPage**

![Streamlit Menu](streamlit-menu.jpg)

### **Summary**

The *summary* page contains a brief summary of the project, together with three sections:
* **Disease Information**. Information about Powdery Mildew disease, its causes, symptoms and life cycle.
* **Business Requirements**. The requirements of the client for a successful outcome to the project.
* **Project Dataset**. A summary of the dataset details.

![Streamlit Summary](streamlit-summary.jpg)

### **Leaves Visualiser**
**This page handles Business Requirement 1**
The *leaves visualiser* page displays a brief summary and three checkboxes:
* Difference between average and variability image.
* Differences between average infected and average healthy leaves.
* Image Montage of either healthy or infected leaves.

![Streamlit Visualiser](streamlit-visualiser.jpg)

### **Mildew Detector**
**This page handles Business Requirement 2**
The *mildew detector* page shows an information section, together with instructions on how to use the detector and a link to sample images. 
When an image is uploaded, a report is generated which displays:
* An image.
* A message indicating the model prediction.
* A probability chart.
* A downloadable report.

![Streamlit Detector](streamlit-detector.jpg)

### **Hypotheses and Validation**
Block for each hypothesis, describe conclusion and how validated

![Streamlit Hypothesis](streamlit-hypothesis.jpg)

### **ML Performance**
**This page handles Business Requirement 2**
Label frequencies for train, test and validation sets
model history, accuracy and losses
model evaluation results.

![Streamlit ML Performance](streamlit-performance.jpg)

***

### **Epics and User Stories**

Information gathering and data collection.
Data visualization, cleaning, and preparation.
Model training, optimization and validation.
Dashboard planning, designing, and development.
Dashboard deployment and release.

### Information gathering and data collection ###

### Data visualization, cleaning, and preparation ###

### Model training, optimization and validation ###

### Dashboard planning, designing, and development ###

### Dashboard deployment and release ###

### **Agile Methodology**

An Agile Approach was followed in the planning and construction of the site.  User stories were built using GitHub Issues, grouped into Epics for different aspects of the project and organised onto a board.
Each user story has a list of tasks to tick off and an acceptance criteria.  As stories were built, they were moved to the Not Started column of the board.  Once they were started, they were moved to the In Progress Column and finally, when all tasks were complete, the story was moved to the complete column and marked closed.  Each story was listed in relevant Epic as a task and ticked off when the story was complete.

The project board can be viewed here: [Mildew Detector Project Board](link).

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
