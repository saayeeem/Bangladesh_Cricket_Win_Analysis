import matplotlib.pyplot as plt
from matplotlib import rcParams
import numpy as np
def line_graph(x_label,play_format,year,ratio,year_from,to,color,name,ratio_2022):

    """
    This function creates a line graph using the following input variables:
    - x_label: a string representing a label for the x-axis of a graph
    - play_format: a string representing the format of a play (e.g. "odi", "test", "t20")
    - year: an integer representing a specific year
    - ratio: a float representing a ratio value
    - year_from: an integer representing a starting year for a range
    - to: an integer representing an ending year for a range
    - color: a string representing a color (e.g. "red", "blue", "green")
    - name: a string representing a name for save the visualization
    - ratio_2022: a float representing a ratio value for the year 2022

    Returns:
    - A line graph with the specified parameters.

    """
    # Shades of gray
    rcParams['font.family'] = 'Montserrat'
    GREY10 = "#1a1a1a"
    GREY30 = "#4d4d4d"
    GREY40 = "#666666"
    GREY50 = "#7f7f7f"
    GREY60 = "#999999"
    GREY75 = "#bfbfbf"
    GREY91 = "#e8e8e8"
    GREY98 = "#fafafa"

    fig, ax = plt.subplots(figsize = (12, 8))

    # Background color
    fig.patch.set_facecolor(GREY98)
    ax.set_facecolor(GREY98)
    # Vertical lines every 2 years
    VLINES = np.arange(year_from,to, 2)

    # # Vertical lines used as scale reference
    for h in VLINES:
        ax.axvline(h, color=GREY91, lw=0.6, zorder=0)

    # Horizontal lines
    ax.hlines(y=np.arange(0, 120,20), xmin=year_from, xmax=to, color=GREY91, lw=0.6)

    # Darker horizontal line at y=0
    ax.hlines(y=ratio.min(), xmin=year_from, xmax=to, color=GREY60, lw=0.8)


    plt.plot(year,ratio,color,lw=3)
    ax.tick_params(axis="x", length=12, color=GREY91)
    ax.tick_params(axis="y", length=8, color=GREY91)


    # First, adjust axes limits so annotations fit in the plot
    ax.set_xlim(year_from, to+2)
    ax.set_ylim(0, 100)

    x_start = to
    x_end = to+2
    PAD = 0.1

    # Format name
    text = play_format

    # Vertical start of line
    y_start = ratio_2022
    # Vertical end of line
    y_end = ratio_2022-5

    # Add line based on three points
    ax.plot(
        [x_start, (x_start + x_end - PAD) / 2 , x_end - PAD],
        [y_start, y_end, y_end],
        color=color,
        alpha=0.5,
        ls="dashed"
    )

    # Add format text
    ax.text(
        x_end,
        y_end,
        text,
        color=color,
        fontsize=14,
        weight="bold",
        fontfamily="Montserrat",
        va="center"
    )

    # Customize axes labels and ticks --------------------------------
    ax.set_yticks([y for y in np.arange(0, 120,20)])
    ax.set_yticklabels(
        [f"{y}" for y in np.arange(0, 120,20)],
        fontname="Montserrat",
        fontsize=11,
        weight=500,
        color=GREY40
    )


    ax.set_xticks([x for x in np.arange(year_from, to+2, 2)])
    ax.set_xticklabels(
        [x for x in np.arange(year_from, to+2, 2)],
        fontname= "Montserrat",
        fontsize=13,
        weight=500,
        color=GREY40
    )

    # Customize spines
    ax.spines["left"].set_color(GREY91)
    ax.spines["bottom"].set_color(GREY91)
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.set_xlabel(f'{x_label}',fontname="Montserrat",size=12,color =GREY40)
    ax.set_ylabel('Win %',fontname="Montserrat",size=12,color =GREY40)

    fig.text(
        0.08,
        0.97,
        f"Win% of Bangladesh Cricket Team in {play_format} from {year_from} to {to}",
        color=GREY10,
        fontsize=15,
        fontname="Montserrat",
        weight="bold"
    )

    fig.text(
        0.08,
        0.91,
        "by Mohammad Sayem Chowdhury",
        ha="left",
        color=GREY30,
        fontname="Montserrat",
        fontsize=10
    )

    fig.text(
        0.15,
        -0.07,
        "All data are collected from http://howstat.com/cricket/home.asp",
        fontname="Montserrat",
        fontsize=7,
        color=GREY30,
        ha="left"
    )
    fig.savefig(f"images/{name}.jpg",dpi=500,bbox_inches = 'tight')
def line_graph_cup(x_label,play_format,year,ratio,year_from,to,color,name,ratio_2022):

    """
    This function creates a line graph using the following input variables:
    - x_label: a string representing a label for the x-axis of a graph
    - play_format: a string representing the format of a play (e.g. "odi", "test", "t20")
    - year: an integer representing a specific year
    - ratio: a float representing a ratio value
    - year_from: an integer representing a starting year for a range
    - to: an integer representing an ending year for a range
    - color: a string representing a color (e.g. "red", "blue", "green")
    - name: a string representing a name for save the visualization
    - ratio_2022: a float representing a ratio value for the year 2022

    Returns:
    - A line graph with the specified parameters.

    """

    # Shades of gray
    rcParams['font.family'] = 'Montserrat'
    GREY10 = "#1a1a1a"
    GREY30 = "#4d4d4d"
    GREY40 = "#666666"
    GREY50 = "#7f7f7f"
    GREY60 = "#999999"
    GREY75 = "#bfbfbf"
    GREY91 = "#e8e8e8"
    GREY98 = "#fafafa"

    fig, ax = plt.subplots(figsize = (12, 6))

    # Background color
    fig.patch.set_facecolor(GREY98)
    ax.set_facecolor(GREY98)
    # Vertical lines every 2 years
    VLINES = np.arange(year_from,to, 2)

    # # Vertical lines used as scale reference
    for h in VLINES:
        ax.axvline(h, color=GREY91, lw=0.6, zorder=0)

    # Horizontal lines
    ax.hlines(y=np.arange(0, 120,20), xmin=year_from, xmax=to, color=GREY91, lw=0.6)

    # Darker horizontal line at y=0
    ax.hlines(y=ratio.min(), xmin=year_from, xmax=to, color=GREY60, lw=0.8)


    plt.plot(year,ratio,color,lw=3)
    ax.tick_params(axis="x", length=12, color=GREY91)
    ax.tick_params(axis="y", length=8, color=GREY91)


    # First, adjust axes limits so annotations fit in the plot
    ax.set_xlim(year_from, to+2)
    ax.set_ylim(0, 100)

    x_start = to
    x_end = to+2
    PAD = 0.1

    # Format name
    text = play_format

    # Vertical start of line
    y_start = ratio_2022
    # Vertical end of line
    y_end = ratio_2022-5

    # Add line based on three points
    ax.plot(
        [x_start, (x_start + x_end - PAD) / 2 , x_end - PAD],
        [y_start, y_end, y_end],
        color=color,
        alpha=0.5,
        ls="dashed"
    )

    # Add format text
    ax.text(
        x_end,
        y_end,
        text,
        color=color,
        fontsize=14,
        weight="bold",
        fontfamily="Montserrat",
        va="center"
    )

    # Customize axes labels and ticks --------------------------------
    ax.set_yticks([y for y in np.arange(0, 120,20)])
    ax.set_yticklabels(
        [f"{y}" for y in np.arange(0, 120,20)],
        fontname="Montserrat",
        fontsize=11,
        weight=500,
        color=GREY40
    )


    ax.set_xticks([x for x in np.arange(year_from, to+4, 4)])
    ax.set_xticklabels(
        [x for x in np.arange(year_from, to+4, 4)],
        fontname= "Montserrat",
        fontsize=13,
        weight=500,
        color=GREY40
    )

    # Customize spines
    ax.spines["left"].set_color(GREY91)
    ax.spines["bottom"].set_color(GREY91)
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.set_xlabel(f'{x_label}',fontname="Montserrat",size=12,color =GREY40)
    ax.set_ylabel('Win %',fontname="Montserrat",size=12,color =GREY40)

    fig.text(
        0.08,
        0.97,
        f"Win% of Bangladesh Cricket Team in {play_format} from {year_from} to {to}",
        color=GREY10,
        fontsize=15,
        fontname="Montserrat",
        weight="bold"
    )

    fig.text(
        0.08,
        0.91,
        "by Mohammad Sayem Chowdhury",
        ha="left",
        color=GREY30,
        fontname="Montserrat",
        fontsize=10
    )

    fig.text(
        0.15,
        -0.07,
        "All data are collected from http://howstat.com/cricket/home.asp",
        fontname="Montserrat",
        fontsize=7,
        color=GREY30,
        ha="left"
    )
    fig.savefig(f"images/{name}.jpg",dpi=500,bbox_inches = 'tight')

def line_graph_month(play_format,month,ratio,color,name,ratio_2022):

    """
    This function creates a line graph using the following input variables::
    - play_format: a string representing the format of a play (e.g. "odi", "test", "t20")
    - month: an integer representing a specific month
    - ratio: a float representing a ratio value
    - color: a string representing a color (e.g. "red", "blue", "green")
    - name: a string representing a name for save the visualization
    - ratio_2022: a float representing a ratio value for the year 2022

    Returns:
    - A line graph with the specified parameters.

    """
    # Shades of gray
    rcParams['font.family'] = 'Montserrat'
    GREY10 = "#1a1a1a"
    GREY30 = "#4d4d4d"
    GREY40 = "#666666"
    GREY50 = "#7f7f7f"
    GREY60 = "#999999"
    GREY75 = "#bfbfbf"
    GREY91 = "#e8e8e8"
    GREY98 = "#fafafa"

    fig, ax = plt.subplots(figsize = (12, 10))

    # Background color
    fig.patch.set_facecolor(GREY98)
    ax.set_facecolor(GREY98)
    # Vertical lines every 2 months
    VLINES = np.arange(0,12, 1)

    # # Vertical lines used as scale reference
    for h in VLINES:
        ax.axvline(h, color=GREY91, lw=0.6, zorder=0)

    # Horizontal lines
    ax.hlines(y=np.arange(0, 110,10), xmin=0, xmax=11, color=GREY91, lw=0.6)

    # Darker horizontal line at y=0
    ax.hlines(y=0, xmin=0, xmax=11, color=GREY60, lw=0.8)


    plt.plot(month,ratio,color,lw=3)
    ax.tick_params(axis="x", length=12, color=GREY91)
    ax.tick_params(axis="y", length=8, color=GREY91)


    # First, adjust axes limits so annotations fit in the plot
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 1)

    x_start = 11
    x_end = 12
    PAD = 0.1

    # Format name
    text = play_format

    # Vertical start of line
    y_start = ratio_2022
    # Vertical end of line
    y_end = ratio_2022-5

    # Add line based on three points
    ax.plot(
        [x_start, (x_start + x_end - PAD) / 2 , x_end - PAD],
        [y_start, y_end, y_end],
        color=color,
        alpha=0.5,
        ls="dashed"
    )

    # Add format text
    ax.text(
        x_end,
        y_end,
        text,
        color=color,
        fontsize=14,
        weight="bold",
        fontfamily="Montserrat",
        va="center"
    )

    # Customize axes labels and ticks --------------------------------
    ax.set_yticks([y for y in np.arange(0, 110,10)])
    ax.set_yticklabels(
        [f"{y}" for y in np.arange(0, 110,10)],
        fontname="Montserrat",
        fontsize=11,
        weight=500,
        color=GREY40
    )


    ax.set_xticks([x for x in month])
    ax.set_xticklabels(
        [x for x in month],
        fontname= "Montserrat",
        fontsize=13,
        weight=500,
        color=GREY40,
        rotation=45
    )

    # Customize spines
    ax.spines["left"].set_color(GREY91)
    ax.spines["bottom"].set_color(GREY91)
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.set_xlabel('Month',fontname="Montserrat",size=12,color =GREY40)
    ax.set_ylabel('Win %',fontname="Montserrat",size=12,color =GREY40)

    fig.text(
        0.08,
        0.97,
        f"Win% of Bangladesh Cricket Team in {play_format} from January to December",
        color=GREY10,
        fontsize=15,
        fontname="Montserrat",
        weight="bold"
    )

    fig.text(
        0.08,
        0.91,
        "by Mohammad Sayem Chowdhury",
        ha="left",
        color=GREY30,
        fontname="Montserrat",
        fontsize=10
    )

    fig.text(
        0.15,
        -0.1,
        "All data are collected from http://howstat.com/cricket/home.asp",
        fontname="Montserrat",
        fontsize=7,
        color=GREY30,
        ha="left"
    )
    fig.savefig(f"images/{name}.jpg",dpi=500,bbox_inches = 'tight')


def bar_graph(title,y,x,color,label,name,method="barh",match_flag=""):
    """
    This function creates a bar graph using the following input variables:
    - title: a string representing the title of the graph
    - y: a list of integers representing the y-axis values for the bar graph
    - x: a list of strings representing the labels for the x-axis of the graph
    - color: a string representing the color of the bars in the graph
    - label: a string representing the label for the y-axis or x-axis of the graph
    - name: a string representing the name of the visualization to save
    - method: a string representing the method for creating the bar graph. The default value is "barh" (horizontal bars).
    - match_flag: a string representing a flag used to match data. The default value is an empty string.

    Returns:
    - A bar graph with the specified parameters.
    """
    rcParams['font.family'] = 'Montserrat'

    # Shades of gray
    GREY10 = "#1a1a1a"
    GREY30 = "#4d4d4d"
    GREY40 = "#666666"
    GREY50 = "#7f7f7f"
    GREY60 = "#999999"
    GREY75 = "#bfbfbf"
    GREY91 = "#e8e8e8"
    GREY98 = "#fafafa"

    # change the bar color to be less bright blue
    if method =="bar":
        fig, ax = plt.subplots(figsize = (8, 8))
        # Background color
        fig.patch.set_facecolor(GREY98)
        ax.set_facecolor(GREY98)
        bars =ax.bar(x, y, linewidth=0, color=color)
        ax.set_yticks([])

        ax.set_xticks(x)
        ax.set_xticklabels(
            x,
            fontname= "Montserrat",
            fontsize=13,
            weight=500,
            color=GREY40
        )


        ax.set_ylabel(f'{label}',fontname="Montserrat",size=12,color =GREY40)
        ax.bar_label(bars,label_type='edge', fmt='%.2f',color=GREY30,
            fontname="Montserrat",
            size=14)

        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,      # ticks along the top edge are off) # labels along the bottom edge are off
            left = False,
            right = False,

        )

    else:
        fig, ax = plt.subplots(figsize = (14, 8))
        # Background color
        fig.patch.set_facecolor(GREY98)
        ax.set_facecolor(GREY98)
        bars =ax.barh(y, x, linewidth=0, color=color)


        ax.set_xticks([])


        ax.set_yticks(y)
        ax.set_yticklabels(
            y,
            fontname= "Montserrat",
            fontsize=13,
            weight=500,
            color=GREY40
        )


        ax.set_xlabel(f'{label}',fontname="Montserrat",size=12,color =GREY40)
        ax.bar_label(bars,label_type='edge', fmt='%.2f',color=GREY30,
            fontname="Montserrat",
            size=14)

        plt.tick_params(
            axis='y',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,      # ticks along the top edge are off) # labels along the bottom edge are off
            left = False,
            right = False,

        )
    # Customize spines
    ax.spines["left"].set_color("none")
    ax.spines["bottom"].set_color("none")
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    fig.text(
        0.08,
        0.97,
        title,
        color=GREY10,
        fontsize=15,
        fontname="Montserrat",
        weight="bold"
    )

    fig.text(
        0.08,
        0.91,
        f"{match_flag} \nby Mohammad Sayem Chowdhury",
        ha="left",
        color=GREY30,
        fontname="Montserrat",
        fontsize=10
    )

    fig.text(
        0.15,
        -0.07,
        "All data are collected from http://howstat.com/cricket/home.asp",
        fontname="Montserrat",
        fontsize=7,
        color=GREY30,
        ha="left"
    )
    fig.savefig(f"images/{name}.jpg",dpi=500,bbox_inches = 'tight')
def line_graph_ten_years(x1,y1,x2,y2,x3,y3,name,t20_10_years_2022,odi_10_years_2022,test_10_years_2022):

    """
    This function creates a line graph with three lines, each representing data for the past 10 years. The lines are plotted using the following input variables:
    - x1: a list of strings representing the labels for the x-axis of the first line
    - y1: a list of integers representing the y-axis values for the first line
    - x2: a list of strings representing the labels for the x-axis of the second line
    - y2: a list of integers representing the y-axis values for the second line
    - x3: a list of strings representing the labels for the x-axis of the third line
    - y3: a list of integers representing the y-axis values for the third line
    - name: a string representing the name of the data being saved the plot.
    - t20_10_years_2022: a float representing a value for the year 2022 for the first line
    - odi_10_years_2022: a float representing a value for the year 2022 for the second line
    - test_10_years_2022: a float representing a value for the year 2022 for the third line

    Returns:
    - A line graph with three lines, each representing data for the past 10 years
    """

    # Shades of gray
    GREY10 = "#1a1a1a"
    GREY30 = "#4d4d4d"
    GREY40 = "#666666"
    GREY50 = "#7f7f7f"
    GREY60 = "#999999"
    GREY75 = "#bfbfbf"
    GREY91 = "#e8e8e8"
    GREY98 = "#fafafa"

    fig, ax = plt.subplots(figsize = (14, 8))

    # Background color
    fig.patch.set_facecolor(GREY98)
    ax.set_facecolor(GREY98)

    # Vertical lines every 2 years
    VLINES = np.arange(2012, 2023, 1)

    # # Vertical lines used as scale reference
    for h in VLINES:
        ax.axvline(h, color=GREY91, lw=0.6, zorder=0)

    # Horizontal lines
    ax.hlines(y=np.arange(0, 120,20), xmin=2012, xmax=2022, color=GREY91, lw=0.6)

    # Darker horizontal line at y=0
    ax.hlines(y=0, xmin=2012, xmax=2022, color=GREY60, lw=0.8)

    plt.plot(x1,y1,"#7F3C8D",lw=3)
    plt.plot(x2,y2,"#3969AC",lw=3)
    plt.plot(x3,y3,"#80BA5A",lw=3)

    ax.tick_params(axis="x", length=12, color=GREY91)
    ax.tick_params(axis="y", length=8, color=GREY91)


    # First, adjust axes limits so annotations fit in the plot
    ax.set_xlim(2012, 2023)
    ax.set_ylim(0, 100)

    color = ["#7F3C8D","#3969AC","#80BA5A"]
    x_start = 2022
    x_end = 2023
    PAD = 0.1

    # Format name
    text = ["T20","ODI","TEST"]

    # Vertical start of line
    y_start = [t20_10_years_2022,odi_10_years_2022,test_10_years_2022]
    # Vertical end of line
    y_end = [t20_10_years_2022-5,odi_10_years_2022-5,test_10_years_2022-5]

    for i in range(3):
        # Add line based on three points
        ax.plot(
            [x_start, (x_start + x_end - PAD) / 2 , x_end - PAD],
            [y_start[i], y_end[i], y_end[i]],
            color=color[i],
            alpha=0.5,
            ls="dashed"
        )

        # Add format text
        ax.text(
            x_end,
            y_end[i],
            text[i],
            color=color[i],
            fontsize=14,
            weight="bold",
            fontfamily="Montserrat",
            va="center"
        )



    # Customize axes labels and ticks --------------------------------
    ax.set_yticks([y for y in np.arange(0, 120,20)])
    ax.set_yticklabels(
        [f"{y}" for y in np.arange(0, 120,20)],
        fontname="Montserrat",
        fontsize=11,
        weight=500,
        color=GREY40
    )


    ax.set_xticks([x for x in np.arange(2012, 2023, 1)])
    ax.set_xticklabels(
        [x for x in np.arange(2012, 2023, 1)],
        fontname= "Montserrat",
        fontsize=13,
        weight=500,
        color=GREY40
    )

    # Customize spines
    ax.spines["left"].set_color(GREY91)
    ax.spines["bottom"].set_color(GREY91)
    ax.spines["right"].set_color("none")
    ax.spines["top"].set_color("none")
    ax.set_xlabel('Year',fontname="Montserrat",size=12,color =GREY40)
    ax.set_ylabel('Win %',fontname="Montserrat",size=12,color =GREY40)

    fig.text(
        0.08,
        0.97,
        "Win% of Bangladesh Cricket Team in All Format from 2012 to 2022",
        color=GREY10,
        fontsize=15,
        fontname="Montserrat",
        weight="bold"
    )

    fig.text(
        0.08,
        0.91,
        "by Mohammad Sayem Chowdhury",
        ha="left",
        color=GREY30,
        fontname="Montserrat",
        fontsize=10
    )

    fig.text(
        0.15,
        -0.07,
        "All data are collected from http://howstat.com/cricket/home.asp",
        fontname="Montserrat",
        fontsize=7,
        color=GREY30,
        ha="left"
    )
    fig.savefig(f"images/{name}.jpg",dpi=500,bbox_inches = 'tight')
