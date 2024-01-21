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
  - [**Model Rationale**](#model-rationale)
  - [**ML Business Case**](#ml-business-case)
  - [**Dashboard Design**](#dashboard-design)
  - [**Unfixed Bugs**](#unfixed-bugs)
  - [**Deployment**](#deployment)
  - [**Technologies Used**](#technologies-used)
  - [**Credits**](#credits)

## **Dataset Contents**

The dataset contains 4000+ featured photos of single cherry leaves, split evenly between infected and healthy leaves. It was sourced from [Kaggle](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves). 
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

An image montage was used to show a clear difference between healthy and infected cherry leaves.
![MONTAGE_IMAGE](link to image)
![MONTAGE_IMAGE](link to image)

White mass in center.
![IMAGE](link to image)

and contrast.
![IMAGE](link to image)

The model was able to detect these differences and was able to successfully predict if a leaf was healthy or infected.
To validate this, images were taken from our test data were successfully identified by the model.