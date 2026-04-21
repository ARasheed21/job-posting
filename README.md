# Job Posting Platform

A comprehensive job board application built with Django that facilitates the connection between job seekers and employers. This project provides separate interfaces for regular users to find and apply for jobs, and for admins/employers to manage job postings.

## Features

### For Job Seekers (Regular Users)
- **User Authentication:** Secure registration and login functionality.
- **Job Discovery:** Browse a comprehensive list of available job opportunities.
- **Job Details:** View in-depth information about specific job roles, requirements, and salaries.
- **Application Management:**
  - Apply for jobs with a single click.
  - Track all submitted applications.
  - Withdraw applications if needed.
- **Job Search:** Quickly find relevant positions using the search functionality.

### For Employers & Admins
- **Dashboard:** Access a centralized home for management.
- **Job Management:**
  - Create new job postings with detailed descriptions and salary information.
  - Edit existing job listings to keep information up-to-date.
  - Delete outdated or filled job postings.
- **Posted Jobs Overview:** View and manage all active job listings in one place.

## Tech Stack
- **Backend:** Django 5.0.6 (Python)
- **Frontend:** HTML5, CSS3 (Vanilla CSS)
- **Database:** SQLite3

## Installation and Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ARasheed21/job-posting.git
   cd job-posting/project
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r ../requirements.txt
   ```

4. **Run migrations:**
   ```bash
   python manage.py migrate
   ```

5. **Start the development server:**
   ```bash
   python manage.py runserver
   ```

6. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`

## Project Structure
- `accounts/`: Handles user authentication and home views.
- `jobs/`: Management logic for job postings (create, edit, delete).
- `regularuser/`: Logic for job seekers (list, details, apply).
- `project/`: Main project configuration and settings.
- `static/` & `globalstatic/`: Contains CSS styles and images.
