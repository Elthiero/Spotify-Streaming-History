import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
MS_TO_MINUTES = 60000

# Monthly/yearly listening patterns
def analyze_listening_patterns(df):
    """
    Analyze monthly and yearly listening patterns.
    
    Parameters:
    df (pandas.DataFrame): Spotify listening data
    
    Returns:
    Dict containing listening pattern insights
    """
    # Monthly listening time
    monthly_listening = df.groupby('month')['ms_played'].sum() / MS_TO_MINUTES
    
    # Yearly listening time
    yearly_listening = df.groupby('year')['ms_played'].sum() / MS_TO_MINUTES
    
    # Visualization
    plt.figure(figsize=(15, 5))
    
    # Monthly listening time
    plt.subplot(1, 2, 1)
    monthly_listening.plot(kind='bar')
    plt.title('Listening Time by Month')
    plt.xlabel('Month')
    plt.ylabel('Total Listening Time (Minutes)')
    plt.xticks(rotation=45)
    
    # Yearly listening time
    plt.subplot(1, 2, 2)
    yearly_listening.plot(kind='bar')
    plt.title('Listening Time by Year')
    plt.xlabel('Year')
    plt.ylabel('Total Listening Time (Minutes)')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    return {
        'monthly_listening': monthly_listening,
        'yearly_listening': yearly_listening
    }
    
# Hour of day listening frequency
def analyze_hourly_listening(df):
    """
    Analyze listening frequency by hour of the day.
    
    Parameters:
    df (pandas.DataFrame): Spotify listening data
    
    Returns:
    Dict containing hourly listening insights
    """
    # Listening count by hour
    hourly_listening_count = df.groupby('hour').size()
    
    # Listening time by hour (in minutes)
    hourly_listening_time = df.groupby('hour')['ms_played'].sum() / MS_TO_MINUTES
    
    # Visualization
    plt.figure(figsize=(15, 5))
    
    # Listening count by hour
    plt.subplot(1, 2, 1)
    hourly_listening_count.plot(kind='bar')
    plt.title('Listening Frequency by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Listening Sessions')
    plt.xticks(rotation=45)
    
    # Listening time by hour
    plt.subplot(1, 2, 2)
    hourly_listening_time.plot(kind='bar')
    plt.title('Listening Time by Hour')
    plt.xlabel('Hour of Day')
    plt.ylabel('Total Listening Time (Minutes)')
    plt.xticks(rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    return {
        'hourly_listening_count': hourly_listening_count,
        'hourly_listening_time': hourly_listening_time
    }
    
# Year-over-year listening behavior changes
def analyze_year_over_year_changes(df):
    """
    Analyze year-over-year listening behavior changes.
    
    Parameters:
    df (pandas.DataFrame): Spotify listening data
    
    Returns:
    Dict containing year-over-year listening insights
    """
    # Yearly metrics
    yearly_metrics = df.groupby('year').agg({
        'ms_played': 'sum',  # Total listening time
        'track_name': 'count',  # Total tracks played
        'artist_name': 'nunique',  # Unique artists
        'skipped': 'mean'  # Average skip rate
    })
    
    # Convert listening time to minutes
    yearly_metrics['listening_time_minutes'] = yearly_metrics['ms_played'] / MS_TO_MINUTES
    
    # Calculate year-over-year changes
    yearly_changes = yearly_metrics.pct_change() * 100
    yearly_changes.columns = [f'{col}_change_percent' for col in yearly_changes.columns]
    
    # Visualization
    plt.figure(figsize=(15, 5))
    
    # Listening time trend
    plt.subplot(1, 2, 1)
    yearly_metrics['listening_time_minutes'].plot(kind='line', marker='o')
    plt.title('Yearly Listening Time')
    plt.xlabel('Year')
    plt.ylabel('Total Listening Time (Minutes)')
    
    # Unique artists trend
    plt.subplot(1, 2, 2)
    yearly_metrics['artist_name'].plot(kind='line', marker='o')
    plt.title('Unique Artists per Year')
    plt.xlabel('Year')
    plt.ylabel('Number of Unique Artists')
    
    plt.tight_layout()
    plt.show()
    
    return {
        'yearly_metrics': yearly_metrics,
        'yearly_changes': yearly_changes
    }
    
