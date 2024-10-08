# EBS Transliteration Backend

This project provides a Flask-based API for transliterating text using the Indic Trans library. It is designed to facilitate easy access to transliteration services for various Indian languages.
## Frontend

A frontend for this API is available at [EBS Transliteration Frontend](https://github.com/suryatejathodupunuri/ebs.transliteration). This frontend provides a user-friendly interface for interacting with the transliteration API, allowing users to easily input text and view transliterated results.

## Installation  
Follow these steps to set up the EBS Transliteration Backend on your local machine.

1. **Clone and install [Indic-Trans](https://github.com/libindic/indic-trans.git):**
   - Clone the repository:
     ```bash
     git clone https://github.com/libindic/indic-trans.git
     ```
   - Change to the cloned directory and install:
     ```bash
     cd indic-trans
     pip install -r requirements.txt
     pip install .
     ```

2. **Download Python, check the version and install mysql-connector-python:**
   - Ensure Python is installed,check the version and install mysql-connector-python:
     ```bash
     python --version
     pip install mysql-connector-python
     ```

3. **Download Flask and install Flask-CORS:**
   - Install Flask and Flask-CORS:
     ```bash
     pip install Flask
     pip install Flask-CORS
     ```

4. **Clone the GitHub repository containing the backend code:**
   - Clone the repository:
     ```bash
     git clone https://github.com/suryatejathodupunuri/ebs_transliteration_backend.git
     ```

5. **Change to the cloned directory:**
   - Navigate into the cloned project directory:
     ```bash
     cd ebs_transliteration_backend
     ```
6. **Set up the database**
   - Modify the host,username and password in the code as per the deployed system
   - Create Database transliteration
     ```bash
     create database transliteration_db;
     ```
   - use transliteration database
     ```bash
     use transliteration_db;
     ```
    - create table transliteration
     ```bash
     CREATE TABLE transliteration (id INT AUTO_INCREMENT PRIMARY KEY, date TIMESTAMP DEFAULT CURRENT_TIMESTAMP, user VARCHAR(255) NOT NULL DEFAULT 'guest', src CHAR(3), tar CHAR(3), inp LONGTEXT, output LONGTEXT,ipaddress VARCHAR(255));
     ```
7. **Run the backend code:**
   - Start the backend server:
     ```bash
     python3 backend.py
     ```
## API Endpoints

### Transliterate Text

**Endpoint:** `/api/transliterate`

**Method:** `POST`

**Description:** Transliterates the given text from the source language to the target language.

**Request Body:**

```json
{
  "src": "eng",
  "tar": "hin",
  "inp": "Mere pyaare desh vasiyo, aaj main aap sabse yah kehna chahta hoon ki hum sabhi ek saath milkar hamare desh ko majboot banayenge. aap sabka sahyog bahumulya hai. Humein milkar pragati ke marg par agrasar hona hai. dhanyavad."
}
```
**Response:**

```json
[
  {
    "output": "मेरे प्यारे देश वसियो, आज में आप सबसे यह कहना चाहता हूँ की हम सभी एक साथ मिलकर हमारे देश को मजबूत बनायेंगे. आप सबका सहयोग बहुमुल्य हैं. हमें मिलकर प्रगती के मार्ग पर अग्रसर होना हैं. धन्यवाद."
  },
  {
    "status": "SUCCESS"
  }
]
```

### Test Endpoint

**Endpoint:** `/api/test`

**Method:** `GET`

**Description:** Checks if the backend server is running successfully.

**Response:** Backend Running Succesfully.

