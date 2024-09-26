
# POTATO Take-Home Task

## Overview

This project provides an API that allows querying a dataset of tweets to retrieve key statistics such as tweet counts, unique users, and average likes based on a search term. It uses Python, MongoDB, and Flask to create a system for efficiently analyzing tweets and their metadata.

## Project Structure

1. **Virtual Environment**: A Python virtual environment `potato_home_task` was created to isolate dependencies.
   
2. **Libraries**: All dependencies are listed in the `requirements.txt` file. Key libraries include:
   - `pandas`
   - `pymongo`
   - `Flask`
   - `seaborn`
   - `jupyter`

3. **Key Features**:
   - **Data Ingestion**: Loads the data from TSV files into MongoDB for querying.
   - **Querying**: Allows you to retrieve information on:
     - Number of tweets posted containing a specific term per day.
     - Number of unique users tweeting that term.
     - Average likes on tweets containing that term.
     - Locations (place IDs) of tweets.
     - Time of day tweets were posted.
     - The user who posted the most tweets containing the term.

4. **API**: The project includes Flask-based APIs to expose query functionalities.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd POTATO-Home_Task
```

### 2. Set Up a Virtual Environment
- Create a virtual environment:
  ```bash
  python -m venv potato_home_task
  ```
- Activate the virtual environment:
  - For Windows:
    ```bash
    .\potato_home_task\Scripts\activate
    ```
  - For Mac/Linux:
    ```bash
    source potato_home_task/bin/activate
    ```

### 3. Install Dependencies
- Install the required Python libraries using the `requirements.txt` file:
  ```bash
  pip install -r requirements.txt
  ```

### 4. Load Data into MongoDB
- Run the script to ingest the tweet data from the TSV file into MongoDB:
  ```bash
  python ingest_data.py
  ```

### 5. Run the Flask API
- To start the API server, run:
  ```bash
  python app.py
  ```

- The API will be running at: `http://127.0.0.1:5000/`

### 6. API Endpoints

Use Postman or curl to access the API.

#### Examples:

- **Tweet Count per Day**:
  ```
  GET /tweets/count?term=music
  ```
  Returns the number of tweets containing the search term, grouped by day.

- **Unique Users**:
  ```
  GET /tweets/unique_users?term=music
  ```
  Returns the number of unique users who tweeted using the term.

- **Average Likes**:
  ```
  GET /tweets/avg_likes?term=music
  ```
  Returns the average number of likes on tweets containing the term.

- **Tweets by Place ID**:
  ```
  GET /tweets/places?term=music
  ```
  Returns the list of unique place IDs where tweets containing the term originated.

- **Most Active User**:
  ```
  GET /tweets/top_user?term=music
  ```
  Returns the user who tweeted the most about the term.

## Testing the API

- Test API endpoints with Postman or curl.
- Example request:
  ```
  GET http://127.0.0.1:5000/tweets/count?term=music
  ```

## Additional Information

- **Docker Support**: If needed, you can set up the project using Docker for easy environment replication.
- **API Documentation**: The API follows standard RESTful practices, and responses are in JSON format for easy consumption.
