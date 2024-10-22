import shiny
from shiny import App, ui, render
import numpy as np
import matplotlib.pyplot as plt

# Define the slider input
bins_slider = ui.input_slider(
    id="selected_number_of_bins",
    label="Number of Bins",
    min=0,
    max=100,
    value=20
)

# Set up the UI
app_ui = ui.page_fluid(
    ui.panel_title("Interactive Histogram"),
    bins_slider,
    ui.output_plot("histogram")
)

# Create the server logic
def server(input, output, session):

    @render.plot
    def histogram():
        count_of_points = 437
        np.random.seed(3)
        random_data_array = 100 + 15 * np.random.randn(count_of_points)
        plt.hist(random_data_array, bins=input.selected_number_of_bins(), density=True)
        plt.title("Random Data Distribution")
        plt.xlabel("Value")
        plt.ylabel("Density")

    output.histogram = histogram

app = App(app_ui, server)


