Adaptive Diagnostic Engine
Overview

This project implements a 1-Dimension Adaptive Testing System that dynamically adjusts question difficulty based on student performance.

The system uses Item Response Theory (IRT) to estimate a student's ability and select questions accordingly.

Tech Stack

Python

FastAPI

MongoDB

OpenAI API

Project Structure
adaptive-diagnostic-engine
│
├── main.py
├── database.py
├── adaptive_logic.py
├── seed_questions.py
├── ai_insights.py
├── requirements.txt
└── README.md
Running the Project
1️⃣ Install dependencies
pip install -r requirements.txt
2️⃣ Start MongoDB

Ensure MongoDB is running locally:

mongodb://localhost:27017
3️⃣ Seed the database
python seed_questions.py

This inserts 20 GRE-style questions.

4️⃣ Start the API server
uvicorn main:app --reload
5️⃣ Open API Documentation
http://127.0.0.1:8000/docs
API Endpoints
Endpoint	Method	Description
/start-session	POST	Create new testing session
/next-question	GET	Retrieve adaptive question
/submit-answer	POST	Submit answer and update ability
/study-plan	GET	Generate AI learning plan
Adaptive Algorithm Logic

The system uses a simplified Item Response Theory model.

Ability is updated after each question using a logistic probability function.

Correct answers increase difficulty while incorrect answers decrease it.

AI Log

AI tools such as ChatGPT were used to assist with:

Designing the adaptive algorithm

Structuring the FastAPI backend

Creating MongoDB schemas

These tools accelerated development while maintaining modular architecture.
