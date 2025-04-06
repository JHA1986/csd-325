# Jonah Aney CSD325 Module 4.2 Assignment: High/Low Temperatures

# Modifications of code assisted by Copilot and JetBrains assistant - JHA
import csv
import sys
from datetime import datetime
from matplotlib import pyplot as plt

filename = r'C:\Users\Jonah\csd\csd-325\module-4\sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

# Get dates, high and low temperatures from this file.
# Added a list for lows - JHA
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[5])
        highs.append(high)
# Added lows to the loop - JHA
        low = int(row[6])
        lows.append(low)

# Created a function to plot the data based on user's input. Added the plot of low temperatures in blue - JHA
def temp_plot(type):
    fig, ax = plt.subplots()
    if type == 'highs':
        ax.plot(dates, highs, c='red', label="High temperatures")
        plt.title("Daily high temperatures - 2018", fontsize=24)
    elif type == 'lows':
        ax.plot(dates, lows, c='blue', label="Low temperatures")
        plt.title("Daily Low temperatures - 2018", fontsize=24)

    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.legend()
    plt.show()

# Created a main loop with choices for the user to choose "high" or "low" temps. Created outputs for clarity and the user's response. - JHA
def main():
    print("Hello! You can choose to see high or low temperatures for 2018.")

    while True:
        choice = input("Would you like to see the highs or lows? Or enter quit to exit the program. \n")
        if choice == 'highs':
            print("Here are the high temperatures for 2018: ")
            temp_plot('highs')
            for date, high in zip(dates, highs):
                print(date, high)
        elif choice == 'lows':
            print("Here are the low temperatures for 2018: ")
            temp_plot('lows')
            for date, low in zip(dates, lows):
                print(date, low)
# Gave the user and option to exit the program with and output of "Goodbye!" - JHA
        elif choice == 'quit':
            print("Goodbye!")
# Used a sys.exit to exit the program instead of "break" - JHA
            sys.exit()
        else:
            print("Please enter 'high' or 'low' as your choice. Or enter quit to exit the program.")

if __name__ == "__main__":
    main()

