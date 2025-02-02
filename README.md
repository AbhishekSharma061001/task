Overview

	This project implements a multilingual FAQ system using Django and Django REST Framework. The system allows administrators to manage frequently asked questions (FAQs) with support for multiple languages, 		including English, Hindi, Bengali. The project utilizes Redis for caching translations and integrates with CKEditor for a rich text editor interface for answers.

Features

	*Multilingual support: FAQs are available in multiple languages with automatic translation through Google Translate.
	*Caching: Translations are cached in Redis to improve performance and reduce external API calls.
	*REST API: Exposes FAQ data via a REST API with automatic translation based on the requested language.
	*WYSIWYG Editor: CKEditor is integrated for easy content management.
	*Django Admin: A custom admin interface for managing FAQ entries.

Installation

	Prerequisites
		Python 3.10 or higher
		Docker (for containerized setup)
		Redis (used for caching)

  Steps to Set Up Locally
  
	1.Clone the repository:
		git clone https://github.com/AbhishekSharma061001/task
		cd task
	2.Install dependencies:
		pip install -r requirements.txt
  	3.Set up the database:
		python manage.py migrate
	4.Ceate a superuser for accessing the Django admin interface:
		python manage.py createsuperuser
  	5.Run the development server:
		python manage.py runserver
  Docker Setup
  
  	1.Build the Docker containers:
   		docker-compose build
	2.Start the containers:
 		docker-compose up

Creating a Record (FAQ Entry)

	To create a FAQ record, you can either use the Django Admin Interface or create records using the Django Shell.

Using Django Admin Interface

	1.Start the development server (if not already running):
		python manage.py runserver
	2.Navigate to http://localhost:8000/admin and log in with the superuser credentials you created earlier.
	3.Under the "FAQ" section, click "Add FAQ" to create a new FAQ entry. Provide the following:
		Question: The main question text (in English by default).
		Answer: The main answer text (use CKEditor for a rich text editor interface).
		Language: Select the language for the FAQ.
		The system will automatically generate translations for Bengali,Hindi.
	4.Click "Save" to store the FAQ. The translations will be cached and saved.
 Using Django Shell
 
	Alternatively, you can create a FAQ record from the Django shell:
	1.Open the Django shell:
		python manage.py shell
	2.Create a new FAQ record:
		from faq.models import FAQ
		faq = FAQ(
    		question="What is Django?",
    		answer="Django is a high-level Python web framework that encourages rapid development.",
    		language="en"
		)
		faq.save()
	This will create a record with the question and answer in English. Translations will be automatically generated for Hindi.
API Usage

	Once you have created some FAQ records, you can fetch them using the REST API.
		*The FAQ model stores FAQs in multiple languages. The get_translated_text method retrieves translations, either from the database or cached using Redis.
		*The API endpoint for fetching FAQs is /api/faqs/, and it supports the lang query parameter for requesting translations (e.g., /api/faqs/?lang=hi).
Testing

	![Screenshot (265)](https://github.com/user-attachments/assets/7c0bc3d1-7aa7-4af3-a3f9-457116df511a)

Caching

	This project uses Redis for caching translated FAQ data. Cached translations are stored for 24 hours. Redis must be running as a service, which is handled through Docker Compose.

Docker Deployment

	This project includes a Docker setup for easy deployment. 
 	To run the application using Docker:
		Ensure that Redis is running (handled by Docker Compose).








  
