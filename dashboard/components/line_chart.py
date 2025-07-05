import streamlit as st
import pandas as pd
import plotly.express as px

def render_line_chart(data):
    """渲染折线图"""
    st.subheader("路段流量趋势")
    
    # 创建折线图
    fig = px.line(
        data, 
        x="date", 
        y="flow",
        markers=True,
        title="路段流量趋势"
    )
    
    st.plotly_chart(fig, use_container_width=True)