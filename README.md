# Wikipedia

A Wikipedia-like web application built with Python and Django, allowing users to browse, search, create, and edit encyclopedia entries.

## Features

- Browse encyclopedia entries
- Search functionality
- Create new entries
- Edit existing entries
- Random article
- Responsive web interface
- Markdown support for content

## Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Content Format**: Markdown

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. Clone the repository:
```bash
git clone https://github.com/jknate/Wikipedia.git
cd Wikipedia
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py migrate
```

4. Start the development server:
```bash
python manage.py runserver
```

5. Open [http://localhost:8000](http://localhost:8000) in your browser.

## Usage

- **Home Page**: View a list of all encyclopedia entries
- **Entry Page**: Click on any entry to view its content
- **Search**: Use the search bar to find entries
- **Create**: Click "Create New Page" to add a new entry
- **Edit**: Click "Edit" on any entry page to modify its content
- **Random**: Click "Random Page" to view a random entry

## Project Structure

- `/wikipedia` - Main Django application directory
  - `/encyclopedia` - Encyclopedia app with models, views, and templates
  - `/static` - CSS, JavaScript, and other static files
  - `/templates` - HTML templates
- `manage.py` - Django management script
