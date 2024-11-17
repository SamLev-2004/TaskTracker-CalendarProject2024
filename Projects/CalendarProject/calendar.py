import sqlite3

from datetime import datetime


conn = sqlite3.connect('SQLEvents.db')
c = conn.cursor()

def createTask():        
    while True: 


        event_title = str(input("Please input an event title: "))
        while True:
            date = input("Please input a date (YYYY-MM-DD):")
            try:
                parsed_date = datetime.strptime(date, "%Y-%m-%d")

                print(f"Valid Date:, {parsed_date.date()}")
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")
        description = str(input("Please input an event description (optional): "))
        while True:
            time = input("Please input a time (HH:MM): ")
            try:
                parsed_time = datetime.strptime(time, "%H:%M")
                break
            except ValueError:
                print("Invalid time format. Please us HH:MM (24hours) format: ")
        
        category = str(input("Please input a category(optional): "))

            
        c.execute('''INSERT INTO events (event_title,date, description, time, category)
                      VALUES (?,?,?,?,?)''',
                      (event_title, date, description, time, category))
        conn.commit()

        print("Event Added Successfully!")

        continue_or_not = input("Add another event? (y/n): ")
        if continue_or_not.strip().lower() != 'y':
            break

        conn.close()

createTask()









