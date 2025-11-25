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

---

## ▶️ 5. Running the Application

After setting up the virtual environment and installing all required packages, you can run the application.

 **1. Navigate into the `app` folder**

In the terminal:

```bash
cd app
```

**2. Run the Application**

```bash
py main.py
```

or, depending on your Python installation:

```bash
python main.py
```