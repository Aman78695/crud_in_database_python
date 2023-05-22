import streamlit as st
from db import dbhelper
import plotly.graph_objects as go
import plotly.express as px
DB=dbhelper()
st.sidebar.title('flight analytics')
option=st.sidebar.selectbox('Menu',['select one','check flights','flight analytics'])
if option=='check flights':
    l=DB.fetchcity()
    st.title('Flight Checks')
    col1,col2=st.columns(2)
    with col1:
        source=st.selectbox('source',sorted(l))
    with col2:
        destination=st.selectbox('destination',sorted(l))

    if st.button('search'):
        k=DB.fetch_all_flights(source,destination)
        print(st.dataframe(k))
elif option=='flight analytics':
    st.title('Analytics')
    airline,frequency = DB.flight_piechart()
    fig = go.Figure(
        go.Pie(
            labels=airline,
            values=frequency,
            hoverinfo="label+percent",
            textinfo="value"
        ))

    st.header("Pie chart")
    st.plotly_chart(fig)
else:
    pass
