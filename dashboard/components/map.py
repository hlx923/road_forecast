import streamlit as st
import pandas as pd
import plotly.express as px

def render_map(data):
    """渲染地图热力图"""
    st.subheader("路段流量热力图")
    
    # 创建地图
    fig = px.scatter_mapbox(
        data, 
        lat="lat", 
        lon="lon", 
        color="flow",
        size="flow",
        color_continuous_scale=px.colors.cyclical.IceFire,
        size_max=15,
        zoom=10,
        mapbox_style="carto-positron",
        hover_name="road_id",
        title="路段流量热力图"
    )
    
    st.plotly_chart(fig, use_container_width=True)