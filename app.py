import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from io import BytesIO
from datetime import datetime
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer, Image, PageBreak
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT
import plotly.io as pio

# ページ設定
st.set_page_config(
    page_title="経営分析ボード",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# カスタムCSSで医療系の清潔感あるデザイン
st.markdown("""
<style>
    /* 全体の背景を真っ白に */
    .stApp {
        background-color: #ffffff;
    }
    
    /* メインコンテンツエリア */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1400px;
        background-color: #ffffff;
    }
    
    /* カード型デザイン - 清潔で上品な影 */
    .metric-card {
        background: #ffffff;
        padding: 28px;
        border-radius: 8px;
        border: 1px solid #e8eef5;
        box-shadow: 0 2px 8px rgba(0, 86, 179, 0.08);
        margin: 10px 0;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        box-shadow: 0 4px 12px rgba(0, 86, 179, 0.15);
        transform: translateY(-2px);
    }
    
    /* KPI数値のスタイル - メディカルブルー */
    .kpi-value {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0056b3;
        margin: 10px 0;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    .kpi-label {
        color: #6c757d;
        font-size: 0.85rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        margin-bottom: 8px;
    }
    
    .kpi-icon {
        font-size: 1.2rem;
        margin-right: 6px;
        color: #0056b3;
    }
    
    /* タイトル - メディカルブルー */
    h1 {
        color: #0056b3 !important;
        text-align: center;
        font-weight: 700 !important;
        font-size: 2.5rem !important;
        margin-bottom: 2rem !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
        border-bottom: 3px solid #0056b3;
        padding-bottom: 1rem;
    }
    
    /* サブヘッダー */
    h2 {
        color: #333333 !important;
        font-weight: 600 !important;
        font-size: 1.5rem !important;
        margin-top: 2rem !important;
        margin-bottom: 1rem !important;
        border-left: 4px solid #0056b3;
        padding-left: 12px;
    }
    
    h3 {
        color: #333333 !important;
        font-weight: 600 !important;
        font-size: 1.2rem !important;
    }
    
    /* サイドバーのスタイル */
    section[data-testid="stSidebar"] {
        background-color: #f8f9fa;
        border-right: 1px solid #dee2e6;
    }
    
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3 {
        color: #0056b3 !important;
    }
    
    /* セレクトボックス */
    .stSelectbox > div > div {
        background-color: #ffffff;
        border: 2px solid #dee2e6;
        border-radius: 6px;
        color: #333333;
        font-weight: 500;
    }
    
    .stSelectbox > div > div:hover {
        border-color: #0056b3;
    }
    
    /* 警告・情報ボックス */
    .stAlert {
        background-color: #fff3cd;
        border-radius: 6px;
        border-left: 4px solid #ffc107;
        color: #333333;
    }
    
    .stSuccess {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
    }
    
    .stInfo {
        background-color: #d1ecf1;
        border-left: 4px solid #0056b3;
    }
    
    /* データフレーム */
    .dataframe {
        border: 1px solid #dee2e6 !important;
        border-radius: 6px;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* メトリックカード */
    div[data-testid="stMetricValue"] {
        color: #0056b3;
        font-size: 1.8rem;
        font-weight: 700;
    }
    
    div[data-testid="stMetricLabel"] {
        color: #6c757d;
        font-weight: 600;
        font-size: 0.9rem;
    }
    
    div[data-testid="stMetricDelta"] {
        font-size: 0.85rem;
    }
    
    /* 区切り線 */
    hr {
        border-color: #dee2e6;
        margin: 2rem 0;
        opacity: 0.5;
    }
    
    /* テキスト - くっきりした黒 */
    p, label, span {
        color: #333333 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* ボタン */
    .stButton > button {
        background-color: #0056b3;
        color: white;
        border: none;
        border-radius: 6px;
        padding: 0.5rem 1.5rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stButton > button:hover {
        background-color: #004494;
        box-shadow: 0 2px 8px rgba(0, 86, 179, 0.2);
    }
    
    /* 目標達成ボタン */
    .achievement-button {
        text-align: center;
        margin: 1.5rem 0;
    }
    
    .achievement-button button {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        font-size: 1.2rem;
        padding: 1rem 3rem;
        border-radius: 50px;
        border: none;
        font-weight: 700;
        box-shadow: 0 4px 15px rgba(40, 167, 69, 0.3);
        transition: all 0.3s ease;
    }
    
    .achievement-button button:hover {
        background: linear-gradient(135deg, #218838 0%, #1aa179 100%);
        box-shadow: 0 6px 20px rgba(40, 167, 69, 0.4);
        transform: translateY(-2px);
    }
    
    /* おめでとうメッセージ */
    .congratulation-message {
        background: linear-gradient(135deg, #28a745 0%, #20c997 100%);
        color: white;
        padding: 2.5rem;
        border-radius: 15px;
        text-align: center;
        font-size: 2rem;
        font-weight: 700;
        box-shadow: 0 8px 30px rgba(40, 167, 69, 0.4);
        margin: 1.5rem 0;
        animation: slideIn 0.5s ease-out;
    }
    
    @keyframes slideIn {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }
    
    .congratulation-emoji {
        font-size: 3rem;
        margin-bottom: 1rem;
    }
    
    /* プロット背景 */
    .js-plotly-plot {
        border-radius: 8px;
        box-shadow: 0 2px 8px rgba(0, 86, 179, 0.08);
    }
</style>
""", unsafe_allow_html=True)

# データの読み込み
@st.cache_data
def load_data():
    df = pd.read_csv('data.csv')
    df['年月'] = pd.to_datetime(df['年月'])
    return df

# カスタムKPIカードの作成
def create_kpi_card(label, value, icon="📊"):
    return f"""
    <div class="metric-card">
        <div class="kpi-label"><span class="kpi-icon">{icon}</span>{label}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """

# PDF生成関数（印刷フレンドリー：白背景・黒文字）
def generate_pdf_report(df, selected_hospital=None):
    """
    ビジネス文書風のPDFレポートを生成
    背景：真っ白、文字：真っ黒、グラフ：白背景カラー
    """
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=A4, topMargin=0.75*inch, bottomMargin=0.75*inch)
    story = []
    
    # スタイル設定（白背景・黒文字）
    styles = getSampleStyleSheet()
    
    # タイトルスタイル
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.black,
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    # 見出しスタイル
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.black,
        spaceAfter=12,
        spaceBefore=12,
        fontName='Helvetica-Bold',
        borderWidth=2,
        borderColor=colors.HexColor('#0056b3'),
        borderPadding=5,
        backColor=colors.HexColor('#f0f0f0')
    )
    
    # 本文スタイル
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.black,
        fontName='Helvetica'
    )
    
    # ドキュメントタイトル
    title = Paragraph("経営分析レポート", title_style)
    story.append(title)
    
    # 作成日時
    date_text = Paragraph(
        f"作成日: {datetime.now().strftime('%Y年%m月%d日 %H:%M')}",
        normal_style
    )
    story.append(date_text)
    story.append(Spacer(1, 0.3*inch))
    
    # 全体サマリー
    story.append(Paragraph("1. 全体サマリー", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    total_cost_reduction = df['削減コスト'].sum()
    total_purchase = df['購入額'].sum()
    overall_reduction_rate = (total_cost_reduction / total_purchase) * 100
    
    # KPIテーブル（ビジネス文書風）
    kpi_data = [
        ['項目', '金額'],
        ['総購入額', f'¥{total_purchase:,.0f}'],
        ['総削減コスト', f'¥{total_cost_reduction:,.0f}'],
        ['全体削減率', f'{overall_reduction_rate:.1f}%']
    ]
    
    kpi_table = Table(kpi_data, colWidths=[3*inch, 3*inch])
    kpi_table.setStyle(TableStyle([
        # ヘッダー行
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0056b3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 12),
        ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
        # データ行
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 11),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')])
    ]))
    
    story.append(kpi_table)
    story.append(Spacer(1, 0.3*inch))
    
    # 病院別データ
    story.append(Paragraph("2. 病院別最新データ", heading_style))
    story.append(Spacer(1, 0.1*inch))
    
    latest_data = df.sort_values('年月').groupby('病院名').last().reset_index()
    hospital_data = [['病院名', '購入額', '削減コスト', '削減率']]
    
    for _, row in latest_data.iterrows():
        reduction_rate = (row['削減コスト'] / row['購入額'] * 100)
        hospital_data.append([
            row['病院名'],
            f"¥{row['購入額']:,.0f}",
            f"¥{row['削減コスト']:,.0f}",
            f"{reduction_rate:.1f}%"
        ])
    
    hospital_table = Table(hospital_data, colWidths=[1.5*inch, 1.5*inch, 1.5*inch, 1.5*inch])
    hospital_table.setStyle(TableStyle([
        # ヘッダー行
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0056b3')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 11),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        # データ行
        ('BACKGROUND', (0, 1), (-1, -1), colors.white),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 10),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc')),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')])
    ]))
    
    story.append(hospital_table)
    story.append(Spacer(1, 0.3*inch))
    
    # 選択された病院の詳細（オプション）
    if selected_hospital:
        story.append(PageBreak())
        story.append(Paragraph(f"3. {selected_hospital} 詳細分析", heading_style))
        story.append(Spacer(1, 0.2*inch))
        
        hospital_df = df[df['病院名'] == selected_hospital].sort_values('年月')
        
        # 月次データテーブル
        monthly_data = [['年月', '購入額', '削減コスト']]
        for _, row in hospital_df.iterrows():
            monthly_data.append([
                row['年月'].strftime('%Y年%m月'),
                f"¥{row['購入額']:,.0f}",
                f"¥{row['削減コスト']:,.0f}"
            ])
        
        monthly_table = Table(monthly_data, colWidths=[2*inch, 2*inch, 2*inch])
        monthly_table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#0056b3')),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 11),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('BACKGROUND', (0, 1), (-1, -1), colors.white),
            ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
            ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
            ('FONTSIZE', (0, 1), (-1, -1), 10),
            ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#cccccc')),
            ('ROWBACKGROUNDS', (0, 1), (-1, -1), [colors.white, colors.HexColor('#f9f9f9')])
        ]))
        
        story.append(monthly_table)
        story.append(Spacer(1, 0.3*inch))
        
        # グラフの生成（白背景・カラー - PDF印刷用）
        hospital_df_copy = hospital_df.copy()
        hospital_df_copy['年月表示'] = hospital_df_copy['年月'].dt.strftime('%Y年%m月')
        
        # 購入推移グラフ（PDF用：白背景・黒文字）
        fig = px.bar(
            hospital_df_copy,
            x='年月表示',
            y='購入額',
            title=f'{selected_hospital}の月次購入額推移',
            color_discrete_sequence=['#0056b3']
        )
        
        # 【重要】画像化直前に白背景テーマを強制適用（印刷フレンドリー）
        # これによりPDF内のグラフが白背景・黒文字になります
        fig.update_layout(
            template='plotly_white',  # Plotly白背景テーマ
            paper_bgcolor='white',  # 外側の背景を白に
            plot_bgcolor='white',  # プロット領域の背景を白に
            font=dict(
                color='black',  # すべてのテキストを黒に
                size=10,
                family='Arial'
            ),
            title_font=dict(
                size=14,
                color='black',  # タイトルを黒に
                family='Arial'
            ),
            xaxis=dict(
                gridcolor='#e0e0e0',  # グリッド線を薄いグレーに
                linecolor='black',  # 軸線を黒に
                tickfont=dict(color='black'),  # 目盛りラベルを黒に
                title_font=dict(color='black')  # 軸タイトルを黒に
            ),
            yaxis=dict(
                gridcolor='#e0e0e0',
                linecolor='black',
                tickfont=dict(color='black'),
                title_font=dict(color='black')
            ),
            width=550,
            height=300,
            margin=dict(l=60, r=30, t=50, b=50)
        )
        
        # バーの色も確実に設定
        fig.update_traces(
            marker=dict(
                color='#0056b3',
                line=dict(color='#004494', width=1)
            )
        )
        
        # グラフを画像として保存（kaleido）- エラーハンドリング強化
        try:
            img_bytes = pio.to_image(fig, format='png', engine='kaleido')
            img_buffer = BytesIO(img_bytes)
            img = Image(img_buffer, width=5.5*inch, height=3*inch)
            story.append(img)
            story.append(Spacer(1, 0.3*inch))
        except Exception as e:
            # グラフ画像化エラー時の代替処理
            error_text = Paragraph(
                f"<i>※ グラフ画像の生成に失敗しました: {str(e)}</i>",
                normal_style
            )
            story.append(error_text)
            story.append(Spacer(1, 0.2*inch))
        
        # 削減コスト推移グラフ（PDF用：白背景・黒文字）
        fig2 = px.line(
            hospital_df_copy,
            x='年月表示',
            y='削減コスト',
            title=f'{selected_hospital}の月次削減コスト推移',
            markers=True
        )
        
        # 【重要】画像化直前に白背景テーマを強制適用（印刷フレンドリー）
        # これによりPDF内のグラフが白背景・黒文字になります
        fig2.update_layout(
            template='plotly_white',  # Plotly白背景テーマ
            paper_bgcolor='white',  # 外側の背景を白に
            plot_bgcolor='white',  # プロット領域の背景を白に
            font=dict(
                color='black',  # すべてのテキストを黒に
                size=10,
                family='Arial'
            ),
            title_font=dict(
                size=14,
                color='black',  # タイトルを黒に
                family='Arial'
            ),
            xaxis=dict(
                gridcolor='#e0e0e0',  # グリッド線を薄いグレーに
                linecolor='black',  # 軸線を黒に
                tickfont=dict(color='black'),  # 目盛りラベルを黒に
                title_font=dict(color='black')  # 軸タイトルを黒に
            ),
            yaxis=dict(
                gridcolor='#e0e0e0',
                linecolor='black',
                tickfont=dict(color='black'),
                title_font=dict(color='black')
            ),
            width=550,
            height=300,
            margin=dict(l=60, r=30, t=50, b=50)
        )
        
        # 線とマーカーの色を確実に設定
        fig2.update_traces(
            line=dict(color='#28a745', width=3),  # 緑色の線
            marker=dict(
                color='#28a745',
                size=8,
                line=dict(color='#1e7e34', width=2)
            ),
            fill='tozeroy',
            fillcolor='rgba(40, 167, 69, 0.1)'  # 薄い緑の塗りつぶし
        )
        
        # グラフを画像として保存（kaleido）- エラーハンドリング強化
        try:
            img_bytes2 = pio.to_image(fig2, format='png', engine='kaleido')
            img_buffer2 = BytesIO(img_bytes2)
            img2 = Image(img_buffer2, width=5.5*inch, height=3*inch)
            story.append(img2)
        except Exception as e:
            # グラフ画像化エラー時の代替処理
            error_text = Paragraph(
                f"<i>※ グラフ画像の生成に失敗しました: {str(e)}</i>",
                normal_style
            )
            story.append(error_text)
    
    # フッター
    story.append(Spacer(1, 0.5*inch))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#666666'),
        alignment=TA_CENTER
    )
    footer = Paragraph("共同購買サービス 経営分析ダッシュボード | 機密文書", footer_style)
    story.append(footer)
    
    # PDF生成
    doc.build(story)
    buffer.seek(0)
    return buffer

# メイン処理
def main():
    st.title("🏥 経営者様専用 経営分析ボード")
    
    # セッション状態の初期化
    if 'show_celebration' not in st.session_state:
        st.session_state.show_celebration = False
    
    # 目標達成ボタン
    st.markdown('<div class="achievement-button">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎉 今月の目標達成！", use_container_width=True, type="primary"):
            st.session_state.show_celebration = True
            st.balloons()
    st.markdown('</div>', unsafe_allow_html=True)
    
    # おめでとうメッセージの表示
    if st.session_state.show_celebration:
        st.markdown("""
        <div class="congratulation-message">
            <div class="congratulation-emoji">🎊🎉🎊</div>
            <div>おめでとうございます！</div>
            <div style="font-size: 1.5rem; margin-top: 1rem;">素晴らしい成果です！</div>
        </div>
        """, unsafe_allow_html=True)
        
        # メッセージを閉じるボタン
        col1, col2, col3 = st.columns([2, 1, 2])
        with col2:
            if st.button("メッセージを閉じる", use_container_width=True):
                st.session_state.show_celebration = False
                st.rerun()
    
    # データ読み込み
    df = load_data()
    
    # サイドバー：今月の目標達成率
    with st.sidebar:
        st.header("📊 今月の目標達成率")
        st.markdown("---")
        
        # 今月（11月）の実績を計算
        latest_month = df['年月'].max()
        current_month_data = df[df['年月'] == latest_month]
        current_month_purchase = current_month_data['購入額'].sum()
        
        # 目標額の設定（調整可能）
        target_amount = 6500000  # 650万円を目標とする
        achievement_rate = (current_month_purchase / target_amount) * 100
        
        # ゲージチャートの作成（メディカルブルー）
        fig_gauge = go.Figure(go.Indicator(
            mode="gauge+number+delta",
            value=achievement_rate,
            domain={'x': [0, 1], 'y': [0, 1]},
            title={'text': "達成率 (%)", 'font': {'size': 18, 'color': '#333333', 'family': 'Arial'}},
            delta={'reference': 100, 'increasing': {'color': "#28a745"}, 'decreasing': {'color': "#dc3545"}},
            number={'font': {'size': 38, 'color': '#0056b3', 'family': 'Arial'}},
            gauge={
                'axis': {'range': [None, 150], 'tickwidth': 1, 'tickcolor': "#6c757d"},
                'bar': {'color': "#0056b3", 'thickness': 0.75},
                'bgcolor': "#ffffff",
                'borderwidth': 2,
                'bordercolor': "#dee2e6",
                'steps': [
                    {'range': [0, 50], 'color': '#f8d7da'},
                    {'range': [50, 80], 'color': '#fff3cd'},
                    {'range': [80, 100], 'color': '#d4edda'},
                    {'range': [100, 150], 'color': '#d1ecf1'}
                ],
                'threshold': {
                    'line': {'color': "#28a745", 'width': 3},
                    'thickness': 0.75,
                    'value': 100
                }
            }
        ))
        
        fig_gauge.update_layout(
            height=300,
            margin=dict(l=20, r=20, t=50, b=20),
            font={'size': 13, 'color': '#333333', 'family': 'Arial'},
            paper_bgcolor='#f8f9fa',
            plot_bgcolor='#f8f9fa'
        )
        
        st.plotly_chart(fig_gauge, use_container_width=True)
        
        # 目標額と実績額の表示
        st.markdown("### 📈 今月の詳細")
        st.metric(
            label="目標額",
            value=f"¥{target_amount:,}"
        )
        st.metric(
            label="実績額",
            value=f"¥{current_month_purchase:,}",
            delta=f"{current_month_purchase - target_amount:,}"
        )
        st.metric(
            label="達成率",
            value=f"{achievement_rate:.1f}%",
            delta=f"{achievement_rate - 100:.1f}%"
        )
        
        # 目標達成状況のメッセージ
        if achievement_rate >= 100:
            st.success("🎉 目標達成！素晴らしいです！")
        elif achievement_rate >= 80:
            st.info("💪 もう少しで目標達成です！")
        else:
            st.warning("⚠️ 目標達成に向けて追加施策が必要です")
        
        # PDFレポートダウンロード
        st.markdown("---")
        st.markdown("### 📄 レポート出力")
        
        # 全体レポート
        if st.button("📊 全体レポートをダウンロード", use_container_width=True):
            try:
                pdf_buffer = generate_pdf_report(df, selected_hospital=None)
                st.download_button(
                    label="💾 PDFをダウンロード",
                    data=pdf_buffer,
                    file_name=f"経営分析レポート_全体_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
                st.success("✅ レポートが生成されました！")
            except Exception as e:
                st.error(f"⚠️ PDF生成エラー: {str(e)}")
                st.warning("📦 Kaleidoのバージョン互換性の問題が発生している可能性があります")
                st.info("💡 以下のコマンドで互換性の高いバージョンをインストールしてください:")
                st.code('pip install "kaleido==0.2.1"', language='bash')
                st.info("または、最新版を試す場合: `pip install --upgrade kaleido`")
    
    # メインコンテンツ
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 1. 総削減コストの表示（KPI）- カード型デザイン
    total_cost_reduction = df['削減コスト'].sum()
    total_purchase = df['購入額'].sum()
    overall_reduction_rate = (total_cost_reduction / total_purchase) * 100
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(create_kpi_card(
            "総削減コスト",
            f"¥{total_cost_reduction:,}",
            "💎"
        ), unsafe_allow_html=True)
    
    with col2:
        st.markdown(create_kpi_card(
            "総購入額",
            f"¥{total_purchase:,}",
            "💰"
        ), unsafe_allow_html=True)
    
    with col3:
        st.markdown(create_kpi_card(
            "全体削減率",
            f"{overall_reduction_rate:.1f}%",
            "📈"
        ), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 2. 病院選択プルダウン
    st.subheader("🏥 病院選択")
    hospitals = sorted(df['病院名'].unique())
    selected_hospital = st.selectbox(
        "分析する病院を選択してください",
        hospitals,
        label_visibility="collapsed"
    )
    
    # 選択した病院のデータをフィルタリング
    hospital_df = df[df['病院名'] == selected_hospital].sort_values('年月')
    
    # 3. 前月比チェックとアラート表示
    if len(hospital_df) >= 2:
        latest_purchase = hospital_df.iloc[-1]['購入額']
        previous_purchase = hospital_df.iloc[-2]['購入額']
        
        if latest_purchase < previous_purchase:
            st.warning(f"⚠️ **フォローが必要**: {selected_hospital}の購入額が前月より減少しています（前月: ¥{previous_purchase:,} → 今月: ¥{latest_purchase:,}）")
    
    # 病院別PDFダウンロード
    col_pdf1, col_pdf2, col_pdf3 = st.columns([1, 1, 1])
    with col_pdf2:
        if st.button(f"📄 {selected_hospital}のレポートをダウンロード", use_container_width=True):
            try:
                pdf_buffer = generate_pdf_report(df, selected_hospital=selected_hospital)
                st.download_button(
                    label=f"💾 {selected_hospital} PDFダウンロード",
                    data=pdf_buffer,
                    file_name=f"経営分析レポート_{selected_hospital}_{datetime.now().strftime('%Y%m%d_%H%M')}.pdf",
                    mime="application/pdf",
                    use_container_width=True
                )
                st.success("✅ レポートが生成されました！")
            except Exception as e:
                st.error(f"⚠️ PDF生成エラー: {str(e)}")
                st.warning("📦 Kaleidoのバージョン互換性の問題が発生している可能性があります")
                st.info("💡 ターミナルで以下を実行してください:")
                st.code('pip install "kaleido==0.2.1"', language='bash')
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 4. 選択した病院の詳細情報（カード型）
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_purchase_hosp = hospital_df['購入額'].sum()
        st.markdown(create_kpi_card(
            f"{selected_hospital} 総購入額",
            f"¥{total_purchase_hosp:,}",
            "🏥"
        ), unsafe_allow_html=True)
    
    with col2:
        total_reduction_hosp = hospital_df['削減コスト'].sum()
        st.markdown(create_kpi_card(
            f"{selected_hospital} 総削減コスト",
            f"¥{total_reduction_hosp:,}",
            "💎"
        ), unsafe_allow_html=True)
    
    with col3:
        if total_purchase_hosp > 0:
            reduction_rate = (total_reduction_hosp / total_purchase_hosp) * 100
            st.markdown(create_kpi_card(
                f"{selected_hospital} 削減率",
                f"{reduction_rate:.1f}%",
                "📈"
            ), unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("---")
    
    # 5. 購入推移の棒グラフ（メディカルブルー）
    st.subheader(f"📈 {selected_hospital}の購入推移")
    
    # データを整形
    hospital_df_copy = hospital_df.copy()
    hospital_df_copy['年月表示'] = hospital_df_copy['年月'].dt.strftime('%Y年%m月')
    
    fig = px.bar(
        hospital_df_copy,
        x='年月表示',
        y='購入額',
        title=f'{selected_hospital}の月次購入額推移',
        labels={'購入額': '購入額（円）', '年月表示': '年月'},
        text='購入額',
        color_discrete_sequence=['#0056b3']
    )
    
    # 清潔感のあるスタイル適用
    fig.update_traces(
        texttemplate='¥%{text:,.0f}',
        textposition='outside',
        marker=dict(
            line=dict(color='#004494', width=1),
            opacity=0.9
        ),
        textfont=dict(color='#333333', size=11)
    )
    
    fig.update_layout(
        height=450,
        xaxis_tickangle=-45,
        showlegend=False,
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#333333', size=12, family='Arial'),
        title_font=dict(size=16, color='#333333', family='Arial'),
        xaxis=dict(
            gridcolor='#e8eef5',
            zerolinecolor='#dee2e6',
            linecolor='#dee2e6'
        ),
        yaxis=dict(
            gridcolor='#e8eef5',
            zerolinecolor='#dee2e6',
            linecolor='#dee2e6'
        ),
        margin=dict(t=60, b=60, l=60, r=40)
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 6. 削減コスト推移（メディカルブルー）
    st.subheader(f"💰 {selected_hospital}の削減コスト推移")
    
    fig2 = px.line(
        hospital_df_copy,
        x='年月表示',
        y='削減コスト',
        title=f'{selected_hospital}の月次削減コスト推移',
        labels={'削減コスト': '削減コスト（円）', '年月表示': '年月'},
        markers=True,
        color_discrete_sequence=['#0056b3']
    )
    
    # エリアチャートに変更して清潔感を出す
    fig2.update_traces(
        line=dict(width=3, color='#0056b3'),
        marker=dict(size=8, color='#0056b3', line=dict(width=2, color='#ffffff')),
        fill='tozeroy',
        fillcolor='rgba(0, 86, 179, 0.1)'
    )
    
    fig2.update_layout(
        height=400,
        xaxis_tickangle=-45,
        plot_bgcolor='#ffffff',
        paper_bgcolor='#ffffff',
        font=dict(color='#333333', size=12, family='Arial'),
        title_font=dict(size=16, color='#333333', family='Arial'),
        xaxis=dict(
            gridcolor='#e8eef5',
            zerolinecolor='#dee2e6',
            linecolor='#dee2e6'
        ),
        yaxis=dict(
            gridcolor='#e8eef5',
            zerolinecolor='#dee2e6',
            linecolor='#dee2e6'
        ),
        margin=dict(t=60, b=60, l=60, r=40)
    )
    
    st.plotly_chart(fig2, use_container_width=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 7. 全病院の比較表
    st.markdown("---")
    st.subheader("🏥 全病院の最新月データ比較")
    
    # 各病院の最新データを取得
    latest_data = df.sort_values('年月').groupby('病院名').last().reset_index()
    latest_data_display = latest_data[['病院名', '購入額', '削減コスト']].copy()
    latest_data_display['削減率'] = (latest_data['削減コスト'] / latest_data['購入額'] * 100).round(1)
    
    # スタイリング用の関数
    def highlight_data(val):
        if isinstance(val, str):
            return ''
        if val > 15:
            return 'background-color: #d1ecf1; color: #0056b3; font-weight: 600'
        elif val > 10:
            return 'background-color: #d4edda; color: #155724; font-weight: 600'
        else:
            return 'background-color: #fff3cd; color: #856404; font-weight: 600'
    
    # データフレームの表示
    st.dataframe(
        latest_data_display.style.applymap(highlight_data, subset=['削減率']).format({
            '購入額': '¥{:,.0f}',
            '削減コスト': '¥{:,.0f}',
            '削減率': '{:.1f}%'
        }),
        use_container_width=True,
        height=250
    )
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # フッター
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: #6c757d; font-size: 0.85rem;'>"
        "© 2025 共同購買サービス | 経営分析ダッシュボード"
        "</div>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
