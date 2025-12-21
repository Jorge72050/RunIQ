# app/logic/training_plan.py

from datetime import datetime, timedelta

# Based on Strava's marathon prep article + health factors that commonly affect running
# Average starting time derived from RunRepeat's article on times based on gender + percentile
# Start with basic marathon plan

def build_plan(profile):
    
    # Initializing all variables
    prev_injury = profile["basic_info"]["prev_injury"]
    dob = (int(num) for num in profile["basic_info"]["date_of_birth"].split("-"))
    gender = profile["basic_info"]["gender"]
    injury_type = profile["basic_info"]["specific_injury"]
    new_to_running = profile["running_history"][""]
    weekly_mileage = profile["running_history"]["weekly_mileage"]
    goal_distance = profile["goals"]["goal_distance"]
    date_of_race = profile["goals"]["date_of_race"]
    age = (datetime.today() - datetime(dob[0], dob[1], dob[2])) // 365

    # If new to running, start out with lower intensity work, basic mileage - 
    # Then get to real workout plan. Ease them into running
    
    # Otherwise, they can jump into the plan
    # Will determine average times based on male or female - assuming mostly new runners. 
    # Based off of 50th percentile values for times and weights
    # As weight increases past 50th percentile and age increase (past 30), decrease starting running pace by fixed amount
    
    # Conditions and their effects:
        # <7 hours of sleep - add in rest day, increase training program length
        # Injury recovery - implement second recovery day and increase 

    plan = {}
    if gender == "Male":
        if new_to_running:
            
        if age > 30:
            
        
        if goal_distance == "Marathon":

    
    else:

