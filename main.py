# Main

# Importing Packages/libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Importing custom functions
from data.data_manipulation import (
    get_csv_data,
    check_missing_values,
    view_missing_values,
    fill_missing_values,
    information_dataset,
    columns_for_analysis,
)
from analysis.interaction_patterns.interaction import (
    analyze_shuffle_listening,
    analyze_track_start_end_reasons,
)
from analysis.listening_behavior.listening import (
    calculate_artist_listening_time,
    plot_artist_listening_time,
    analyze_peak_listening_times,
    analyze_most_played_artists,
    analyze_skip_rates,
    analyze_platform_usage,
)
from analysis.temporal_trends.temporal import (
    analyze_listening_patterns,
    analyze_hourly_listening,
    analyze_year_over_year_changes,
)

# Loading the dataset and making copy
original_spotify_df = get_csv_data()
if original_spotify_df is not None:
    spotify_df = original_spotify_df.copy()
else:
    print("Error: Dataset could not be loaded or is empty.")
    exit()


if spotify_df is None or spotify_df.empty:
    print("Error: Dataset could not be loaded or is empty.")
    exit()


def print_welcome_message():
    print("*" * 50)
    print("\tWelcome to Spotify History Analysis")
    print("*" * 50)
    print("\nThis script will help you analyze the Spotify history dataset\n")

print_welcome_message()


# Defining menu functions
def explore_menu():
    while True:
        print("\nExplore Menu:")
        print("1. Information about the dataset")
        print("2. View sample of the dataset")
        print("3. Use bar chart to visualize missing data")
        print("4. Fill missing values")
        print("5. Go back\n")
        choice = input("Enter your choice: ")

        if choice == "1":
            info = information_dataset(spotify_df)

            print("\nInformation about the dataset:\n")
            print("The dataset is about the streaming history of Spotify.")
            print(
                f"It contains {info['length']} rows and {len(info['columns'])} columns."
            )
            print(f"The columns are: {info['columns']}")
            print(f"Number of missing values: {info['total_missing_values']}")
            print("Data types of columns:")
            print(info["data_types"])

        elif choice == "2":
            print("\nView data samples:\n")
            try:
                num = int(input("\nHow many samples to display: "))
                print(spotify_df.sample(num))
            except ValueError:
                print("Invalid input. Please enter a number.")
        elif choice == "3":
            print("\nUse bar chart to visualize missing data:\n")
            if check_missing_values(spotify_df):
                view_missing_values(spotify_df)
            else:
                print("No missing values found.")
        elif choice == "4":
            print("\nFill missing values:\n")
            if check_missing_values(spotify_df):
                fill_missing_values(
                    spotify_df, columns_name=["reason_start", "reason_end"]
                )
                print("Missing values filled successfully.")
            else:
                print("No missing values found.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def analyze_menu():
    columns_for_analysis(spotify_df)
    while True:
        print("\nAnalyze Menu:")
        print("1. Listening behavior")
        print("2. Temporal trends")
        print("3. Interaction patterns")
        print("4. Back to Main Menu\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            listening_behavior_menu()
        elif choice == "2":
            temporal_trends_menu()
        elif choice == "3":
            interaction_patterns_menu()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def listening_behavior_menu():
    while True:
        print("\nListening behavior Menu:")
        print("1. Total listening time by artist")
        print("2. Peak listening hours and days")
        print("3. Most played tracks/artist")
        print("4. Skip rate insight")
        print("5. platform usage distribution")
        print("6. Back to Analyze Menu\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Getting Total listening time by artist
            total_listening_time_per_artist = calculate_artist_listening_time(
                spotify_df
            )
            # Visualizing the top 10 artist with the most listening time ()
            plot_artist_listening_time(total_listening_time_per_artist, top_n=10)
        elif choice == "2":
            peak_times = analyze_peak_listening_times(spotify_df)
        elif choice == "3":
            most_played = analyze_most_played_artists(spotify_df, top_n=10)
        elif choice == "4":
            skip_insights = analyze_skip_rates(spotify_df)
        elif choice == "5":
            platform_insights = analyze_platform_usage(spotify_df)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")


def temporal_trends_menu():
    while True:
        print("\nTemporal trends Menu:")
        print("1. Monthly/yearly listening patterns")
        print("2. Hour of day listening frequency")
        print("3. Year-over-year listening behavior changes")
        print("4. Back to Analyze Menu\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            listening_patterns = analyze_listening_patterns(spotify_df)
        elif choice == "2":
            hourly_insights = analyze_hourly_listening(spotify_df)
        elif choice == "3":
            yoy_insights = analyze_year_over_year_changes(spotify_df)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")


def interaction_patterns_menu():
    while True:
        print("\nInteraction patterns Menu:")
        print("1. Shuffle vs non-shuffle listening")
        print("2. Reason for track start/end")
        print("3. Back to Analyze Menu\n")

        choice = input("Enter your choice: ")

        if choice == "1":
            shuffle_insights = analyze_shuffle_listening(spotify_df)
        elif choice == "2":
            track_reason_insights = analyze_track_start_end_reasons(spotify_df)
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")


def main_menu():
    while True:
        print("\nSpotify History Analysis Menu:")
        print("-----------------------------")
        print("1. Explore")
        print("2. Analyze")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            explore_menu()
        elif choice == "2":
            if check_missing_values(spotify_df):
                print("Missing values found. Please fill missing values first.")
                explore_menu()
            else:
                analyze_menu()
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
