# AI-FRCES (AI-powered food recognition and cost estimation system) Project

## Overview

This project aims to provide an innovative solution to the problem of food waste in homes using advanced AI technology. The current implementation allows for food identification and cost calculation through image recognition, and operates in a local environment. Future development will include integration with sensors and cameras, cloud data transmission, and a smartphone app. The system under development automatically identifies and records the amount and type of food discarded using deep learning-based image recognition and high-precision sensing technologies. Furthermore, by implementing a dedicated smartphone app, users will be able to understand and analyze their food waste situation in real-time, promoting awareness and behavioral changes towards food waste reduction. This system not only visualizes food waste but also provides personalized advice tailored to the user's lifestyle, leading to more effective food waste reduction.

## Motivation and Background

Reducing food waste is a crucial challenge in addressing the worsening global food crisis. According to the Food and Agriculture Organization of the United Nations (FAO), it is estimated that approximately one-third of the world's food production is wasted, resulting in significant economic losses and environmental problems. In Japan, approximately 6.12 million tons of food waste was generated in fiscal year 2019, accounting for about 10% of the global total. Household food waste accounts for about half of this, approximately 2.84 million tons, posing a significant problem.

However, many households are not accurately aware of how much food they are actually discarding. Existing data on food waste often relies on national-level statistics or past surveys, lacking real-time data reflecting individual household situations. This makes it difficult for people to internalize the severity of the food waste problem and take concrete action. Furthermore, information provided for food waste reduction is often limited to general knowledge and tips, lacking specific advice tailored to individual household lifestyles and dietary habits.

## Solution

This project aims to contribute to solving the food waste problem in households by developing the AI-powered food and ingredient recognition system. This system, unlike conventional food waste countermeasures, promotes behavioral changes in users through the following three approaches:

1. **High-Precision Data Collection and Visualization:** By combining high-precision sensing technology and AI image recognition technology, the type, quantity, and monetary value of discarded food are measured and recorded in real-time, allowing users to easily grasp their food waste situation. Eliminating the manual input required by conventional recording methods, visualizing food waste based on objective data fosters problem awareness.

2. **Personalized Advice:** Based on the collected data, the system analyzes the user's food waste trends and provides specific advice tailored to individual lifestyles and eating habits. For example, offering practical advice like "You tend to waste a lot of vegetables this week. Let's review how you organize your refrigerator," or suggesting recipes, supports users in reducing food waste in actionable ways.

3. **Automation through Smart Appliance Integration (Future Prospect):** In the future, by integrating with smart appliances such as refrigerators and cooking appliances, we will build a system that automatically manages food from the date of purchase to the expiration date and inventory status, minimizing food waste. For instance, when the expiration date of an ingredient in the refrigerator approaches, the system will automatically suggest recipes or list and warn about soon-to-expire items, reducing the burden on users while achieving food waste reduction.

## System Architecture

The AI-powered food and ingredient recognition system operates in the following four steps:

1. **Sensing and Image Recognition:** Sensors installed in disposers or trash cans measure the weight of the food, and simultaneously, a camera captures an image of the discarded food. The sensor and camera are wirelessly connected to the system, transmitting data in real time.

2. **AI-based Food Classification and Quantity Estimation:** An AI model built on the cloud analyzes the captured image and estimates the type and quantity of discarded food. The AI model is trained on a vast dataset of food images and can identify food items with high accuracy. An algorithm for estimating food volume from images will also be implemented to calculate the discarded amount more precisely.

3. **Cost Calculation and Data Storage:** Based on the estimated food type and quantity, the system calculates the cost of the discarded food by referencing unit price information (stored in `food_prices.csv`) in the system's database. The calculated cost, discarded amount, food type, and other data are stored in the database, linked to the user ID.

4. **Data Transmission and Visualization on Smartphone App:** The stored data is transmitted to the user's smartphone app via an API. The smartphone app displays the daily, weekly, and monthly food waste amount and cost in easy-to-understand graphs, allowing users to check their food waste situation easily. The app will also provide personalized food waste reduction advice to support behavioral changes.

## Tech Stack

* **Python:** Programming language used throughout the project.
* **PyTorch:**  Deep learning framework used to run the AI model (recommended). TensorFlow can also be used, but PyTorch is recommended for better compatibility with timm.
* **Hugging Face Transformers:** A library that provides transformer models for natural language processing and image processing. `DetrForObjectDetection` and `DetrImageProcessor` are used.
* **Pillow (PIL):** Image processing library used for loading, manipulating, and saving images.
* **OpenCV (cv2):** Image processing library used for image acquisition from the camera in `image_capture.py`.
* **Timm (PyTorch Image Models):** A PyTorch image model library. Provides an efficient implementation of the ResNet backbone used in the `facebook/detr-resnet-50` model.
* **Requests:** HTTP library used for sending and receiving HTTP requests in `data_api.py`.
* **NumPy:** Numerical computation library used for multi-dimensional array processing.
* **Pandas:** Data analysis library used for loading `food_prices.csv` and manipulating data.
* **Flask:** Lightweight web framework used to create the API in `data_api.py`.
* **SQLAlchemy:** Python SQL toolkit and Object Relational Mapper (ORM). Used for database operations in `user_data.py`.
* **SQLite:** Lightweight database used to store user data. (Other databases can also be used)


## AI-FRCES_Project Directory Structure and File Explanations

```
AI-FRCES_Project/
├── database/              # Database related
│   ├── food_database.py   # Food price database operations
│   └── user_data.py       # User data management
├── data_acquisition/      # Data acquisition related
│   ├── sensor_reader.py   # Sensor data acquisition
│   └── image_capture.py   # Image capture
├── image_processing/      # Image processing related
│   └── image_classifier.py # Image classification & quantity estimation
├── data_analysis/          # Data analysis related
│   └── cost_calculator.py # Cost calculation
├── cloud_functions/      # Cloud functions
│   └── data_api.py        # Data API
├── app/                   # Smartphone app related
│   └── app.py            # Application logic
├── food_prices.csv        # Food unit price data
├── main.py                # Main program
├── requirements.txt       # Required libraries for execution
└── requirements-dev.txt   # Required libraries for development


```

### `database/`

* **`food_database.py`:** This file is a module for managing food price information. The `load_food_prices` function reads food name and unit price data from the `food_prices.csv` file and returns it in dictionary format. The `get_unit_price` function retrieves the unit price of a specified food item from the dictionary. These functions are used in `cost_calculator.py` to calculate the cost of discarded food.  Error handling for CSV file reading and cases where the food name is not found is implemented to improve system stability. In the future, modifying this to read price information from a database instead of a CSV file will allow for handling larger datasets.

* **`user_data.py`:** This file is a module for saving and retrieving user food waste data to/from a database. The `create_table` function creates the `food_waste_data` table in an SQLite database. The `insert_data` function inserts the user ID, food type, weight, cost, and timestamp into the table.  The `get_data` function retrieves food waste data for a specified user ID. These functions are called from `main.py` and `cloud_functions/data_api.py`. Proper implementation of database connection management, data integrity checks, and error handling ensures system reliability.  Future development will need to include security measures like user authentication and data encryption.


### `data_acquisition/`

* **`sensor_reader.py`:** This file is a module for acquiring weight data from a sensor. Currently, it implements a `read_sensor_data` function that generates random weight data as a simulation.  In the future, this function needs to be replaced with an interface to actual sensor hardware.  The specific implementation will depend on the type of sensor and communication method used. Error handling and data validation should be added to ensure the reliability of the sensor data.  Calibration of sensor data and noise reduction processing may also be necessary.

* **`image_capture.py`:** This file is a module for capturing images from a camera. The `capture_image` function uses the OpenCV library to acquire an image from a connected camera and save it to the specified path.  It implements a series of processes required for image capture, including camera initialization, image capture, saving to a file, and error handling.  Future development will involve adding features like camera setting adjustments (resolution, brightness, etc.), capturing multiple images, and controlling capture timing to enable more flexible image acquisition.  Compatibility with embedded devices like Raspberry Pi will also need to be considered.


### `image_processing/`

* **`image_classifier.py`:** This file is a module for classifying food and estimating its quantity using image recognition AI.  The `classify_image` function reads an image from the given image path and performs object detection using the Hugging Face Transformers `DetrForObjectDetection` model and `DetrImageProcessor`. It identifies the type of food from the detected object's class label. In the future, the functionality to estimate the quantity of food from the image will be added. Currently, it returns a dummy weight value instead of quantity estimation.  This module is the core part of the system, and the accuracy of the AI model significantly affects the overall system performance. Continuous model training, evaluation, and parameter tuning are required to improve recognition accuracy.

### `data_analysis/`

* **`cost_calculator.py`:** This file defines the `calculate_cost` function, which calculates the cost of discarded food based on the type and weight of food output by `image_classifier.py`, and the food unit price data provided by `food_database.py`. This function retrieves the unit price corresponding to the food type from `food_prices.csv` and multiplies it by the weight to calculate the cost.  Error handling for cases where unit price data does not exist is also implemented to ensure system stability.  In the future, more accurate cost calculations could be achieved by considering higher update frequencies for unit price information, and dynamic pricing that takes into account regional and seasonal variations.


### `cloud_functions/`

* **`data_api.py`:** This file defines a cloud-based API that primarily handles data exchange with smartphone apps. It uses the Flask framework to provide two endpoints: `/upload` and `/data/<user_id>`. The `/upload` endpoint saves food waste data sent from the app to the database. The `/data/<user_id>` endpoint retrieves food waste data for a specified user ID and sends it back to the app. Implementation of features necessary for a robust API, such as API authentication, error handling, and data validation, enhances the overall reliability of the system.


### `app/`

* **`app.py`:**  This file is a placeholder for a smartphone app planned for future development. Currently, it has no concrete functionality implemented and simply displays the message "The smartphone app is not yet developed."  In the future, the main logic of the app will be implemented in this file, communicating with `cloud_functions/data_api.py` to send and receive data, visualize data, display feedback to the user, and so on. It is expected to be developed using a cross-platform framework like Flutter or React Native, or with native iOS and Android languages (Swift/Kotlin).


### Other Files

* **`food_prices.csv`:** This CSV file stores food unit price information. It consists of two columns, "food name" and "unit price," and is loaded and used by `database/food_database.py`. Maintaining the accuracy and up-to-dateness of this data is crucial.

* **`main.py`:** This file is the main program for testing the overall system operation in a local environment. It sequentially executes the main functions of the system, such as reading sensor data, image classification, cost calculation, and saving data to the database. It is used to verify that each module is working correctly by using test data and dummy data.

* **`requirements.txt`:** This file lists the required Python libraries for running `AI-FRCES_Project`.  All necessary libraries can be installed by running the command `pip install -r requirements.txt`.

* **`requirements-dev.txt`:** This file lists the libraries needed during the development of `AI-FRCES_Project`.  It includes libraries that assist with development, such as those for testing, code formatting, and static analysis.  Running the command `pip install -r requirements-dev.txt` will install the libraries necessary for development.

These files and directory structure are designed for efficient development and maintenance of the AI-FRCES_Project. The modular nature of each component makes it easy to modify code and add features.


## Installation

The installation procedure for running AI-FRCES_Project is as follows:

1. **Clone the project:**

   Clone the project from GitHub. Execute the following command, replacing `your-username` with your GitHub username and `AI-FRCES_Project` with the repository name.

   ```bash
   git clone https://github.com/your-username/AI-FRCES_Project.git
   ```

   Alternatively, you can download the ZIP file from the GitHub repository page and extract it.


2. **Create and activate a virtual environment:**

   Navigate to the project's root directory (`AI-FRCES_Project`) and create and activate a virtual environment. Using a virtual environment isolates the libraries required for the project from other projects, preventing conflicts.

   * **Windows:**

     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

   * **macOS/Linux:**

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```


3. **Install required libraries:**

   Install the libraries necessary to run the project using `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

   This will install `transformers`, `torch`, `Pillow`, `timm`, `requests`, `numpy`, `pandas`, `opencv-python`, `Flask`, and `SQLAlchemy`.


4. **Install development libraries (optional):**

   Install the libraries required for development (testing, code formatting, static analysis, etc.) using `requirements-dev.txt`.

   ```bash
   pip install -r requirements-dev.txt
   ```

   This will install `pytest`, `flake8`, `black`, `isort`, `mypy`, `jupyter`, and `requests-mock`.



## How to Run

To test and run the system in a local environment, follow the steps below:

1. **Database setup:** Create the database file (`user_data.db`) specified in `database/user_data.py`, and run the `create_table()` function once to create the table. You can do this by running a Python script with the following lines within your activated virtual environment:
    ```python
    from database.user_data import create_table
    create_table()
    ```

2. **Place `food_prices.csv`:** Ensure that `food_prices.csv` exists in the project's root directory.

3. **Place test image:** Create an `images` folder in the project's root directory and place `test_image.jpg` inside it.

4. **Execute `main.py`:** In the project root directory, run the following command:

   ```bash
   python main.py
   ```

   This will execute `main.py` and perform simulated sensor data reading, image classification, cost calculation, and data storage in the database. The execution results will be output to the console.

**Running Cloud Functions:**

`cloud_functions/data_api.py` needs to be deployed and run as a cloud function. The deployment procedure varies depending on the cloud platform used (Google Cloud Functions, AWS Lambda, Azure Functions, etc.).  For local testing, you can run it with `flask run`.

**Running the smartphone app:**

`app/app.py` is currently a placeholder and cannot be run. Develop a smartphone app and link it with the cloud functions.



## Additional Notes on requirements.txt

* **`transformers`:** Hugging Face Transformers. Provides natural language processing and image processing models and toolkits, including `DetrForObjectDetection` and `DetrImageProcessor`.
* **`torch`:** PyTorch. A deep learning framework used as the backend for `transformers`.
* **`Pillow`:** Image processing library used for loading, manipulating, and saving images.
* **`timm`:** PyTorch Image Models. Provides efficient implementations of the ResNet backbone used in the `facebook/detr-resnet-50` model.
* **`requests`:** HTTP library for sending and receiving HTTP requests. Used in `data_api.py`.
* **`numpy`:** Numerical computation library used for multi-dimensional array processing.
* **`pandas`:** Data analysis library used for data manipulation and analysis. Used for loading `food_prices.csv`.
* **`opencv-python`:** OpenCV (Computer Vision) library. Used for image processing and computer vision tasks in `image_capture.py`.
* **`Flask`:** Lightweight web framework. Used to create the API in `cloud_functions/data_api.py`.
* **`SQLAlchemy`:** Python SQL toolkit and Object Relational Mapper (ORM). Simplifies database interaction. Used in `database/user_data.py`.



## Explanation of requirements-dev.txt

* **`pytest`:** Testing framework for creating and running unit and integration tests.
* **`flake8`:** Code style checker. Checks for compliance with style guides such as PEP 8.
* **`black`:** Code formatter. Automatically formats code to maintain a consistent style.
* **`isort`:** Import statement sorter. Organizes import statements for improved readability.
* **`mypy`:** Static type checker. Performs type checking based on type hints to detect potential errors.
* **`jupyter`:** Jupyter Notebook/Lab. Provides an interactive Python environment.
* **`requests-mock`:**  Library for mocking HTTP requests made with the `requests` library. Used for testing `cloud_functions/data_api.py`.



## Future Prospects

AI-FRCES_Project is still in its early stages of development, and many feature additions and improvements are planned.  The main future prospects are as follows:

* **Smartphone App Integration:** Currently, the integration between the cloud functions and the smartphone app is not implemented. In the future, we plan to develop native apps for both iOS and Android, allowing users to check food waste data, view graphs, and receive personalized advice. The app will include various features to promote behavioral changes in users, such as data visualization, personalized advice, and reminder notifications via push notifications.

* **Simultaneous Recognition of Multiple Food Items:**  Currently, `image_classifier.py` can only recognize one type of food at a time.  In the future, we will develop a function to individually recognize and estimate the type and quantity of multiple food items even from images containing various foods. This will allow users to register multiple food items at once, improving convenience.  Implementing this feature will involve adopting more advanced object detection models and image segmentation techniques like instance segmentation.

* **Development of More Accurate AI Models and Expansion of Training Datasets:** The accuracy of the AI model is a crucial factor affecting the overall system performance.  In the future, we plan to improve the recognition accuracy by retraining the model with a larger and more diverse dataset. We will also continuously evaluate and verify the training data for bias, adding and modifying data as needed to build a more versatile model.  Furthermore, we will consider introducing state-of-the-art object detection models and models specifically designed for food recognition.

* **Enhancement of Data Analysis Features:** Currently, the system only performs simple cost calculations. In the future, we aim to provide more useful information to users by enhancing data analysis features.  For example, we envision features such as analyzing user food waste trends, visualizing which foods are discarded how often and in what quantities, and providing personalized advice on food storage methods and recipes tailored to the user's dietary habits.  We are also considering conducting data analysis by region, season, and age group to contribute to the development of effective measures for food waste reduction.

* **Sensor and Camera Integration:** Currently, sensor data acquisition and image capture are simulated.  In the future, we will implement integration with actual sensors and cameras. This will automate the system and improve data accuracy.  The specific implementation will depend on the type of sensors and cameras used and the communication method. We will also consider integration with devices like Raspberry Pi and Arduino to promote the integration of the entire system, including hardware.

* **Implementation of Volume/Weight Estimation Functionality:** Implementing volume/weight estimation functionality in `image_classifier.py` is a significant challenge.  Accurately estimating the volume or weight of food from an image requires the development of advanced image processing techniques and machine learning models.  We will consider introducing 3D cameras, developing depth estimation algorithms, or utilizing existing pre-trained models.



## License

See the LICENSE file.


## Disclaimer

This project is a research and development project aimed at calculating household food waste and its associated costs. It is not provided as a practical product or service. Features such as sensor/camera integration, smartphone app integration, and volume/weight estimation are still under development and their full functionality is not guaranteed.  Furthermore, as this system is in the development stage, stability and security are not guaranteed.

The AI model used in this project is trained on a specific dataset and therefore may not correctly recognize all foods.  The recognition accuracy is limited, and misrecognition may occur. In addition, the food prices listed in `food_prices.csv` are sample data and may not reflect actual market prices.  The accuracy of this data is not guaranteed.

The code and data of this project are intended for educational and research purposes only, and commercial use is **expressly prohibited**. The developer assumes no responsibility for any damages resulting from the use of this project. Please use it at your own risk.

This project is developed and provided by yf591.
