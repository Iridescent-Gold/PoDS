# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "matplotlib==3.10.8",
#     "seaborn==0.13.2",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(
    width="medium",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell
def _():
    import marimo as mo
    import seaborn as sns
    import matplotlib.pyplot as plt

    tips = sns.load_dataset("tips")
    sns.set_theme(style="whitegrid")
    return mo, plt, sns, tips


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > <span style="color: #2e6f95; font-weight: bold; font-style: normal;">Default Jitter:</span>
    > <div style="color: #1a1a1a; font-style: normal; margin-top: 4px;">
    > In a strip plot, the data points are jittered by default. This adds a small amount of random noise to the categorical axis so that points with identical values don't completely overlap, allowing you to see the distribution density.
    > </div>
    """)
    return


@app.cell
def _(plt, sns, tips):
    sns.catplot(x="day", y="total_bill", data=tips, kind="strip", hue="day", legend=False)
    plt.title("Default Strip Plot")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > <span style="color: #2e6f95; font-weight: bold; font-style: normal;">Manual Jitter (0.5):</span>
    > <div style="color: #1a1a1a; font-style: normal; margin-top: 4px;">
    > The extent of overlap is determined by the jitter amount. You can specify a float between 0 and 1 to control the width of the spread. A value of 0.5 creates a moderately tight cluster.
    > </div>
    """)
    return


@app.cell
def _(plt, sns, tips):
    sns.catplot(x="day", y="total_bill", data=tips, kind="strip", jitter=0.5, hue="day", legend=False)
    plt.title("Jitter = 0.5")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > <span style="color: #2e6f95; font-weight: bold; font-style: normal;">No Jitter (False):</span>
    > <div style="color: #1a1a1a; font-style: normal; margin-top: 4px;">
    > The jitter can be eliminated entirely by passing a False Boolean. This aligns all points in a perfectly straight line. While organized, this often masks the true number of data points due to heavy overlapping.
    > </div>
    """)
    return


@app.cell
def _(plt, sns, tips):
    sns.catplot(x="day", y="total_bill", data=tips, kind="strip", jitter=False, hue="day", legend=False)
    plt.title("Jitter = False")
    plt.gca()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > <span style="color: #2e6f95; font-weight: bold; font-style: normal;">Maximum Jitter (1.0):</span>
    > <div style="color: #1a1a1a; font-style: normal; margin-top: 4px;">
    > A value of 1 represents the maximum default jitter width. This spreads the points across the entire width of the category bin, which is helpful for datasets with a very high volume of overlapping points.
    > </div>
    """)
    return


@app.cell
def _(plt, sns, tips):
    sns.catplot(x="day", y="total_bill", data=tips, kind="strip", jitter=1, hue="day", legend=False)
    plt.title("Jitter = 1")
    plt.gca()
    return


if __name__ == "__main__":
    app.run()
