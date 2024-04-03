# Master Chef AI

## Description

* Problem definiton : How can a local restaurant with no Master Chefs on staff consistently cook and serve great recipes to their customers?


* This project utilizes Django, a high-level Python web framework, to create an end-to-end solution that streamlines the cooking process. It smartly incorporates sessions within Django, minimizing repetitive API calls and preserving the valuable insights provided by the Language Model (LLM). This ensures that once fetched, the messages and guidance from the LLM remain readily accessible, enhancing efficiency and user experience.

## Installation

Follow these steps to set up the "Master Chef AI" project on your local machine:

1. Ensure that you have Python and pip installed on your system. If not, download and install them from the official Python website.

2. Clone the repository to your local machine:

    `git clone https://github.com/singhabhishekkk/LangChain.git`

    `cd MasterChefAI`


3. Create a virtual environment to manage the project's dependencies:

    `python -m venv chefenv`
    `source chefenv/bin/activate ` # On Windows use `chefenv\Scripts\activate`

    Install the required dependencies using the provided requirements.txt file:

4. `pip install -r requirements.txt`
    Navigate to the project directory and run the Django migrations to set up your database schema:


5. Start the Django development server:

    `python manage.py runserver`

    Open your web browser and go to `http://127.0.0.1:8000/` to view the application.


## Credits

* LangChain: For their exceptional tools that bridge the gap between language models and application-specific functionalities.

* Geeky Shows: For their comprehensive tutorials on Django and LangChain

