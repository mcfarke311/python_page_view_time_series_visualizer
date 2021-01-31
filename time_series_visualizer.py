import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date', parse_dates=['date'])

# Clean data
df = df.loc[(df.value >= df.value.quantile(0.025)) & (df.value <= df.value.quantile(0.975))]


def draw_line_plot():
    # Draw line plot
    fig, ax = plt.subplots(figsize=(8,4))
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_ylim(0,180000)
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    ax.plot_date(df.index.date, df.value, fmt='r-')

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.groupby([(df.index.year),(df.index.month)]).mean()

    # Draw bar plot
    fig = df_bar.unstack().plot(kind="bar", figsize=(10, 10)).figure
    plt.legend(labels=("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"))
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.title("Average Page Views per Year")

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(ncols=2)

    months_in_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    ax0 = sns.boxplot(x='year', y='value', data=df_box, ax=ax[0])
    ax0.set_title('Year-wise Box Plot (Trend)')
    ax0.set_xlabel('Year')
    ax0.set_ylabel('Page Views')
    ax1 = sns.boxplot(x='month', y='value', data=df_box, order=months_in_order, ax=ax[1])
    ax1.set_title('Month-wise Box Plot (Seasonality)')
    ax1.set_xlabel('Month')
    ax1.set_ylabel('Page Views')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
