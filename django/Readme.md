# Django
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
            env\Scripts\activate.bat
        ```
    - If you are using Linux
        ```shell
            source env/bin/activate
        ```
3. Once the virtual environment is activated, install **requirements.txt**.
    ```shell
        pip install -r requirements.txt
    ```
4. Run `python manage.py migrate` to apply migrations for all django apps.
5. Run `python manage.py collectstatic` to collect statics.
6. Run the application.
    - If you are using Windows:
        ```shell
            python manage.py runserver
        ```
    - If you are using Linux:
        ```shell
            python3 manage.py runserver
        ```
    > The application will be listening by default on **http://127.0.0.1:8000/**

7. To deploy this sample to Azure Web App Linux review the following recommendations: [Oryx Django Tips](https://github.com/microsoft/Oryx/wiki/Django-Tips)