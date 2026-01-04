import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder


st.set_page_config(
    page_title="学生成绩分析与预测系统",
    page_icon="🎓",
    layout="wide"
)

with st.sidebar:
    st.title('🎓 导航菜单')
    page = st.radio(
        "选择功能模块",
        ("项目介绍", "专业数据分析", "成绩预测")
    )


def generate_student_data():
    """生成模拟学生数据，确保代码独立运行"""
    majors = ['大数据管理', '计算机科学', '信息系统', '软件工程', '人工智能']
    genders = ['男', '女']
    # 固定随机种子，保证数据可复现
    np.random.seed(42)
    data = {
        '学号': [f'2023{str(i).zfill(4)}' for i in range(1, 201)],
        '性别': np.random.choice(genders, 200, p=[0.55, 0.45]),
        '专业': np.random.choice(majors, 200),
        '每周学习时长': np.random.randint(8, 30, 200),
        '上课出勤率': np.round(np.random.uniform(0.7, 0.98, 200), 2),
        '期中考试分数': np.random.randint(50, 95, 200),
        '作业完成率': np.round(np.random.uniform(0.6, 0.99, 200), 2),
        '期末考试分数': np.random.randint(55, 98, 200)
    }
    return pd.DataFrame(data)

# 生成数据
df = generate_student_data()


if page == "项目介绍":
    st.title("📚 学生成绩分析与预测系统")
    st.markdown('---')

    # 项目概述
    col1, col2 = st.columns([4, 2])
    with col1:
        st.markdown('## 项目概述')
        st.write("""
        本系统基于Streamlit开发，面向教育管理者和教师，提供学生成绩的多维度分析与智能预测功能。
        无需复杂操作，即可快速洞察不同专业、不同维度的学习数据特征，并预测学生期末成绩。
        """)
        st.markdown('### 核心功能')
        st.markdown('''
        - 📊 **数据可视化**：用原生图表展示专业、性别、成绩等维度数据
        - 📈 **专业分析**：按专业统计学习时长、出勤率、成绩等核心指标
        - 🎯 **成绩预测**：基于机器学习模型预测学生期末成绩
        - 📋 **数据报表**：导出/查看核心数据表格
        ''')
    with col2:
        st.markdown("### 系统特点")
        st.info("""
        ✅ 无需安装额外可视化库
        ✅ 纯Python代码，开箱即用
        ✅ 模拟数据，无外部依赖
        ✅ 适配Windows系统
        """)

    st.markdown('---')

    # 项目目标
    st.markdown('## 🎯 项目目标')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('### 分析影响因素')
        st.write("""
        - 识别学习时长、出勤率等关键指标
        - 探索指标与成绩的相关性
        - 为教学决策提供数据支撑
        """)
    with col2:
        st.markdown('### 可视化展示')
        st.write("""
        - 专业间数据对比分析
        - 性别差异可视化
        - 成绩分布趋势展示
        """)
    with col3:
        st.markdown('### 智能预测')
        st.write("""
        - 线性回归模型预测成绩
        - 个性化成绩反馈
        - 不及格预警提示
        """)

    st.markdown('---')

    # 技术架构
    st.markdown('## 🔧 技术架构')
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown('### 前端框架')
        st.code('Streamlit\n- 快速构建网页应用\n- 原生组件丰富\n- 无需前端知识', language='text')
    with col2:
        st.markdown('### 数据处理')
        st.code('Pandas / NumPy\n- 数据清洗与统计\n- 随机数据生成\n- 特征工程处理', language='text')
    with col3:
        st.markdown('### 机器学习')
        st.code('Scikit-learn\n- 线性回归模型\n- 标签编码\n- 预测结果输出', language='text')


elif page == "专业数据分析":
    st.title("📊 专业数据分析")
    st.markdown('---')

    # 1. 核心数据总览
    st.subheader("1. 各专业核心数据总览")
    major_stats = df.groupby('专业').agg({
        '每周学习时长': 'mean',
        '上课出勤率': 'mean',
        '期中考试分数': 'mean',
        '期末考试分数': 'mean'
    }).round(2)
    major_stats.columns = ['每周平均学时', '平均出勤率', '期中平均分', '期末平均分']
    # 展示数据表格
    st.dataframe(major_stats, use_container_width=True)
    # 数据导出按钮
    csv = major_stats.to_csv(index=True).encode('utf-8')
    st.download_button(
        label="📥 导出核心数据",
        data=csv,
        file_name="各专业核心数据.csv",
        mime="text/csv"
    )

    st.markdown('---')

    # 2. 各专业性别分布（原生柱状图）
    st.subheader("2. 各专业性别分布")
    gender_count = df.groupby(['专业', '性别']).size().unstack(fill_value=0)
    gender_count = gender_count[['女', '男']] if '女' in gender_count.columns else gender_count
    st.bar_chart(gender_count, use_container_width=True, color=["#4A90E2", "#50C878"])
    # 性别比例说明
    st.markdown("### 性别比例统计（%）")
    total = gender_count.sum(axis=1)
    ratio = (gender_count / total * 100).round(1)
    st.dataframe(ratio, use_container_width=True)

    st.markdown('---')

    # 3. 期中/期末成绩对比（原生折线图）
    st.subheader("3. 各专业期中/期末成绩对比")
    score_data = df.groupby('专业')[['期中考试分数', '期末考试分数']].mean().round(1)
    st.line_chart(score_data, use_container_width=True, color=["#F5A623", "#2ECC71"])
    # 成绩差值计算
    score_data['成绩变化'] = score_data['期末平均分'] - score_data['期中平均分']
    st.markdown("### 成绩变化统计")
    st.dataframe(score_data[['期中平均分', '期末平均分', '成绩变化']], use_container_width=True)

    st.markdown('---')

    # 4. 各专业出勤率分析
    st.subheader("4. 各专业平均出勤率")
    attendance_data = df.groupby('专业')['上课出勤率'].mean().round(2)
    st.bar_chart(attendance_data, use_container_width=True, color="#6A5ACD")
    # 出勤率排名
    st.markdown("### 出勤率排名（从高到低）")
    st.dataframe(
        attendance_data.sort_values(ascending=False).reset_index(),
        use_container_width=True,
        column_config={
            '专业': '专业名称',
            '上课出勤率': st.column_config.NumberColumn('平均出勤率', format="%.2f")
        }
    )

    st.markdown('---')

    # 5. 大数据管理专业专项分析
    st.subheader("5. 大数据管理专业专项分析")
    if '大数据管理' in df['专业'].unique():
        bd_data = df[df['专业'] == '大数据管理']
        bd_stats = bd_data[['上课出勤率', '期末考试分数', '每周学习时长']].mean().round(2)
        
        # 核心指标卡片
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("平均出勤率", f"{bd_stats['上课出勤率']:.2f}", delta=f"{(bd_stats['上课出勤率']-df['上课出勤率'].mean()):.2f}")
        with col2:
            st.metric("期末平均分", f"{bd_stats['期末考试分数']:.1f}分", delta=f"{(bd_stats['期末考试分数']-df['期末考试分数'].mean()):.1f}")
        with col3:
            st.metric("每周平均学时", f"{bd_stats['每周学习时长']:.1f}小时", delta=f"{(bd_stats['每周学习时长']-df['每周学习时长'].mean()):.1f}")

        # 成绩等级分布
        st.markdown('### 成绩等级分布')
        score_bins = [0, 60, 70, 80, 90, 100]
        score_labels = ['不及格', '及格', '中等', '良好', '优秀']
        bd_data['成绩等级'] = pd.cut(bd_data['期末考试分数'], bins=score_bins, labels=score_labels)
        score_dist = bd_data['成绩等级'].value_counts()
        st.bar_chart(score_dist, use_container_width=True, color="#3498DB")
    else:
        st.warning("⚠️ 未找到'大数据管理'专业数据")


else:
    st.title("🎯 期末成绩预测")
    st.markdown('---')
    st.write("输入学生信息，系统将基于线性回归模型预测期末成绩（60分及以上为及格）")

    # 表单输入
    with st.form("prediction_form", clear_on_submit=False):
        col1, col2 = st.columns(2)
        with col1:
            student_id = st.text_input("📝 学号", placeholder="例如：20230001")
            gender = st.selectbox("👤 性别", ["男", "女"])
            major = st.selectbox("🎓 专业", df['专业'].unique())
        with col2:
            study_hours = st.number_input("⏰ 每周学习时长（小时）", min_value=0, max_value=40, value=15, step=1)
            attendance = st.number_input("📈 上课出勤率（0-1）", min_value=0.0, max_value=1.0, value=0.85, step=0.01)
            midterm = st.number_input("📚 期中考试分数", min_value=0, max_value=100, value=70, step=1)
            homework = st.number_input("✅ 作业完成率（0-1）", min_value=0.0, max_value=1.0, value=0.9, step=0.01)
        
        submit_btn = st.form_submit_button("🚀 预测期末成绩", type="primary")

    # 预测逻辑
    if submit_btn:
        # 数据预处理（编码分类变量）
        le_gender = LabelEncoder()
        le_major = LabelEncoder()
        X = df.copy()
        X['性别'] = le_gender.fit_transform(X['性别'])
        X['专业'] = le_major.fit_transform(X['专业'])
        
        # 选择特征和目标变量
        features = ['性别', '专业', '每周学习时长', '上课出勤率', '期中考试分数', '作业完成率']
        X_train = X[features]
        y_train = X['期末考试分数']

        # 训练线性回归模型
        model = LinearRegression()
        model.fit(X_train, y_train)

        # 输入数据编码
        input_gender = le_gender.transform([gender])[0]
        input_major = le_major.transform([major])[0]
        input_data = np.array([[input_gender, input_major, study_hours, attendance, midterm, homework]])

        # 预测成绩并限制范围
        pred_score = model.predict(input_data)[0]
        pred_score = np.clip(round(pred_score, 1), 0, 100)

        # 结果展示
        st.markdown('---')
        st.subheader(f"📊 预测结果")
        col1, col2 = st.columns([1, 2])
        with col1:
            if pred_score >= 60:
                st.success(f"🎉 预测成绩：{pred_score}分")
                st.write("✅ 成绩及格")
            else:
                st.warning(f"😞 预测成绩：{pred_score}分")
                st.write("❌ 成绩未及格")
        with col2:
            st.markdown("### 📋 预测依据")
            st.write(f"""
            - 专业：{major}（该专业期末平均分：{df[df['专业']==major]['期末考试分数'].mean():.1f}分）
            - 每周学习时长：{study_hours}小时（参考均值：{df['每周学习时长'].mean():.1f}小时）
            - 出勤率：{attendance}（参考均值：{df['上课出勤率'].mean():.2f}）
            - 期中成绩：{midterm}分（参考均值：{df['期中考试分数'].mean():.1f}分）
            """)
        
        # 学习建议
        st.markdown('---')
        st.markdown("### 💡 学习建议")
        if pred_score < 60:
            st.info("""
            建议增加每周学习时长（至少达到该专业平均水平），提高上课出勤率，
            重点复习期中考试错题，保证作业完成率100%，可有效提升期末成绩。
            """)
        else:
            st.info("""
            保持当前学习节奏，建议适当总结学习方法，巩固优势知识点，
            可尝试帮助同学共同进步，进一步提升成绩稳定性。
            """)
