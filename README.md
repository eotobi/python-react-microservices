# Python-React Microservices

## Welcome
Welcome to the Python-React Microservices project! This repository contains a powerful combination of Django and Flask REST frameworks that expose admin and product APIs, specially crafted for seamless integration with React frontend applications. The admin functionalities are implemented using Django, while Flask takes charge of handling product-related operations. These components communicate seamlessly through a RabbitMQ queue, ensuring efficient and robust data flow from frontend to the 2 MySql databases

## Features

- **Admin Functionality with Django:** Leverage the capabilities of Django for comprehensive admin operations, providing a user-friendly interface and powerful administrative tools.

- **Product API with Flask:** Utilize Flask to handle product-related functionalities, ensuring a lightweight and efficient solution for managing your product data.

- **RabbitMQ Queue Integration:** Seamless communication between Django and Flask components via a RabbitMQ queue ensures reliable and asynchronous data exchange.

- **Docker Container Deployment:** Deploy the entire application effortlessly using Docker containers, simplifying the setup process and ensuring consistency across different environments.

## Getting Started

To run the application from the ground up, follow these simple steps:

1. **Navigate to the Main Directory:**

   ```bash
   cd main

3. **Launch Main Application:**

    ```bash
    docker-compose up

2. **Navigate to Admin Directory:**

    ```bash
    cd admin

3. **Launch Admin Application:**

    ```bash

    docker-compose up

4. **Access the Frontend App:**
    Once the setup is complete, the frontend application will be accessible at http://localhost:3000.

## Contributions
Feel free to contribute to this project by submitting issues or pull requests. Your input is highly valued!