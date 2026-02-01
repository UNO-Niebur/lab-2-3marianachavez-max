#Magic8Ball.py
#Name: Mariana Chavez
#Date: 02.01.2026
#Assignment: Lab 2
#Purpose: practice with variables and assignments, numeric data types, arithmetic operators, type conversion

#We will need random for this program, import to use this package.
import random

def main():
  #Create a list of your responses.
  print("Magic 8 Ball")
  
  #Prompt the user for their question.
  question = input("Ask me a question, please: ")
  answers = ["Yes", "No", "Maybe", "One day", "Possibly", "Don't count on it", 
             "Absolutely", "Never in a million years", "Certainly", "Ask again later", 
             "Definitely not", "Without a doubt", "Very doubtful", "It is certain", 
             "Most likely", "Outlook good", "Reply hazy, try again"]
  
  #Answer question randomly with one of the options from your earlier list.
  response = random.choice(answers)
  print(response)

if __name__ == '__main__':
  main()
