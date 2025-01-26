# import libraries
import pandas as pd
import streamlit as st 
import plotly.express as px 
st.set_page_config(page_title="Tips Dashboard", page_icon=None,
layout="wide", initial_sidebar_state="expanded",
)
# loading data
df= pd.read_csv('tip.csv')

#sidebar
st.sidebar.header("Tips Dashboard")
st.sidebar.image('tips.jpeg')
st.sidebar.write("This dashboard is using Tips dataset fromseaborn for educatidnal purposes.")
st.sidebar.write("")
st.sidebar.write("Filter Your Data:")
cat_filter =st.sidebar.selectbox("Categorical Filtering",[None,'sex','smoker','day','time'])
num_filter =st.sidebar.selectbox("Numerical Filtering",[None,'total_bill','tip'])
row_filter =st.sidebar.selectbox("Row Filtering",[None,'sex','smoker','day','time'])
col_filter=st.sidebar.selectbox("Col Filtering",[None,'sex','smoker','day','time'])


st.sidebar.write("")
st.sidebar.markdown("Made With :heart_eyes:  by Eng. [Mohamed Babikir](https://www.linkedin.com/in/mohamed-abdalbasit-b185bb262/)")



# body

#row a
a1,a2,a3,a4 = st.columns(4)
a1.metric("Max. Total Bill",df['total_bill'].max())
a2.metric("Max. Tip",df['tip'].max())
a3.metric("Min. Total Bill",df['total_bill'].min())
a4.metric("Min. Tip",df['tip'].min())


#row b
st.write(" ")
st.subheader("Total Bill Vs. Tips")
fig = px.scatter(data_frame=df, x='total_bill',
                 y='tip',color=cat_filter,size=num_filter,
                 facet_col=col_filter,facet_row=row_filter)
st.plotly_chart(fig,use_container_width=True)

st.write("\n")
st.write("-"*50)
st.write("\n")

# row c
c1,c2,c3=st.columns((4,3,3))


with c1:
    st.text("Sex Vs. Total Bill")
    fig= px.bar(df,x='sex',y='total_bill',color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)
with c2:
    st.text("Smoker/Non-Smoker Vs. Tips")
    fig= px.pie(df,names='smoker',values='tip',color=cat_filter)
    st.plotly_chart(fig,use_container_width=True)
with c3:
    st.text("Days Vs. Tips")
    fig= px.pie(df,names='day',values='tip',
                color=cat_filter,hole=0.4)
    st.plotly_chart(fig,use_container_width=True)
