#FutureTime.py
#Name: Mariana Chavez
#Date: 02.01.2026
#Assignment: Lab 2
#Purpose: practice with variables and assignments, numeric data types, arithmetic operators, type conversion

# datetime will allow us to access the system date and time.
import datetime

def main():
  #getting current time from system, storing to variable
  now = datetime.datetime.now()
  currentHour = (now.hour - 6) % 24 #adjusting for CST timezone, I know it is not required but I want it to be correct
  currentMinute = now.minute


  #TODO:
  #Ask user for hours
  #Ask user for minutes
  hoursToAdd = int(input("Enter hours to add: "))
  minutesToAdd = int(input("Enter minutes to add: "))

  #Calculate the time after the user-supplied time has passed.
  futureHour = (currentHour + hoursToAdd + (currentMinute + minutesToAdd) // 60) % 24
  futureMinute = (currentMinute + minutesToAdd) % 60
  #Do not use any if statements in calculating the time.

  #Output the future time in standard format "HH:MM"
  print(f"Future time: {futureHour:02d}:{futureMinute:02d}")

if __name__ == '__main__':
  main()
