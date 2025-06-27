# End to End Hotel Reservation Prediction App


### Overview

This project provides a robust Hotel Reservation Prediction application designed to assist hotel management staff in foreseeing whether a customer is likely to cancel their reservation. By leveraging machine learning, the application aims to reduce revenue loss due to last-minute cancellations and optimize resource allocation.

The backend of the application is built using Flask, a lightweight and powerful Python web framework.

### Benefits for Hotel Management
This application offers significant benefits for hotel operations:

Proactive Management: Predict potential cancellations in advance, allowing staff to implement strategies to retain customers or fill vacant rooms.

Revenue Optimization: Minimize "no-show" losses by identifying high-risk reservations and taking appropriate action (e.g., re-marketing, overbooking strategies, personalized offers).

Improved Resource Allocation: Optimize staffing, inventory, and other resources by having a clearer picture of expected occupancy.

Enhanced Customer Satisfaction: By proactively addressing potential issues, hotels can offer better service and improve guest experience.

Data-Driven Decision Making: Provides actionable insights based on predictive analytics, leading to more informed business decisions.

### Architecture and Technologies
The project follows a modern MLOps architecture, incorporating best practices for development, deployment, and MLOps.

Backend: Flask

Source Code Management: GitHub

CI/CD: Jenkins

Containerization: Docker

Container Registry: Google Container Registry (GCR)

Deployment: Google Cloud Run

CI/CD Pipeline (Jenkins)
The CI/CD pipeline is orchestrated using Jenkins. A key aspect of this setup is the use of a Docker-in-Docker (DinD) architecture for Jenkins. This allows Jenkins to build Docker images within its own container, providing a clean and isolated build environment.

The Jenkins pipeline automates the following steps:

Fetches the latest code from GitHub.

Builds the Docker image for the Flask application.

Pushes the Docker image to Google Container Registry (GCR).

Deploys the new image to Google Cloud Run.

Training Pipeline
The machine learning model's training pipeline is designed for efficiency and scalability:

Data Ingestion: The pipeline fetches raw reservation data from a Google Cloud Storage Bucket.

Data Preprocessing: The fetched data undergoes rigorous preprocessing steps, including cleaning, feature engineering, and transformation, to prepare it for model training.

Model Training: A machine learning model is trained on the preprocessed data to learn patterns associated with reservation cancellations. The trained model is then integrated with the Flask application for predictions.

Deployment (Google Cloud Run)
The application is deployed as a containerized service on Google Cloud Run. Cloud Run provides a fully managed, serverless platform that automatically scales the application based on demand, ensuring high availability and cost-effectiveness.


### Screenshots
Here are a couple of screenshots demonstrating the application in action:

##### Application Screenshot 1

![Screenshot 1](https://github.com/maskedwolf4/Hotel-Reservation-Prediction/blob/main/images/img1.png)

![Screenshot 2](https://github.com/maskedwolf4/Hotel-Reservation-Prediction/blob/main/images/img2.png)
