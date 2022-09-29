import streamlit as st
import pandas as pd
import numpy as np
#====================================== IMPLEMENTATION 1 START ===========================================

# st.write("Test app")
# st.markdown(f'<iframe src="https://spinzam.com/shot/embed/?idx=351919" width="500" height="500" frameborder="0" scrolling="no" style="max-width:100%; max-height:100vw;"></iframe>', unsafe_allow_html=True)


#====================================== IMPLEMENTATION 1 END ===========================================

#--------------------------------------------------------------------------------------------------------------------------------------

#====================================== IMPLEMENTATION 2 START ===========================================
st.set_page_config(layout="wide")
st.title("Test app - Training Template")
st.write("Text in the image can be hyperlinked with media")
col1, col2, col3 = st.columns(3)
with col1:
   #st.header("A cat")
   st.markdown(f'<iframe src="https://spinzam.com/shot/embed/?idx=351919" width="500" height="500" frameborder="0" scrolling="no" style="max-width:100%; max-height:100vw;"></iframe>', unsafe_allow_html=True)
with col2:
   #st.header("A dog")
   st.image('cable.jpg')
with col3:
   #st.header("An owl")
   st.image('cpu.jpg')

numpy_array = np.array([['1','info/hyperlink on 1'],
                        ['3','info on 3'],
                        ['4', 'info on 4'],
                        ['5','info/hyperlink on 5'],
                        ['application/process - 1','info on application/process - 1'],
                        ['application/process - 2','info on application/process - 2'],
                        ['application/process - 3','info on application/process - 3'],
                        ['application/process - 4','info on application/process - 4']])

tableData = pd.DataFrame(numpy_array,columns=['image annotation','description'])

secondCol1, secondCol2 = st.columns(2)

with secondCol1:
    #video_file = open('https://pixabay.com/en/videos/star-long-exposure-starry-sky-sky-6962/', 'rb')
    #video_bytes = video_file.read()
    st.markdown("**xyz instructions**")
    st.video('https://pixabay.com/en/videos/star-long-exposure-starry-sky-sky-6962/')

with secondCol2:
    st.table(tableData)


#====================================== IMPLEMENTATION 2 END ===========================================
