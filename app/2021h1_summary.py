import streamlit as st
import pandas as pd
import plotly.express as px

if st.sidebar.checkbox('2021年半年工作总结'):

    st.title('2021年上半年工作总结！')
    st.markdown('# ')
    st.markdown('''
    ## 套期保值
    * 2021.2-2021.6套期保值。2021年6月平仓，共盈利1551万元。
        * 项目降本：
            * 为隆化项目平仓4110吨钢材，降本678元/吨
            * 为张北二期项目线缆平仓160吨铜，降本4668元/吨
    ## 商情分析
    * 商情分析月刊 **5**篇
    * 大宗物料价格趋势分析及通报**5**次
    * 周报**20**篇
    * 其他报告
        - 2021吊装市场评估
        - 股份公司月度报告的大宗物料价格分析部分
        - 2021 年组件市场分析&采购计划（与孙晓琦合写）
        - 《2021年第一季度新能源行业主要设备物资材料市场价格趋势分析及采购策略》（股份公司汇报材料，与郭部长合写）
    * 大宗物料价格曲线的更新

    ## 上半年读的书
    * 《需求预测和库存计划》
    * 《python机器学习基础教程》
    * 《采购与供应链管理：一个实践者的角度》
    * 《深入浅出统计学》
    * 《python数据科学手册》
    ## 其他方面的提升
    * 加强健身锻炼，争取9月相比现在体重下降5kg。
    * 继续学习python及统计学、概率学知识
    ## 问题
    * 套期保值方面：
        * 价格预警滞后
        * 套保量计算杂乱（制作统一的套保量计算模板）
        * 事业部反馈较慢（套保项目按供需统筹组月度统计量的70%计算）
        * 期权交易不熟练（看书学习，多参加相关培训）
    * 商情分析方面：
        * 负责风机、组件、铜、铝、钢材的趋势分析，加上套保工作，很难兼顾
        * 事业部经常有取价之类的需求，价格曲线利用效率低
    ## 下半年工作计划
    1. 关注大宗物料特别是钢材的宏观和供需变化，出现趋势性上涨迹象将再次申请套保
    2. 继续完成商情分析的例行工作
    3. 三季度完成铜、铝、钢材的预警和趋势分析系统
    4. 四季度完成风机、组件的预警和趋势分析系统


        ''')
  
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



