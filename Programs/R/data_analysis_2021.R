#Import Data
setwd("C:/Users/migue/Documents/F1 Data Center/R")
data = read.csv("data.csv", sep= ';')

#These ones for Data Visualization
library(gridExtra)
library(ggplot2)
library(leaflet)
library(rgdal)
library(stringr)
library(reshape2)
library(forcats)
#These for PCA
library(tidyverse)
library(GGally) # ggplot2-based visualization of correlations
library(factoextra) # ggplot2-based visualization of pca
#Finally, those for Clustering
library(cluster)
library(mclust)

library(skimr)
library(mice)
library(VIM)
library(MASS)
library(glmnet)
library(e1071) 
library(rpart)
library(pROC)
library(class)
library(randomForest)
library(caret)
library(Rcpp)
library(naivebayes)
library(rpart.plot)

#Deal with null values ('NO TIME')

#Assign NA's properly
index = which(data$fp1_quali_Pace == 'NO TIME ') 
data$fp1_quali_Pace[index] = NA
index = which(data$fp1_race_Pace == 'NO TIME ') 
data$fp1_race_Pace[index] = NA
index = which(data$fp1_fastest_lap == 0) 
data$fp1_quali_Pace[index] = NA

index = which(data$fp2_quali_Pace == 'NO TIME ') 
data$fp2_quali_Pace[index] = NA
index = which(data$fp2_race_Pace == 'NO TIME ') 
data$fp2_race_Pace[index] = NA
index = which(data$fp2_fastest_lap == 0) 
data$fp2_quali_Pace[index] = NA

index = which(data$fp3_quali_Pace == 'NO TIME ') 
data$fp3_quali_Pace[index] = NA
index = which(data$fp3_race_Pace == 'NO TIME ') 
data$fp3_race_Pace[index] = NA
index = which(data$fp3_fastest_lap == 0) 
data$fp3_quali_Pace[index] = NA

index = which(data$quali_Pace == 'NO TIME ') 
data$quali_Pace[index] = NA
index = which(data$quali_fastest_lap == 0) 
data$quali_fastest_lap[index] = NA

index = which(data$race_Pace == 'NO TIME ') 
data$race_Pace[index] = NA
index = which(data$race_fastest_lap == 0) 
data$race_fastest_lap[index] = NA

#Data preprocessing
data = data[-which(data$quali_Laps == 0),]


aggr(data, numbers = TRUE, sortVars = TRUE, labels = names(data), cex.axis = 0.7, gap = 1.5, 
     ylab= c('Missing data','Pattern'))

#Remove those with over 0.6 of null values
data = data[,-c(24,25,34,36)]

#Try to use mice library to make data imputation
#If it does not work, for example True or False about if the session started or not could be useful.

#From now, I will keep 0 in 'NO TIME' values, if it does not perform, I could change it.
for (i in 1:ncol(data)){
  nul = which(is.na(data[,i]))
  data[c(nul),i] = 0
}


#Factorize and numeric values
for (i in 1:ncol(data)){
  if(i %in% c(8,10,15,17,22,27)) {
    data[,i] = as.integer(data[,i])
  } else {
    if(!(is.integer(data[,i]))) {
    data[,i] = as.factor(data[,i])}
  }
}

#Correlations among data

ggcorr(data, label = T,label_alpha=T,nbreaks = 4)
#LUEGO DE PLOTS, ELIMINAR QUALI DETAILS, RACE Y FASTEST LAPS

#Teams Colors
fer = #9f121d
rb = #340db0
mer = #25b8a1
am = #185d5b
at = #2d3c4f
ar = #6b101b
alp = #2180c3
wil = #1e52b8
mcl = #ca923e
haa = #f0eff2
  
#Incident rate by drivers


#Question X: Young vs Old drivers (old over 30 years old)
#Incident rate
y = which(data$Age < 30)
young = data[y,]
old = data[-y,]

fp1_crash_old = length(which(old$fp1_Incident == 'Yes'))
fp1_crash_young = length(which(young$fp1_Incident == 'Yes'))
fp2_crash_old = length(which(old$fp2_Incident == 'Yes'))
fp2_crash_young = length(which(young$fp2_Incident == 'Yes'))
fp3_crash_old = length(which(old$fp3_Incident == 'Yes'))
fp3_crash_young = length(which(young$fp3_Incident == 'Yes'))
quali_crash_old = length(which(old$quali_Incident == 'Yes'))
quali_crash_young = length(which(young$quali_Incident == 'Yes'))
race_crash_old = length(which(old$race_Incident == 'Yes'))
race_crash_young = length(which(young$race_Incident == 'Yes'))

#Each session
y_o = c('Old_Drivers', 'Young_Drivers')
crash = c(fp1_crash_old,fp1_crash_young)
fp1 = data.frame(crash,y_o)
fp1 = ggplot(data=fp1, aes(x=reorder(y_o,crash), y=crash)) +
  geom_bar(stat="identity", fill="red")+
  geom_text(aes(label=crash), vjust=1.6, color="white", size=3.5)+
  theme_minimal()+labs(x = 'FP1')

crash = c(fp2_crash_old,fp2_crash_young)
fp2 = data.frame(crash,y_o)
fp2 = ggplot(data=fp2, aes(x=reorder(y_o,crash), y=crash)) +
  geom_bar(stat="identity", fill="red")+
  geom_text(aes(label=crash), vjust=1.6, color="white", size=3.5)+
  theme_minimal()+labs(x = 'FP2')

crash = c(fp3_crash_old,fp3_crash_young)
fp3 = data.frame(crash,y_o)
fp3 = ggplot(data=fp3, aes(x=reorder(y_o,crash), y=crash)) +
  geom_bar(stat="identity", fill="red")+
  geom_text(aes(label=crash), vjust=1.6, color="white", size=3.5)+
  theme_minimal()+labs(x = 'FP3')

crash = c(quali_crash_old,quali_crash_young)
quali = data.frame(crash,y_o)
quali = ggplot(data=quali, aes(x=reorder(y_o,crash), y=crash)) +
  geom_bar(stat="identity", fill="red")+
  geom_text(aes(label=crash), vjust=1.6, color="white", size=3.5)+
  theme_minimal()+labs(x = 'Qualyfing')

crash = c(race_crash_old,race_crash_young)
race = data.frame(crash,y_o)
race = ggplot(data=race, aes(x=reorder(y_o,crash), y=crash)) +
  geom_bar(stat="identity", fill="red")+
  geom_text(aes(label=crash), vjust=1.6, color="white", size=3.5)+
  theme_minimal()+labs(x = 'Race')

plot <- grid.arrange(fp1, fp2, fp3, quali, race, ncol=5)

total_old = race_crash_old + quali_crash_old + fp1_crash_old +fp2_crash_old + fp3_crash_old
total_young = race_crash_young + quali_crash_young + fp1_crash_young +fp2_crash_young + fp3_crash_young

crash = c(total_old,total_young)
total = data.frame(crash,y_o)
ggplot(data=total, aes(x=reorder(y_o,crash), y=crash)) +
  geom_bar(stat="identity", fill="red")+
  geom_text(aes(label=crash), vjust=1.6, color="white", size=3.5)+
  theme_minimal()

#As expected, young drivers crash more often than old drivers do.
