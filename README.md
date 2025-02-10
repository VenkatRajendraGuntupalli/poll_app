# **Poll Hub - Django Web Application**

Poll Hub is a simple yet powerful polling application built with **Django**. Users can **create polls, vote in them, and view poll results in a well-structured and interactive interface**. This project follows a **dark mode theme** with a professional UI design.

---

## **🛠 Technologies Used**
The project is built using the following technologies:

- **Backend**: Django (Python)
- **Frontend**: HTML, CSS (Dark Theme)
- **Database**: SQLite (default Django database)
- **Styling & UI**:
  - Bootstrap (for layout and responsiveness)
  - Custom CSS (Dark theme with Calibri font)
  - Django Widget Tweaks (for form customization)
- **Version Control**: Git & GitHub

---

## **📂 Project Structure**
<img width="503" alt="image" src="https://github.com/user-attachments/assets/f70ca360-1ac6-4f27-a2f5-bdd3b58f3978" />

---

## **🚀 Installation & Setup**

Follow these steps to set up and run the project on your local machine:

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/poll-hub.git
cd poll-hub
```


### 2️⃣ Create a Virtual Environment (Recommended)
```sh
python3 -m venv env
source env/bin/activate  # On MacOS/Linux
env\Scripts\activate     # On Windows
```

### 3️⃣ Install Required Dependencies
```sh
pip install -r requirements.txt
```

### 4️⃣ Apply Database Migrations
```sh
python manage.py makemigrations
python manage.py migrate
```

### 5️⃣ Create a Superuser (for Admin Panel)
```sh
python manage.py createsuperuser
```

Follow the instructions to create an admin user.

### 6️⃣ Collect Static Files
```sh
python manage.py collectstatic --noinput
```

### 7️⃣ Run the Development Server
```sh
python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser.
```


## 🖼 Screenshots
Below are some screenshots of the application:

### 🏠 Homepage

<img width="1699" alt="image" src="https://github.com/user-attachments/assets/650cc4b4-f854-41f2-972e-bc6ad24a89bd" />

### 🗳 Vote Page

<img width="1703" alt="image" src="https://github.com/user-attachments/assets/3c08ea9f-b29b-4094-bc20-5ff39813cd31" />


### 📊 Results Page

<img width="1685" alt="image" src="https://github.com/user-attachments/assets/3f3865bc-b92c-40d2-be90-d8bbd6281501" />

---

## 💡 Application Workflow

1. The user lands on the **Homepage**, where all available polls are displayed.
2. The created polls **appears in the list**.
3. The user can **vote** by selecting an option and clicking **Submit**.
4. After voting, the user is **redirected to the Results Page** to see the poll statistics.

---

## 📜 License
This project is **open-source** and available under the **MIT License**.

---

## 🤝 Contributing
Contributions are welcome! If you'd like to improve this project:

1. **Fork** the repository.
2. **Create** a new branch.
3. **Make your changes**.
4. **Open a pull request**.

---

## 📞 Contact
For any queries or suggestions, contact:

- **Venkat Rajendra Guntupalli**
- **guntupalliv1@udayton.edu**
- **GitHub Profile**: [[https://github.com/VenkatRajendraGuntupalli]](https://github.com/VenkatRajendraGuntupalli)
