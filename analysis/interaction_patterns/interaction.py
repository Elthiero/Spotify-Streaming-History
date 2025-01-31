import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Constants
MS_TO_MINUTES = 60000

# Shuffle vs non-shuffle listening
def analyze_shuffle_listening(df):
    """
    Analyze shuffle vs non-shuffle listening behavior.
    
    Parameters:
    df (pandas.DataFrame): Spotify listening data
    
    Returns:
    Dict containing shuffle listening insights
    """
    # Shuffle usage metrics
    shuffle_metrics = df.groupby('shuffle').agg({
        'ms_played': ['count', 'sum', 'mean'],
        'skipped': 'mean'
    })
    
    # Convert metrics
    shuffle_metrics['ms_played', 'sum'] /= MS_TO_MINUTES  # Convert to minutes
    shuffle_metrics.columns = ['play_count', 'total_listening_minutes', 'avg_listening_minutes', 'skip_rate']
    
    # Visualization
    plt.figure(figsize=(12, 5))
    
    # Play count comparison
    plt.subplot(1, 2, 1)
    shuffle_metrics['play_count'].plot(kind='bar')
    plt.title('Listening Sessions: Shuffle vs Non-Shuffle')
    plt.xlabel('Shuffle')
    plt.ylabel('Number of Sessions')
    
    # Total listening time comparison
    plt.subplot(1, 2, 2)
    shuffle_metrics['total_listening_minutes'].plot(kind='bar')
    plt.title('Total Listening Time: Shuffle vs Non-Shuffle')
    plt.xlabel('Shuffle')
    plt.ylabel('Listening Time (Minutes)')
    
    plt.tight_layout()
    plt.show()
    
    return {
        'shuffle_metrics': shuffle_metrics
    }
    
# Reason for track start/end
def analyze_track_start_end_reasons(df):
    """
    Analyze reasons for track start and end.
    
    Parameters:
    df (pandas.DataFrame): Spotify listening data
    
    Returns:
    Dict containing start and end reason insights
    """
    # Start reasons analysis
    start_reasons = df['reason_start'].value_counts()
    start_reasons_percent = start_reasons / len(df) * 100
    
    # End reasons analysis
    end_reasons = df['reason_end'].value_counts()
    end_reasons_percent = end_reasons / len(df) * 100
    
    # Visualization
    plt.figure(figsize=(15, 5))
    
    # Start reasons
    # plt.subplot(1, 2, 1)
    # start_reasons_percent.plot(kind='pie', autopct='%1.1f%%')
    # plt.title('Reasons for Track Start')
    
    plt.subplot(1, 2, 1)
    start_reasons_percent.plot(kind='bar')
    plt.title('Reasons for Track Start')
    plt.xlabel('Start Reason')
    plt.ylabel('Start Reason Percentage')
    
    # End reasons
    # plt.subplot(1, 2, 2)
    # end_reasons_percent.plot(kind='pie', autopct='%1.1f%%')
    # plt.title('Reasons for Track End')

    plt.subplot(1, 2, 2)
    end_reasons_percent.plot(kind='bar')
    plt.title('Reasons for Track End')
    plt.xlabel('End Reason')
    plt.ylabel('End Reason Count')
    
    plt.tight_layout()
    plt.show()
    
    return {
        'start_reasons_count': start_reasons,
        'start_reasons_percent': start_reasons_percent,
        'end_reasons_count': end_reasons,
        'end_reasons_percent': end_reasons_percent
    }
    
