import time
import pandas as pd
import numpy as np

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
    valid_cities = {'chicago', 'new york city', 'washington'}
    valid_months = {'all', 'january', 'february', 'march', 'april', 'may', 'june'}
    valid_days = {'all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'}
    while True:

        city = input("Which city would you like? (chicago, new york city, washington) ").lower()
        if city not in valid_cities:
            print("City must be in the list (chicago, new york city, washington)")
            continue
       # TO DO: get user input for month (all, january, february, ... , june)

        month = input("Which month would you like? (all, january, february, ... , june): ").lower()
        if month not in valid_months:
            print("Month must be in the list (all, january, february, ... , june)")
            continue
        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        day = input("Which day of week would you like? (all, monday, tuesday, ... sunday): ").lower()
        if day not in valid_days:
            print("Day must be in the list (all, monday, tuesday, ... sunday)")
            continue
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
    df = pd.read_csv(CITY_DATA[city])
    df['start_time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['start_time'].dt.month
    df['day_of_week'] = df['start_time'].dt.weekday_name
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) +1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most common month is: ', popular_month)
    # TO DO: display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week is: ', popular_day_of_week)
    # TO DO: display the most common start hour
    df['hour'] = df['start_time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most common start hour is: ', popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    used_start_station = df['Start Station'].mode()[0]
    print('The most commonly used start station is: ', used_start_station)
    # TO DO: display most commonly used end station
    used_end_station = df['End Station'].mode()[0]
    print('The most commonly used end station is: ', used_end_station)

    # TO DO: display most frequent combination of start station and end station trip
    frequent_combination = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print('The most frequent combination of start station and end station trip is: ')
    print(frequent_combination)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print('Total travel time is: ', total_travel_time)
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('Average travel time is: ', mean_travel_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of user types is: ')
    print(user_types,'\n')
    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print('Counts of gender is: ')
        print(gender,'\n')
    else:
        print("Gender column does not exists")



    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:

        earliest_year = df['Birth Year'].min()
        print('The earliest year of birth is: ', earliest_year)

        most_recent_year = df['Birth Year'].max()
        print('The most recent year of birth is: ', most_recent_year)

        most_common_year = df['Birth Year'].mode()[0]
        print('The most common year of birth is: ', most_common_year)
    else:
        print("Birth Year column does not exists")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    user_input = input('\nWhat would you like to see the first 5 rows?\nPlease enter yes or no\n').lower()

    if user_input in ('yes', 'y'):
        i = 0
        while True:
            print(df.iloc[i:i+5])
            i += 5
            more_data = input('Would you like to see more data? Please enter yes or no: ').lower()
            if more_data not in ('yes', 'y'):
                break

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
