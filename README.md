# Week 3 technical exercise for the COMP.CS.530-2024-2025-1 Fine-tuning Large Language Models (LLM)

This is a monorepo holding the python flask app for sentiment analysis with a react frontend. It also holds the google colab notebook for week 3. To be noted, the notebook is not compatible with the virtual env and the environment variables; it is made to be run in google colab with appropriate secrets.

## Installation

To run the app, you just need to set up the python backend - fronend is built to the static "dist" folder.

After cloning, make a virtual environment and activate:
>python -m venv .venv
>.venv\scripts\activate

Install dependancies:
>pip install -r requirements.txt

Please note, that the torch required by the models is system specific. Installing from the requirements.txt probably does not work. Visit:
>https://pytorch.org/get-started/locally/

after you have your virtual environment ready, just run:
>python app.py

The app can be found on your local host at port 5000, so open a browser in:
>http://localhost:5000/


If you want to tamper with the frontend, it is in the frontend folder and it is a vite project.
>cd frontend
>npm install .

.. and you are ready to go.

After tweaking, just run
>npm run build

.. and copy with overwrite the "dist" folder in the project root with the frontend "dist folder. This enables the Flask app to serve these files as static files.

## Entry points

Other entry points than the already mentioned app.py are:

test_groq.py - this is for testing the backend as the exercise required and testing the keys etc...
week3_technical_assignment_SL.ipynb - the Jupyter notebook required to be in the repo too. <b>This does not run with the requirements.txt modules, you have to install more. For Colab!</b>

## Important notes

The Jupyter notebook requires you to set certain secrets in your Colab and allow access to them from the notebook.
The assignment wanted, that the dataset is loaded from Kaggle, so I think you need Kaggle authentication (the JSON file...)
Also, you need a HuggingFace token set, even though my model is public.

The actual python app needs
- HF Token for my model, set environment variable HF_HUB_TOKEN
- LLaMa 3.3 is used though groq. Set environment variable GROQ_API_KEY
