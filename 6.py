import streamlit as st
from datetime import datetime, timedelta

st.set_page_config(page_title='个人简历生成器',layout="wide")
st.title("个人简历生产器")
st.text('使用streamlit创建你的个性化简历')

c1,c2=st.columns([1,2])
with c1:
    user_name=st.text_input('姓名')
    user_job=st.text_input('期望职位')
    user_phone=st.text_input('手机号码')
    user_email=st.text_input('邮箱')
    csrq = st.date_input("选择一个日期", value=None)
    st.text('性别')
    mf = st.radio(
        '你的性别是什么',
        ['男', '女', '其他'],
        horizontal=True,
        label_visibility='hidden'
        )
    st.text('学历')
    xl = st.selectbox(
        '学历',
        ['初中', '高中', '中专', '大专', '本科', '硕士', '博士'],
        label_visibility='hidden'
        )
    st.text('语言能力（可多选）')
    yynl = st.multiselect(
        '你的语言能力',
        ['中文', '英语', '法语', '泰语', '韩语', '西班牙语'],
        )
    st.text('技能（可多选）')
    jn = st.multiselect(
        '你的技能',
        ['Java', 'C++', 'python', 'photoshop', 'AutoCAD', '数据分析','HTML/CSS'],
        )
    st.text('工作经验（年）')
    jy = st.slider('工作经验', 0,30,1)
    st.text('期望薪资（元）')
    xz= st.slider(
    '选择你的薪资范围',
    0,500000,(0,3000)
    )
    jj=st.text_area(label='个人简介:',placeholder='请输入个人简介')
    time=st.time_input('最佳联系实际')
    uploaded_file=st.file_uploader("上传个人证件照",type=["jpg","jpeg","png"])



with c2:
    st.title('姓名：'+user_name)
    st.text('期望职位：'+user_job)
    st.text('手机电话：'+user_phone)
    st.text('电子邮箱：'+user_email)
    st.text('出生日期：')
    st.text(csrq)
    st.text('性别：'+mf)
    st.text('学历：'+xl)
    st.text('语言能力:',)
    st.text(yynl)
    st.text('技能:',)
    st.text(jn)
    st.text('工作经验（年）：')
    st.text(jy)
    st.text('薪资范围（元）：')
    st.text(xz)
    st.text('个人简介：'+jj)
    st.text('最佳联系时间：')
    st.text(time)
