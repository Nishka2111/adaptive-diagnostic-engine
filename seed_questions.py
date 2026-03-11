from database import questions_collection

from database import questions_collection

questions = [

{
"question": "What is 2x + 4 = 10?",
"options": ["2", "3", "4", "5"],
"correct_answer": "3",
"difficulty": 0.1,
"topic": "Algebra",
"tags": ["linear equations"]
},

{
"question": "What is 5 + 7 × 2?",
"options": ["19", "24", "17", "26"],
"correct_answer": "19",
"difficulty": 0.2,
"topic": "Arithmetic",
"tags": ["order of operations"]
},

{
"question": "What is 15% of 200?",
"options": ["20", "25", "30", "35"],
"correct_answer": "30",
"difficulty": 0.3,
"topic": "Arithmetic",
"tags": ["percentages"]
},

{
"question": "If x² = 36, what is x?",
"options": ["5", "6", "7", "8"],
"correct_answer": "6",
"difficulty": 0.3,
"topic": "Algebra",
"tags": ["square roots"]
},

{
"question": "Simplify: 3x + 2x",
"options": ["5x", "6x", "x²", "3x²"],
"correct_answer": "5x",
"difficulty": 0.2,
"topic": "Algebra",
"tags": ["simplification"]
},

{
"question": "What is the synonym of 'Aberration'?",
"options": ["Deviation", "Balance", "Harmony", "Normality"],
"correct_answer": "Deviation",
"difficulty": 0.5,
"topic": "Vocabulary",
"tags": ["GRE vocab"]
},

{
"question": "What is the antonym of 'Benevolent'?",
"options": ["Kind", "Generous", "Cruel", "Helpful"],
"correct_answer": "Cruel",
"difficulty": 0.4,
"topic": "Vocabulary",
"tags": ["GRE vocab"]
},

{
"question": "Solve: 3x − 9 = 0",
"options": ["1", "2", "3", "4"],
"correct_answer": "3",
"difficulty": 0.2,
"topic": "Algebra",
"tags": ["linear equations"]
},

{
"question": "What is the area of a square with side 6?",
"options": ["12", "18", "36", "24"],
"correct_answer": "36",
"difficulty": 0.3,
"topic": "Geometry",
"tags": ["area"]
},

{
"question": "What is the perimeter of a rectangle with sides 4 and 7?",
"options": ["18", "20", "22", "24"],
"correct_answer": "22",
"difficulty": 0.3,
"topic": "Geometry",
"tags": ["perimeter"]
},

{
"question": "Solve: 2x² + 3x − 2 = 0",
"options": ["1 or -2", "2 or -1", "1 or 2", "-1 or -2"],
"correct_answer": "1 or -2",
"difficulty": 0.7,
"topic": "Algebra",
"tags": ["quadratic"]
},

{
"question": "What is the cube of 4?",
"options": ["16", "32", "64", "48"],
"correct_answer": "64",
"difficulty": 0.4,
"topic": "Arithmetic",
"tags": ["powers"]
},

{
"question": "What is the synonym of 'Candid'?",
"options": ["Honest", "Hidden", "Silent", "Complex"],
"correct_answer": "Honest",
"difficulty": 0.4,
"topic": "Vocabulary",
"tags": ["GRE vocab"]
},

{
"question": "What is the antonym of 'Scarce'?",
"options": ["Rare", "Limited", "Abundant", "Small"],
"correct_answer": "Abundant",
"difficulty": 0.5,
"topic": "Vocabulary",
"tags": ["GRE vocab"]
},

{
"question": "What is √144?",
"options": ["10", "11", "12", "14"],
"correct_answer": "12",
"difficulty": 0.3,
"topic": "Arithmetic",
"tags": ["square root"]
},

{
"question": "Solve: 5x + 10 = 0",
"options": ["-1", "-2", "1", "2"],
"correct_answer": "-2",
"difficulty": 0.4,
"topic": "Algebra",
"tags": ["linear equations"]
},

{
"question": "If a triangle has angles 60°, 60°, 60°, it is?",
"options": ["Right", "Isosceles", "Equilateral", "Scalene"],
"correct_answer": "Equilateral",
"difficulty": 0.3,
"topic": "Geometry",
"tags": ["triangles"]
},

{
"question": "What is 9²?",
"options": ["18", "27", "81", "72"],
"correct_answer": "81",
"difficulty": 0.3,
"topic": "Arithmetic",
"tags": ["powers"]
},

{
"question": "What is the synonym of 'Meticulous'?",
"options": ["Careful", "Careless", "Messy", "Lazy"],
"correct_answer": "Careful",
"difficulty": 0.6,
"topic": "Vocabulary",
"tags": ["GRE vocab"]
},

{
"question": "If log10(100) = ?",
"options": ["1", "2", "10", "100"],
"correct_answer": "2",
"difficulty": 0.6,
"topic": "Algebra",
"tags": ["logarithms"]
}

]

questions_collection.insert_many(questions)

print("20 questions successfully inserted into MongoDB")
