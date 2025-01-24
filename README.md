AI E-commerce Product Inquiries Chatbot
Project Description
This project is a Django-based backend for an AI chatbot to aid users in acquiring information on products in e-commerce. The details of the product, such as description, price, and suppliers, are found based on a user's query. The general queries that are supported include a list of products by category, brand, or supplier.

Main Features
Natural Language Processing: "Who sells Asus Vivobook?" or "Laptops"
Database Integration : Retrieves real-time product and supplier information from a structured database.
Category and Brand Filters: Gives the respective product list only on category or brand.
-Supplier Information: Displays the information of suppliers for specific products
-Error Handling: Handling unrecognized queries or the absence of information.
-Technical Stack
-Backend : Python based Framework Django, Django REST Framework(DRF)
-Database : SQLite (any preferred database is fine)
-API Development: REST API of the chatbot responses
-Frontend Integration: React-based chat UI can be integrated easily
-Setup Guide
-Clone the repository:
-git clone https://github.com/yourusername/your-repo-name.git

-cd chatbotbackend

-Install dependencies:

-bash
-Copy
-pip install -r requirements.txt

-Run migrations:
-bash
-Copy
-python manage.py makemigrations
-python manage.py migrate

-Populate the database with sample data:
-bash
-Copy
-python manage.py loaddata sample_data.json

-Start the development server:
-bash
-Copy
-python manage.py runserver

-Usage
-Interact with the chatbot through the connected React frontend.
-Example queries:
-"Show me all products."
-"List all laptops."
-"Who supplies Asus Vivobook?"

Contributions are welcome! Please submit a pull request or report issues via GitHub.
