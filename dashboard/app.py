import streamlit as st
import pandas as pd
from dashboard.components.map import render_map
from dashboard.components.line_chart import render_line_chart
import os

st.title("城市交通流量预测与拥堵预警系统")

# 读取真实数据
data_path = os.path.join('data', '路段车流量每日汇总信息20240813.csv')
df = pd.read_csv(data_path, encoding='utf-8')

# 数据预处理
df['日期'] = pd.to_datetime(df['日期'])
df['date'] = df['日期'].dt.date  # 提取日期部分
df['road_id'] = df['道路名称']
df['flow'] = df['车流量'] * 100  # 放大流量数值以便于可视化

# 添加经纬度信息（模拟数据，实际应该有真实的经纬度）
road_locations = {
    '环北路': (30.28, 120.15),
    '凤起路': (30.25, 120.17),
    '庆春路': (30.26, 120.19),
    '延安路': (30.27, 120.16),
    '环城西路': (30.29, 120.14),
    '武林路': (30.27, 120.18),
    '体育场路': (30.26, 120.21),
    '天目山路': (30.28, 120.13),
    '德胜快速路': (30.30, 120.12),
    '秋涛路': (30.25, 120.22),
    '教工路': (30.31, 120.11)
}

# 添加经纬度列 
df['lat'] = df['道路名称'].map(lambda x: road_locations.get(x, (30.25, 120.15))[0])
df['lon'] = df['道路名称'].map(lambda x: road_locations.get(x, (30.25, 120.15))[1])

# 获取所有路段和日期范围
roads = df['道路名称'].unique().tolist()
min_date = df['date'].min()
max_date = df['date'].max()

# 选择器
date = st.date_input("选择日期", value=min_date, min_value=min_date, max_value=max_date)
road_id = st.selectbox("选择路段", options=roads)

# 筛选数据
selected_data = df[(df['date'] == date) & (df['road_id'] == road_id)]

# 地图热力图（传入当天所有路段数据）
map_data = df[df['date'] == date]
render_map(map_data)

# 动态折线图（展示该路段一周流量变化）
line_data = df[df['road_id'] == road_id][['date', 'flow']]
render_line_chart(line_data)

# 添加统计信息
st.subheader("路段流量统计")
avg_flow = df[df['road_id'] == road_id]['flow'].mean()
max_flow = df[df['road_id'] == road_id]['flow'].max()
min_flow = df[df['road_id'] == road_id]['flow'].min()

col1, col2, col3 = st.columns(3)
col1.metric("平均流量", f"{avg_flow:.1f}")
col2.metric("最大流量", f"{max_flow:.1f}")
col3.metric("最小流量", f"{min_flow:.1f}")