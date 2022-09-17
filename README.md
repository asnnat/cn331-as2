<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/asnnat/cn331-as2)

BookingReg is a Web Application of Registration for admin and user.

### Built With

* [![Django][djangoproject.com]][Django-url]
* [![Bootstrap][Bootstrap.com]][Bootstrap-url]

<!-- GETTING STARTED -->
## Getting Started

This is a website where students can check the details of the courses they are registed in, regist courses and cancel the regist request.

### Prerequisites

You have to install software before using the project.

1. Download [Python](https://www.python.org/downloads/)
2. Install [Visual Studio Code](https://code.visualstudio.com/download)

### Installation

1. Clone the repo
    ```sh
    git clone https://github.com/asnnat/cn331-as2.git cn331-as2
    ```
2. Change directory to the project
    ```sh
    cd cn331-as2
    ```
2. Open the dirctory with Visual Studio Code
    ```sh
    code .
    ```
5. Install requirements for the project
    ```sh
    python -m pip install -r requirements.txt
    ```

<!-- USAGE -->
## Usage

1. Open git bash terminal in Visual Studio Code
2. Activate virtual environment
    ```sh
    source ./.venv/Scripts/activate
    ```
3. Change directory to project directory
    ```sh
    cd registration
    ```
4. Run server
    ```sh
    python manage.py runserver
    ```
5. If you are user, log in via [http://127.0.0.1:8000](http://127.0.0.1:8000/)
6. If you are admin, log in via [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

### LogIn Page 

[![Login Page][images/user_login.png]]()

Students can login with `Username is student id` and `Password is cn331pass`

Once you have successfully logged in The system will display the Register page as follows.
 
### Regist Page
[![Regist Page][images/user_subject.png]](http://127.0.0.1:8000/regist/)
In this page you can see all subject that you able to registed and if you click button ***Detail*** you can see a detail of that subject and you can regist that subject if you click ***Regist*** button

[![Regist Page Detail][images/user_registsubject.png]]()

Once you have successfully registered. The system will take you to [My Subject](#my-subject-page) page

### My Subject Page
[![My Subject Page][images/user_mysubject.png]](http://127.0.0.1:8000/regist/mysubject)
In this page you can see all subject that you have registed and if you click button ***Detail*** you can see a detail of that subject and you can unregist that subject if you click ***Remove*** button

[![My Subject Page Detail]([mages/user_removesubject.png]]()

### Logout
You can logout at any time by clicking on the logout button on the right top of bar and Whenever you successfully logout, you will be returned to the login page and there is a warning message saying 
* "You are logged out."

<!-- CONTACT -->
## Contact

* Natnicha Faksang - 6310682635
* Kantapat Kowadisai - 6310682783

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/user_login.png
[djangoproject.com]: https://img.shields.io/badge/Djang0-35495E?style=for-the-badge&logo=django&logoColor=4FC08D
[Django-url]: https://www.djangoproject.com/
[Bootstrap.com]: https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white
[Bootstrap-url]: https://getbootstrap.com