#import the packages
import time
import pandas as pd
import numpy as np

#define the cities for each file
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        try:
            city = input('Which city would you like to explore the data of? Chicago, New York or Washington?\n').lower()
        except:
            print('Invalid input. Please enter valid city name\n')
        else:
            if not city in CITY_DATA:
                 print('No avialable data for entered city. Please try another city.\n')
            else:
                break
    while True:
        try:
            filter_choice = input('would you like to filter the date by month, day, both or none? Type "none" for no time filter\n').lower()
        except:
            print('Invalid input. Please enter valid choice\n')
        else:
            if not filter_choice in ['month','day','both','none']:
                print('Invalid input. Please enter valid choice\n')
            else:
                break

    # TO DO: get user input for month (all, january, february, ... , june)
    month = 'all'
    months = ['January','February','March','April','May','June']

    if filter_choice == 'both' or filter_choice == 'month' :
        while True:
            try:
                month = input('Please enter desired month name: ({})\n'.format(",".join(months))).title()
            except:
                 print('Invalid input. Please enter valid month name\n')
            else:
                if not month in months:
                    
                    print('Please enter valid month name.\n')
                else:
                    break

    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = 'all'
    days = ['Saturday','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday']

    if filter_choice == 'both' or filter_choice == 'day' :
        while True:
            try:
                day = input('Please enter desired day name: ({})\n'.format(",".join(days))).title()
            except:
                print('Invalid input. Please enter valid day name\n')
            else:
                if not day in days:
                    print('Please enter valid day name.\n')
                else:
                    break

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    #read the csv file
    df = pd.read_csv(CITY_DATA[city])
    #Convert the start date time to date type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #month column
    df['month'] = df['Start Time'].dt.month_name()
    #day column
    df['day_of_week'] = df['Start Time'].dt.day_name()
    if month != 'all':
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    #df['End Time'] = pd.to_datetime(df['End Time'])

    # TO DO: display the most common month
    print((df['Start Time'].dt.month).mode()[0])

    # TO DO: display the most common day of week
    print((df['Start Time'].dt.day).mode()[0])

    # TO DO: display the most common start hour
    print((df['Start Time'].dt.hour).mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df['trip'] = df['Start Station'] + " - " + df['End Station']

    # TO DO: display most commonly used start station
    print( df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print( df['End Station'].mode()[0])
    
    # TO DO: display most frequent combination of start station and end station trip
    print( df['trip'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())

    # TO DO: Display counts of gender
    print(df['Gender'].value_counts())

    # TO DO: Display earliest, most recent, and most common year of birth
    print(df['Birth Year'].min(), df['Birth Year'].max(), df['Birth Year'].mode())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def invidual_dataframe(df):
    """Displays invidual data for the user"""
    i = 0
    while True:
        try:
            display_data = input('\nWould you like to view invidual trip data? Enter yes or no.\n').lower().replace(" ","")
            if display_data.lower() == 'yes':
                if i+5< len(df):
                    print(df.iloc[:i+5])
                    i+=5
                else:
                    print('no more data to display')
             
            else:
                break

        except:
            print('that invalid choice. Please choose yes or no.\n')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        invidual_dataframe(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
