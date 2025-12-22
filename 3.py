import streamlit as st

st.set_page_config(page_title='五大diva', page_icon='🐒')

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
