# FastAPI
1. Create a **virtual environment** with any python version >=3.
    - If you are using Windows:
        ```shell
            python -m venv env
        ```
    - If you are using Linux:
        ```shell
            python3 -m venv env
       ```
2. Activate the virtual environment.
    - If you are using Windows in cmd:
        ```shell
            env\Scripts\activate
        ```
    - If you are using Linux
        ```shell
            source env/bin/activate
        ```
3. Once the virtual environment is activated, install **requirements.txt**.
    ```shell
        pip install -r requirements.txt
    ```
4. Run the application with `uvicorn main:app --reload`

    > The application will be listening by default on **http://127.0.0.1:8000/**

5. To deploy this sample to Azure Web App Linux with Gunicorn, use this startup command `gunicorn --bind=0.0.0.0 --timeout 600 -w 4 -k uvicorn.workers.UvicornWorker main:app`