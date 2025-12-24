import streamlit as st

st.set_page_config(page_title='音乐播放器')
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
