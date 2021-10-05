# Pyramid
1. Cd into pyramidsite folder.
2. Create a **virtual environment** with any python version >=3.
    - If you are using Windows:
        ```shell
            python -m venv env
        ```
    - If you are using Linux:
        ```shell
            python3 -m venv env
       ```
3. Activate the virtual environment.
    - If you are using Windows in cmd:
        ```shell
            env\Scripts\activate
        ```
    - If you are using Linux
        ```shell
            source env/bin/activate
        ```
4. Once the virtual environment is activated, install  **setup.py** or **requirements.txt**.
It is better to use setup.py to create egg-info with the metadata and definition.
    - To use setup.py use the following command:
        ```shell
            python setup.py install
        ```
    - To use requirements.txt use the following command:
        ```shell
            pip install -r requirements.txt
        ```
5. To run the application locally, you have two configuration files development.ini and production.ini, for each one you can run `pserve development.ini` 
    > The application will be listening by default on **http://127.0.0.1:6543/**
6. To deploy to Azure Web App Linux with Gunicorn use a startup command with `gunicorn --bind=0.0.0.0 --timeout 600 --chdir pyramidsite --paste production.ini`