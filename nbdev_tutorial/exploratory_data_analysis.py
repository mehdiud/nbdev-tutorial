# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_dataset_exploration.ipynb.

# %% auto 0
__all__ = ['source']

# %% ../nbs/01_dataset_exploration.ipynb 10
source = data.stocks()

alt.Chart(source).mark_area(
    color="lightblue",
    interpolate='step-after',
    line=True
).encode(
    x='date',
    y='price'
).transform_filter(alt.datum.symbol == 'GOOG')
