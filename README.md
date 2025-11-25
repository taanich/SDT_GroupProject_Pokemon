# Pokémon Multi-Model – Project Setup Guide

This guide explains how to set up a **Python virtual environment** and install the dependencies.

---

## 🔧 1. Check Python Installation

Open the (e.g. VS Code) terminal and run:

```bash
python --version
```
or Windows specific
```
py --version
```
You should see something like
```
Python 3.10.x
```
If Python is not installed, download it here:
https://www.python.org/downloads/

---

## 🔧 2. Create a Virtual Environment

Inside your project folder, run:

```
py -m venv venv
```
This creates a folder named `venv/` which contains your isolated Python environment.

---

## ▶️ 3. Activate the Virtual Environment

Windows
```
venv\Scripts\activate
```

macOS/Linux
```
source venv/bin/activate
```
After activation, your terminal prompt should look like this:
```
(venv) C:\Users\...\your-project>
```

---

## 📦 4. Installing Dependencies from `requirements.txt`

Instead of installing packages manually, you can list all required dependencies in a `requirements.txt` file and install them in one step.

**Make sure your virtual environment is activated!**

Then install everything from the file:
```bash
pip install -r requirements.txt
```

If pip is not recognised on your system, you can use the following instead:
```bash
py -m pip install -r requirements.txt
```

To deactivate the virtual environment, type:
```
deactivate
```

---

## 🔐 5. Storing Credentials in a `.env` File

To keep your database credentials secure and avoid hardcoding passwords in your source code, this project uses a `.env` file.


Inside the project root, create a new file named:
```
.env
```


Add the following variables (**do not use quotes**, and never commit real credentials):

```
BASE_URL=<your-URL>

NEO4J_URI=neo4j+s://<your-host>.databases.neo4j.io
NEO4J_USER=<your-username>
NEO4J_PASSWORD=<your-password>
```

---

## 🚀 6. Running the FastAPI Server

Before accessing any API endpoints, the FastAPI application must be started.

**1. Navigate into the `app` folder**
```
cd app
```

**2. Start FastAPI using Uvicorn**
```
uvicorn main:app --reload
```

FastAPI will now be available at:
```
http://127.0.0.1:8000
```

You can explore all endpoints via the automatically generated Swagger UI:
```
http://127.0.0.1:8000/docs
```

The file `routes.py` contains the API routes (e.g., Pokémon data, Neo4j services, etc.)

---

## ▶️ 7. Running the Application

If you want to test your services directly in Python (without going through the browser), run:

```bash
py main.py
```
or, depending on your Python installation:

```bash
python main.py
```