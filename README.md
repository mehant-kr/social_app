# Social App

A lightweight social networking web application built with Django that enables users to:

- Register accounts, authenticate, and manage sessions
- Create, join, and leave community groups
- Publish content within groups
- Manage personal content and view group activities

## Features

- **User Authentication:** Complete user management system with registration, login, and session handling
- **Group Management:** Create and join interest-based communities
- **Content Publishing:** Share posts within your groups
- **Content Control:** Full ownership of your published content with deletion capabilities
- **Group Feeds:** Browse aggregated content from your communities

## Prerequisites

- Python 3.x
- Node.js and npm
- Virtualenv (recommended)

## Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/social_app.git
   cd social_app
   ```

2. Create and activate a virtual environment
   ```bash
   python -m venv .venv
   
   # On Windows
   .\.venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. Install Python dependencies
   ```bash
   pip install -r requirements.txt
   ```

## Frontend Setup

This project uses Tailwind CSS for styling. Set up the frontend build system:

1. Install Tailwind CSS via Django integration
   ```bash
   python manage.py tailwind install
   ```

2. Build the CSS assets
   ```bash
   python manage.py tailwind build
   ```

## Development

1. Start the Tailwind CSS watcher for development
   ```bash
   python manage.py tailwind start
   ```

2. In a separate terminal, run the Django development server
   ```bash
   python manage.py runserver
   ```

3. Access the application at `http://127.0.0.1:8000`