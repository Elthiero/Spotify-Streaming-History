import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
MS_TO_MINUTES = 60000

# Total listening time by artist
def calculate_artist_listening_time(your_dataframe):
    """
    Calculate total listening time in minutes for each artist.
    
    Parameters:
    your_dataframe (pandas.DataFrame): DataFrame containing Spotify listening data.
    and has artist_name, ms_played as columns
    
    Returns:
    pandas.Series: Total listening time in minutes per artist, sorted descending
    """
    # Convert milliseconds to minutes and group by artist
    artist_listening_time = your_dataframe.groupby('artist_name')['ms_played'].sum() / MS_TO_MINUTES
    
    # Sort in descending order of total listening time
    return artist_listening_time.sort_values(ascending=False)

# Function to visualize artist Listening time using Bar Chart
def plot_artist_listening_time(artist_listening_time, top_n=10):
    """
    Create a bar chart of total listening time for top artists.
    
    Parameters:
    artist_listening_time (pandas.Series): Total listening time per artist
    top_n (int): Number of top artists to display (default 10)
    """
    # Select top N artists
    top_artists = artist_listening_time.head(top_n)
    
    # Set up the plot style
    plt.figure(figsize=(12, 6))
    sns.set(style="whitegrid")
    
    # Create bar plot
    sns.barplot(x=top_artists.index, y=top_artists.values)
    
    # Customize the plot
    plt.title(f'Top {top_n} Artists by Total Listening Time', fontsize=15)
    plt.xlabel('Artist', fontsize=12)
    plt.ylabel('Listening Time (Minutes)', fontsize=12)
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    
    # Show the plot
    plt.show()
    
# Peak listening hours and days
def analyze_peak_listening_times(df):
    """
    Analyze peak listening hours and days.
    
    Parameters:
    df (pandas.DataFrame): Spotify listening data
    
    Returns:
    Dict containing analysis results and visualization methods
    """
    # Peak hours analysis
    hourly_listening = df.groupby('hour')['ms_played'].sum() / MS_TO_MINUTES
    daily_listening = df.groupby('day')['ms_played'].sum() / MS_TO_MINUTES
    
    # Visualization of peak hours
    plt.figure(figsize=(12, 5))
    
    # Hourly listening plot
    plt.subplot(1, 2, 1)
    sns.barplot(x=hourly_listening.index, y=hourly_listening.values)
    plt.title('Listening Time by Hour', fontsize=10)
    plt.xlabel('Hour of Day', fontsize=8)
    plt.ylabel('Total Listening Time (Minutes)', fontsize=8)
    plt.xticks(rotation=45)
    
    # Daily listening plot
    plt.subplot(1, 2, 2)
    sns.barplot(x=daily_listening.index, y=daily_listening.values)
    plt.title('Listening Time by Day', fontsize=10)
    plt.xlabel('Day of Week', fontsize=8)
    plt.ylabel('Total Listening Time (Minutes)', fontsize=8)
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    return {
        'peak_hours': hourly_listening.sort_values(ascending=False).head(),
        'peak_days': daily_listening.sort_values(ascending=False).head()
    }
    
# Most played tracks/artist
def analyze_most_played_artists(df, top_n=10):
    """
    Analyze and visualize most played artists.
    
    Parameters:
    df (pandas.DataFrame): Spotify listening data
    top_n (int): Number of top artists to display
    
    Returns:
    pandas.Series: Top artists by number of plays and total listening time
    """
    # Count number of plays per artist
    plays_per_artist = df['artist_name'].value_counts().head(top_n)
    
    # Total listening time per artist (in minutes)
    listening_time_per_artist = df.groupby('artist_name')['ms_played'].sum() / MS_TO_MINUTES
    listening_time_per_artist = listening_time_per_artist.sort_values(ascending=False).head(top_n)
    
    # Visualization
    plt.figure(figsize=(15, 5))
    
    # Number of plays plot
    plt.subplot(1, 2, 1)
    plays_per_artist.plot(kind='bar')
    plt.title(f'Top {top_n} Artists by Number of Plays')
    plt.xlabel('Artist')
    plt.ylabel('Number of Plays')
    plt.xticks(rotation=45, ha='right')
    
    # Listening time plot
    plt.subplot(1, 2, 2)
    listening_time_per_artist.plot(kind='bar')
    plt.title(f'Top {top_n} Artists by Listening Time')
    plt.xlabel('Artist')
    plt.ylabel('Listening Time (Minutes)')
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()
    
    return {
        'plays_per_artist': plays_per_artist,
        'listening_time_per_artist': listening_time_per_artist
    }
    
# Skip rate insight
def analyze_skip_rates(df):
    """
    Analyze skip rates across different dimensions.
    
    Parameters:
    df (pandas.DataFrame): Spotify listening data
    
    Returns:
    Dict containing skip rate insights
    """
    # Overall skip rate
    total_plays = len(df)
    total_skips = df['skipped'].sum()
    overall_skip_rate = total_skips / total_plays * 100
    
    # Skip rate by artist
    artist_skip_rates = df.groupby('artist_name').agg({
        'skipped': 'mean',
        'track_name': 'count'
    }).rename(columns={'skipped': 'skip_rate', 'track_name': 'total_plays'})
    artist_skip_rates['skip_rate'] = artist_skip_rates['skip_rate'] * 100
    top_skipped_artists = artist_skip_rates.sort_values('skip_rate', ascending=False).head(10)
    
    # Skip rate by hour
    hourly_skip_rates = df.groupby('hour').agg({
        'skipped': 'mean',
        'track_name': 'count'
    }).rename(columns={'skipped': 'skip_rate', 'track_name': 'total_plays'})
    hourly_skip_rates['skip_rate'] = hourly_skip_rates['skip_rate'] * 100
    
    # Visualization
    plt.figure(figsize=(15, 5))
    
    # Hourly skip rates
    plt.subplot(1, 2, 1)
    sns.barplot(x=hourly_skip_rates.index, y=hourly_skip_rates['skip_rate'])
    plt.title('Skip Rates by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Skip Rate (%)')
    plt.xticks(rotation=45)
    
    # Top skipped artists
    plt.subplot(1, 2, 2)
    sns.barplot(x=top_skipped_artists.index, y=top_skipped_artists['skip_rate'])
    plt.title('Top 10 Artists by Skip Rate')
    plt.xlabel('Artist')
    plt.ylabel('Skip Rate (%)')
    plt.xticks(rotation=45, ha='right')
    
    plt.tight_layout()
    plt.show()
    
    return {
        'overall_skip_rate': overall_skip_rate,
        'top_skipped_artists': top_skipped_artists,
        'hourly_skip_rates': hourly_skip_rates
    }
    
# Platform usage distribution
def analyze_platform_usage(df):
    """
    Analyze platform usage distribution.
    
    Parameters:
    df (pandas.DataFrame): Spotify listening data
    
    Returns:
    Dict containing platform usage insights
    """
    # Platform usage count
    platform_counts = df['platform'].value_counts()
    
    # Platform usage time (minutes)
    platform_listening_time = df.groupby('platform')['ms_played'].sum() / MS_TO_MINUTES
    
    # Visualization
    plt.figure(figsize=(12, 5))
    
    # Platform usage count
    # plt.subplot(1, 2, 1)
    # platform_counts.plot(kind='pie', autopct='%1.1f%%')
    # plt.title('Platform Usage Count')

    plt.subplot(1, 2, 1)
    platform_counts.plot(kind='bar')
    plt.title('Platform Usage Count')
    plt.xlabel('Platform')
    plt.ylabel('Count Number')
    plt.xticks(rotation=45)
    
    # Platform listening time
    plt.subplot(1, 2, 2)
    platform_listening_time.plot(kind='bar')
    plt.title('Platform Listening Time (Minutes)')
    plt.xlabel('Platform')
    plt.ylabel('Total Listening Time')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    return {
        'platform_counts': platform_counts,
        'platform_listening_time': platform_listening_time
    }
    
# 
    