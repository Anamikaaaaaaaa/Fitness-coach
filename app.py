from flask import Flask, render_template, request

app = Flask(__name__)

# Static list of exercises based on fitness goals
EXERCISES = {
    "weight_loss": ["Running", "Cycling", "Jump Rope", "Burpees", "Mountain Climbers"],
    "muscle_gain": ["Push-ups", "Pull-ups", "Squats", "Deadlifts", "Bench Press"],
    "general_fitness": ["Yoga", "Plank", "Lunges", "Jumping Jacks", "Stretching"],
}

# Function to calculate BMI
def calculate_bmi(weight, height):
    height_in_meters = height / 100  # Convert height from cm to meters
    return round(weight / (height_in_meters ** 2), 2)

# Function to generate a personalized fitness plan
def generate_fitness_plan(age, weight, height, goal, gender):
    # Get exercises based on the goal
    exercises = EXERCISES.get(goal, ["Walking"])  # Default to walking if goal is invalid
    workout = ", ".join(exercises)  # Join exercises into a string

    # Add YouTube video links based on goal and gender
    if gender == "male":
        if goal == "weight_loss":
            diet = "Low-carb, high-protein meals"
            video_link = "https://www.youtube.com/embed/ml6cT4AZdqI"  # Male weight loss video
        elif goal == "muscle_gain":
            diet = "High-protein, balanced meals"
            video_link = "https://www.youtube.com/embed/U0bhE67HuDY"  # Male muscle gain video
        else:  # General Fitness
            diet = "Balanced diet with fruits and vegetables"
            video_link = "https://www.youtube.com/embed/3p8EBPVZ2Iw"  # Male general fitness video
    else:  # Female
        if goal == "weight_loss":
            diet = "Low-carb, high-protein meals"
            video_link = "https://www.youtube.com/embed/IT94xC35u6k"  # Female weight loss video
        elif goal == "muscle_gain":
            diet = "High-protein, balanced meals"
            video_link = "https://www.youtube.com/embed/6kALZikXxLc"  # Female muscle gain video
        else:  # General Fitness
            diet = "Balanced diet with fruits and vegetables"
            video_link = "https://www.youtube.com/embed/2pLT-olgUJs"  # Female general fitness video

    # Weekly plan based on gender and goal
    if gender == "male":
        if goal == "weight_loss":
            weekly_plan = {
                "Day 1": "Cardio (Running, Cycling) + Upper Body Strength",
                "Day 2": "HIIT + Core Workout",
                "Day 3": "Yoga + Stretching",
                "Day 4": "Rest Day",
                "Day 5": "Strength Training (Chest, Back, Arms)",
                "Day 6": "Cardio (Swimming, Rowing) + Lower Body Strength",
                "Day 7": "Active Recovery (Walking, Light Stretching)",
            }
        elif goal == "muscle_gain":
            weekly_plan = {
                "Day 1": "Heavy Strength Training (Chest, Triceps)",
                "Day 2": "Cardio (Running, Cycling) + Core Workout",
                "Day 3": "Heavy Strength Training (Back, Biceps)",
                "Day 4": "Rest Day",
                "Day 5": "Heavy Strength Training (Legs, Shoulders)",
                "Day 6": "Cardio (Swimming, Rowing) + Core Workout",
                "Day 7": "Active Recovery (Walking, Light Stretching)",
            }
        else:  # General Fitness
            weekly_plan = {
                "Day 1": "Cardio (Running, Cycling) + Upper Body Strength",
                "Day 2": "Yoga + Core Workout",
                "Day 3": "Strength Training (Full Body)",
                "Day 4": "Rest Day",
                "Day 5": "Cardio (Swimming, Rowing) + Lower Body Strength",
                "Day 6": "Yoga + Stretching",
                "Day 7": "Active Recovery (Walking, Light Stretching)",
            }
    else:  # Female
        if goal == "weight_loss":
            weekly_plan = {
                "Day 1": "Cardio (Running, Cycling) + Core Workout",
                "Day 2": "HIIT + Lower Body Strength",
                "Day 3": "Yoga + Stretching",
                "Day 4": "Rest Day",
                "Day 5": "Strength Training (Upper Body)",
                "Day 6": "Cardio (Swimming, Rowing) + Core Workout",
                "Day 7": "Active Recovery (Walking, Light Stretching)",
            }
        elif goal == "muscle_gain":
            weekly_plan = {
                "Day 1": "Strength Training (Legs, Glutes)",
                "Day 2": "Cardio (Running, Cycling) + Core Workout",
                "Day 3": "Strength Training (Upper Body)",
                "Day 4": "Rest Day",
                "Day 5": "Strength Training (Full Body)",
                "Day 6": "Cardio (Swimming, Rowing) + Core Workout",
                "Day 7": "Active Recovery (Walking, Light Stretching)",
            }
        else:  # General Fitness
            weekly_plan = {
                "Day 1": "Cardio (Running, Cycling) + Core Workout",
                "Day 2": "Yoga + Lower Body Strength",
                "Day 3": "Strength Training (Upper Body)",
                "Day 4": "Rest Day",
                "Day 5": "Cardio (Swimming, Rowing) + Core Workout",
                "Day 6": "Yoga + Stretching",
                "Day 7": "Active Recovery (Walking, Light Stretching)",
            }

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    return {
        "workout": workout,
        "diet": diet,
        "video_link": video_link,
        "weekly_plan": weekly_plan,
        "bmi": bmi,
    }
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get user input from the form
        age = int(request.form["age"])
        weight = float(request.form["weight"])
        height = float(request.form["height"])
        goal = request.form["goal"]
        gender = request.form["gender"]

        # Generate fitness plan
        plan = generate_fitness_plan(age, weight, height, goal, gender)

        # Render the result page with the plan
        return render_template("index.html", plan=plan, show_result=True)

    # Render the form page for GET requests
    return render_template("index.html", show_result=False)

if __name__ == "__main__":
    app.run(debug=True)