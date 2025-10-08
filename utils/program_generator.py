"""Program generator for 5/3/1 workouts."""

from typing import Dict, List


def generate_531_program(user_data: Dict) -> Dict:
    """
    Generate a complete 5/3/1 program based on user data.

    Args:
        user_data (dict): User's 1RM estimates and preferences

    Returns:
        dict: Complete 4-week program
    """
    # Calculate training maxes (90% of 1RM)
    training_maxes = {
        "squat": user_data["squat_1rm"] * 0.9,
        "bench": user_data["bench_1rm"] * 0.9,
        "deadlift": user_data["deadlift_1rm"] * 0.9,
        "ohp": user_data["ohp_1rm"] * 0.9,
    }

    # Generate 4-week program
    program = {"user_data": user_data, "training_maxes": training_maxes, "weeks": {}}

    # Week percentages for 5/3/1
    week_percentages = {
        1: {"sets": [65, 75, 85], "reps": [5, 5, 5], "description": "Base week"},
        2: {"sets": [70, 80, 90], "reps": [3, 3, 3], "description": "Build week"},
        3: {"sets": [75, 85, 95], "reps": [5, 3, 1], "description": "Peak week"},
        4: {"sets": [40, 50, 60], "reps": [5, 5, 5], "description": "Deload week"},
    }

    for week_num, week_data in week_percentages.items():
        program["weeks"][week_num] = {
            "description": week_data["description"],
            "percentages": week_data["sets"],
            "reps": week_data["reps"],
            "workouts": generate_weekly_workouts(
                training_maxes, week_data["sets"], week_data["reps"], user_data
            ),
        }

    return program


def generate_weekly_workouts(
    training_maxes: Dict, percentages: List[int], reps: List[int], user_data: Dict
) -> List[Dict]:
    """
    Generate individual workouts for a week.

    Args:
        training_maxes (dict): Training maxes for each lift
        percentages (list): Week percentages
        reps (list): Reps for each set
        user_data (dict): User preferences

    Returns:
        list: List of workout dictionaries
    """
    workouts = []

    # Main lifts
    main_lifts = [
        {"name": "Squat", "max": training_maxes["squat"]},
        {"name": "Bench Press", "max": training_maxes["bench"]},
        {"name": "Deadlift", "max": training_maxes["deadlift"]},
        {"name": "Overhead Press", "max": training_maxes["ohp"]},
    ]

    # Generate workouts based on frequency
    workouts_per_week = user_data["workouts_per_week"]

    if workouts_per_week == 3:
        # 3-day split: Squat, Bench, Deadlift
        workout_schedule = [
            {"main_lift": main_lifts[0], "accessories": ["Leg Press", "Calf Raises"]},
            {"main_lift": main_lifts[1], "accessories": ["Push-ups", "Tricep Dips"]},
            {"main_lift": main_lifts[2], "accessories": ["Pull-ups", "Planks"]},
        ]
    elif workouts_per_week == 4:
        # 4-day split: Each main lift gets its own day
        workout_schedule = [
            {"main_lift": main_lifts[0], "accessories": ["Leg Press", "Calf Raises"]},
            {"main_lift": main_lifts[1], "accessories": ["Push-ups", "Tricep Dips"]},
            {"main_lift": main_lifts[2], "accessories": ["Pull-ups", "Planks"]},
            {
                "main_lift": main_lifts[3],
                "accessories": ["Lateral Raises", "Face Pulls"],
            },
        ]
    else:
        # 5-6 day split: More specialized workouts
        workout_schedule = [
            {"main_lift": main_lifts[0], "accessories": ["Leg Press", "Calf Raises"]},
            {"main_lift": main_lifts[1], "accessories": ["Push-ups", "Tricep Dips"]},
            {"main_lift": main_lifts[2], "accessories": ["Pull-ups", "Planks"]},
            {
                "main_lift": main_lifts[3],
                "accessories": ["Lateral Raises", "Face Pulls"],
            },
            {"main_lift": None, "accessories": ["Cardio", "Core Work"]},
        ]

    # Generate workout details
    for i, workout_template in enumerate(workout_schedule[:workouts_per_week]):
        workout = {
            "day": i + 1,
            "main_lift": workout_template["main_lift"],
            "accessories": workout_template["accessories"],
            "sets": [],
        }

        # Add main lift sets if present
        if workout_template["main_lift"]:
            for j, (percentage, rep_count) in enumerate(zip(percentages, reps)):
                weight = workout_template["main_lift"]["max"] * (percentage / 100)
                workout["sets"].append(
                    {
                        "exercise": workout_template["main_lift"]["name"],
                        "weight": round(weight),
                        "reps": rep_count,
                        "percentage": percentage,
                    }
                )

        workouts.append(workout)

    return workouts
