# EBS Transliteration Backend

This project provides a Flask-based API for transliterating text using the Indic Trans library. It is designed to facilitate easy access to transliteration services for various Indian languages.
## Frontend

A frontend for this API is available at [EBS Transliteration Frontend](https://github.com/suryatejathodupunuri/ebs.transliteration). This frontend provides a user-friendly interface for interacting with the transliteration API, allowing users to easily input text and view transliterated results.

## Installation  
Follow these steps to set up the EBS Transliteration Backend on your local machine.

1. **Clone and install Indic-Trans:**
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

2. **Download Python and check the version:**
   - Ensure Python is installed and check the version:
     ```bash
     python --version
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

6. **Run the backend code:**
   - Start the backend server:
     ```bash
     python3 backend.py
     ```
## API Endpoints

### Transliterate Text

**Endpoint:** `/transliterate`

**Method:** `POST`

**Description:** Transliterates the given text from the source language to the target language.

**Request Body:**

```json
{
  "src": "eng",
  "tar": "hin",
  "inp": "Mere pyaare desh vasiyo, aaj main aap sabse yah kehna chahta hoon ki hum sabhi ek saath milkar hamare desh ko majboot banayenge. aap sabka sahyog bahumulya hai. Humein milkar pragati ke marg par agrasar hona hai. dhanyavad."
}

