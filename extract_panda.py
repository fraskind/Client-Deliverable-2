import pandas as pd

html_content = html_content = '''<!DOCTYPE html>
<html lang="en" dir="ltr">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/style.css">
        <title> Cross Country Athlete Progres </title>
    </head>
    <body>
        <section>
            <h3>Athlete Overview</h3>
'''

csv_files = ["Alex Nemecek18820260.csv", "Adrienne Stewart21142907.csv"]

athlete_overviews = {}
# print(df.head(5))
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    
    athlete = df.iloc[0]
    # extract data only from recent meet
    athlete_name = athlete[0]  # Assuming 'athlete-name' is in the first column
    athlete_place = athlete[1]  # Assuming 'athlete-place' is in the second column
    athlete_grade = athlete[2]  # Assuming 'athlete-grade' is in the third column
    athlete_time = athlete[3]  # Assuming 'athlete-time' is in the fourth column
    athlete_date = athlete[4]  # Assuming 'athlete-date' is in the fifth column
    athlete_meet = athlete[5]  # Assuming 'athlete-meet' is in the sixth column
    athlete_comments = athlete[6]  # Assuming 'athlete-comments' is in the seventh column
    athlete_photo = athlete[7]  # Assuming 'athlete-photo' is in the eighth column
    athlete_bio = "Brief bio about the athlete."  # Customize as needed
    last_meet_details = f'''
        <p>Last Meet: {athlete_meet} on {athlete_date} with a time of {athlete_time}. </p>
    '''
    print("ATHLETE COMMENTS: ", athlete_comments)

    # Overview of each athlete
    athlete_overviews[athlete_name] = {
        "grade": athlete_grade,
        "bio": athlete_bio,
        "last_meet": last_meet_details,
        "notes": athlete_comments,  # Customize
        "photo": athlete_photo  # Adjust accordingly
    }

for name, info in athlete_overviews.items():
    html_content += f'''
        <div class="athlete-overview">
            <h4>{name}</h4>
            <p>Grade: {info['grade']}</p>
            <p>Bio: {info['bio']}</p>
            {info['last_meet']}
            <div class="gallery">
                <img src="{info['photo']}" alt="{name}" width="100" height="100">
            </div>
            <p>Notes from caoch: {info['notes']}</p>
        </div>
    '''
    

html_content += f'''
        </section>
        <footer>
            <p>University of Michigan School of Information <br/>
                &copy; Fanny, Moe, Shawn - Web Design 2024 </p>
        </footer>
        </body>
        </html>
    '''

# df = pd.read_csv("Alex Nemecek18820260.csv")

# print(df.head(5))
# for index, athlete in df.iterrows():
#     athlete_name = athlete[0]  # Assuming 'athlete-name' is in the first column
#     athlete_place = athlete[1]  # Assuming 'athlete-place' is in the second column
#     athlete_grade = athlete[2]  # Assuming 'athlete-grade' is in the third column
#     athlete_time = athlete[3]  # Assuming 'athlete-time' is in the fourth column
#     athlete_date = athlete[4]  # Assuming 'athlete-date' is in the fifth column
#     athlete_meet = athlete[5]  # Assuming 'athlete-meet' is in the sixth column
#     athlete_comments = athlete[6]  # Assuming 'athlete-comments' is in the seventh column
#     athlete_photo = athlete[7]  # Assuming 'athlete-photo' is in the eighth column

#     # Print each athlete's information
#     print(f"name: {athlete_name}, place: {athlete_place}, grade: {athlete_grade}, "
#           f"time: {athlete_time}, date: {athlete_date}, meet: {athlete_meet}, "
#           f"comments: {athlete_comments}, photo: {athlete_photo}")

# Write the HTML content to a file
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)