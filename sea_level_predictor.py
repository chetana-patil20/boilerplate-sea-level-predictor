import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
    # Import data
    df = pd.read_csv("epa-sea-level.csv")

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Line of best fit using all data
    slope, intercept, r_value, p_value, std_err = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # Predict through 2050
    years = pd.Series(
        range(df["Year"].min(), 2051)
    )

    predicted_sea_level = (
        slope * years + intercept
    )

    ax.plot(
        years,
        predicted_sea_level
    )

    # Line of best fit using data from 2000 onwards
    df_recent = df[df["Year"] >= 2000]

    slope_recent, intercept_recent, _, _, _ = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    recent_years = pd.Series(
        range(2000, 2051)
    )

    recent_predicted_sea_level = (
        slope_recent * recent_years +
        intercept_recent
    )

    ax.plot(
        recent_years,
        recent_predicted_sea_level
    )

    # Labels and title
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (inches)")
    ax.set_title("Rise in Sea Level")

    # Save plot
    fig.savefig("sea_level_plot.png")

    # Return Axes, because the tests expect it
    return ax