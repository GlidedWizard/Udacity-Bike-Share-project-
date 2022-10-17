import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


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
        city = input('Which city do you want to see data for? chicago, new york city or washington?')
        city = city.lower().strip()
        if city in CITY_DATA.keys():
            break
        print('opps invalid input please try again ')
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            'Which month do you want to see data for (january, february, march, april, may or june)? or type all to see data for all months')
        global months
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = month.lower().strip()
        if month == 'all' or month in months:
            break
        print('opps invalid input please try again')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:

        # By default day will be set to all
        # This is done to avoid variable referenced before assignment error at the return line
        global days
        days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

        day = 'all'
        global day_num
        day_num = input(
            'Which day of the week? please type your desired day or ''all'' to see for all days')
        try:
            if day_num.lower().strip() in days or (float(day_num) == int(day_num) and (0 < int(day_num) < 8)):
                break
                """this is to make sure no decimal number are entered and then rounded """
        except:
            pass
        print('opps invalid input please try again')


    try:
        day_num = int(day_num)
        day = days[int(day_num) - 1]
    except:
        day = day_num.lower().strip()
        pass

    print('-' * 40)


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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.isocalendar().day

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        """" the months list is now a global variable that can be used anywhere, it was first defined in the get_filters() function"""
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == days.index(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # TO DO: display the most common day of week
    print('most common day was', days[df['day_of_week'].mode()[0]])

    # TO DO: display the most common start hour
    print('the most common start hour was :', df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('most commonly used start station is :', df['Start Station'].mode()[0])
    # TO DO: display most commonly used end station
    print('most commonly used end station is :', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    df['Start To End'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    max_combination = df['Start To End'].mode()[0]
    print('The most frequent combination of start station and end station trip :', max_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    travel_time = df['Trip Duration'].sum()
    print('Total travel time :', travel_time)
    # TO DO: display mean travel time
    print('Mean travel time :', df['Trip Duration'].mean())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('The types of users and their number are :')
    print(df['User Type'].value_counts())

    try:
        # TO DO: Display counts of gender
        print('The counts of gender are as follows :')
        print(df['Gender'].value_counts())
        # TO DO: Display earliest, most recent, and most common year of birth
        print('The earliest year of birth is :', int(df['Birth Year'].min()))
        print('The most recent year of birth is :', int(df['Birth Year'].max()))
        print('The most common year of birth is :', int(df['Birth Year'].mode()[0]))
    except:
        pass 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def display_data(df):
    start_loc = 0
    while True:
        user_input = input('Do you want to see the first 5 rows of raw data? type "yes" or "no" ')
        if user_input.lower().strip() in ['yes','no']:
            break
        else:
            print('invalid input try again')

    while user_input.lower().strip() == 'yes':
        if df.iloc[start_loc:start_loc+5].empty:
            print('That\'s all the data we have!')
            break
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        while True:
            user_input = input('Do you want to see 5 more rows of raw data? type "yes" or "no" ')
            if user_input.lower().strip() in ['yes','no']:
                break
            else:
                print('invalid input try again')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
