import pandas as pd

df = pd.read_csv("Alex Nemecek18820260.csv")

print(df.head(5))
for index, athlete in df.iterrows():
    athlete_name = athlete[0]  # Assuming 'athlete-name' is in the first column
    athlete_place = athlete[1]  # Assuming 'athlete-place' is in the second column
    athlete_grade = athlete[2]  # Assuming 'athlete-grade' is in the third column
    athlete_time = athlete[3]  # Assuming 'athlete-time' is in the fourth column
    athlete_date = athlete[4]  # Assuming 'athlete-date' is in the fifth column
    athlete_meet = athlete[5]  # Assuming 'athlete-meet' is in the sixth column
    athlete_comments = athlete[6]  # Assuming 'athlete-comments' is in the seventh column
    athlete_photo = athlete[7]  # Assuming 'athlete-photo' is in the eighth column

    # Print each athlete's information
    print(f"name: {athlete_name}, place: {athlete_place}, grade: {athlete_grade}, "
          f"time: {athlete_time}, date: {athlete_date}, meet: {athlete_meet}, "
          f"comments: {athlete_comments}, photo: {athlete_photo}")