from scipy.fft import fft, fftfreq
import random
import numpy as np
from plotly.subplots import make_subplots
import plotly.express as px
import pandas as pd
import settings
from loading import data


def mean_std():
    
    df_mean=data()[0].mean()
    fig=px.scatter(df_mean)
    fig.update_xaxes(title_text='Channel')
    fig.update_yaxes(title_text='Mean ADC Values')

    df_std=data()[0].std()
    fig2=px.scatter(df_std)
    fig2.update_xaxes(title_text='Channel')
    fig2.update_yaxes(title_text='Standard Deviation of ADCs')

    return fig,fig2


def det_df(decision):

    df_adcs = data()[0]
    t0=data()[2]
    print(t0)
    if decision==1:
        df_adcs=df_adcs-df_adcs.mean()
    df_T= df_adcs.T
    df_sorted=df_T.sort_index()
    
    return df_sorted,t0

def mult_graphs(value_list,decision):

    fig1 = make_subplots(rows=1, cols=1)

    fig1.update_yaxes(title_text='ADCs') 


    fig2 = make_subplots(rows=1, cols=1)
    fig2.update_xaxes(title_text='Frequency')
    fig2.update_yaxes(title_text='|FFT [ADCs]|')


    fig1.add_annotation(text='<b>Initial TS: </b> <br>'+str(det_df(decision)[1]), align='left',showarrow=False,
                    xref='paper',
                    yref='paper',
                    x=1.0,
                    y=1.0,
                    bordercolor='black',
                    borderwidth=1)
    fig1.update_layout(
    
    margin = {'t':50, 'b':10},
    xaxis = {'domain': [0, 0.88]},
    xaxis2 = {'domain': [0.45, 1.],'title':'year'},
    yaxis2 = {'anchor': 'x2', 'title': 'lifeExp'}
)
    fig2.update_layout(
    
    margin = {'t':50, 'b':10},
    xaxis = {'domain': [0, 0.88]},
    xaxis2 = {'domain': [0.45, 1.],'title':'year'},
    yaxis2 = {'anchor': 'x2', 'title': 'lifeExp'}
)
    
        
    random.seed(1)

    for a in value_list:   

        i=0
        x=det_df(decision)[0]
        x=x.iloc[a]
            
        number_of_colors = len(value_list)
        color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])
        for i in range((number_of_colors))]

        N = len(x)
            
        yf = np.abs(fft(x.values))[:N//2]
        xf =fftfreq(N,1/N)[:N//2]

        data={'xf':xf,'yf':yf}

        df_temp=pd.DataFrame(data)

        df_fft = df_temp.iloc[1: , :]

        fig1.add_trace(px.line(x,color_discrete_sequence=[color[i]]).data[0])
        fig2.add_trace(px.line(df_fft,x="xf",y="yf",color_discrete_sequence=[color[i]]).data[0])
            
        i+=1
            
    return fig1,fig2

def td_2d():

    df_adcs = data()[0]
    df_tps=data()[1]
    t0=data()[2]
    print(df_adcs)


    df_base_rdc=df_adcs-df_adcs.mean()

    df_T= df_base_rdc.T

    df_sorted=df_T.sort_index()

    df_adcs_rdc=df_sorted.iloc[:,:]
    df_tps_rdc=df_tps.iloc[:]


    fig=px.imshow(df_adcs_rdc,aspect="auto")
    fig.update_xaxes(title_text='Time Stamp')
    fig.update_yaxes(title_text='Channel')

    fig1=px.imshow(df_adcs_rdc,aspect="auto")
    fig2=px.scatter(df_tps_rdc,x="time_start", y="channel")


    fig2.update_traces(marker={'size': 3}) 
    fig3=fig1.add_trace(fig2.data[0])
    fig3.update_xaxes(title_text='Time Stamp')
    fig3.update_yaxes(title_text='Channel')
    fig.add_annotation(text='<b>Initial TS: </b> <br>'+str(t0), align='left',showarrow=False,
                        xref='paper',
                        yref='paper',
                        x=1.01,
                        y=1.0,
                        bordercolor='black',
                        borderwidth=1)
    fig.update_layout(
        
        margin = {'t':50, 'b':10},
        xaxis = {'domain': [0, 0.88]},
        xaxis2 = {'domain': [0.45, 1.],'title':'year'},
        yaxis2 = {'anchor': 'x2', 'title': 'lifeExp'}
    )


    fig3.add_annotation(text='<b>Initial TS: </b> <br>'+str(t0), align='left',showarrow=False,
                        xref='paper',
                        yref='paper',
                        x=1.01,
                        y=1.0,
                        bordercolor='black',
                        borderwidth=1)
    fig3.update_layout(
        
        margin = {'t':50, 'b':10},
        xaxis = {'domain': [0, 0.88]},
        xaxis2 = {'domain': [0.45, 1.],'title':'year'},
        yaxis2 = {'anchor': 'x2', 'title': 'lifeExp'}
    )
    return fig, fig3