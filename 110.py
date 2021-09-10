import csv
from os import name
import pandas as pd
import plotly.figure_factory as pff
import plotly.express as px
import statistics
import random
import plotly.graph_objects as pg

df = pd.read_csv("C:\\Users\\TRUSTANA MARKETING\\OneDrive\\Desktop\\Whitehat jr\\Python_Class\\medium_data.csv")
data = df["reading_time"].tolist()
#fig = pff.create_distplot([data], ["Reading time in min"], show_hist=False)
#fig.show()

stat_mean = statistics.mean(data)
stat_std = statistics.stdev(data)

print("The mean is: ", stat_mean)
print("The standard deviation is: ", stat_std)

def random_set_of_mean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean
def show_fig(mean_list):
    df = mean_list
    print("Mean of the sampling distribution: ",statistics.mean(mean_list))
    print("Standard deviation of the sampling distribution: ",statistics.stdev(mean_list))
    fig=pff.create_distplot([df],["Reading List"],show_hist=False)
    #fig.show()
    
def setup():
    mean_list=[]
    for i in range(0,100):
        set_of_means = random_set_of_mean(30)
        mean_list.append(set_of_means)
    show_fig(mean_list)
    std = statistics.stdev(mean_list)

    firstStdStart, firstStdEnd = stat_mean-std, stat_mean+std
    secondStdStart, secondStdEnd = stat_mean-2*std, stat_mean+2*std
    thirdStdStart, thirdStdEnd = stat_mean-3*std, stat_mean+3*std
    
    data_within_1_std_deviation = [result for result in data if result > firstStdStart
    and result < firstStdEnd]
    print("Standard 1 ", firstStdStart,firstStdEnd)

    data_within_2_std_deviation = [result for result in data if result > secondStdStart
    and result < secondStdEnd]
    print("Standard 2 ", secondStdStart,secondStdEnd)

    data_within_3_std_deviation = [result for result in data if result > thirdStdStart
    and result < thirdStdEnd]
    print("Standard 3 ", thirdStdStart,thirdStdEnd)
    fig = pff.create_distplot([mean_list], ["Students Marks"], show_hist=False)
    fig.add_trace(pg.Scatter(x=[stat_mean,stat_mean],y=[0,0.17],mode="lines", name="mean"))

    fig.add_trace(pg.Scatter(x=[firstStdStart, firstStdStart],y=[0,0.17],mode="lines", name="First std Deviation Start "))
    fig.add_trace(pg.Scatter(x=[firstStdEnd, firstStdEnd],y=[0,0.17],mode="lines", name="First std deviation end"))

    fig.add_trace(pg.Scatter(x=[secondStdStart, secondStdStart],y=[0,0.17],mode="lines", name="Second std Deviation Start "))
    fig.add_trace(pg.Scatter(x=[secondStdEnd, secondStdEnd],y=[0,0.17],mode="lines", name="Second std deviation end"))

    fig.add_trace(pg.Scatter(x=[thirdStdStart, thirdStdStart],y=[0,0.17],mode="lines", name="Third std Deviation Start "))
    fig.add_trace(pg.Scatter(x=[thirdStdEnd, thirdStdEnd],y=[0,0.17],mode="lines", name="Third std deviation end"))

    #fig.show()
    
      
    df = pd.read_csv("C:\\Users\\TRUSTANA MARKETING\\OneDrive\\Desktop\\Whitehat jr\\Python_Class\\medium_data.csv")
    data1 = df["reading_time"].tolist()
    meanOfSample1 = statistics.mean(data1)
    zScore = (meanOfSample1-stat_mean)/stat_std
    print("Mean of sample 1", meanOfSample1)
    print("Standard deviation", std)
    print("Mean is", stat_mean)
    print("ZScore", zScore)
    
setup()

#new sample mean - sampling distribution mean/std deviation






