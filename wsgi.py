import sys
import os

# Add your project directory to the sys.path
project_home = os.path.dirname(os.path.abspath(__file__))
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Import your Flask application
from neo_infra.app import create_app

# Create the application instance
application = create_app()

# Set the secret key
application.secret_key = os.environ.get('SECRET_KEY', 'your-secret-key-here') 