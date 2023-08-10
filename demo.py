import streamlit as st

# https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/

st.title('DS Career Analysis')
st.subheader(':blue[Dais OpenLab]')
st.caption('Member. 울산대학교 산업경영공학부 윤기창, 홍재민')

tab1, tab2, tab3, tab4, tab5 = st.tabs(['🖊️ Info', '🗂️ Skills of DS ▪️ DA ▪️ DE', '🔍 Find My Keyword', '✨ 채용공고 모음', '🏙️ 대기업 모음'])

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

    # 크롤링 진행 과정 
    # def file_upload(f):
    #     file_open = open(f'{f}', 'rb')
    #     file_read = file_open.read()
    #     return file_read
    
    st.subheader('채용공고 수집')
    st.markdown('원티드, 사람인, 잡플래닛, 인쿠르트 버튼을 선택하면, "#### 👇 NNN" 이 문구 띄우고 그 아래에 각각의 코드와 돌아가는 모습 보여주기')
    
    # st.markdown('#### 👇 wanted')
    # f = '/BTS2023/JJaemni/DS_Career_Analysis/Streamlit/wanted.mp4'
    # st.video(file_upload(f))
    
    st.markdown('---')
    
    # 텍스트 분석 진행 과정
    st.subheader('텍스트 분석')
    st.markdown('원티드, 사람인, 잡플래닛, 인쿠르트 버튼을 선택하면, "#### 👇 NNN" 이 문구 띄우고 그 아래에 각각의 코드와 돌아가는 모습 보여주고, 그 밑에 워드클라우드 보여주기')
    
    # f = '/BTS2023/JJaemni/DS_Career_Analysis/Streamlit/wanted.mp4'
    # st.video(file_upload(f))
    
    # f = 'TA_EDA.png'
    # st.image(file_upload(f))


with tab2:
    
    genre = st.radio(
    '관심있는 키워드를 선택해주세요.',
    ('데이터 사이언티스트', '데이터 애널리스트', '데이터 엔지니어'))

    if genre == '데이터 사이언티스트':
        st.markdown('버튼 선택 후 뜨도록')
        st.markdown('''
            0. 개발 언어
                - Python, ...
        ''')
        st.markdown('''
            1. 역량
                - 영어 및 한글
        ''')

    elif genre == '데이터 애널리스트':
        st.markdown('''
            0. 개발 언어
                - Python, ...
        ''')
        st.markdown('''
            1. 역량
                - 영어 및 한글
        ''')

    else:
        st.markdown('''
            0. 개발 언어
                - Python, ...
        ''')
        st.markdown('''
            1. 역량
                - 영어 및 한글
        ''')


with tab3:
    
    options = st.multiselect(
        '자신의 역량을 선택해주세요! (중복 선택 가능)',
        ['정형데이터 분석', '이미지 분석', '텍스트 분석', '웹 제작', '의사소통']
    )
    st.write('나의 역량 👇', options)
    st.markdown('나의 역량이 보인 후에, 이 위치 쯤에 버튼을 생성하고, 버튼을 누르면 자신에게 맞는 DS DA DE 키워드가 나오게 하기')
    
    
with tab4:
    
    genre = st.radio(
    '관심있는 키워드를 선택해주세요!',
    ('데이터 사이언티스트', '데이터 애널리스트', '데이터 엔지니어'))

    if genre == '데이터 사이언티스트':
        st.markdown('''
            버튼 선택 후 채용공고 뜨도록 
        ''')

    elif genre == '데이터 애널리스트':
        st.markdown('''
            버튼 선택 후 채용공고 뜨도록
        ''')

    else:
        st.markdown('''
            버튼 선택 후 채용공고 뜨도록
        ''')
        
        
with tab5:
    
    st.markdown('오늘의 대기업 채용공고 입니다!')
