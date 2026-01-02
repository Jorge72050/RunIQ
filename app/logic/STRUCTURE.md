# Basic Structure of Code

## logic.py

logic.py takes in several data points from a person and develops a running plan for them based on the running distance they want to achieve, being a marathon, half-marathon, 10k, or 5k. It accomodates for several factors, such as age, weight, injuries, and more while taking in feedback as the user goes through the running plan to make any necessary adjustments.

### Code logic

In the code, the whole plan is formatted like so:
    {YYYY-MM-DD: {workout1}}
We develop a plan in this fashion:
    - Take in the date the user requests the plan and shift it one day (have them start the next day)
    - Check if the days between the start date and race day meet the threshold:

        - If so, this is the most ideal case and we generate the plan as normal.

            _Marathon_
            - For new runners, they do their two months of introduction running, working up mileage, and then start their plan four months before the marathon, where they start the real plan.
            - For experienced runner

            _Half-Marathon_
            - It will likely be the same as the marathon, but do two weeks of each month instead for a two-month prep and a one-month introduction for new runners.
        
        - If they do not meet the threshold (user is starting plan later than ideal), then we adjust the plan. The user will not be as prepared and risks greater injury but a plan will be developed nonetheless:
            - 

