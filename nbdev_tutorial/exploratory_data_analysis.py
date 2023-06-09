# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_dataset_exploration.ipynb.

# %% auto 0
__all__ = ['MyViz']

# %% ../nbs/01_dataset_exploration.ipynb 12
class MyViz():
    """ This class is used to create various visualizations via `altair` library """
    def __init__(self):
        self.file_path = ""
        
    def plot_stock(self, stock_ticker: str):
        """ Gets `stock ticker` as parameter, returns a chart object. """
        source = data.stocks()
        chart = alt.Chart(source).mark_area(
            color="lightblue",
            interpolate='step-after',
            line=True
            ).encode(
                x='date',
                y='price',
                tooltip=[ 'symbol', 'date', 'price']
            ).transform_filter(alt.datum.symbol == stock_ticker)
           
        return chart
        
