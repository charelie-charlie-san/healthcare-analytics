import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import random

# ページ設定
st.set_page_config(
    page_title="クリニック経営分析ダッシュボード",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSS - 清潔感のある医療系デザイン
st.markdown("""
<style>
    /* 全体の背景 */
    .stApp {
        background-color: #f8f9fa;
    }
    
    /* メトリックカードのスタイル */
    [data-testid="stMetricValue"] {
        font-size: 2rem;
        color: #0056b3;
        font-weight: 600;
    }
    
    [data-testid="stMetricLabel"] {
        font-size: 1rem;
        color: #495057;
        font-weight: 500;
    }
    
    /* サイドバーのスタイル */
    [data-testid="stSidebar"] {
        background-color: #ffffff;
        border-right: 1px solid #dee2e6;
    }
    
    /* ヘッダー */
    h1 {
        color: #0056b3;
        font-weight: 700;
        padding-bottom: 1rem;
        border-bottom: 3px solid #0056b3;
    }
    
    h2 {
        color: #495057;
        font-weight: 600;
        margin-top: 2rem;
    }
    
    h3 {
        color: #6c757d;
        font-weight: 500;
    }
</style>
""", unsafe_allow_html=True)

# ダミーデータ生成関数
@st.cache_data
def generate_clinic_data():
    """
    都心の総合内科クリニックのダミーデータを生成
    - 医師1名、1日平均60人前後
    - 6ヶ月分のデータ
    """
    np.random.seed(42)
    random.seed(42)
    
    # 6ヶ月前から今日まで
    end_date = datetime.now()
    start_date = end_date - timedelta(days=180)
    
    # 全日付を生成
    all_dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    data = []
    
    for date in all_dates:
        # 休診日の判定（日曜日、祝日想定）
        if date.weekday() == 6:  # 日曜日
            continue
        
        # 木曜日・土曜日は午前のみ（来院数少なめ）
        if date.weekday() in [3, 5]:  # 木曜日、土曜日
            base_patients = 30
        else:
            base_patients = 60
        
        # 日ごとの来院数にランダムな揺らぎ
        daily_patients = int(np.random.normal(base_patients, 10))
        daily_patients = max(20, min(80, daily_patients))  # 20〜80人の範囲
        
        # その日の患者データを生成
        for _ in range(daily_patients):
            # 初診 vs 再診（初診2:再診8）
            visit_type = np.random.choice(['初診', '再診'], p=[0.2, 0.8])
            
            # 年齢分布（都心オフィス街、働き盛りが中心）
            age_distribution = np.random.choice(
                [25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75],
                p=[0.05, 0.15, 0.20, 0.20, 0.15, 0.10, 0.08, 0.04, 0.02, 0.005, 0.005]
            )
            age = int(np.random.normal(age_distribution, 5))
            age = max(20, min(85, age))
            
            # 性別
            gender = np.random.choice(['男性', '女性'], p=[0.48, 0.52])
            
            # 保険種別（都心オフィス街なので社保が多い）
            if age >= 75:
                insurance_type = '後期高齢'
            elif age >= 65:
                insurance_type = np.random.choice(['社保', '国保', '後期高齢'], p=[0.4, 0.5, 0.1])
            else:
                insurance_type = np.random.choice(['社保', '国保'], p=[0.75, 0.25])
            
            # 売上（診療報酬点数ベース）
            if visit_type == '初診':
                # 初診は平均3,500円（2,000〜5,000円の範囲）
                revenue = int(np.random.normal(3500, 800))
                revenue = max(2000, min(5000, revenue))
            else:
                # 再診は平均1,500円（800〜2,500円の範囲）
                revenue = int(np.random.normal(1500, 400))
                revenue = max(800, min(2500, revenue))
            
            # 時間帯（9時〜18時、ピークは11時と15時）
            hour_distribution = np.random.choice(
                [9, 10, 11, 12, 14, 15, 16, 17, 18],
                p=[0.08, 0.15, 0.20, 0.12, 0.10, 0.18, 0.10, 0.05, 0.02]
            )
            
            data.append({
                'visit_date': date,
                'visit_type': visit_type,
                'age': age,
                'gender': gender,
                'insurance_type': insurance_type,
                'revenue': revenue,
                'hour': hour_distribution,
                'weekday': date.strftime('%A'),
                'weekday_jp': ['月', '火', '水', '木', '金', '土', '日'][date.weekday()]
            })
    
    df = pd.DataFrame(data)
    df['visit_date'] = pd.to_datetime(df['visit_date'])
    df['year_month'] = df['visit_date'].dt.to_period('M')
    
    return df

# データ生成
df = generate_clinic_data()

# ========================================
# サイドバー
# ========================================
st.sidebar.title("🏥 クリニック経営分析")
st.sidebar.markdown("---")

# 期間フィルター
st.sidebar.subheader("📅 表示期間")
available_months = df['year_month'].unique()
available_months_str = [str(m) for m in sorted(available_months)]

selected_months = st.sidebar.multiselect(
    "表示する月を選択",
    options=available_months_str,
    default=available_months_str[-3:]  # デフォルトは直近3ヶ月
)

if not selected_months:
    selected_months = available_months_str[-3:]

# フィルタリング
filtered_df = df[df['year_month'].astype(str).isin(selected_months)]

# サイドバーに統計情報
st.sidebar.markdown("---")
st.sidebar.subheader("📊 クリニック概要")
st.sidebar.info("""
**診療科**: 総合内科  
**所在地**: 都心オフィス街  
**医師数**: 1名（1診制）  
**営業日**: 月〜土（木・土は午前のみ）  
**休診日**: 日曜・祝日
""")

st.sidebar.markdown("---")
st.sidebar.caption("© 2025 Clinic Analytics Dashboard")

# ========================================
# メインエリア
# ========================================
st.title("🏥 クリニック経営分析ダッシュボード")
st.markdown(f"**表示期間**: {', '.join(selected_months)}")
st.markdown("---")

# ========================================
# 1. トップKPI指標
# ========================================
st.subheader("📈 主要指標（KPI）")

# 営業日数の計算
operating_days = filtered_df['visit_date'].nunique()

# KPI計算
total_visits = len(filtered_df)
avg_daily_visits = total_visits / operating_days if operating_days > 0 else 0
first_visit_rate = (filtered_df['visit_type'] == '初診').sum() / total_visits * 100 if total_visits > 0 else 0
total_revenue = filtered_df['revenue'].sum()

# メトリクス表示（4列）
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="📊 総来院数",
        value=f"{total_visits:,}人",
        delta=f"{operating_days}営業日"
    )

with col2:
    st.metric(
        label="👥 1日平均来院数",
        value=f"{avg_daily_visits:.1f}人",
        delta="目標: 60人"
    )

with col3:
    st.metric(
        label="🆕 初診率",
        value=f"{first_visit_rate:.1f}%",
        delta="理想: 15-20%"
    )

with col4:
    st.metric(
        label="💰 概算総売上",
        value=f"¥{total_revenue:,.0f}",
        delta=f"¥{total_revenue/operating_days:,.0f}/日"
    )

st.markdown("---")

# ========================================
# 2. グラフエリア
# ========================================

# ========================================
# 2-1. 日次来院数推移（初診・再診の積み上げ）
# ========================================
st.subheader("📅 日次来院数推移")

# 日付ごとに初診・再診を集計
daily_visits = filtered_df.groupby(['visit_date', 'visit_type']).size().reset_index(name='count')
daily_visits_pivot = daily_visits.pivot(index='visit_date', columns='visit_type', values='count').fillna(0)

# Plotlyで積み上げ棒グラフ
fig_daily = go.Figure()

fig_daily.add_trace(go.Bar(
    x=daily_visits_pivot.index,
    y=daily_visits_pivot['再診'] if '再診' in daily_visits_pivot.columns else [],
    name='再診',
    marker_color='#4ECDC4'
))

fig_daily.add_trace(go.Bar(
    x=daily_visits_pivot.index,
    y=daily_visits_pivot['初診'] if '初診' in daily_visits_pivot.columns else [],
    name='初診',
    marker_color='#FF6B6B'
))

fig_daily.update_layout(
    barmode='stack',
    title='日次来院数（初診 vs 再診）',
    xaxis_title='日付',
    yaxis_title='来院数（人）',
    hovermode='x unified',
    template='plotly_white',
    height=400
)

st.plotly_chart(fig_daily, use_container_width=True)

# ========================================
# 2-2. 曜日別・時間帯別の混雑傾向
# ========================================
st.subheader("🕐 曜日別・時間帯別の混雑傾向")

col1, col2 = st.columns(2)

with col1:
    # 曜日別来院数
    weekday_order = ['月', '火', '水', '木', '金', '土']
    weekday_visits = filtered_df.groupby('weekday_jp').size().reset_index(name='count')
    weekday_visits['weekday_jp'] = pd.Categorical(weekday_visits['weekday_jp'], categories=weekday_order, ordered=True)
    weekday_visits = weekday_visits.sort_values('weekday_jp')
    
    fig_weekday = px.bar(
        weekday_visits,
        x='weekday_jp',
        y='count',
        title='曜日別来院数',
        labels={'weekday_jp': '曜日', 'count': '来院数（人）'},
        color='count',
        color_continuous_scale='Blues',
        text='count'
    )
    
    fig_weekday.update_traces(texttemplate='%{text}人', textposition='outside')
    fig_weekday.update_layout(
        template='plotly_white',
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig_weekday, use_container_width=True)

with col2:
    # 時間帯別来院数
    hour_visits = filtered_df.groupby('hour').size().reset_index(name='count')
    hour_visits = hour_visits.sort_values('hour')
    
    fig_hour = px.bar(
        hour_visits,
        x='hour',
        y='count',
        title='時間帯別来院数',
        labels={'hour': '時間帯', 'count': '来院数（人）'},
        color='count',
        color_continuous_scale='Greens',
        text='count'
    )
    
    fig_hour.update_traces(texttemplate='%{text}人', textposition='outside')
    fig_hour.update_layout(
        template='plotly_white',
        showlegend=False,
        height=400,
        xaxis=dict(tickmode='linear', tick0=9, dtick=1)
    )
    
    st.plotly_chart(fig_hour, use_container_width=True)

# ========================================
# 2-3. 患者属性分析
# ========================================
st.subheader("👥 患者属性分析")

col1, col2 = st.columns(2)

with col1:
    # 年齢階層別分布
    age_bins = [0, 30, 40, 50, 60, 70, 100]
    age_labels = ['20代', '30代', '40代', '50代', '60代', '70代以上']
    filtered_df['age_group'] = pd.cut(filtered_df['age'], bins=age_bins, labels=age_labels, right=False)
    
    age_dist = filtered_df['age_group'].value_counts().sort_index().reset_index()
    age_dist.columns = ['age_group', 'count']
    
    fig_age = px.bar(
        age_dist,
        x='age_group',
        y='count',
        title='年齢階層別来院数',
        labels={'age_group': '年齢層', 'count': '来院数（人）'},
        color='count',
        color_continuous_scale='Purples',
        text='count'
    )
    
    fig_age.update_traces(texttemplate='%{text}人', textposition='outside')
    fig_age.update_layout(
        template='plotly_white',
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig_age, use_container_width=True)

with col2:
    # 保険種別分布
    insurance_dist = filtered_df['insurance_type'].value_counts().reset_index()
    insurance_dist.columns = ['insurance_type', 'count']
    
    fig_insurance = px.pie(
        insurance_dist,
        names='insurance_type',
        values='count',
        title='保険種別の割合',
        color_discrete_sequence=['#0056b3', '#4ECDC4', '#FF6B6B'],
        hole=0.4
    )
    
    fig_insurance.update_traces(textposition='inside', textinfo='percent+label')
    fig_insurance.update_layout(
        template='plotly_white',
        height=400
    )
    
    st.plotly_chart(fig_insurance, use_container_width=True)

# ========================================
# 3. 売上分析
# ========================================
st.markdown("---")
st.subheader("💰 売上分析")

col1, col2 = st.columns(2)

with col1:
    # 日次売上推移
    daily_revenue = filtered_df.groupby('visit_date')['revenue'].sum().reset_index()
    
    fig_revenue = px.line(
        daily_revenue,
        x='visit_date',
        y='revenue',
        title='日次売上推移',
        labels={'visit_date': '日付', 'revenue': '売上（円）'},
        markers=True
    )
    
    fig_revenue.update_traces(line_color='#0056b3', line_width=2)
    fig_revenue.update_layout(
        template='plotly_white',
        height=400
    )
    
    st.plotly_chart(fig_revenue, use_container_width=True)

with col2:
    # 初診 vs 再診の売上比較
    revenue_by_type = filtered_df.groupby('visit_type')['revenue'].sum().reset_index()
    
    fig_revenue_type = px.bar(
        revenue_by_type,
        x='visit_type',
        y='revenue',
        title='初診 vs 再診の売上比較',
        labels={'visit_type': '来院タイプ', 'revenue': '売上（円）'},
        color='visit_type',
        color_discrete_map={'初診': '#FF6B6B', '再診': '#4ECDC4'},
        text='revenue'
    )
    
    fig_revenue_type.update_traces(texttemplate='¥%{text:,.0f}', textposition='outside')
    fig_revenue_type.update_layout(
        template='plotly_white',
        showlegend=False,
        height=400
    )
    
    st.plotly_chart(fig_revenue_type, use_container_width=True)

# ========================================
# 4. データテーブル（エキスパンダー）
# ========================================
st.markdown("---")
with st.expander("📋 詳細データテーブル"):
    st.dataframe(
        filtered_df[['visit_date', 'visit_type', 'age', 'gender', 'insurance_type', 'revenue', 'weekday_jp', 'hour']]
        .sort_values('visit_date', ascending=False)
        .head(100),
        use_container_width=True
    )
    
    st.download_button(
        label="📥 CSVダウンロード",
        data=filtered_df.to_csv(index=False).encode('utf-8-sig'),
        file_name=f"clinic_data_{datetime.now().strftime('%Y%m%d')}.csv",
        mime="text/csv"
    )

# ========================================
# フッター
# ========================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #6c757d; padding: 2rem;'>
    <p><strong>🏥 クリニック経営分析ダッシュボード</strong></p>
    <p>Developed with Streamlit × Plotly | AI駆動開発</p>
</div>
""", unsafe_allow_html=True)
