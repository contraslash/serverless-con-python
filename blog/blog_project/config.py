import os
# Statement for enabling the development environment
DEBUG = True

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# SQLALCHEMY_DATABASE_URI  = 'sqlite:///db.sqlite3'
SQLALCHEMY_DATABASE_URI  = 'mysql+mysqlconnector://{}:{}@{}/{}'.format(
    os.getenv("MYSQL_USER", ""),
    os.getenv("MYSQL_PASSWORD", ""),
    os.getenv("MYSQL_HOST", ""),
    os.getenv("MYSQL_DABATASE", ""),

)
SQLALCHEMY_TRACK_MODIFICATIONS = True

print("Loading configuration")