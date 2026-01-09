# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
#     "numpy==2.2.6",
# ]
# ///

import marimo

__generated_with = "0.18.4"
app = marimo.App(
    width="full",
    css_file="/usr/local/_marimo/custom.css",
    auto_download=["html"],
)


@app.cell
def _():
    import marimo as mo
    import numpy as np
    return mo, np


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > <span style="color: #2e6f95; font-weight: bold; font-style: normal;">Vector (1D Array):</span>
    > <div style="color: #1a1a1a; font-style: normal; margin-top: 4px;">
    > A one-dimensional array possesses only one axis which stores a list of elements of the same data type in a linear order. This type of array is often referred to as a vector.
    > </div>
    """)
    return


@app.cell
def _(np):
    a = np.array([1, 2, 333, 4, 5])
    a
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > <span style="color: #2d8a3c; font-weight: bold; font-style: normal;">Matrix (2D Array):</span>
    > <div style="color: #1a1a1a; font-style: normal; margin-top: 4px;">
    > Likewise, a two-dimensional array possesses two axes which store multiple values of the same type in a rectangular grid. This type of array is often referred to as a matrix.
    > </div>
    """)
    return


@app.cell
def _(np):
    b = np.array([[1, 2, 3], [4, 5, 6]]) 
    b
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    > <span style="color: #6f42c1; font-weight: bold; font-style: normal;">Tensor (3D Array):</span>
    > <div style="color: #1a1a1a; font-style: normal; margin-top: 4px;">
    > For three-dimensional or higher dimensional arrays, the term tensor is also commonly used.
    > </div>
    """)
    return


@app.cell
def _(np):
    c = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
    c
    return


if __name__ == "__main__":
    app.run()
