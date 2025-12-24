import streamlit as st

st.set_page_config(page_title='时代巡演纪录片')

#st.title(video_arr[st.session_state['ind']]['title'])

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
