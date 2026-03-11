from fastapi import FastAPI
from database import questions_collection, sessions_collection
from adaptive_logic import update_ability
from ai_insights import generate_study_plan
from bson import ObjectId

app = FastAPI()


@app.post("/start-session")
def start_session():

    session = {
        "ability": 0.5,
        "questions_answered": [],
        "topics_missed": []
    }

    result = sessions_collection.insert_one(session)

    return {"session_id": str(result.inserted_id)}



@app.get("/next-question")
def next_question(session_id: str):

    session = sessions_collection.find_one({"_id": ObjectId(session_id)})

    ability = session["ability"]

    question = questions_collection.find_one({
        "difficulty": {
            "$gte": ability - 0.1,
            "$lte": ability + 0.1
        }
    })

    return {
        "question_id": str(question["_id"]),
        "question": question["question"],
        "options": question["options"]
    }



@app.post("/submit-answer")
def submit_answer(session_id: str, question_id: str, answer: str):

    question = questions_collection.find_one({"_id": ObjectId(question_id)})
    session = sessions_collection.find_one({"_id": ObjectId(session_id)})

    correct = answer == question["correct_answer"]

    new_ability = update_ability(
        session["ability"],
        question["difficulty"],
        correct
    )

    update = {
        "$set": {"ability": new_ability},
        "$push": {"questions_answered": question_id}
    }

    if not correct:
        update["$push"]["topics_missed"] = question["topic"]

    sessions_collection.update_one(
        {"_id": ObjectId(session_id)},
        update
    )

    return {
        "correct": correct,
        "new_ability": new_ability
    }



@app.get("/study-plan")
def study_plan(session_id: str):

    session = sessions_collection.find_one({"_id": ObjectId(session_id)})

    weaknesses = session["topics_missed"]

    plan = generate_study_plan(weaknesses)

    return {"study_plan": plan}