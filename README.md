# **Powdery Mildew in Cherry Leaves**

The deployed site can be visited by clicking [**here**](https://portfolio-five-e905b6564a53.herokuapp.com/).

The site code can be viewed in this [**GitHub Repository**](https://github.com/Marc-Hanson/portfolio-five).

I designed the app for submission as my 'Portfolio Project 5', part of the [**Code Institute Fullstack Software Development Diploma**](https://codeinstitute.net/ie/full-stack-software-development-diploma/). The aim of this project is to build a full-stack site based on business-oriented logic, used to control a centrally-owned dataset. A requirement is to set up an authentication mechanism and provide role-based access to the site's data, and for the site to be fully deployed for public use. The required technologies for the project are:

## **Table of Contents**

- [**Powdery Mildew in Cherry Leaves**](#powdery-mildew-in-cherry-leaves)
  - [**Table of Contents**](#table-of-contents)
  - [**Dataset Contents**](#dataset-contents)
  - [**Business Requirements**](#business-requirements)
  - [**Hypothesis and Validation**](#hypothesis-and-validation)
  - [**Project Rationale**](#project-rationale)
  - [**Business Case**](#business-case)
  - [**Dashboard Design**](#dashboard-design)
    - [Page 1: Project Summary](#page-1-project-summary)
    - [Page 2: Leaves Visualizer](#page-2-leaves-visualizer)
    - [Page 3: Mildew Detector](#page-3-mildew-detector)
    - [Page 4: Project Hypothesis and Validation](#page-4-project-hypothesis-and-validation)
    - [Page 5: ML Performance Metrics](#page-5-ml-performance-metrics)
  - [**Deployment**](#deployment)
    - [Creating A Heroku App](#creating-a-heroku-app)
    - [Forking the Repository](#forking-the-repository)
    - [Making a local clone](#making-a-local-clone)
  - [**Technologies Used**](#technologies-used)
  - [**Credits**](#credits)

## **Dataset Contents**

The dataset contains 4000+ photos of single cherry leaves, split evenly between infected and healthy leaves. It was sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).  
The images are taken from the client's crop fields and show leaves that are either healthy or infected by Podosphaera clandestina, an obligate biotrophic fungus.  
The cherry plantation crop is one of the finest products in their portfolio, and the company is concerned about supplying the market with a compromised quality product.

## **Business Requirements**

The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew.
Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree,  
taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew,  
the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute. The company has thousands of cherry trees,  
located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

In summary:

1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.
2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## **Hypothesis and Validation**

My initial hypothesis was that infected leaves have a clear discolouration seperating them from the healthy leaves.
Infected leaves display a soft white powdery coating, my hope was that this contrast between green and white would provide a feature for image classification.

An average image study was used to show a clear difference between healthy and infected cherry leaves.

![average_image](https://github.com/Marc-Hanson/portfolio-five/blob/main/readme_images/average_image.png)
![average_variabiity](https://github.com/Marc-Hanson/portfolio-five/blob/main/readme_images/image_variability.png)

The model was able to detect these differences and was able to successfully predict if a leaf was healthy or infected.
To validate this, images were taken from our test data were successfully identified by the model.  

## **Project Rationale**

- The 2 main business requirements were split in to several user stories:
  - As a client I want to view the mean and standard deviation for healthy and infected leaves, so I can visually distinguish them.
  - As a client I wish to view the difference between the average healthy and infected cherry leaf, so I can visually distinguish them.
  - As a client I wish to view an image montage of healthy and infected cherry leaves, so I can visually distinguish them.
  - As a client I wish to view this data on an interactive dashboard, so the data is easily interpreted.

The user stories were then resolved using ML tasks in Jupyter notebooks and displayed on a Streamlit dashboard.

## **Business Case**

- We want a ML model to predict if a leaf is either healthy or infected with powdery mildew, based on the images provided by the client. It is through supervised learning, a 2-class, single-label, classification model.
- Our ideal outcome is to provide the client with a fast and reliable detector for powdery mildew.
- The model success metrics are:
  - Accuracy of 87% or above on our test data set.
- The model output is defined as a flag, reporting if the leaf has powdery mildew or not and the associated probability of being healthy or not. The client will take a picture of a leaf and upload it to the App. The prediction is made on the fly (not in batches).
- Heuristics: The current detection method is based on a manual inspection. The client spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. Visual criteria is slow and it leaves room to produce inaccurate diagnostics due to human error.
- The training data used to fit the model is from the leaves database provided by the client and uploaded on Kaggle. This dataset contains 4000+ images of cherry leaves.

## **Dashboard Design**

### Page 1: Project Summary

- Project summary
  - General Information
    - Powdery mildew of sweet and sour cherry is caused by Podosphaera Clandestina, an obligate biotrophic fungus.
    - Mid- and late-season sweet cherry (Prunus avium) cultivars are commonly affected, rendering them unmarketable due to the covering of white fungal growth on the cherry surface.
    - Season long disease control of both leaves and fruit is critical to minimize overall disease pressure in the orchard and consequently to protect developing fruit from accumulating spores on their surfaces.
  - Project Dataset
    - The available dataset contains 4208 leaves, split exactly in half with 2104 healthy leaves and 2104 infected leaves. These photos are taken with a plain background.
  - For additional information, please visit and read the Project README file.
  - Business requirements
    - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
    - The client is interested in predicting if a cherry lead is healthy or contains powdery mildew.

### Page 2: Leaves Visualizer

- The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
  - Checkbox 1 - Difference between average and variability image.
  - Checkbox 2 - Differences between average infected and average healthy leaves.
  - Checkbox 3 - Image Montage.

### Page 3: Mildew Detector

- The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.
- You can download a set of infected and uninfected leaves for live prediction. You can download the images from here.
- User Interface with a file uploader widget. The user should upload multiple cherry leaf images. It will display the image and a prediction statement, indicating if the leaf is infected or not, and the probability associated with this statement.
- Table with image name and prediction results.
- Download button to download table.

### Page 4: Project Hypothesis and Validation

- We suspect mildew infected leaves have clear marks/signs, typically in the middle of the leaf, that can be used to differentiate between infected and healthy leaves.
- Our Image Montage, shows that typically an infected leaf has a stringy white growth across the leafs surface. Average Image, Variability Image and Difference between Averages studies didn't reveal any clear pattern to differentiate one to another.

### Page 5: ML Performance Metrics

- Label Frequencies for Train, Validation and Test Sets.
- Model History - Accuracy and Losses.
- Model evaluation result.

## **Deployment**

The project is coded and hosted on GitHub and deployed with [Heroku](https://www.heroku.com/).

### Creating A Heroku App

The steps needed to deploy this projects are as follows:

1. Create a `requirement.txt` file in GitHub, for Heroku to read, listing the dependencies the program needs in order to run.
2. Set the `runtime.txt` Python version to a Heroku-20 stack currently supported version.
3. `push` the recent changes to GitHub and go to your [Heroku account page](https://id.heroku.com/login) to create and deploy the app running the project.
4. Chose "CREATE NEW APP", give it a unique name, and select a geographical region.
5. Add  `heroku/python` buildpack from the _Settings_ tab.
6. From the _Deploy_ tab, chose GitHub as deployment method, connect to GitHub and select the project's repository.
7. Select the branch you want to deploy, then click Deploy Branch.
8. Click to "Enable Automatic Deploys " or chose to "Deploy Branch" from the _Manual Deploy_ section.
9. Wait for the logs to run while the dependencies are installed and the app is being built.
10. The mock terminal is then ready and accessible from a link similar to `https://your-projects-name.herokuapp.com/`
11. If the slug size is too large then add large files not required for the app to the `.slugignore` file.

### Forking the Repository

- By forking this GitHub Repository you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original repository. The steps to fork the repository are as follows:
  - Locate the [GitHub Repository](https://github.com/Marc-Hanson/portfolio-five) of this project and log into your GitHub account.
  - Click on the "Fork" button, on the top right of the page, just above the "Settings".
  - Decide where to fork the repository (your account for instance)
  - You now have a copy of the original repository in your GitHub account.

### Making a local clone

- Cloning a repository pulls down a full copy of all the repository data that GitHub.com has at that point in time, including all versions of every file and folder for the project. The steps to clone a repository are as follows:
  - Locate the [GitHub Repository](https://github.com/Marc-Hanson/portfolio-five) of this project and log into your GitHub account.
  - Click on the "Code" button, on the top right of your page.
  - Chose one of the available options: Clone with HTTPS, Open with Git Hub desktop, Download ZIP.
  - To clone the repository using HTTPS, under "Clone with HTTPS", copy the link.
  - Open Git Bash. [How to download and install](https://phoenixnap.com/kb/how-to-install-git-windows).
  - Chose the location where you want the repository to be created.
  - Type: `$ git clone https://github.com/Marc-Hanson/portfolio-five.git`
  - Press Enter, and wait for the repository to be created.
  - Click [Here](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) for a more detailed explanation.

**You can find the live link to the site here: [Cherry Powdery Mildew Detector](https://portfolio-five-e905b6564a53.herokuapp.com/)**

## **Technologies Used**

- [Heroku](https://www.heroku.com/) was used to deploy the streamlit app.
- [Jupiter Notebook](https://jupyter.org/) was used to create ML notebooks for Data collection and visualization.
- [Kaggle](https://www.kaggle.com/) provided the datasets for this project.
- [GitHub](https://github.com/) was used for version control.
- [CodeAnywhere](https://app.codeanywhere.com/) was the IDE of choice and all code was written using this app.

## **Credits**

- The template used for this project belongs to CodeInstitute - [GitHub](https://github.com/Code-Institute-Submissions) and [website](https://codeinstitute.net/global/).
- Inspiration for this project was also provided by CodeInstitute via their 'Walkthrough Project 01' - [GyanShashwat1611](https://github.com/GyanShashwat1611/WalkthroughProject01/tree/main).
- Lots of help was provded by from Claudia Cifaldi - [cla-cif](https://github.com/cla-cif) on Github.
- As well as help from Nicholas Renotte - [NicholasRenotte](https://www.youtube.com/@NicholasRenotte) on YouTube.
- Also thanks to my mentor Mo Shami - [mshami](https://github.com/mshami).
