import streamlit as st

# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

st.title('DS Career Analysis')
st.subheader(':blue[Dais OpenLab]')
st.caption('Member. 울산대학교 산업경영공학부 윤기창, 홍재민')

tab1, tab2, tab3, tab4 = st.tabs(['🖊️ Info', '🗂️ Skills of DS ▪️ DA ▪️ DE', '🔍 Find My Keyword', '🏙️ 대기업 모음'])

with tab1:
    
    # 깃허브 링크
    st.caption('👉 [Github](https://github.com/DS-Career-Analysis)')
    
    # 프로젝트 설명
    st.markdown('''
        0. 프로젝트 설명
            - Data Scientist의 역량을 알아보기 위하여 채용공고의 정보를 크롤링하여 데이터 수집을 한 후, 텍스트 마이닝을 진행하였습니다.
    ''')
    
    # 채용공고 수집 사이트 4가지
    st.markdown('''
        1. 채용공고 수집 사이트
            - [wanted](https://www.wanted.co.kr/)
            - [saramin](https://www.saramin.co.kr)
            - [Jobplanet](https://www.jobplanet.co.kr)
            - [Incruit](http://www.incruit.com)
    ''')
    
    # 채용공고 수집 키워드 3가지
    st.markdown('''
        2. 채용공고 수집 키워드
            - 데이터 사이언티스트
            - 데이터 애널리스트
            - 데이터 엔지니어
    ''')
    
    # DS Career Analysis 기능 소개
    st.markdown('''
        3. 제공 기능
            - ...
            - ...
            - ...
    ''')
    
    st.markdown('---')

    # DS 워드클라우드
    # def file_upload(f):
    #     file_open = open(f'{f}', 'rb')
    #     file_read = file_open.read()
    #     return file_read
    
    st.subheader('데이터 사이언티스트 Wordcloud')
    st.markdown('이미지')
    
    st.markdown('---')

    st.subheader('데이터 애널리스트 Wordcloud')
    st.markdown('이미지')
    
    st.markdown('---')

    st.subheader('데이터 엔지니어 Wordcloud')
    st.markdown('이미지')
    
    st.markdown('---')
    
    # f = 'TA_EDA.png'
    # st.image(file_upload(f))


with tab2:
    
    genre = st.radio(
    '관심있는 키워드를 선택해주세요.',
    ('데이터 사이언티스트', '데이터 애널리스트', '데이터 엔지니어'))

    if genre == '데이터 사이언티스트':
        st.markdown('버튼 선택 후 1가지 키워드 뜨도록')
        st.markdown('''
            0. 개발 언어
                - Python, ...
        ''')

        st.markdown('3가지 다 워드클라우드 띄우기')
        
        st.markdown('''
            1. 역량
                - 자격요건
                - 우대사항
                - 기술스택
        ''')

    elif genre == '데이터 애널리스트':
        st.markdown('''
            0. 개발 언어
                - Python, ...
        ''')
        st.markdown('''
            1. 역량
                - 자격요건
                - 우대사항
                - 기술스택
        ''')

    else:
        st.markdown('''
            0. 개발 언어
                - Python, ...
        ''')
        st.markdown('''
            1. 역량
                - 자격요건
                - 우대사항
                - 기술스택
        ''')


with tab3:
    
    options = st.multiselect(
        '자신의 역량을 선택해주세요! (중복 선택 가능)',
        ['정형데이터 분석', '이미지 분석', '텍스트 분석', '웹 제작', '의사소통']
    )
    st.write('나의 역량 👇', options)
    st.markdown('역량에 맞게 채용공고 보여주기')
            
        
with tab4:
    
    st.markdown('오늘의 대기업 채용공고 입니다!')
