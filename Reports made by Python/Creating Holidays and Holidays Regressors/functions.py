import pandas as pd
import re
from datetime import datetime
from datetime import timedelta
import numpy as np
def create_holidays_province_weekly_dictionary(
    dataframe, *, start_year=2019, end_year=2025
):
 
    # Create a unique list of provinces
    unique_provinces = dataframe["Province"].unique()
 
    # Initialize a dictionary to hold holiday vectors and names
    holiday_dict = {}
 
    # Clean the 'Holiday Name' column
    dataframe["Holiday"] = dataframe["Holiday"].apply(clean_holiday_name)
 
    # Create a dictionary that maps each holiday to its dates for each province
    holiday_weeks = (
        dataframe.groupby(["Province", "Holiday", "Year", "Week Number"])[
            "Holiday Indicator"
        ]
        .max()
        .to_dict()
    )
 
    # Create a set to hold all unique holidays across all provinces
    all_holidays = set(
        holiday for holiday in dataframe["Holiday"].unique() if holiday != ""
    )
    all_holidays.update(
        [
            "Cyber Week",
            "Cyber Week Plus 1",
            "Cyber Week Minus 1",
            "Cyber Week Plus 2",
        ]
    )  # Adding Cyber Week, Cyber Week Plus 1, Cyber Week Minus 1, Cyber Week Plus 2, and Working Days to all holidays
 
    # Generate holiday vectors for each province
    for province in unique_provinces:
        # Filter the dataframe based on the province
        filtered_df = dataframe[
            (dataframe["Province"] == province)
            & (dataframe["Year"].between(start_year, end_year))
        ]
 
        # Initialize a list to hold holiday vectors for the province
        province_holiday_vectors = []
 
        # Generate holiday vectors for each holiday in all_holidays set
        for holiday in all_holidays:
            if holiday == "Cyber Week":
                # Special handling for Cyber Week
                holiday_vector = []
                for year in range(start_year, end_year + 1):
                    cyber_monday = calculate_cyber_monday(year)
                    cyber_week_number = cyber_monday.isocalendar()[1]
                    for week in range(1, 53):
                        holiday_vector.append(1 if week == cyber_week_number else 0)
            elif holiday == "Cyber Week Plus 1":
                # Special handling for Cyber Week Plus 1
                holiday_vector = []
                for year in range(start_year, end_year + 1):
                    cyber_monday = calculate_cyber_monday(year)
                    cyber_week_number = cyber_monday.isocalendar()[1]
                    for week in range(1, 53):
                        holiday_vector.append(1 if week == cyber_week_number + 1 else 0)
            elif holiday == "Cyber Week Minus 1":
                # Special handling for Cyber Week Minus 1
                holiday_vector = []
                for year in range(start_year, end_year + 1):
                    cyber_monday = calculate_cyber_monday(year)
                    cyber_week_number = cyber_monday.isocalendar()[1]
                    for week in range(1, 53):
                        holiday_vector.append(1 if week == cyber_week_number - 1 else 0)
            elif holiday == "Cyber Week Plus 2":
                # Special handling for Cyber Week Plus 2
                holiday_vector = []
                for year in range(start_year, end_year + 1):
                    cyber_monday = calculate_cyber_monday(year)
                    cyber_week_number = cyber_monday.isocalendar()[1]
                    for week in range(1, 53):
                        holiday_vector.append(1 if week == cyber_week_number + 2 else 0)
            else:
                # Regular holidays
                holiday_vector = [
                    (
                        1
                        if holiday_weeks.get((province, holiday, year, week), 0) == 1
                        else 0
                    )
                    for year in range(start_year, end_year + 1)
                    for week in range(1, 53)  # Assuming a maximum of 52 weeks in a year
                ]
            province_holiday_vectors.append(holiday_vector)
 
        # Add the province and its holiday vectors to the dictionary
        holiday_dict[province] = (
            np.array(province_holiday_vectors).tolist(),
            np.array(list(all_holidays)).tolist(),
        )
 
    return holiday_dict


def test_holidays_province_weekly_dictionary(
    holidays_province_weekly_dict, *, start_year=2019
):
    # Initialize a dictionary to hold test results
    test_results_dict = {}
 
    # Iterate over each province and its holiday vectors in the dictionary
    for province, (
        holiday_vectors,
        holiday_names,
    ) in holidays_province_weekly_dict.items():
        # Initialize a list to hold test results for the province
        province_test_results = []
 
        # Iterate over each holiday vector and its corresponding holiday name
        for holiday_vector, holiday_name in zip(holiday_vectors, holiday_names):
            # Calculate the length of the binary vector
            length_of_binary_vector = len(holiday_vector)
 
            # Calculate the number of occurrences of the holiday
            number_of_occurrences = sum(holiday_vector)
 
            # Create a list of holiday weeks
            holiday_weeks = [
                (year + start_year, week)
                for year in range(len(holiday_vector) // 52)
                for week in range(1, 53)
                if holiday_vector[year * 52 + week - 1] == 1
            ]
 
            # Add the test results for the holiday to the list
            province_test_results.append(
                {
                    "Holiday Name": holiday_name,
                    "Length of Binary Vector": length_of_binary_vector,
                    "Number of Occurrences": number_of_occurrences,
                    "Holiday Weeks": holiday_weeks,
                }
            )
 
        # Convert the results into a DataFrame for the current province
        test_results_df = pd.DataFrame(province_test_results)
 
        # Add the province and its test results to the dictionary
        test_results_dict[province] = test_results_df
 
    return test_results_dict


def clean_holiday_name(name):
    # Fill NaN values with an empty string
    name = name if pd.notnull(name) else ""
    # Remove parentheses and strip leading/trailing whitespace
    name = re.sub(r"\(.*\)", "", name).strip()
    # Remove spaces before comma
    name = name.replace(" ,", ",")
    # Remove everything after the comma, including the comma
    name = name.split(",")[0]
    return name
 
 
def calculate_cyber_monday(year):
    # Find the date for the fourth Thursday of November (Thanksgiving in the US)
    november_first = datetime(year, 11, 1)
    day_of_week = november_first.weekday()
    first_thursday = 1 + ((3 - day_of_week) % 7)
    thanksgiving = november_first + timedelta(days=(first_thursday - 1) + 3 * 7)
    # Calculate Cyber Monday
    cyber_monday = thanksgiving + timedelta(days=4)  # Friday, Saturday, Sunday, Monday
    return cyber_monday


def create_external_variables(holiday_dict, *,start_year):
    # Get all unique holiday names
    all_holidays = list(next(iter(holiday_dict.values()))[1])
 
    # Initialize an empty DataFrame with columns as "Year", "Province", "Week Number", and each unique holiday name
    df = pd.DataFrame(columns=["Year", "Province", "Week Number"] + all_holidays)
 
    for province, (holiday_vectors, holiday_names) in holiday_dict.items():
        num_years = len(holiday_vectors[0]) // 52
        for year in range(start_year, start_year + num_years):
            for week in range(1, 53):
                row = {"Year": year, "Province": province, "Week Number": week}
                for i, holiday in enumerate(holiday_names):
                    row[holiday] = holiday_vectors[i][
                        (year - start_year) * 52 + week - 1
                    ]
                df = pd.concat([df, pd.DataFrame([row])], ignore_index=True)
    return df