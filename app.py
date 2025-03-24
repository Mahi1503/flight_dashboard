import streamlit as st
from dbhelper import DB
import plotly.graph_objects as go
import plotly.express as px


db = DB()

st.sidebar.title('Flights Analytics')
user_option = st.sidebar.selectbox('menu',['Select One','Check Flights','Analytics'])
if user_option == 'Check Flights':
    st.title('Check Flights')
    col1,col2 = st.columns(2)
    with col1:
        city_name = db.fetch_cities()
        source = st.selectbox('Source',sorted(city_name))
    with col2:
        destination = st.selectbox('Destination',sorted(city_name))
    if st.button("Search"):
        result = db.fetch_all_flights(source,destination)
        if result:
            st.dataframe(result)
        else:
            st.header("No flights record {} to {}".format(source,destination))

elif user_option == 'Analytics':
    st.title('Flight Analysis')
    airlines,frequency = db.fetch_airline_frequency()
    fig = go.Figure(
        go.Pie(
            labels = airlines,
            values = frequency,
            hoverinfo = 'label+percent',
            textinfo = 'value'
        ))
    st.header("Pie chart")
    st.plotly_chart(fig)

    df = db.busy_airport()
    fig = px.bar(df,
        x = 'city',
        y = 'frequency',
        color = 'city'
    )
    st.header("Bar chart Flight Frequency by Airport")
    st.plotly_chart(fig,theme='streamlit',use_container_width=True)

    df1 = db.daily_frequency()
    fig = px.line(df1,
                 x='date',
                 y='frequency'
                 )
    st.header("Line chart Daily Flight Frequency")
    st.plotly_chart(fig, theme='streamlit', use_container_width=True)

else:
    pass