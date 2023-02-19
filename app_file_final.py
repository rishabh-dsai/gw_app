
import pandas as pd
import streamlit as st
import datetime
from bokeh.plotting import figure


st.set_page_config(page_title='Ground Water Level Prediction',layout="wide")

ram_train_pred=pd.read_excel("Predictions_Rampura.xlsx",sheet_name="Train Predictions")
ram_test_pred=pd.read_excel("Predictions_Rampura.xlsx",sheet_name="Test Predictions")
ram_pred_df=pd.concat([ram_train_pred,ram_test_pred])

ovr_train_pred=pd.read_excel("Predictions overall.xlsx",sheet_name="Train Predictions")
ovr_test_pred=pd.read_excel("Predictions overall.xlsx",sheet_name="Test Predictions")
ovr_pred_df=pd.concat([ovr_train_pred,ovr_test_pred])



#%%

col1,col2,col3=st.columns(3)

with col1:    
    st.metric("Data Availability Period","04-01-2011 to 08-01-2021")
#    st.metric(st.markdown('<div style="text-align: center; font-size:30px; font-weight:bold">DSAI DIGI AGRI PLATFORM</div>', unsafe_allow_html=True),"04-01-2011 to 08-01-2021")

with col2:
    st.metric('Training Period',"09-01-2011 to 31-08-2018")
    
with col3:
    st.metric("Test Period","01-09-2018 to 08-01-2021")



#%%

tab1,tab2=st.tabs(['Rampura','Overall'])

with tab1:
    st.header("Rampura Ground Water Level Prediction")
    st.markdown("\n\n")    
    st.markdown("\n\n")
    
    ch1,ch2=st.columns(2)
    with ch1:
        p = figure(title="Test Actual vs Predicted GW Level", x_axis_label="Date", y_axis_label="GW_level",x_axis_type="datetime",
                   height=500)
        p.line(ram_test_pred['Date'], ram_test_pred['Actual'], legend_label="Actual", color="blue", line_width=5,alpha=0.4)
        p.line(ram_test_pred['Date'], ram_test_pred['Predicted'], legend_label="Predicted", color="red", line_width=1)
        st.bokeh_chart(p,use_container_width=True)    
        
    with ch2:    
        z = figure(title="Train Actual vs Predicted GW Level", x_axis_label="Date", y_axis_label="GW_level",x_axis_type="datetime",
                   height=500)
        z.line(ram_train_pred['Date'], ram_train_pred['Actual'], legend_label="Actual", color="blue",line_width=5,alpha=0.4)
        z.line(ram_train_pred['Date'], ram_train_pred['Predicted'], legend_label="Predicted", color="red", line_width=1)
        st.bokeh_chart(z, use_container_width=True)    

    c1,c2,c3,c4,c5,c6,c7,c8=st.columns(8)

    with c2:    
        st.metric("Test Accuracy","99.94%")

    with c3:
        st.metric('Test MAPE',"0.06%")
        
    with c6:    
        st.metric("Train Accuracy","99.95%")

    with c7:
        st.metric('Train MAPE',"0.05%")
        
    st.markdown("\n\n")
    st.markdown("\n\n")
    st.header(" ")  
    start_date=st.date_input("Select the date from which the predictions will be plotted:",
                             value=datetime.date(year=2018,month=7,day=23),key='rampura')
    num_days=st.number_input("Type the number of days for which the prediction will be plotted:",
                             value=30,step=10,key='rampura_num')
    ram_pred_df.set_index("Date",inplace=True)
    end_date=start_date+pd.offsets.DateOffset(days=num_days)
    ram_subset_pred=ram_pred_df[start_date:end_date]
    
    ram_subset_pred.reset_index(inplace=True)
    
    q = figure(title="Subset Actual vs Predicted GW Level", x_axis_label="Date", y_axis_label="GW_level",x_axis_type="datetime",
               width=500, height=400)
    q.line(ram_subset_pred['Date'], ram_subset_pred['Actual'], legend_label="Actual", color="blue",line_width=5,alpha=0.4)
    q.line(ram_subset_pred['Date'], ram_subset_pred['Predicted'], legend_label="Predicted", color="red", line_width=1)
    st.bokeh_chart(q, use_container_width=True)
    st.markdown("\n\n")    
    s1,s2,s3,s4=st.columns(4)
    with s3:
        st.metric("Cross-validated mean Accuracy","99.93%")


with tab2:
    st.header("Overall Ground Water Level Prediction") 
    st.markdown("\n\n")
    ch3,ch4=st.columns(2)    
    with ch3:
        p = figure(title="Test Actual vs Predicted GW Level", x_axis_label="Date", y_axis_label="GW_level",x_axis_type="datetime",
                   width=500, height=500)
        p.line(ovr_test_pred['Date'],ovr_test_pred['Actual'], legend_label="Actual", color="blue", line_width=5,alpha=0.4)
        p.line(ovr_test_pred['Date'], ovr_test_pred['Predicted'], legend_label="Predicted", color="red", line_width=1)
        st.bokeh_chart(p, use_container_width=True)    
        st.markdown("\n\n")    

    with ch4:
        z = figure(title="Train Actual vs Predicted GW Level", x_axis_label="Date", y_axis_label="GW_level",x_axis_type="datetime",
                   width=500, height=500)
        z.line(ovr_train_pred['Date'], ovr_train_pred['Actual'], legend_label="Actual", color="blue",line_width=5,alpha=0.4)
        z.line(ovr_train_pred['Date'], ovr_train_pred['Predicted'], legend_label="Predicted", color="red", line_width=1)
        st.bokeh_chart(z, use_container_width=True)       

    q1,q2,q3,q4,q5,q6,q7,q8=st.columns(8)

    with q2:    
        st.metric("Test Accuracy","98.65%")
    with q3:
        st.metric('Test MAPE',"1.35%")
    with q6:    
        st.metric("Train Accuracy","99.44%")
    with q7:
        st.metric('Train MAPE',"0.56%")
        
    st.markdown("\n\n")
    st.markdown("<br></br>",unsafe_allow_html=True)
    start_date=st.date_input("Select the date from which the predictions will be plotted:",
                             value=datetime.date(year=2019,month=2,day=18))
    num_days=st.number_input("Type the number of days for which the prediction will be plotted:",
                             value=30,step=10)
    ovr_pred_df.set_index("Date",inplace=True)
    end_date=start_date+pd.offsets.DateOffset(days=num_days)
    ovr_subset_pred=ovr_pred_df[start_date:end_date]
    
    ovr_subset_pred.reset_index(inplace=True)
    
    q = figure(title="Subset Actual vs Predicted GW Level", x_axis_label="Date", y_axis_label="GW_level",x_axis_type="datetime",
               width=500, height=400)
    q.line(ovr_subset_pred['Date'], ovr_subset_pred['Actual'], legend_label="Actual", color="blue",line_width=5,alpha=0.4)
    q.line(ovr_subset_pred['Date'], ovr_subset_pred['Predicted'], legend_label="Predicted", color="red", line_width=1)
    st.bokeh_chart(q, use_container_width=True)    
    l1,l2,l3,l4=st.columns(4)
    with l3:
        st.metric("Cross-validated mean Accuracy","99.37%")    
