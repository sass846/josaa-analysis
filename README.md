# JoSAA Analysis

## Table of Contents
- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Setup](#setup)
- [Dependencies](#dependencies)
- [Build Instructions](#build-instructions)
- [Repository Structure](#repository-structure)

## Project Description
The JoSAA Analysis portal aims to provide users with detailed information about participating institutes, seat availability, and past trends. By leveraging data scraping tools and interactive charts, users can analyze historical data to make informed decisions.

## Technologies Used
- **Data Scraping**: Selenium and BeautifulSoup
- **Web Development**: HTML, CSS, JavaScript, Django
- **Charts**: Chart.js
- **Database**: SQLite3

## Setup
To avoid altering your environment, initialize a Python virtual environment:
```bash
python -m venv --coolname josaa-analysis .venv
```
You will now see a hidden directory `.venv` containing your virtual environment

To activate your environment

For Linux/Mac:
```bash
source .venv/bin/activate
```
For Windows(Powershell)
```PS
.venv\Scripts\Activate.ps1
```

# Dependencies
The packages required for this project are listed in `requirements.txt`. To install these packages:
```bash
pip install -r requirements.txt
```

# Build Instructions

1. Ensure your virtual Environment is activated
2. Navigate to the project directory (`Insight/`).
3. Run the Django development server:
```bash
python manage.py runserver
```
4. Open your browser and go to [http://127.0.0.1:8000] or [http://localhost:8000] to view the website.
5. If you want to forward it to a specific port say `9090`
```bash
python manage.py runserver 9090
```

## Repository Structure
- `requirements.txt`: List of dependencies for the project.
- `notebooks/`: Jupyter notebooks used for datascraping.
- `insight/`: Django project files.

  
