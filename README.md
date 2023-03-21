# LOCAL CHATGPT

This is a project for setting up chatGPT for local use in Python and Docker

### Configuration files
To be able to use the project, some configuration files are needed (a single one for now):
* .env file at the project root

#### .env file
The `.env` file is used to store credentials for connections to databases for instance. Since passwords are sensitive, 
this file should never be committed as is. Instead, a CI system will be implemented to insert the sensitive data in a 
template `.env` file.

To setup your local environment, create at the project root a `.env` file with:
```dotenv
# OPEN_AI_KEY
OPEN_AI_KEY=YOUR_API_KEY

# GPT Models
MODEL_CODE=YOUR_MODEL_CODE
```
Fill the missing fields with their appropriate values.

#### Running the Application
The application can simply be run by using this code in the terminal:
* run application: `python -m main`

