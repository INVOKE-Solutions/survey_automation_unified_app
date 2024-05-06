### INVOKE-Solutions/survey_automation_unified_app

#### Overview

This project is a unified web application for automating IVR data cleaning, weighting, and cross-tabulation. It combines Streamlit, Shiny, FastAPI, and AWS services, including API Gateway, S3, ECR, and ECS. The application features a dual frontend with Streamlit for Python tasks and Shiny for R tasks, supported by FastAPI for efficient data processing. AWS S3 stores both raw and processed data, while ECR and ECS manage and deploy Docker containers for scalability and reliability.

#### Components

- **Streamlit and Shiny**: Frontend interfaces for interactive data processing tasks.
- **FastAPI**: Backend logic for data operations and frontend service.
- **AWS API Gateway**: Manages API calls and routes them to the appropriate services.
- **AWS S3**: Stores application data securely.
- **AWS ECR and ECS**: Store Docker images and manage container deployment and scaling.
- **Docker**: Essential for containerizing the application, ensuring consistent operation across environments.

#### Workflow

1. **Frontend Development**: Create interactive interfaces using Streamlit and Shiny.
2. **Backend Development**: Implement data processing logic with FastAPI.
3. **Containerization**: Package the application into Docker containers for portability.
4. **AWS Setup**: Configure AWS services for data storage and container orchestration.
5. **Deployment**: Launch the application on ECS for public or private use.
6. **Operation**: Users interact with the application for data tasks, with AWS managing storage and scalability.

#### Usage

To use this application, ensure you have Docker installed. Clone the repository and navigate to the project directory. Run `docker-compose up` to build and start the application. Access the application at `http://localhost:8501` for Streamlit and `http://localhost:3838` for Shiny.

#### License

This project is licensed under the INVOKE License, which prohibits unauthorized copying, modification, merging, publishing, distribution, sublicensing, or selling of the software without explicit permission from INVOKE.

#### Contributors

- [Fahmi Zainal]([https://github.com/fahmizainal17])
