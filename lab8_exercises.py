# ==========================================
# 🐍 LAB 8: Visualization & Pandas DateTime
# ==========================================
# NOTE:
# - Each exercise is independent.
# - Student implementations MUST be written where "pass" is placed.
# - No extra solution hints exist in this file (by design).

import pandas as pd
import matplotlib.pyplot as plt


# ==========================================
# SECTION A: EASY (2 Points Each) — 5 Exercises
# ==========================================

# ==========================================
# EXERCISE 1: Week 6 Reminder - DateTime Parsing (2 points)
# ==========================================
# TODO:
#   Function Name: parse_and_enrich_dates
#   Parameters:
#       date_strings (list): List of date strings
#   Returns:
#       pandas.DataFrame with EXACT columns (in this order):
#           ["datetime", "year", "month", "day", "day_name", "is_leap_year"]
#   Description:
#       Convert each string to datetime and add datetime-based features.
#       Preserve input order.
#   Note:
#       date_strings may include both "YYYY-MM-DD" and "YYYY-MM-DD HH:MM" formats.
#   IMPORTANT:
#       Function name MUST be exactly "parse_and_enrich_dates".


# ==========================================
# EXERCISE 2: Week 7 Reminder - OO Line Plot (2 points)
# ==========================================
# TODO:
#   Function Name: make_line_plot
#   Parameters:
#       x (list): x-values
#       y (list): y-values
#       title (str): plot title
#   Returns:
#       tuple: (fig, ax) from matplotlib
#   Description:
#       Create a line plot using Matplotlib object-oriented API (plt.subplots()).
#       Set xlabel="x", ylabel="y" and set the given title.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "make_line_plot".


# ==========================================
# EXERCISE 3: Lab 8 - Histogram Basics (2 points)
# ==========================================
# TODO:
#   Function Name: make_histogram
#   Parameters:
#       values (list): list of numeric values
#   Returns:
#       tuple: (fig, ax)
#   Description:
#       Create a histogram using Matplotlib OO API with bins=10.
#       Set title EXACTLY: "Value Distribution".
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "make_histogram".
#       Title must match exactly.


# ==========================================
# EXERCISE 4: Lab 8 - Bar Plot (Category Counts) (2 points)
# ==========================================
# TODO:
#   Function Name: plot_category_counts
#   Parameters:
#       df (pandas.DataFrame): must contain column "category"
#   Returns:
#       tuple: (fig, ax)
#   Description:
#       Count occurrences of each category and create a bar plot (OO API).
#       Set title EXACTLY: "Category Counts".
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "plot_category_counts".
#       Title must match exactly.


# ==========================================
# EXERCISE 5: Lab 8 - Pandas Line Plot (2 points)
# ==========================================
# TODO:
#   Function Name: pandas_line_plot
#   Parameters:
#       df (pandas.DataFrame): must contain columns "x" and "y"
#   Returns:
#       matplotlib.axes.Axes: the axes returned by pandas plotting
#   Description:
#       Create a line plot using pandas plotting (df.plot(...)).
#       Return the Axes object.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "pandas_line_plot".


# ==========================================
# SECTION B: MEDIUM (3 Points Each) — 5 Exercises
# ==========================================

# ==========================================
# EXERCISE 6: Daily Aggregation (3 points)
# ==========================================
# TODO:
#   Function Name: daily_totals
#   Parameters:
#       df (pandas.DataFrame): must contain columns "timestamp" and "value"
#   Returns:
#       pandas.DataFrame: DataFrame with EXACT columns ["date", "total"]
#   Description:
#       Convert "timestamp" to datetime.
#       Aggregate values by DATE only (not full timestamp).
#       Sort result by date ascending.
#   IMPORTANT:
#       Function name MUST be exactly "daily_totals".
#       Output columns must match exactly.


# ==========================================
# EXERCISE 7: Line Plot + Save to File (3 points)
# ==========================================
# TODO:
#   Function Name: plot_and_save_line
#   Parameters:
#       x (list): x-values
#       y (list): y-values
#       out_file (str): output file path to save the figure
#   Returns:
#       tuple: (fig, ax)
#   Description:
#       Create a line plot (OO API) and save it to out_file.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "plot_and_save_line".
#       Must save the figure to the given path.


# ==========================================
# EXERCISE 8: Pandas Plot on Provided Axes (3 points)
# ==========================================
# TODO:
#   Function Name: plot_on_existing_ax
#   Parameters:
#       df (pandas.DataFrame): must contain columns "Sale Date" and "Total Sales"
#       ax (matplotlib.axes.Axes): target axes to plot on
#   Returns:
#       matplotlib.axes.Axes: the same ax after plotting
#   Description:
#       Convert "Sale Date" to datetime.
#       Plot "Total Sales" over "Sale Date" using pandas plotting on the given ax.
#       Set title EXACTLY: "Total Sales Over Time".
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "plot_on_existing_ax".
#       Must plot on the provided ax (not a new figure).
#       Title must match exactly.


# ==========================================
# EXERCISE 9: Histogram with Custom Bins (3 points)
# ==========================================
# TODO:
#   Function Name: histogram_with_bins
#   Parameters:
#       df (pandas.DataFrame): must contain column "value"
#       bins (int): number of bins for histogram
#   Returns:
#       tuple: (fig, ax)
#   Description:
#       Plot a histogram of df["value"] using OO API with the given bins.
#       Set title EXACTLY: "Histogram".
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "histogram_with_bins".
#       Title must match exactly.


# ==========================================
# EXERCISE 10: Simple Subplots (3 points)
# ==========================================
# TODO:
#   Function Name: simple_subplots
#   Parameters:
#       x (list): x-values
#       y (list): y-values
#   Returns:
#       tuple: (fig, axes)
#   Description:
#       Create a figure with 2 subplots (nrows=2, ncols=1, sharex=True).
#       Top subplot: line plot of x vs y.
#       Bottom subplot: histogram of y with bins=10.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "simple_subplots".


# ==========================================
# SECTION C: HARD (5 Points Each) — 5 Exercises
# ==========================================

# ==========================================
# EXERCISE 11: Sales Dashboard (5 points)
# ==========================================
# TODO:
#   Function Name: plot_sales_dashboard
#   Parameters:
#       df (pandas.DataFrame): must contain columns "date" and "sales"
#       out_file (str): output file path to save the figure
#   Returns:
#       tuple: (fig, axes)
#   Description:
#       Create a 2-row dashboard (subplots).
#       Row 1: line plot of sales over date.
#       Row 2: histogram of sales with bins=10.
#       Save the figure to out_file.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "plot_sales_dashboard".
#       Must save figure.


# ==========================================
# EXERCISE 12: Weekly Mean with DateTimeIndex (5 points)
# ==========================================
# TODO:
#   Function Name: weekly_mean
#   Parameters:
#       df (pandas.DataFrame): must contain columns "timestamp" and "value"
#   Returns:
#       pandas.DataFrame: DataFrame with EXACT columns ["week", "mean_value"]
#   Description:
#       Convert "timestamp" to datetime and set it as DateTimeIndex.
#       Compute weekly mean values using weekly resampling.
#   IMPORTANT:
#       Function name MUST be exactly "weekly_mean".
#       Output columns must match exactly.


# ==========================================
# EXERCISE 13: Top N Days by Total Value (5 points)
# ==========================================
# TODO:
#   Function Name: top_n_days_by_total
#   Parameters:
#       df (pandas.DataFrame): must contain columns "timestamp" and "value"
#       n (int): number of top days to return
#   Returns:
#       pandas.DataFrame: DataFrame with EXACT columns ["date", "total"]
#   Description:
#       Aggregate values by DATE and compute total per day.
#       Return only the top N days by total (descending).
#   IMPORTANT:
#       Function name MUST be exactly "top_n_days_by_total".
#       Output columns must match exactly.


# ==========================================
# EXERCISE 14: Compare Two Metrics (5 points)
# ==========================================
# TODO:
#   Function Name: compare_two_metrics
#   Parameters:
#       df (pandas.DataFrame): must contain numeric columns "a" and "b"
#   Returns:
#       tuple: (fig, axes)
#   Description:
#       Create 2 subplots (nrows=2, ncols=1, sharex=True).
#       Plot df["a"] as a line in the first axes.
#       Plot df["b"] as a line in the second axes.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "compare_two_metrics".


# ==========================================
# EXERCISE 15: Date Range Filter + Plot (5 points)
# ==========================================
# TODO:
#   Function Name: plot_date_range
#   Parameters:
#       df (pandas.DataFrame): must contain columns "timestamp" and "value"
#       start_date (str): start date string
#       end_date (str): end date string
#   Returns:
#       tuple: (fig, ax)
#   Description:
#       Convert "timestamp" to datetime.
#       Filter rows between start_date and end_date (inclusive).
#       Create a line plot of filtered values over time.
#       Do NOT call plt.show().
#   IMPORTANT:
#       Function name MUST be exactly "plot_date_range".
