# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
import sys
sys.path.append('../src')
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px
pd.set_option('display.max_rows', None)
import datetime
from plotly.subplots import make_subplots
from covid19.config import covid_19_data


# %%
data = covid_19_data


# %%
data[["Confirmed","Deaths","Recovered"]] =data[["Confirmed","Deaths","Recovered"]].astype(int)


# %%
data['Active_case'] = data['Confirmed'] - data['Deaths'] - data['Recovered']


# %%
Data_India = data [(data['Country/Region'] == 'India') ].reset_index(drop=True)
Data_India_op= Data_India.groupby(["ObservationDate","Country/Region"])[["Confirmed","Deaths","Recovered","Active_case"]].sum().reset_index().reset_index(drop=True)


# %%
fig = go.Figure()
fig.add_trace(go.Scatter(x=Data_India_op["ObservationDate"], y=Data_India_op['Confirmed'],
                    mode="lines+text",
                    name='Confirmed cases',
                    marker_color='orange',
                        ))

fig.add_annotation(
            x="03/24/2020",
            y=Data_India_op['Confirmed'].max(),
            text="COVID-19 pandemic lockdown in India",
             font=dict(
            family="Courier New, monospace",
            size=16,
            color="red"
            ),
)


fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0="03/24/2020",
            y0=Data_India_op['Confirmed'].max(),
            x1="03/24/2020",
    
            line=dict(
                color="red",
                width=3
            )
))
fig.add_annotation(
            x="04/24/2020",
            y=Data_India_op['Confirmed'].max()-30000,
            text="Month after lockdown",
             font=dict(
            family="Courier New, monospace",
            size=16,
            color="#00FE58"
            ),
)

fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0="04/24/2020",
            y0=Data_India_op['Confirmed'].max(),
            x1="04/24/2020",
    
            line=dict(
                color="#00FE58",
                width=3
            )
))
fig
fig.update_layout(
    title='Evolution of Confirmed cases over time in India',
        template='plotly_dark'

)

fig.show()


# %%
fig = go.Figure()
fig.add_trace(go.Scatter(x=Data_India_op["ObservationDate"], y=Data_India_op['Active_case'],
                    mode="lines+text",
                    name='Active cases',
                    marker_color='#00FE58',
                        ))

fig.add_annotation(
            x="03/24/2020",
            y=Data_India_op['Active_case'].max(),
            text="COVID-19 pandemic lockdown in India",
             font=dict(
            family="Courier New, monospace",
            size=16,
            color="red"
            ),
)


fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0="03/24/2020",
            y0=Data_India_op['Active_case'].max(),
            x1="03/24/2020",
    
            line=dict(
                color="red",
                width=3
            )
))


fig.add_annotation(
            x="04/24/2020",
            y=Data_India_op['Active_case'].max()-20000,
            text="Month after lockdown",
             font=dict(
            family="Courier New, monospace",
            size=16,
            color="rgb(255,217,47)"
            ),
)

fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0="04/24/2020",
            y0=Data_India_op['Active_case'].max(),
            x1="04/24/2020",
    
            line=dict(
                color="rgb(255,217,47)",
                width=3
            )
))
fig.update_layout(
    title='Evolution of Active cases over time in India',
        template='plotly_dark'

)

fig.show()


# %%
fig = go.Figure()
fig.add_trace(go.Scatter(x=Data_India_op["ObservationDate"], y=Data_India_op['Recovered'],
                    mode="lines+text",
                    name='Recovered cases',
                    marker_color='rgb(229,151,232)',
                        ))

fig.add_annotation(
            x="03/24/2020",
            y=Data_India_op['Recovered'].max(),
            text="COVID-19 pandemic lockdown in India",
             font=dict(
            family="Courier New, monospace",
            size=16,
            color="red"
            ),
)


fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0="03/24/2020",
            y0=Data_India_op['Recovered'].max(),
            x1="03/24/2020",
    
            line=dict(
                color="red",
                width=3
            )
))


fig.add_annotation(
            x="04/24/2020",
            y=Data_India_op['Recovered'].max()-20000,
            text="Month after lockdown",
             font=dict(
            family="Courier New, monospace",
            size=16,
            color="rgb(103,219,165)"
            ),
)

fig.add_shape(
        # Line Vertical
        dict(
            type="line",
            x0="04/24/2020",
            y0=Data_India_op['Recovered'].max(),
            x1="04/24/2020",
    
            line=dict(
                color="rgb(103,219,165)",
                width=3
            )
))
fig.update_layout(
    title='Evolution of Recovered cases over time in India',
        template='plotly_dark'

)

fig.show()

