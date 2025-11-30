"""
Metro Central Internal Medicine - Executive Dashboard
Commercial Grade | Streamlit Application
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime, timedelta
from dataclasses import dataclass

# ============================================================
# 1. CONFIG & STYLE
# ============================================================

@dataclass
class ColorPalette:
    """Medical Pro Design System"""
    BACKGROUND = "#F4F6F9"
    CARD_SURFACE = "#FFFFFF"
    PRIMARY = "#0EA5E9"
    SECONDARY = "#64748B"
    ACCENT = "#F43F5E"
    TEXT = "#1E293B"
    GRID = "#E2E8F0"
    SUCCESS = "#10B981"
    WARNING = "#F59E0B"

COLOR = ColorPalette()

# Page Configuration
st.set_page_config(
    page_title="Metro Central Internal Medicine",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS Injection
st.markdown(f"""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
    
    /* Base Overrides */
    .stApp {{
        background-color: {COLOR.BACKGROUND} !important;
        font-family: 'Inter', 'Noto Sans JP', sans-serif !important;
    }}
    
    .css-1d391kg, .main .block-container {{
        padding: 2rem 3rem !important;
        max-width: 100% !important;
    }}
    
    /* Hide Streamlit Branding */
    #MainMenu {{visibility: hidden;}}
    footer {{visibility: hidden;}}
    header {{visibility: hidden;}}
    
    /* Custom KPI Card */
    .kpi-card {{
        background: {COLOR.CARD_SURFACE};
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        height: 100%;
    }}
    
    .kpi-card:hover {{
        transform: translateY(-2px);
        box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
    }}
    
    .kpi-icon {{
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }}
    
    .kpi-label {{
        color: {COLOR.SECONDARY};
        font-size: 0.875rem;
        font-weight: 500;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        margin-bottom: 0.5rem;
    }}
    
    .kpi-value {{
        color: {COLOR.TEXT};
        font-size: 2rem;
        font-weight: 700;
        line-height: 1.2;
        margin-bottom: 0.5rem;
    }}
    
    .kpi-delta {{
        font-size: 0.875rem;
        font-weight: 600;
        display: flex;
        align-items: center;
        gap: 0.25rem;
    }}
    
    .kpi-delta.positive {{
        color: {COLOR.SUCCESS};
    }}
    
    .kpi-delta.negative {{
        color: {COLOR.ACCENT};
    }}
    
    /* Header Styles */
    .dashboard-header {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 2rem;
        padding-bottom: 1rem;
        border-bottom: 2px solid {COLOR.PRIMARY};
    }}
    
    .clinic-title {{
        color: {COLOR.TEXT};
        font-size: 2rem;
        font-weight: 700;
        margin: 0;
    }}
    
    .last-updated {{
        color: {COLOR.SECONDARY};
        font-size: 0.875rem;
        font-weight: 500;
    }}
    
    /* Graph Container */
    .graph-container {{
        background: {COLOR.CARD_SURFACE};
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
        margin-bottom: 1.5rem;
    }}
    
    /* Remove default margins */
    .element-container {{
        margin: 0 !important;
    }}
</style>
""", unsafe_allow_html=True)

# ============================================================
# 2. DATA MANAGER
# ============================================================

class DataManager:
    """Encapsulates all data generation and aggregation logic"""
    
    def __init__(self, months_back: int = 6, seed: int = 42):
        self.months_back = months_back
        np.random.seed(seed)
        self.data = self._generate_data()
        
    def _generate_data(self) -> pd.DataFrame:
        """Generate realistic clinic data with sophisticated logic"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30 * self.months_back)
        
        date_range = pd.date_range(start=start_date, end=end_date, freq='D')
        records = []
        
        for date in date_range:
            # Skip Sundays
            if date.weekday() == 6:
                continue
            
            # Base patient count (Poisson distribution λ=60)
            base_lambda = 60
            
            # Weekday coefficient
            weekday = date.weekday()
            if weekday == 0:  # Monday
                weekday_coef = 1.2
            elif weekday in [3, 5]:  # Thursday, Saturday
                weekday_coef = 0.6
            else:
                weekday_coef = 1.0
            
            # Random "rainy day" effect (5% chance)
            is_rainy = np.random.random() < 0.05
            rain_coef = 0.8 if is_rainy else 1.0
            
            # Seasonal effect (winter boost for acute cases)
            month = date.month
            seasonal_coef = 1.5 if month in [12, 1, 2] else 1.0
            
            # Final patient count
            adjusted_lambda = base_lambda * weekday_coef * rain_coef
            daily_patients = int(np.random.poisson(adjusted_lambda))
            daily_patients = max(10, min(100, daily_patients))
            
            # Generate individual patient records
            for i in range(daily_patients):
                # Patient segment (Case Mix)
                segment = np.random.choice(
                    ['lifestyle', 'acute', 'checkup'],
                    p=[0.4, 0.5, 0.1]
                )
                
                # Adjust acute cases for winter
                if segment == 'acute' and month in [12, 1, 2]:
                    segment = 'acute' if np.random.random() < 0.75 else segment
                
                # Revenue based on segment
                if segment == 'lifestyle':
                    revenue = int(np.random.normal(5000, 1000))
                    revenue = max(3000, min(8000, revenue))
                    visit_type = '再診' if np.random.random() < 0.9 else '初診'
                elif segment == 'acute':
                    revenue = int(np.random.normal(2500, 500))
                    revenue = max(1500, min(4000, revenue))
                    visit_type = '初診' if np.random.random() < 0.4 else '再診'
                else:  # checkup
                    revenue = int(np.random.normal(15000, 2000))
                    revenue = max(10000, min(20000, revenue))
                    visit_type = '検診'
                    # Checkups concentrate on Saturday
                    if weekday != 5:
                        continue
                
                # Age distribution by segment
                if segment == 'lifestyle':
                    age = int(np.random.normal(55, 10))
                elif segment == 'acute':
                    age = int(np.random.normal(38, 15))
                else:  # checkup
                    age = int(np.random.normal(45, 8))
                age = max(20, min(85, age))
                
                # Gender
                gender = np.random.choice(['男性', '女性'], p=[0.48, 0.52])
                
                # Visit hour distribution
                hour = np.random.choice(
                    [9, 10, 11, 12, 14, 15, 16, 17],
                    p=[0.08, 0.15, 0.22, 0.10, 0.12, 0.20, 0.10, 0.03]
                )
                
                records.append({
                    'date': date,
                    'segment': segment,
                    'visit_type': visit_type,
                    'age': age,
                    'gender': gender,
                    'revenue': revenue,
                    'hour': hour,
                    'weekday': weekday,
                    'is_rainy': is_rainy
                })
        
        df = pd.DataFrame(records)
        df['date'] = pd.to_datetime(df['date'])
        
        # Calculate wait time (exponential relationship with patient count)
        daily_counts = df.groupby('date').size()
        physician_capacity = 60
        df['wait_time'] = df['date'].map(
            lambda d: int(((daily_counts.get(d, 0) / physician_capacity) ** 2) * 30)
        )
        df['wait_time'] = df['wait_time'].clip(5, 120)  # 5-120 minutes
        
        return df
    
    def get_monthly_summary(self, target_month: pd.Period) -> dict:
        """Calculate monthly KPIs"""
        df_month = self.data[self.data['date'].dt.to_period('M') == target_month]
        
        # Previous month for comparison
        prev_month = target_month - 1
        df_prev = self.data[self.data['date'].dt.to_period('M') == prev_month]
        
        total_revenue = df_month['revenue'].sum()
        prev_revenue = df_prev['revenue'].sum()
        revenue_delta = ((total_revenue - prev_revenue) / prev_revenue * 100) if prev_revenue > 0 else 0
        
        total_visits = len(df_month)
        prev_visits = len(df_prev)
        visits_delta = ((total_visits - prev_visits) / prev_visits * 100) if prev_visits > 0 else 0
        
        avg_wait = df_month['wait_time'].mean()
        prev_wait = df_prev['wait_time'].mean()
        wait_delta = ((avg_wait - prev_wait) / prev_wait * 100) if prev_wait > 0 else 0
        
        first_visit_rate = (df_month['visit_type'] == '初診').sum() / total_visits * 100 if total_visits > 0 else 0
        prev_first_rate = (df_prev['visit_type'] == '初診').sum() / prev_visits * 100 if prev_visits > 0 else 0
        first_delta = first_visit_rate - prev_first_rate
        
        return {
            'revenue': {'value': total_revenue, 'delta': revenue_delta},
            'visits': {'value': total_visits, 'delta': visits_delta},
            'wait_time': {'value': avg_wait, 'delta': wait_delta},
            'first_rate': {'value': first_visit_rate, 'delta': first_delta}
        }
    
    def get_daily_trend(self, target_month: pd.Period) -> pd.DataFrame:
        """Get daily revenue and visit trends"""
        df_month = self.data[self.data['date'].dt.to_period('M') == target_month]
        
        daily = df_month.groupby('date').agg({
            'revenue': 'sum',
            'date': 'count'
        }).rename(columns={'date': 'visits'})
        
        return daily.reset_index()
    
    def get_heatmap_data(self, target_month: pd.Period) -> pd.DataFrame:
        """Get congestion heatmap (weekday × hour)"""
        df_month = self.data[self.data['date'].dt.to_period('M') == target_month]
        
        heatmap = df_month.groupby(['weekday', 'hour']).size().reset_index(name='count')
        heatmap_pivot = heatmap.pivot(index='hour', columns='weekday', values='count').fillna(0)
        
        return heatmap_pivot
    
    def get_segment_distribution(self, target_month: pd.Period) -> pd.DataFrame:
        """Get patient segment distribution"""
        df_month = self.data[self.data['date'].dt.to_period('M') == target_month]
        
        segment_map = {
            'lifestyle': '生活習慣病',
            'acute': '急性疾患',
            'checkup': '検診・ドック'
        }
        
        dist = df_month['segment'].value_counts().reset_index()
        dist.columns = ['segment', 'count']
        dist['segment'] = dist['segment'].map(segment_map)
        
        return dist
    
    def get_age_distribution(self, target_month: pd.Period) -> pd.DataFrame:
        """Get age distribution"""
        df_month = self.data[self.data['date'].dt.to_period('M') == target_month]
        
        return df_month[['age']]

# ============================================================
# 3. DASHBOARD UI
# ============================================================

def render_header():
    """Render dashboard header"""
    st.markdown(f"""
    <div class="dashboard-header">
        <h2 class="clinic-title">🏥 Metro Central Internal Medicine</h2>
        <div class="last-updated">最終データ更新: {datetime.now().strftime('%Y年%m月%d日 %H:%M')}</div>
    </div>
    """, unsafe_allow_html=True)

def render_kpi_card(icon: str, label: str, value: str, delta: float, inverse: bool = False):
    """Render custom KPI card with HTML/CSS"""
    delta_class = "negative" if (delta < 0 and not inverse) or (delta > 0 and inverse) else "positive"
    delta_arrow = "↓" if delta < 0 else "↑"
    delta_text = f"{abs(delta):.1f}%" if delta != 0 else "0%"
    
    return f"""
    <div class="kpi-card">
        <div class="kpi-icon">{icon}</div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-delta {delta_class}">
            <span>{delta_arrow}</span>
            <span>{delta_text} vs 前月</span>
        </div>
    </div>
    """

def configure_plotly_layout(fig: go.Figure, title: str = None) -> go.Figure:
    """Apply consistent Plotly styling"""
    fig.update_layout(
        title=dict(
            text=title,
            font=dict(size=18, weight=600, color=COLOR.TEXT, family="Inter, Noto Sans JP, sans-serif"),
            x=0,
            xanchor='left'
        ) if title else None,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font=dict(family="Inter, Noto Sans JP, sans-serif", color=COLOR.TEXT),
        margin=dict(t=60 if title else 30, b=30, l=30, r=30),
        hovermode='x unified',
        xaxis=dict(
            showgrid=False,
            showline=True,
            linecolor=COLOR.GRID,
            linewidth=1
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor=COLOR.GRID,
            gridwidth=1,
            showline=False
        ),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        )
    )
    return fig

def render_dual_axis_chart(daily_data: pd.DataFrame):
    """Render revenue & visits dual-axis chart"""
    fig = go.Figure()
    
    # Bar chart for visits
    fig.add_trace(go.Bar(
        x=daily_data['date'],
        y=daily_data['visits'],
        name='来院数',
        marker_color=COLOR.PRIMARY,
        opacity=0.3,
        yaxis='y',
        hovertemplate='%{y}人<extra></extra>'
    ))
    
    # Line chart for revenue
    fig.add_trace(go.Scatter(
        x=daily_data['date'],
        y=daily_data['revenue'],
        name='売上',
        mode='lines+markers',
        line=dict(color=COLOR.PRIMARY, width=3),
        marker=dict(size=6),
        yaxis='y2',
        hovertemplate='¥%{y:,.0f}<extra></extra>'
    ))
    
    fig.update_layout(
        yaxis=dict(
            title='来院数（人）',
            side='left',
            showgrid=True,
            gridcolor=COLOR.GRID
        ),
        yaxis2=dict(
            title='売上（円）',
            overlaying='y',
            side='right',
            showgrid=False
        ),
        hovermode='x unified'
    )
    
    fig = configure_plotly_layout(fig, title="売上 & 来院数トレンド")
    
    return fig

def render_heatmap(heatmap_data: pd.DataFrame):
    """Render congestion heatmap"""
    weekday_labels = ['月', '火', '水', '木', '金', '土']
    
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=[weekday_labels[i] for i in heatmap_data.columns],
        y=[f"{h}:00" for h in heatmap_data.index],
        colorscale='Blues',
        showscale=True,
        hovertemplate='%{x} %{y}<br>来院数: %{z}人<extra></extra>'
    ))
    
    fig = configure_plotly_layout(fig, title="混雑ヒートマップ")
    fig.update_xaxes(side='top')
    
    return fig

def render_donut_chart(segment_data: pd.DataFrame):
    """Render disease segment donut chart"""
    fig = go.Figure(data=[go.Pie(
        labels=segment_data['segment'],
        values=segment_data['count'],
        hole=0.5,
        marker=dict(colors=[COLOR.PRIMARY, COLOR.SECONDARY, COLOR.ACCENT]),
        textinfo='label+percent',
        textposition='outside',
        hovertemplate='%{label}<br>%{value}人 (%{percent})<extra></extra>'
    )])
    
    fig = configure_plotly_layout(fig, title="疾患別構成比")
    
    return fig

def render_age_histogram(age_data: pd.DataFrame):
    """Render age distribution histogram"""
    fig = go.Figure(data=[go.Histogram(
        x=age_data['age'],
        nbinsx=13,
        marker_color=COLOR.PRIMARY,
        opacity=0.7,
        hovertemplate='年齢: %{x}<br>人数: %{y}<extra></extra>'
    )])
    
    fig.update_xaxes(title='年齢')
    fig.update_yaxes(title='来院数（人）')
    
    fig = configure_plotly_layout(fig, title="年齢分布")
    
    return fig

# ============================================================
# 4. MAIN APPLICATION
# ============================================================

def main():
    # Initialize Data Manager
    dm = DataManager(months_back=6)
    
    # Current month
    current_month = pd.Period(datetime.now(), freq='M')
    
    # Get KPIs
    kpis = dm.get_monthly_summary(current_month)
    
    # Render Header
    render_header()
    
    # ========== ROW 1: Executive KPI Cards ==========
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(
            render_kpi_card(
                "💰",
                "今月の売上",
                f"¥{kpis['revenue']['value']:,.0f}",
                kpis['revenue']['delta']
            ),
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            render_kpi_card(
                "👥",
                "来院数",
                f"{kpis['visits']['value']:,}人",
                kpis['visits']['delta']
            ),
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            render_kpi_card(
                "⏱️",
                "平均待ち時間",
                f"{kpis['wait_time']['value']:.0f}分",
                kpis['wait_time']['delta'],
                inverse=True  # Lower is better
            ),
            unsafe_allow_html=True
        )
    
    with col4:
        st.markdown(
            render_kpi_card(
                "🆕",
                "初診率",
                f"{kpis['first_rate']['value']:.1f}%",
                kpis['first_rate']['delta']
            ),
            unsafe_allow_html=True
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ========== ROW 2: Trends & Operations ==========
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        daily_trend = dm.get_daily_trend(current_month)
        fig_dual = render_dual_axis_chart(daily_trend)
        st.markdown('<div class="graph-container">', unsafe_allow_html=True)
        st.plotly_chart(fig_dual, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_right:
        heatmap_data = dm.get_heatmap_data(current_month)
        fig_heatmap = render_heatmap(heatmap_data)
        st.markdown('<div class="graph-container">', unsafe_allow_html=True)
        st.plotly_chart(fig_heatmap, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ========== ROW 3: Patient Insights ==========
    col_left, col_right = st.columns(2)
    
    with col_left:
        segment_data = dm.get_segment_distribution(current_month)
        fig_donut = render_donut_chart(segment_data)
        st.markdown('<div class="graph-container">', unsafe_allow_html=True)
        st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_right:
        age_data = dm.get_age_distribution(current_month)
        fig_age = render_age_histogram(age_data)
        st.markdown('<div class="graph-container">', unsafe_allow_html=True)
        st.plotly_chart(fig_age, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
