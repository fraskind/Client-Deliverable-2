import csv

# File paths
csv_file = "Alex Nemecek18820260.csv"
output_file = "index.html"

# Open the CSV file and extract the data
with open(csv_file, newline='', encoding='utf-8') as file:
    reader = csv.reader(file)
    data = list(reader)

# Skip the first two rows (if they're irrelevant)
data = data[2:]

# Start building the HTML structure
meet_name = "Lamplighter Invite"  # Replace this with relevant data
meet_date = "Sep 2023"  # Replace with relevant data

html_content = f'''<!DOCTYPE html>
<html lang="en" dir="ltr">  
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="css/reset.css">
        <link rel="stylesheet" href="css/style.css">
        <title>{meet_name} Country Meet</title>
    </head>
    <body>
        <header>
            <h1>{meet_name}</h1>
            <h2>{meet_date}</h2>
        </header>
        <section>
            <h3>Athletes Results</h3>
            <ul>
'''

# Athlete details start from row 2 (index 1)
for row in data[1:]:
    # Check if the row has enough columns to avoid IndexError
    if len(row) < 7:  # Assuming there are at least 7 columns
        continue  # Skip rows that don't have enough data

    # Extract the values safely
    name = row[0] if len(row) > 0 else "N/A"  # Column A - Name
    overall_place = row[1] if len(row) > 1 else "N/A"  # Column B - Overall Place
    grade = row[2] if len(row) > 2 else "N/A"  # Column C - Grade
    time = row[3] if len(row) > 3 else "N/A"  # Column D - Time
    date = row[4] if len(row) > 4 else "N/A"  # Column E - Date
    meet = row[5] if len(row) > 5 else "N/A"  # Column F - Meet
    comment = row[6] if len(row) > 6 else "N/A"  # Column G - Comment
    photo = row[7] if len(row) > 7 else "N/A"  # Column H - Photo

    # Add each athlete's information to the HTML
    html_content += f'''
            <li>
                <strong>{name}</strong><br/>
                Place: {overall_place}, Grade: {grade}, Time: {time}, Meet: {meet}, Date: {date}<br/>
                Comment: {comment}<br/>
                Photo: <img src="{photo}" alt="Photo of {name}">
            </li>
    '''

# Close HTML tags
html_content += '''
            </ul>
        </section>
    </body>
    <footer>
        <p>University of Michigan School of Information <br/>
        &copy; Fanny, Moe, Shawn - Web Design 2024</p>
    </footer>
</html>
'''

# Write the generated HTML to a file
with open(output_file, 'w', encoding='utf-8') as file:
    file.write(html_content)

print(f"HTML file '{output_file}' generated successfully!")
