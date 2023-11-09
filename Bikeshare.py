#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

   


# In[ ]:


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
        city = input('Enter the name of the city (Chicago, New York City, Washington): ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Invalid city. Please choose from Chicago, New York City, or Washington.')

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter the month to filter by (January, February, ..., June), or "all" for no filter: ').lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Invalid month. Please enter a valid month or "all".')


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter the day of the week to filter by (Monday, Tuesday, ..., Sunday), or "all" for no filter: ').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Invalid day. Please enter a valid day or "all".')


    print('-'*40)
    return city, month, day 


# # Statistics 

# In[ ]:


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

    # Define a dictionary mapping city names to data file paths
    CITY_DATA = {
        'chicago': 'chicago.csv',
        'new york city': 'new_york_city.csv',
        'washington': 'washington.csv'
    }

    # Check if the provided city is valid
    if city.lower() not in CITY_DATA:
        return None  # Return None if the city is not valid

    # Load the data for the specified city
    filename = CITY_DATA[city.lower()]
    df = pd.read_csv(filename)

    # Convert the 'Start Time' column to datetime for filtering by month and day
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Apply filters for month and day
    if month != 'all':
        # Extract the month from the 'Start Time' column and filter by it
        df = df[df['Start Time'].dt.month == pd.to_datetime(month, format='%B').month]

    if day != 'all':
        # Extract the day of the week from the 'Start Time' column and filter by it
        df = df[df['Start Time'].dt.day_name() == day.title()]

    return df


# In[ ]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['Month'].mode()[0]
    print(f"The most common month for travel is: {common_month}")

    # TO DO: display the most common day of week
    common_day_of_week = df['Day of Week'].mode()[0]
    print(f"The most common day of the week for travel is: {common_day_of_week}")

    # TO DO: display the most common start hour
    
    # Extract the hour from the 'Start Time' column
    df['Start Hour'] = pd.to_datetime(df['Start Time']).dt.hour
    
    common_start_hour = df['Start Hour'].mode()[0]
    
    print(f"The most common start hour for travel is: {common_start_hour}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[ ]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    start_time = time.time()

    # TO DO: display most commonly used start station

    common_start_station = df['Start Station'].mode()[0]
    print(f"The most commonly used start station is: {common_start_station}")

    # TO DO: Display most commonly used end station
    
    common_end_station = df['End Station'].mode()[0]
    print(f"The most commonly used end station is: {common_end_station}")

    # TO DO: Display most frequent combination of start station and end station for trips
      
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent combination of start station and end station for trips is: {common_trip}")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



# In[ ]:


# Call get_filters to get user input
city, month, day = get_filters()

# Load data into a DataFrame based on the selected city
if city in CITY_DATA:
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)
    # Call the station_stats function with the loaded DataFrame
    station_stats(df)
else:
    print('Invalid city. Please choose from Chicago, New York City, or Washington.')


# In[ ]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: Display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f"The total travel time for all trips is: {total_travel_time} seconds")

    # TO DO: Display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print(f"The mean travel time for trips is: {mean_travel_time} seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# In[ ]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type_counts = df['User Type'].value_counts()
    print("Counts of each user type:")
    
    for user_type, count in user_type_counts.items():
        print(f"{user_type}: {count}")

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of each gender:")
        for gender, count in gender_counts.items():
            print(f"{gender}: {count}")
    else:
        print("\nGender data not available for this city.")

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        common_birth_year = int(df['Birth Year'].mode()[0])
        print("\nYear of birth statistics:")
        print(f"Earliest birth year: {earliest_birth_year}")
        print(f"Most recent birth year: {most_recent_birth_year}")
        print(f"Most common birth year: {common_birth_year}")
    else:
        print("\nBirth year data not available for this city.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)





# In[ ]:


def main():
    while True:
        # Get user input for city, month, and day
        city, month, day = get_filters()

        # Load and filter data based on user input
        df = load_data(city, month, day)

        # Display statistics on the most frequent times of travel
        time_stats(df)

        # Display statistics on the most popular stations and trips
        station_stats(df)

        # Display statistics on trip duration
        trip_duration_stats(df)

        # Display statistics on bikeshare users
        user_stats(df)

        # Ask if the user wants to restart the program
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
    main()


# In[ ]:




