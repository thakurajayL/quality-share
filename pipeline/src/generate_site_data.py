from data_generator import generate_articles_json_and_markdown
from database import create_database

if __name__ == "__main__":
    create_database()
    generate_articles_json_and_markdown()
