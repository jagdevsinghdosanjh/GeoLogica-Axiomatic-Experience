import streamlit as st
import plotly.graph_objects as go

def show_visuals():
    st.header("Visual Playground")
    st.markdown("Drag points and observe geometric relationships.")

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=[1, 4], y=[2, 6], mode='lines+markers', name='Line AB'))
    fig.update_layout(width=600, height=400, title="Line through Two Points")
    
    st.plotly_chart(fig)
