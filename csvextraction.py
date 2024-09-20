# python data extraction 
import csv
csv_file = "Alex Nemecek18820260.csv"
output_file = "index.html"
# Open the CSV file and extract the data 
with open(csv_file, newline='', encoding='utf-8') as file:
  reader = csv.reader(file)
  data = list(reader)
      
      
      # Sample code for extracting data from a row
      # Start extracting data from row 6 (index 5, since Python indexing starts at 0)
for row in data[5:]:
        name = row[0]  # Column A - Name
        overall_place = row[1]  # Column B - Overall Place
        time = row[2]  # Column C - Time
        date = row[3]  # Column D - Date
        meet = row[4]  # Column E - Meet
        comment = row[5]  # Column F - Comment
        photo = row[6]  # Column G - Photo

    ## For demonstration, print out the extracted values
print(f"Name: {name}, Place: {overall_place}, Time: {time}, Date: {date}, Meet: {meet}, Comment: {comment}, Photo: {photo}")


      # # Extract the data from the CSV 
meet_name = data[1][0]  # Column A - h1 (Meet Name)
meet_date = data[1][1]  # Column B - h2 (Meet Date)
team_results_link = data[1][2]  # Column C - hyperlink for the team-results section
folder_name = data[1][3]  # Column D - folder name used in photo-gallery links
race_comments = data[1][4]  # Column E - race-comments section
      
      
      # # print(f"meet name {meet_name}")
      # print(f"meet_date {meet_date}")
      # print(f"folder_name {folder_name}")
      # print(f"race_comments{race_comments}")
       
      
      # # Athlete details start from row 2 (index 1) 
athletes = data[5:]
      # Add each athlete's information to the list
for athlete in athletes[5:]:
        athlete_name = athlete[5][0]  # Column A - athlete-name
        # print(f"name {athlete_name}")
        athlete_place = athlete[5][1]  # Column B (updated) - athlete-place
        # print(f"place {athlete_place}")
        athlete_grade = athlete[5][2]  # Column C (updated) - athlete-grade
        # print(f"grade {athlete_grade}")
        athlete_time = athlete[5][3]  # Column D (updated) - athlete-time
        # print(f"time {athlete_time}")
        athlete_date = athlete[5][4]  # Column E (updated) - athlete-date
        # print(f"date {athlete_date}")
        athlete_meet = athlete[5][5] # Column F - athlete-meet
        # print(f"meet {athlete_meet})
        athlete_comments = athlete[5][6] # Column G - athlete-comments
        # print(f"comments {athlete_comments})
        athlete_photo = athlete[5][7] # Column G - athlete-photo
        # print(f"photo {athlete_photo})
