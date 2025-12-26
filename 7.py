import streamlit as st
import pandas as pd
import numpy as np

page = st.sidebar.selectbox("选择页面", ["首页","音乐播放器", "个人简历生成器", "五大Diva", "时代巡演纪录片", "南宁美食图鉴", "数字档案"])

if page == "首页":
    st.title("主页")
    st.image("https://pic.rmb.bdstatic.com/bjh/events/c4c70e5a92e514d66799b566830429d0651.jpeg@h_1280")
    st.write("泰勒·斯威夫特（Taylor Swift），1989年12月13日出生于美国宾夕法尼亚州，美国女歌手、词曲作者、音乐制作人、演员。2006年，发行个人首张音乐专辑《Taylor Swift》 [1]。2008年，凭借音乐专辑《Fearless》获得广泛关注 [2]，该专辑亦获得第52届格莱美奖“年度专辑奖”等奖项 [3]，成为史上获奖最多的乡村专辑 [138]。2010年-2012年间，相继发行融合多种风格的音乐专辑《Speak Now》《Red》 [139] [235]。2014年，转战流行乐并发行音乐专辑《1989》 [4]，打破12年内美国唱片市场的单周销量最高纪录 [5]，并获得第58届格莱美奖“年度专辑奖” [140]。2017年，发行音乐专辑《reputation》 [7]，并因此成为首位拥有四张首周百万销量专辑的歌手 [147]。2019年，发行音乐专辑《Lover》 [142]，并因此获得第47届全美音乐奖“年度艺人奖”等六个奖项 [123]、第36届MTV音乐录影带奖“年度录影带奖”等三个奖项 [10]；同年，因版权纠纷决定重录前6张音乐专辑 [138]。2020年，发行音乐专辑《folklore》《evermore》 [14-15]，前者获得第63届格莱美奖“年度专辑奖” [88] [122] [143]。 [145]2025年12月，泰勒·斯威夫特荣登《福布斯》杂志“全球最具影响力女性”榜单并登上封面，泰勒在全球总榜中位列第21名。 [462]泰勒共拥有7张首周销量超百万的音乐专辑 [148]、14张公告牌200强专辑榜冠军专辑、12首公告牌百强单曲榜冠军单曲 [149]，获得14座格莱美奖 [150]，亦是获得全美音乐奖最多的歌手（40座） [151]。作为音乐创作人，她创作了所有原唱歌曲，歌词私人化、旋律抓耳 [145]。作为行业领头人，她亦维护其他音乐人的权益 [152]。")
    
elif page == "音乐播放器":
    st.header("♪简易音乐播放器")
    st.text("使用Seamlit制作的简单音乐播放器，支持切歌和基本音乐播放与控制")
    # 音乐数组
    music_ur1= [
        {
           'musicur1': 'https://music.163.com/song/media/outer/url?id=28033745.mp3',
           'imgur1':'http://p1.music.126.net/rhDrdkvsZ-RSelQuPSzA9w==/109951170215770688.jpg?param=130y130',
           'text':'All I Want For Christmas Is You',
           'text1':'歌手：Mariah Carey'
            },
        {
           'musicur1': 'https://music.163.com/song/media/outer/url?id=1999170057.mp3',
           'imgur1':'http://p1.music.126.net/bYz6Tmye6r3hKDZsfSAKuA==/109951168066873279.jpg?param=130y130',
           'text':'Christmas List',
           'text1':'歌手：Anson Seabra'
            },
        {
           'musicur1': 'https://music.163.com/song/media/outer/url?id=2217955.mp3',
           'imgur1':'http://p1.music.126.net/DG8_ia-NKWLYENbThswdyw==/109951169332000399.jpg?param=130y130',
           'text':"Rockin' Around The Christmas Tree",
           'text1':'歌手：Brenda Lee'
            },
        ]


    if 'ind' not in st.session_state:
        st.session_state['ind']=0

         
    c1,c2=st.columns(2)

    def lastMusic():
        st.session_state['ind']=(st.session_state['ind']-1)%len(music_ur1)
    
    def nextMusic():
        st.session_state['ind']=(st.session_state['ind']+1)%len(music_ur1)

    with c1:
        st.image(music_ur1[st.session_state['ind']]['imgur1'])
        st.text("专辑封面")

    with c2:
        st.text(music_ur1[st.session_state['ind']]['text'])
        st.text(music_ur1[st.session_state['ind']]['text1'])
        st.audio(music_ur1[st.session_state['ind']]['musicur1'])
        c11,c22=st.columns(2)
        with c11:
            st.button('上一首',use_container_width=True,on_click=lastMusic)
        with c22:
            st.button('下一首',use_container_width=True,on_click=nextMusic)




    
elif page == "个人简历生成器":
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


elif page == "五大Diva":
    # 图片数组
    image_ua= [
        {
           'ur1': 'https://i8.amplience.net/i/naras/Taylor-Swift-2024-GettyImages-2181107453.jpg',
           'text':'taylor swift'
            },
        {
           'ur1': 'https://a57.foxnews.com/static.foxnews.com/foxnews.com/content/uploads/2024/02/1200/675/katy-perry.jpg?ve=1&tl=1',
           'text':'katy perry'
            },
        {
           'ur1': 'https://www.rollingstone.com/wp-content/uploads/2022/10/rihanna-new-song.jpg?w=1600&h=900&crop=1',
           'text':'rihanna'
            },
        {
            'ur1':'https://ourculturemag.com/wp-content/uploads/2025/01/lady-gaga-e1737995824174.jpg',
            'text':'lady gaga'
            },
        {
            'ur1':'https://ts1.tc.mm.bing.net/th/id/R-C.a41d736a88cebceb85abbbe3d33dfd6a?rik=JGU2dZN9drTF8w&riu=http%3a%2f%2fi2.hdslb.com%2fbfs%2farchive%2f6422c6c41f6dd3c7cb2d9d9abcc410bdbd49a2c1.png&ehk=5%2fkhd4bOVnbaNiASmc0WY4J0nksuFDaov6cltD2Fub4%3d&risl=&pid=ImgRaw&r=0',
            'text':'adele'
            },
        ]

    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    st.image(image_ua[st.session_state['ind']]['ur1'],caption=image_ua[st.session_state['ind']]['text'])
         
    c1,c2=st.columns(2)

    def lastImg():
        st.session_state['ind']=(st.session_state['ind']-1)%len(image_ua)
    
    def nextImg():
        st.session_state['ind']=(st.session_state['ind']+1)%len(image_ua)

    with c1:
        st.button('上一张',use_container_width=True,on_click=lastImg)

    with c2:
        st.button('下一张',use_container_width=True,on_click=nextImg)

    
elif page == "时代巡演纪录片":
    video_arr=[
        {
            'ur1':'https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/18/25/34914042518/34914042518-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&gen=playurlv3&os=cosovbv&og=hw&oi=771356656&trid=6020a19bbf264379ae426ca3c955302h&mid=0&uipk=5&deadline=1766565349&nbs=1&platform=html5&upsig=e6003543cbbca1a38be4c9ad759ebb7a&uparams=e,gen,os,og,oi,trid,mid,uipk,deadline,nbs,platform&bvc=vod&nettype=0&bw=725834&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
            'title':'时代巡演纪录片EP01 - Welcome To The Eras Tour | 欢迎来到时代巡演'
            },
        {
            'ur1':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/33/51/34841035133/34841035133-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&deadline=1766569715&platform=html5&og=hw&oi=1782047712&nbs=1&trid=00005727284cfd8449ac8b670c562f30537h&mid=0&uipk=5&gen=playurlv3&os=bcache&upsig=71b7ea3ef2aebe17a01cd3a9a8c93488&uparams=e,deadline,platform,og,oi,nbs,trid,mid,uipk,gen,os&cdnid=61310&bvc=vod&nettype=0&bw=730224&f=h_0_0&agrr=1&buvid=&build=0&dl=0&orderid=0,1',
            'title':'时代巡演纪录片EP02 - Magic in the Eras | 时代中的魔法'
            },
        {
            'ur1':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/72/83/34843198372/34843198372-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&mid=0&og=cos&nbs=1&oi=1782047712&deadline=1766569741&trid=0000546157179f6c484d8af6dd508a012aah&gen=playurlv3&os=bcache&uipk=5&platform=html5&upsig=7305e6ec375025cb7da46ff3e3fbd893&uparams=e,mid,og,nbs,oi,deadline,trid,gen,os,uipk,platform&cdnid=60902&bvc=vod&nettype=0&bw=781570&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
            'title':'时代巡演纪录片EP03 - Kismet | 命中注定'
            },
        {
            'ur1':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/07/62/34844446207/34844446207-1-192.mp4?e=ig8euxZM2rNcNbRVhWdVhwdlhWd1hwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&platform=html5&oi=1782047712&trid=0000341f17ffb1004df29e645f7efede623h&nbs=1&uipk=5&os=bcache&og=ali&deadline=1766569757&mid=0&gen=playurlv3&upsig=5319122152d4f257999e1dad02881d49&uparams=e,platform,oi,trid,nbs,uipk,os,og,deadline,mid,gen&cdnid=61312&bvc=vod&nettype=0&bw=813638&buvid=&build=0&dl=0&f=h_0_0&agrr=1&orderid=0,1',
            'title':'时代巡演纪录片EP04 - Thank You For The Lovely Bouquet | 谢谢你送我这束漂亮的花'
            },
        {
            'ur1':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/89/17/34929051789/34929051789-1-192.mp4?e=ig8euxZM2rNcNbRVhwdVhwdlhWdVhwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=bcache&og=ali&oi=1782047712&mid=0&nbs=1&platform=html5&trid=00002848b5ac45084980a3193ce9fe8a4f2h&deadline=1766569771&uipk=5&gen=playurlv3&upsig=383e77eb46645710dc3ff9c5ba82293c&uparams=e,os,og,oi,mid,nbs,platform,trid,deadline,uipk,gen&cdnid=61310&bvc=vod&nettype=0&bw=715542&agrr=1&buvid=&build=0&dl=0&f=h_0_0&orderid=0,1',
            'title':'时代巡演纪录片EP05 - Marjorie | 玛乔丽'
            },
        {
            'ur1':'https://upos-sz-mirrorcos.bilivideo.com/upgcxcode/62/90/34929969062/34929969062-1-192.mp4?e=ig8euxZM2rNcNbRV7zdVhwdlhWdahwdVhoNvNC8BqJIzNbfq9rVEuxTEnE8L5F6VnEsSTx0vkX8fqJeYTj_lta53NCM=&os=bcache&og=hw&trid=000048f788d959204be4a141aca379c0d39h&platform=html5&oi=1782047712&mid=0&deadline=1766569786&uipk=5&nbs=1&gen=playurlv3&upsig=24cb75408da49f96ddfa850306b70a32&uparams=e,os,og,trid,platform,oi,mid,deadline,uipk,nbs,gen&cdnid=61310&bvc=vod&nettype=0&bw=862593&dl=0&f=h_0_0&agrr=1&buvid=&build=0&orderid=0,1',
            'title':'时代巡演纪录片EP06 - Remember This Moment | 铭记这个时刻'
            }

    ]

    if 'ind' not in st.session_state:
        st.session_state['ind']=0

    st.title(video_arr[st.session_state['ind']]['title'])
    st.video(video_arr[st.session_state['ind']]['ur1'])

    def playVideo(e):
        #修改ind的值
        st.session_state['ind']=int(e)

    c=st.columns(len(video_arr))

    for i,cc in enumerate(c):
        with cc:
            st.button(
                f"第{i+1}集",
                key=f"btn_{i}",
                on_click=playVideo,
                args=(i,),
                use_container_width=True
            )

    st.markdown('***')
    st.header("视频简介")
    st.text('这部纪录片史诗般地记录了一个文化现象的时代终章——“时代巡回演唱会”的收官之战。影片不仅完整呈现了在温哥华举办的最终场震撼演出，更以前所未有的幕后视角，深入这场历时近两年、跨越五大洲、吸引了超过10,000,000名现场观众的传奇巡演。从应对恐怖袭击威胁后的情感挣扎，到为融入新专辑《The Tortured Poets Department》而进行的顶级机密排练，它见证了巨星泰勒如何在巨大的压力下，坚持为粉丝呈现一场极致的表演，最终写下流行音乐史上最浓墨重彩的一笔。')



elif page == "南宁美食图鉴":
    st.header("🍲南宁美食探索")
    st.text("探索广西南宁最受欢迎的美食地点！选择你感兴趣的餐厅类型，查看评分和位置。")
    st.subheader("📍南宁美食地图")

    map_data={
        "latitude": [22.811045, 22.867965, 22.843267, 22.809343, 22.811859],
        "longitude": [108.388877,108.250785, 108.268211, 108.373935, 108.392082]
        }
    mapd=pd.DataFrame(map_data)

    st.map(mapd)


    st.subheader("⭐️餐厅评分")

    # 定义数据,以便创建数据框
    fen_data = {
        "餐厅":["新天海南鸡饭(石门公园店)", "广西壮锦博物馆艺术主题餐厅·广西菜","胜记海鲜煲仔粥(动物园店)","樾餐厅泰式海鲜火锅(民歌湖店)","焱铁烧·黑毛和牛专门店(南宁万象城店)"],
        "评分":[4.0,4.8,4.3,5.0,4.4]

    }
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(fen_data)
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3,4,5], name='评分')
    # 将新索引应用到数据框上
    df.index = index


    # 通过x指定月份所在这一列为条形图的x轴
    st.bar_chart(df, x='餐厅')


    st.subheader("🕐用餐高峰时段")
    can_data={
        "餐厅":["新天海南鸡饭(石门公园店)", "广西壮锦博物馆艺术主题餐厅·广西菜","胜记海鲜煲仔粥(动物园店)","樾餐厅泰式海鲜火锅(民歌湖店)","焱铁烧·黑毛和牛专门店(南宁万象城店)"],
        '12点':[150,140,30,54,144],
        '13点':[160,150,200,145,121],
        '14点':[59,98,140,54,63],
        '15点':[40,55,66,41,25],
        '16点':[50,60,71,55,94],
        '17点':[154,244,156,225,156],
        '18点':[200,251,354,125,156],
        '19点':[156,145,135,145,126],
        '20点':[125,114,101,92,158],
        '21点':[50,46,55,80,93],
        '22点':[23,12,60,35,14],
    }
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(can_data)
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3,4,5], name='12点')
    # 将新索引应用到数据框上
    df.index = index



# 通过x指定月份所在这一列为面积图的x轴
    st.area_chart(df, x='餐厅')



    st.subheader("💹餐厅1-12月价格走势")
    # 定义数据,以便创建数据框
    data = {
        '月份':['01月', '02月', '03月', '04月', '05月', '06月', '07月', '08月', '09月', '10月', '11月', '12月'],
        '新天海南鸡饭(石门公园店)':[200, 150, 180,102,111,445,125,425,141,415,452,421],
        '广西壮锦博物馆艺术主题餐厅·广西菜':[120, 160, 123,111,514,112,254,154,136,142,152,114],
        '胜记海鲜煲仔粥(动物园店)':[110, 100, 160,178,169,166,415,152,141,471,145,141],
        '樾餐厅泰式海鲜火锅(民歌湖店)':[14,14,12,12,13,10,15,16,14,14,14,12],
        '焱铁烧·黑毛和牛专门店(南宁万象城店)':[22,52,34,35,36,36,41,55,45,16,45,12],
    }
    # 根据上面创建的data，创建数据框
    df = pd.DataFrame(data)
    # 定义数据框所用的新索引
    index = pd.Series([1, 2, 3,4,5,6,7,8,9,10,11,12], name='序号')
    # 将新索引应用到数据框上
    df.index = index

    # 使用write()方法展示数据框
    st.write(df)

    # 通过x指定月份所在这一列为折线图的x轴
    st.line_chart(df, x='月份')


    # 修改df，用月份列作为df的索引，替换原有的索引
    df.set_index('月份', inplace=True)


else:
    st.title("🗄️学生 秋葵-教学档案")
    st.header("ℹ️基础信息")
    st.text("学生ID：U22053020222541")
    st.markdown("注册时间：:green[2022.09.12] |精神状态：✅良好")
    st.markdown("当前教室：:green[实训楼710] |安全等级：:green[满级]")

    st.header("📊技能矩阵")
    c1, c2, c3 = st.columns(3)# 定义列布局，分成3列
    c1.metric(label="中文", help="语言类", value="100%", delta="0%")
    c2.metric(label="英语", help="语言类",value="80%", delta="-20%")
    c3.metric(label="泰语", help="语言类",value="65%", delta="-35%")

    st.subheader("⏩️课程进度")
    st.text("进度")
    st.header("✍任务日志")
    # 定义数据,以便创建数据框
    data = {
        '学习任务':['中文', '英文', '泰语', '俄语',' 法语'],
        '任务状态':['✅️已完成', '🕐进行中', '🕐进行中', '🕐进行中', '❎️未完成'],
        '任务难度':['★⛤⛤⛤⛤', '★★★⛤⛤', '★★★⛤⛤',' ★★★★⛤',' ★★★⛤⛤'],
    }
    # 定义数据框所用的索引
    index = pd.Series(['01', '02', '03', '04', '05'], name='任务序号')
    # 根据上面创建的data和index，创建数据框
    df = pd.DataFrame(data, index=index)

    st.table(df)

    st.subheader("🔐最新代码成果")

    python_code = '''def hello():
        print("你好，老师！")
    '''
    st.code(python_code)

    # 分割线
    st.markdown('***')

    st.markdown(":green[SYSTEM MESSAGE:]下一个任务目标已解锁")
    st.markdown(":green[TARGET:]韩语")
    st.markdown(":green[COUNTDOWN:]2025-12-18 15:50:22")
    st.text("系统状态：在线   连接状态：已加密")

