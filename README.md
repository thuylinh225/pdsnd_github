### Date created
4/13/2020
### Project Title
Bikeshare Data
### Description
The project includes data of bikeshare information of 3 cities: chicago, new york and washington.
Used python3, pandas and numpy
There are 7 parts:

    def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
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
    def time_stats(df):
        """Displays statistics on the most frequent times of travel."""
    def station_stats(df):
        """Displays statistics on the most popular stations and trip."""
    def trip_duration_stats(df):
        """Displays statistics on the total and average trip duration."""
    def user_stats(df):
        """Displays statistics on bikeshare users."""
    def main():
    if __name__ == "__main__":
    	 main()

### Files used
bikeshare.py
washington.csv
chicago.csv
new_york_city.csv
### Credits
https://github.com/joshnh/Git-Commands/blob/master/README.md

https://docs.scipy.org/doc/numpy-1.13.0/contents.html

https://docs.scipy.org/doc/numpy-1.13.0/reference/index.html#reference

http://scipy-lectures.org/intro/numpy/index.html

https://pandas.pydata.org/pandas-docs/stable/
