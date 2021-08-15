import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # 1 How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # 2 What is the average age of men?
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # 3 What is the percentage of people who have a Bachelor's degree?
    bachelor = df[df['education'] == 'Bachelors']
    percentage_bachelors = round(bachelor.shape[0] * 100 / df['education'].value_counts().sum(), 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K
   
    high_education = df[(df['education'] == 'Bachelors') |
                    (df['education'] == 'Masters') |
                    (df['education'] == 'Doctorate')]
    high_education_salary = high_education[high_education['salary'] == '>50K']
    higher_education_rich = round(high_education_salary.shape[0] * 100 / high_education.shape[0], 1)

    
    low_education = df[(df['education'] != 'Bachelors') &
                   (df['education'] != 'Masters') &
                   (df['education'] != 'Doctorate')]
    low_education_salary = low_education[low_education['salary'] == '>50K']
    lower_education_rich = round(low_education_salary.shape[0] * 100 / low_education.shape[0], 1)
    
    # 6 What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # 7 What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_hour_workers = df[(df['hours-per-week'] == min_work_hours)]
    rich_min_hour_workers = min_hour_workers[(min_hour_workers['salary'] == '>50K')]
    rich_percentage = round(rich_min_hour_workers.shape[0] * 100 / min_hour_workers.shape[0], 1)
    
    # 8 What country has the highest percentage of people that earn >50K?
    pop = df['native-country'].value_counts()
    rich = df.loc[df['salary'] == '>50K', 'native-country'].value_counts()

    country_rich_percentage = pd.DataFrame({'pop_count': pop, 'rich_count': rich})
    country_rich_percentage['rich_percentage'] = country_rich_percentage['rich_count'] * 100 / country_rich_percentage['pop_count']

    highest_earning_country = country_rich_percentage.index[country_rich_percentage['rich_percentage'] == country_rich_percentage['rich_percentage'].max()]
    highest_earning_country_percentage = round(country_rich_percentage['rich_percentage'].max(), 1)

    # 9 Identify the most popular occupation for those who earn >50K in India.
    rich_india = df.loc[(df['salary'] == '>50K') & (df['native-country'] == 'India'), 'occupation'].value_counts().to_frame()
    top_IN_occupation = rich_india.iloc[0].name

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
