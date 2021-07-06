import streamlit as st
import pandas as pd
import plotly.express as px

if st.sidebar.checkbox('2021年半年工作总结'):
    st.markdown('# stay tuned.')

   

       
if st.sidebar.checkbox('套期保值/商情分析的新世界'):
    st.write('**解决问题的关键在于生产效率的提高！**')
    st.subheader('**借助python，我们可以轻松的进行数据聚合、分析和绘图、预测价格**')
    money_cols=['']
    st.markdown('# 利用python建立web app解决问题')
    st.markdown('## 1. 数据聚合')
    st.markdown('## 2. 数据分析和绘图')
    dateparse = lambda x: pd.datetime.strptime(x, '%Y-%m-%d')
    @st.cache(allow_output_mutation=True)
    def get_data():
        fileloc='pv_forcast.csv'
        return pd.read_csv(fileloc,parse_dates=['index'],index_col=['index'],infer_datetime_format=True)
        
    df=get_data()
    df.index=pd.DatetimeIndex(df.index).date
    st.write('显示__pvinfolink__预测数据前五行')
    st.table(df.head(3))
    #st.write('选择绘图参数：')
    #time_filter=st.slider('选择显示时间', df.index[1], df.index[-1],df.index[1])
    selects=st.multiselect('选择你想要显示的预测数据',df.columns)
    line_chart=px.line(df,y=selects)
    st.plotly_chart(line_chart)
    st.markdown('## 3. 预测数据')
    st.markdown('''
        1.  应用场景1：设定阈值，自动预警并群发email到邮箱
        2.  应用场景2：利用训练好的模型，预测大宗物料价格
        3.  应用场景3：建立明晰的分析系统
        ''')
st.markdown('# stay cool')
st.markdown('# stay hungry')
st.markdown('# stay foolish')



