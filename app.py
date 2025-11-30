"""
Metro Central Internal Medicine - Executive Dashboard
God Tier UI/UX | $10M+ Commercial Grade
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
from dataclasses import dataclass

# ============================================================
# 1. CONFIGURATION & DESIGN SYSTEM
# ============================================================

@dataclass
class ColorSystem:
    """Sophisticated Color Palette - Inspired by Tailwind CSS"""
    # Backgrounds
    BG_PRIMARY = "#F1F5F9"      # Slate-100
    BG_SURFACE = "#FFFFFF"      # Pure White
    
    # Brand Colors
    BRAND_PRIMARY = "#0EA5E9"   # Sky-500
    BRAND_SECONDARY = "#3B82F6" # Blue-500
    BRAND_ACCENT = "#8B5CF6"    # Violet-500
    
    # Text Colors
    TEXT_PRIMARY = "#0F172A"    # Slate-900
    TEXT_SECONDARY = "#475569"  # Slate-600
    TEXT_MUTED = "#94A3B8"      # Slate-400
    
    # Status Colors
    SUCCESS = "#10B981"         # Emerald-500
    WARNING = "#F59E0B"         # Amber-500
    DANGER = "#EF4444"          # Red-500
    
    # Chart Colors
    CHART_1 = "#0EA5E9"         # Sky-500
    CHART_2 = "#8B5CF6"         # Violet-500
    CHART_3 = "#EC4899"         # Pink-500
    CHART_4 = "#F59E0B"         # Amber-500
    
    # Utilities
    BORDER = "#E2E8F0"          # Slate-200
    SHADOW = "rgba(15, 23, 42, 0.1)"

COLOR = ColorSystem()

# Page Configuration
st.set_page_config(
    page_title="Metro Central Internal Medicine | Executive Dashboard",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# 2. GOD TIER CSS & TYPOGRAPHY INJECTION
# ============================================================

def inject_god_tier_styles():
    """Inject sophisticated CSS that transforms Streamlit into a premium web app"""
    
    st.markdown("""
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Noto+Sans+JP:wght@400;500;600;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """, unsafe_allow_html=True)
    
    st.markdown(f"""
    <style>
        /* ====================================
           GLOBAL RESET & BASE STYLES
           ==================================== */
        
        * {{
            font-family: 'Inter', 'Noto Sans JP', -apple-system, BlinkMacSystemFont, sans-serif !important;
        }}
        
        .stApp {{
            background: {COLOR.BG_PRIMARY} !important;
        }}
        
        /* Remove Streamlit Branding & Padding */
        #MainMenu {{visibility: hidden !important;}}
        footer {{visibility: hidden !important;}}
        header {{visibility: hidden !important;}}
        .stDeployButton {{display: none !important;}}
        
        .main .block-container {{
            padding: 2rem 3rem !important;
            max-width: 100% !important;
        }}
        
        /* ====================================
           UTILITY CLASSES (Tailwind-inspired)
           ==================================== */
        
        .card-base {{
            background: {COLOR.BG_SURFACE};
            border-radius: 16px;
            box-shadow: 0 10px 15px -3px {COLOR.SHADOW}, 0 4px 6px -2px {COLOR.SHADOW};
            padding: 28px;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            border: 1px solid {COLOR.BORDER};
            position: relative;
            overflow: hidden;
        }}
        
        .card-base:hover {{
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px {COLOR.SHADOW}, 0 10px 10px -5px {COLOR.SHADOW};
        }}
        
        .card-base::before {{
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            right: 0;
            height: 4px;
            background: linear-gradient(90deg, {COLOR.BRAND_PRIMARY} 0%, {COLOR.BRAND_ACCENT} 100%);
            opacity: 0;
            transition: opacity 0.3s ease;
        }}
        
        .card-base:hover::before {{
            opacity: 1;
        }}
        
        /* ====================================
           TYPOGRAPHY SYSTEM
           ==================================== */
        
        .text-slate-900 {{ color: {COLOR.TEXT_PRIMARY}; }}
        .text-slate-600 {{ color: {COLOR.TEXT_SECONDARY}; }}
        .text-slate-400 {{ color: {COLOR.TEXT_MUTED}; }}
        
        .font-bold {{ font-weight: 700; }}
        .font-semibold {{ font-weight: 600; }}
        .font-medium {{ font-weight: 500; }}
        
        .text-xs {{ font-size: 0.75rem; line-height: 1rem; }}
        .text-sm {{ font-size: 0.875rem; line-height: 1.25rem; }}
        .text-base {{ font-size: 1rem; line-height: 1.5rem; }}
        .text-lg {{ font-size: 1.125rem; line-height: 1.75rem; }}
        .text-xl {{ font-size: 1.25rem; line-height: 1.75rem; }}
        .text-2xl {{ font-size: 1.5rem; line-height: 2rem; }}
        .text-3xl {{ font-size: 1.875rem; line-height: 2.25rem; }}
        .text-4xl {{ font-size: 2.25rem; line-height: 2.5rem; }}
        
        .uppercase {{ text-transform: uppercase; }}
        .tracking-wide {{ letter-spacing: 0.025em; }}
        .tracking-wider {{ letter-spacing: 0.05em; }}
        
        /* ====================================
           HEADER COMPONENT
           ==================================== */
        
        .dashboard-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 3rem;
            padding: 2rem;
            background: {COLOR.BG_SURFACE};
            border-radius: 16px;
            box-shadow: 0 4px 6px -1px {COLOR.SHADOW};
            border-left: 6px solid {COLOR.BRAND_PRIMARY};
        }}
        
        .clinic-logo {{
            display: flex;
            align-items: center;
            gap: 1rem;
        }}
        
        .clinic-icon {{
            font-size: 2.5rem;
            background: linear-gradient(135deg, {COLOR.BRAND_PRIMARY} 0%, {COLOR.BRAND_ACCENT} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .clinic-title {{
            font-size: 1.875rem;
            font-weight: 800;
            color: {COLOR.TEXT_PRIMARY};
            margin: 0;
            line-height: 1.2;
        }}
        
        .clinic-subtitle {{
            font-size: 0.875rem;
            color: {COLOR.TEXT_SECONDARY};
            margin-top: 0.25rem;
            font-weight: 500;
        }}
        
        .last-updated {{
            text-align: right;
        }}
        
        .last-updated-label {{
            font-size: 0.75rem;
            color: {COLOR.TEXT_MUTED};
            text-transform: uppercase;
            letter-spacing: 0.05em;
            font-weight: 600;
        }}
        
        .last-updated-time {{
            font-size: 1rem;
            color: {COLOR.TEXT_SECONDARY};
            font-weight: 600;
            margin-top: 0.25rem;
        }}
        
        /* ====================================
           KPI CARD COMPONENT
           ==================================== */
        
        .kpi-card {{
            background: {COLOR.BG_SURFACE};
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 10px 15px -3px {COLOR.SHADOW}, 0 4px 6px -2px {COLOR.SHADOW};
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            position: relative;
            overflow: hidden;
            border: 1px solid {COLOR.BORDER};
            height: 100%;
        }}
        
        .kpi-card:hover {{
            transform: translateY(-6px) scale(1.02);
            box-shadow: 0 25px 50px -12px {COLOR.SHADOW};
        }}
        
        .kpi-card::after {{
            content: '';
            position: absolute;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            background: linear-gradient(135deg, transparent 0%, {COLOR.BRAND_PRIMARY}08 100%);
            opacity: 0;
            transition: opacity 0.3s ease;
            pointer-events: none;
        }}
        
        .kpi-card:hover::after {{
            opacity: 1;
        }}
        
        .kpi-icon-wrapper {{
            width: 56px;
            height: 56px;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            margin-bottom: 1.25rem;
            font-size: 1.75rem;
            transition: all 0.3s ease;
        }}
        
        .kpi-card:hover .kpi-icon-wrapper {{
            transform: scale(1.1) rotate(5deg);
        }}
        
        .kpi-label {{
            font-size: 0.875rem;
            color: {COLOR.TEXT_SECONDARY};
            font-weight: 600;
            text-transform: uppercase;
            letter-spacing: 0.05em;
            margin-bottom: 0.75rem;
        }}
        
        .kpi-value {{
            font-family: 'Inter', sans-serif;
            font-size: 2.5rem;
            font-weight: 800;
            color: {COLOR.TEXT_PRIMARY};
            line-height: 1.2;
            margin-bottom: 1rem;
            background: linear-gradient(135deg, {COLOR.TEXT_PRIMARY} 0%, {COLOR.TEXT_SECONDARY} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
        }}
        
        .kpi-delta-container {{
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }}
        
        .trend-badge {{
            display: inline-flex;
            align-items: center;
            gap: 0.375rem;
            padding: 0.375rem 0.75rem;
            border-radius: 9999px;
            font-size: 0.875rem;
            font-weight: 700;
            transition: all 0.2s ease;
        }}
        
        .trend-badge.positive {{
            background: {COLOR.SUCCESS}20;
            color: {COLOR.SUCCESS};
        }}
        
        .trend-badge.negative {{
            background: {COLOR.DANGER}20;
            color: {COLOR.DANGER};
        }}
        
        .trend-badge:hover {{
            transform: scale(1.05);
        }}
        
        .trend-arrow {{
            font-size: 0.75rem;
            font-weight: 900;
        }}
        
        .vs-label {{
            font-size: 0.75rem;
            color: {COLOR.TEXT_MUTED};
            font-weight: 500;
        }}
        
        /* ====================================
           GRAPH CONTAINER
           ==================================== */
        
        .graph-container {{
            background: {COLOR.BG_SURFACE};
            border-radius: 16px;
            padding: 2rem;
            box-shadow: 0 10px 15px -3px {COLOR.SHADOW}, 0 4px 6px -2px {COLOR.SHADOW};
            border: 1px solid {COLOR.BORDER};
            margin-bottom: 2rem;
            transition: all 0.3s ease;
        }}
        
        .graph-container:hover {{
            box-shadow: 0 20px 25px -5px {COLOR.SHADOW}, 0 10px 10px -5px {COLOR.SHADOW};
        }}
        
        .graph-title {{
            font-size: 1.25rem;
            font-weight: 700;
            color: {COLOR.TEXT_PRIMARY};
            margin-bottom: 1.5rem;
            display: flex;
            align-items: center;
            gap: 0.75rem;
        }}
        
        .graph-title i {{
            color: {COLOR.BRAND_PRIMARY};
        }}
        
        /* ====================================
           ANIMATIONS
           ==================================== */
        
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(20px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        .animate-fade-in-up {{
            animation: fadeInUp 0.6s ease-out forwards;
        }}
        
        @keyframes pulse {{
            0%, 100% {{
                opacity: 1;
            }}
            50% {{
                opacity: 0.8;
            }}
        }}
        
        .animate-pulse {{
            animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
        }}
        
        /* ====================================
           RESPONSIVE DESIGN
           ==================================== */
        
        @media (max-width: 768px) {{
            .dashboard-header {{
                flex-direction: column;
                gap: 1rem;
                text-align: center;
            }}
            
            .kpi-value {{
                font-size: 2rem;
            }}
        }}
    </style>
    """, unsafe_allow_html=True)

# ============================================================
# 3. DATA MANAGER (Business Logic)
# ============================================================

class DataManager:
    """Sophisticated data generation with realistic medical practice patterns"""
    
    def __init__(self, months_back: int = 6, seed: int = 42):
        self.months_back = months_back
        np.random.seed(seed)
        self.data = self._generate_realistic_data()
    
    def _generate_realistic_data(self) -> pd.DataFrame:
        """Generate highly realistic clinic data with complex patterns"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=30 * self.months_back)
        
        date_range = pd.date_range(start=start_date, end=end_date, freq='D')
        records = []
        
        for date in date_range:
            if date.weekday() == 6:  # Skip Sundays
                continue
            
            # Base patient count with Poisson distribution
            base_lambda = 60
            
            # Monday rush (1.2x), Thu/Sat half-day (0.6x)
            weekday_coef = {0: 1.2, 3: 0.6, 5: 0.6}.get(date.weekday(), 1.0)
            
            # Random rainy day (5% chance, 0.8x patients)
            rain_coef = 0.8 if np.random.random() < 0.05 else 1.0
            
            # Seasonal effect (winter: +50% acute cases)
            seasonal_boost = 1.5 if date.month in [12, 1, 2] else 1.0
            
            adjusted_lambda = base_lambda * weekday_coef * rain_coef
            daily_patients = int(np.random.poisson(adjusted_lambda))
            daily_patients = max(15, min(95, daily_patients))
            
            for _ in range(daily_patients):
                # Patient segment (Case Mix)
                segment_prob = [0.4, 0.5, 0.1]
                if date.month in [12, 1, 2]:  # Winter: more acute cases
                    segment_prob = [0.35, 0.6, 0.05]
                
                segment = np.random.choice(['lifestyle', 'acute', 'checkup'], p=segment_prob)
                
                # Revenue & visit type by segment
                if segment == 'lifestyle':
                    revenue = int(np.random.normal(5000, 1200))
                    revenue = max(3000, min(9000, revenue))
                    visit_type = '再診' if np.random.random() < 0.85 else '初診'
                elif segment == 'acute':
                    revenue = int(np.random.normal(2800, 600))
                    revenue = max(1800, min(5000, revenue))
                    visit_type = '初診' if np.random.random() < 0.35 else '再診'
                else:  # checkup
                    if date.weekday() != 5:  # Checkups mostly on Saturday
                        continue
                    revenue = int(np.random.normal(16000, 2500))
                    revenue = max(12000, min(22000, revenue))
                    visit_type = '検診'
                
                # Age distribution by segment
                age_params = {
                    'lifestyle': (58, 12),
                    'acute': (40, 18),
                    'checkup': (47, 10)
                }
                age = int(np.random.normal(*age_params[segment]))
                age = max(22, min(82, age))
                
                # Visit hour with realistic distribution
                hour = np.random.choice(
                    [9, 10, 11, 12, 14, 15, 16, 17],
                    p=[0.08, 0.16, 0.24, 0.09, 0.11, 0.21, 0.08, 0.03]
                )
                
                records.append({
                    'date': date,
                    'segment': segment,
                    'visit_type': visit_type,
                    'age': age,
                    'revenue': revenue,
                    'hour': hour,
                    'weekday': date.weekday()
                })
        
        df = pd.DataFrame(records)
        df['date'] = pd.to_datetime(df['date'])
        
        # Calculate wait time (quadratic relationship with patient load)
        daily_counts = df.groupby('date').size()
        df['wait_time'] = df['date'].map(
            lambda d: int(((daily_counts.get(d, 0) / 60) ** 2) * 35)
        )
        df['wait_time'] = df['wait_time'].clip(8, 135)
        
        return df
    
    def get_kpi_summary(self, target_month: pd.Period) -> dict:
        """Calculate executive KPIs with month-over-month comparison"""
        df_curr = self.data[self.data['date'].dt.to_period('M') == target_month]
        df_prev = self.data[self.data['date'].dt.to_period('M') == (target_month - 1)]
        
        def calc_delta(curr, prev):
            return ((curr - prev) / prev * 100) if prev > 0 else 0
        
        return {
            'revenue': {
                'value': df_curr['revenue'].sum(),
                'delta': calc_delta(df_curr['revenue'].sum(), df_prev['revenue'].sum())
            },
            'visits': {
                'value': len(df_curr),
                'delta': calc_delta(len(df_curr), len(df_prev))
            },
            'wait_time': {
                'value': df_curr['wait_time'].mean(),
                'delta': calc_delta(df_curr['wait_time'].mean(), df_prev['wait_time'].mean())
            },
            'first_rate': {
                'value': (df_curr['visit_type'] == '初診').sum() / len(df_curr) * 100 if len(df_curr) > 0 else 0,
                'delta': (df_curr['visit_type'] == '初診').sum() / len(df_curr) * 100 - 
                        (df_prev['visit_type'] == '初診').sum() / len(df_prev) * 100 if len(df_prev) > 0 else 0
            }
        }
    
    def get_daily_trend(self, target_month: pd.Period) -> pd.DataFrame:
        """Daily revenue and visits aggregation"""
        df_month = self.data[self.data['date'].dt.to_period('M') == target_month]
        return df_month.groupby('date').agg({
            'revenue': 'sum',
            'date': 'count'
        }).rename(columns={'date': 'visits'}).reset_index()
    
    def get_heatmap_data(self, target_month: pd.Period) -> pd.DataFrame:
        """Congestion heatmap (weekday × hour)"""
        df_month = self.data[self.data['date'].dt.to_period('M') == target_month]
        heatmap = df_month.groupby(['weekday', 'hour']).size().reset_index(name='count')
        return heatmap.pivot(index='hour', columns='weekday', values='count').fillna(0)
    
    def get_segment_distribution(self, target_month: pd.Period) -> pd.DataFrame:
        """Patient segment breakdown"""
        df_month = self.data[self.data['date'].dt.to_period('M') == target_month]
        segment_map = {'lifestyle': '生活習慣病', 'acute': '急性疾患', 'checkup': '検診・ドック'}
        dist = df_month['segment'].value_counts().reset_index()
        dist.columns = ['segment', 'count']
        dist['segment'] = dist['segment'].map(segment_map)
        return dist
    
    def get_age_distribution(self, target_month: pd.Period) -> pd.DataFrame:
        """Age distribution for histogram"""
        df_month = self.data[self.data['date'].dt.to_period('M') == target_month]
        return df_month[['age']]

# ============================================================
# 4. UI COMPONENTS (HTML Rendering)
# ============================================================

def render_premium_header():
    """Render a sophisticated header with logo and timestamp"""
    now = datetime.now()
    
    st.markdown(f"""
    <div class="dashboard-header animate-fade-in-up">
        <div class="clinic-logo">
            <i class="fas fa-hospital-alt clinic-icon"></i>
            <div>
                <h1 class="clinic-title">Metro Central Internal Medicine</h1>
                <p class="clinic-subtitle">Executive Performance Dashboard</p>
            </div>
        </div>
        <div class="last-updated">
            <div class="last-updated-label">LAST UPDATED</div>
            <div class="last-updated-time">
                <i class="far fa-clock" style="color: {COLOR.BRAND_PRIMARY}; margin-right: 0.375rem;"></i>
                {now.strftime('%Y年%m月%d日 %H:%M')}
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

def render_god_tier_kpi_card(icon: str, label: str, value: str, delta: float, 
                              color: str, inverse: bool = False):
    """Render ultimate KPI card with sophisticated design"""
    
    is_positive = (delta >= 0 and not inverse) or (delta < 0 and inverse)
    badge_class = "positive" if is_positive else "negative"
    arrow = "fa-arrow-up" if delta >= 0 else "fa-arrow-down"
    delta_text = f"{abs(delta):.1f}%"
    
    return f"""
    <div class="kpi-card animate-fade-in-up">
        <div class="kpi-icon-wrapper" style="background: {color}15;">
            <i class="{icon}" style="color: {color};"></i>
        </div>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        <div class="kpi-delta-container">
            <span class="trend-badge {badge_class}">
                <i class="fas {arrow} trend-arrow"></i>
                {delta_text}
            </span>
            <span class="vs-label">vs 前月</span>
        </div>
    </div>
    """

# ============================================================
# 5. PLOTLY VISUALIZATION (Beyond Default)
# ============================================================

def create_god_tier_dual_axis_chart(daily_data: pd.DataFrame) -> go.Figure:
    """Premium dual-axis chart with gradient fill and rich tooltips"""
    
    fig = go.Figure()
    
    # Area chart for visits with gradient fill
    fig.add_trace(go.Scatter(
        x=daily_data['date'],
        y=daily_data['visits'],
        name='来院数',
        mode='lines',
        line=dict(color=COLOR.CHART_1, width=3),
        fill='tozeroy',
        fillcolor='rgba(14, 165, 233, 0.2)',
        yaxis='y',
        hovertemplate='<b>%{x|%m/%d}</b><br>' +
                      f'<span style="font-size:16px; color:{COLOR.CHART_1}; font-weight:700;">来院数: %{{y}}人</span>' +
                      '<extra></extra>'
    ))
    
    # Line chart for revenue with markers
    fig.add_trace(go.Scatter(
        x=daily_data['date'],
        y=daily_data['revenue'],
        name='売上',
        mode='lines+markers',
        line=dict(color=COLOR.CHART_2, width=4),
        marker=dict(size=8, color=COLOR.CHART_2, line=dict(width=2, color='white')),
        yaxis='y2',
        hovertemplate='<b>%{x|%m/%d}</b><br>' +
                      f'<span style="font-size:16px; color:{COLOR.CHART_2}; font-weight:700;">売上: ¥%{{y:,.0f}}</span>' +
                      '<extra></extra>'
    ))
    
    fig.update_layout(
        font=dict(family="Inter, Noto Sans JP, sans-serif", color=COLOR.TEXT_PRIMARY),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=40, l=60, r=60),
        hovermode='x unified',
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="center",
            x=0.5,
            font=dict(size=14, weight=600)
        ),
        yaxis=dict(
            title=dict(text='来院数（人）', font=dict(size=14, weight=600)),
            showgrid=True,
            gridcolor=COLOR.BORDER,
            gridwidth=1,
            zeroline=False
        ),
        yaxis2=dict(
            title=dict(text='売上（円）', font=dict(size=14, weight=600)),
            overlaying='y',
            side='right',
            showgrid=False
        ),
        xaxis=dict(
            showgrid=False,
            showline=True,
            linecolor=COLOR.BORDER,
            linewidth=2
        )
    )
    
    return fig

def create_god_tier_heatmap(heatmap_data: pd.DataFrame) -> go.Figure:
    """Premium heatmap with gap styling and rich tooltips"""
    
    weekday_labels = ['月', '火', '水', '木', '金', '土']
    
    fig = go.Figure(data=go.Heatmap(
        z=heatmap_data.values,
        x=[weekday_labels[i] for i in heatmap_data.columns],
        y=[f"{h}:00" for h in heatmap_data.index],
        colorscale=[
            [0, '#F0F9FF'],
            [0.2, '#BAE6FD'],
            [0.4, '#7DD3FC'],
            [0.6, '#38BDF8'],
            [0.8, '#0EA5E9'],
            [1, '#0369A1']
        ],
        showscale=True,
        xgap=2,
        ygap=2,
        hovertemplate='<b>%{x} %{y}</b><br>' +
                      f'<span style="font-size:16px; color:{COLOR.CHART_1}; font-weight:700;">来院数: %{{z}}人</span>' +
                      '<extra></extra>',
        colorbar=dict(
            title=dict(text='来院数', font=dict(size=12, weight=600)),
            thickness=15,
            len=0.7
        )
    ))
    
    fig.update_layout(
        font=dict(family="Inter, Noto Sans JP, sans-serif", color=COLOR.TEXT_PRIMARY),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=40, l=60, r=20),
        xaxis=dict(side='top', showgrid=False),
        yaxis=dict(showgrid=False)
    )
    
    return fig

def create_god_tier_donut(segment_data: pd.DataFrame) -> go.Figure:
    """Premium donut chart with sophisticated styling"""
    
    colors = [COLOR.CHART_1, COLOR.CHART_2, COLOR.CHART_3]
    
    fig = go.Figure(data=[go.Pie(
        labels=segment_data['segment'],
        values=segment_data['count'],
        hole=0.55,
        marker=dict(
            colors=colors,
            line=dict(color='white', width=3)
        ),
        textfont=dict(size=14, weight=700),
        textposition='outside',
        hovertemplate='<b>%{label}</b><br>' +
                      '<span style="font-size:16px; font-weight:700;">%{value}人 (%{percent})</span>' +
                      '<extra></extra>'
    )])
    
    fig.update_layout(
        font=dict(family="Inter, Noto Sans JP, sans-serif", color=COLOR.TEXT_PRIMARY),
        paper_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=20, l=20, r=20),
        showlegend=True,
        legend=dict(
            orientation="v",
            yanchor="middle",
            y=0.5,
            xanchor="left",
            x=1.05,
            font=dict(size=13, weight=600)
        )
    )
    
    return fig

def create_god_tier_histogram(age_data: pd.DataFrame) -> go.Figure:
    """Premium age distribution histogram"""
    
    fig = go.Figure(data=[go.Histogram(
        x=age_data['age'],
        nbinsx=13,
        marker=dict(
            color=COLOR.CHART_2,
            line=dict(color='white', width=2)
        ),
        hovertemplate='<b>年齢: %{x}</b><br>' +
                      f'<span style="font-size:16px; color:{COLOR.CHART_2}; font-weight:700;">人数: %{{y}}人</span>' +
                      '<extra></extra>'
    )])
    
    fig.update_layout(
        font=dict(family="Inter, Noto Sans JP, sans-serif", color=COLOR.TEXT_PRIMARY),
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        margin=dict(t=20, b=40, l=60, r=20),
        xaxis=dict(
            title=dict(text='年齢', font=dict(size=14, weight=600)),
            showgrid=False,
            showline=True,
            linecolor=COLOR.BORDER,
            linewidth=2
        ),
        yaxis=dict(
            title=dict(text='来院数（人）', font=dict(size=14, weight=600)),
            showgrid=True,
            gridcolor=COLOR.BORDER,
            gridwidth=1
        ),
        bargap=0.1
    )
    
    return fig

# ============================================================
# 6. MAIN APPLICATION
# ============================================================

def main():
    """Main application orchestration"""
    
    # Inject God Tier Styles
    inject_god_tier_styles()
    
    # Initialize Data Manager
    dm = DataManager(months_back=6)
    current_month = pd.Period(datetime.now(), freq='M')
    
    # Get KPIs
    kpis = dm.get_kpi_summary(current_month)
    
    # ========== HEADER ==========
    render_premium_header()
    
    # ========== ROW 1: KPI CARDS ==========
    col1, col2, col3, col4 = st.columns(4, gap="large")
    
    with col1:
        st.markdown(
            render_god_tier_kpi_card(
                "fas fa-yen-sign",
                "今月の売上",
                f"¥{kpis['revenue']['value']:,.0f}",
                kpis['revenue']['delta'],
                COLOR.CHART_1
            ),
            unsafe_allow_html=True
        )
    
    with col2:
        st.markdown(
            render_god_tier_kpi_card(
                "fas fa-users",
                "来院数",
                f"{kpis['visits']['value']:,}人",
                kpis['visits']['delta'],
                COLOR.CHART_2
            ),
            unsafe_allow_html=True
        )
    
    with col3:
        st.markdown(
            render_god_tier_kpi_card(
                "fas fa-clock",
                "平均待ち時間",
                f"{kpis['wait_time']['value']:.0f}分",
                kpis['wait_time']['delta'],
                COLOR.CHART_3,
                inverse=True
            ),
            unsafe_allow_html=True
        )
    
    with col4:
        st.markdown(
            render_god_tier_kpi_card(
                "fas fa-user-plus",
                "初診率",
                f"{kpis['first_rate']['value']:.1f}%",
                kpis['first_rate']['delta'],
                COLOR.CHART_4
            ),
            unsafe_allow_html=True
        )
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # ========== ROW 2: DUAL AXIS CHART & HEATMAP ==========
    col_left, col_right = st.columns([2, 1], gap="large")
    
    with col_left:
        st.markdown(
            '<div class="graph-container animate-fade-in-up">' +
            '<div class="graph-title"><i class="fas fa-chart-line"></i>売上 & 来院数トレンド</div>',
            unsafe_allow_html=True
        )
        daily_trend = dm.get_daily_trend(current_month)
        fig_dual = create_god_tier_dual_axis_chart(daily_trend)
        st.plotly_chart(fig_dual, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_right:
        st.markdown(
            '<div class="graph-container animate-fade-in-up">' +
            '<div class="graph-title"><i class="fas fa-fire"></i>混雑ヒートマップ</div>',
            unsafe_allow_html=True
        )
        heatmap_data = dm.get_heatmap_data(current_month)
        fig_heatmap = create_god_tier_heatmap(heatmap_data)
        st.plotly_chart(fig_heatmap, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
    
    # ========== ROW 3: DONUT & HISTOGRAM ==========
    col_left, col_right = st.columns(2, gap="large")
    
    with col_left:
        st.markdown(
            '<div class="graph-container animate-fade-in-up">' +
            '<div class="graph-title"><i class="fas fa-chart-pie"></i>疾患別構成比</div>',
            unsafe_allow_html=True
        )
        segment_data = dm.get_segment_distribution(current_month)
        fig_donut = create_god_tier_donut(segment_data)
        st.plotly_chart(fig_donut, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_right:
        st.markdown(
            '<div class="graph-container animate-fade-in-up">' +
            '<div class="graph-title"><i class="fas fa-chart-bar"></i>年齢分布</div>',
            unsafe_allow_html=True
        )
        age_data = dm.get_age_distribution(current_month)
        fig_age = create_god_tier_histogram(age_data)
        st.plotly_chart(fig_age, use_container_width=True, config={'displayModeBar': False})
        st.markdown('</div>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
