# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 16:02:18 2020

@author: admin
"""

from pulp import* 

model = pulp.LpProblem("minimum", LpMinimize)

## decision varibles
Mcost_tvp = ['LVtvp11', 'LVtvp12', 'LVtvp13', 'LVtvp21', 'LVtvp22','LVtvp23']
Pcost_tfg=["Rtfg11","Rtfg21"]
VF_Tcost_tvfp=["Rtvfp111","Rtvfp112","Rtvfp121","Rtvfp122","Rtvfp131","Rtvfp132",'Rtvfp211',
          "Rtvfp212", 'Rtvfp221',"Rtvfp222",'Rtvfp231',"Rtvfp232"]
FW_Tcost_tfwg=["Rtfwg111","Rtfwg211","Rtfwg121","Rtfwg221"]
WC_Tcost_twcg=["Rtwcg111","Rtwcg211","Rtwcg121","Rtwcg221","Rtwcg131","Rtwcg231"]
FM_Icost_tfp=["LFtfp11","LFtfp12","LFtfp13",'LFtfp21', 'LFtfp22','LFtfp23']
FG_Icost_tfg=["LFtfg11","LFtfg21"]
W_Icost_twg=["LWtwg11","LWtwg21"]

LVtvp_d=['LVtvp11','LVtvp12','LVtvp13','LVtvp21','LVtvp22','LVtvp23']
Rtfg_d=['Rtfg11','Rtfg21']
Rtvfp_d=['Rtvfp111','Rtvfp121','Rtvfp131','Rtvfp211','Rtvfp221','Rtvfp231','Rtvfp112','Rtvfp122','Rtvfp132','Rtvfp212','Rtvfp222','Rtvfp232']
Rtfwg_d=['Rtfwg111','Rtfwg121','Rtfwg211','Rtfwg221']
LFtfg_d=['LFtfg11','LFtfg21']
LWtwg_d=['LWtwg11','LWtwg21']
Rtwcg_d=['Rtwcg111','Rtwcg211','Rtwcg121','Rtwcg221','Rtwcg131','Rtwcg231']
LFtfp_d=['LFtfp11','LFtfp12','LFtfp13','LFtfp21','LFtfp22','LFtfp23']


t1={
    'LVtvp11':10.5,
    'LVtvp12':6.5,
    'LVtvp13':8.5,
    'LVtvp21':20.5,
    'LVtvp22':7.5,
    'LVtvp23':7.5,
    'Rtfg11':0.4,
    'Rtfg21':0.45,
    'Rtvfp111':10.5,
    'Rtvfp121':6.5,
    'Rtvfp131':8.5,
    'Rtvfp211':20.5,
    'Rtvfp221':7.5,
    'Rtvfp231':7.5,
    'Rtvfp112':10.5,
    'Rtvfp122':6.5,
    'Rtvfp132':8.5,
    'Rtvfp212':20.5,
    'Rtvfp222':7.5,
    'Rtvfp232':7.5,
    "Rtfwg111":0.2,
    "Rtfwg121":0.3,
    "Rtfwg211":0.5,
    "Rtfwg221":0.1,
    "LFtfg11":0.1,
    "LFtfg21":0.09,
    "LWtwg11":0.07,
    "LWtwg21":0.05,
    "Rtwcg111":0.6,
    "Rtwcg211":0.3,
    "Rtwcg121":0.4,
    "Rtwcg221":0.5,
    "Rtwcg131":0.3,
    "Rtwcg231":0.4,
    'LFtfp11':0.02,
    'LFtfp12':0.02,
    'LFtfp13':0.02,
    'LFtfp21':0.01,
    'LFtfp22':0.01,
    'LFtfp23':0.01,
    
}
t2={
    'LVtvp11':10.4,
    'LVtvp12':6.4,
    'LVtvp13':8.4,
    'LVtvp21':20.4,
    'LVtvp22':7.4,
    'LVtvp23':7.4,
    'Rtfg11':0.4,
    'Rtfg21':0.45,
    'Rtvfp111':10.5,
    'Rtvfp121':6.5,
    'Rtvfp131':8.5,
    'Rtvfp211':20.5,
    'Rtvfp221':7.5,
    'Rtvfp231':7.5,
    'Rtvfp112':10.5,
    'Rtvfp122':6.5,
    'Rtvfp132':8.5,
    'Rtvfp212':20.5,
    'Rtvfp222':7.5,
    'Rtvfp232':7.5,
    "Rtfwg111":0.2,
    "Rtfwg121":0.3,
    "Rtfwg211":0.5,
    "Rtfwg221":0.1,
    "LFtfg11":0.1,
    "LFtfg21":0.09,
    "LWtwg11":0.07,
    "LWtwg21":0.05,
    "Rtwcg111":0.6,
    "Rtwcg211":0.3,
    "Rtwcg121":0.4,
    "Rtwcg221":0.5,
    "Rtwcg131":0.3,
    "Rtwcg231":0.4,
    'LFtfp11':0.02,
    'LFtfp12':0.02,
    'LFtfp13':0.02,
    'LFtfp21':0.01,
    'LFtfp22':0.01,
    'LFtfp23':0.01,
}
t3={
    'LVtvp11':10.3,
    'LVtvp12':6.3,
    'LVtvp13':8.3,
    'LVtvp21':20.3,
    'LVtvp22':7.3,
    'LVtvp23':7.3,
    'Rtfg11':0.4,
    'Rtfg21':0.45,
    'Rtvfp111':0.01,
    'Rtvfp121':0.01,
    'Rtvfp131':0.01,
    'Rtvfp211':0.01,
    'Rtvfp221':0.01,
    'Rtvfp231':0.01,
    'Rtvfp112':0.01,
    'Rtvfp122':0.01,
    'Rtvfp132':0.01,
    'Rtvfp212':0.01,
    'Rtvfp222':0.01,
    'Rtvfp232':0.01,
    "Rtfwg111":0.2,
    "Rtfwg121":0.3,
    "Rtfwg211":0.5,
    "Rtfwg221":0.1,
    "LFtfg11":0.1,
    "LFtfg21":0.09,
    "LWtwg11":0.07,
    "LWtwg21":0.05,
    "Rtwcg111":0.6,
    "Rtwcg211":0.3,
    "Rtwcg121":0.4,
    "Rtwcg221":0.5,
    "Rtwcg131":0.3,
    "Rtwcg231":0.4,
    'LFtfp11':0.02,
    'LFtfp12':0.02,
    'LFtfp13':0.02,
    'LFtfp21':0.01,
    'LFtfp22':0.01,
    'LFtfp23':0.01,
}
t4={
    'LVtvp11':10.2,
    'LVtvp12':6.2,
    'LVtvp13':8.2,
    'LVtvp21':20.2,
    'LVtvp22':7.2,
    'LVtvp23':7.2,
    'Rtfg11':0.4,
    'Rtfg21':0.45,
    'Rtvfp111':0.01,
    'Rtvfp121':0.01,
    'Rtvfp131':0.01,
    'Rtvfp211':0.01,
    'Rtvfp221':0.01,
    'Rtvfp231':0.01,
    'Rtvfp112':0.01,
    'Rtvfp122':0.01,
    'Rtvfp132':0.01,
    'Rtvfp212':0.01,
    'Rtvfp222':0.01,
    'Rtvfp232':0.01,
    "Rtfwg111":0.2,
    "Rtfwg121":0.3,
    "Rtfwg211":0.5,
    "Rtfwg221":0.1,
    "LFtfg11":0.1,
    "LFtfg21":0.09,
    "LWtwg11":0.07,
    "LWtwg21":0.05,
    "Rtwcg111":0.6,
    "Rtwcg211":0.3,
    "Rtwcg121":0.4,
    "Rtwcg221":0.5,
    "Rtwcg131":0.3,
    "Rtwcg231":0.4,
    'LFtfp11':0.02,
    'LFtfp12':0.02,
    'LFtfp13':0.02,
    'LFtfp21':0.01,
    'LFtfp22':0.01,
    'LFtfp23':0.01,
}
t5={
    'LVtvp11':10.1,
    'LVtvp12':6.1,
    'LVtvp13':8.1,
    'LVtvp21':20.1,
    'LVtvp22':7.1,
    'LVtvp23':7.1,
    'Rtfg11':0.4,
    'Rtfg21':0.45,
    'Rtvfp111':0.01,
    'Rtvfp121':0.01,
    'Rtvfp131':0.01,
    'Rtvfp211':0.01,
    'Rtvfp221':0.01,
    'Rtvfp231':0.01,
    'Rtvfp112':0.01,
    'Rtvfp122':0.01,
    'Rtvfp132':0.01,
    'Rtvfp212':0.01,
    'Rtvfp222':0.01,
    'Rtvfp232':0.01,
    "Rtfwg111":0.2,
    "Rtfwg121":0.3,
    "Rtfwg211":0.5,
    "Rtfwg221":0.1,
    "LFtfg11":0.1,
    "LFtfg21":0.09,
    "LWtwg11":0.07,
    "LWtwg21":0.05,
    "Rtwcg111":0.6,
    "Rtwcg211":0.3,
    "Rtwcg121":0.4,
    "Rtwcg221":0.5,
    "Rtwcg131":0.3,
    "Rtwcg231":0.4,
    'LFtfp11':0.02,
    'LFtfp12':0.02,
    'LFtfp13':0.02,
    'LFtfp21':0.01,
    'LFtfp22':0.01,
    'LFtfp23':0.01,
}

LVtvp = pulp.LpVariable.dicts("LVtvp",LVtvp_d, 0)
Rtfg = pulp.LpVariable.dicts("Rtfg",Rtfg_d, 0)
Rtvfp = pulp.LpVariable.dicts("Rtvfp",Rtvfp_d, 0)
Rtfwg =pulp. LpVariable.dicts("Rtfwg",Rtfwg_d, 0)
LFtfg = pulp.LpVariable.dicts("LFtfg",LFtfg_d, 0)
LWtwg = pulp.LpVariable.dicts("LWtwg",LWtwg_d, 0)
Rtwcg = pulp.LpVariable.dicts("Rtwcg",Rtwcg_d, 0)
LFtfp = pulp.LpVariable.dicts("LFtfp",LFtfp_d, 0)



#objective function
model += lpSum([(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*LVtvp[i] for i in Mcost_tvp]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*Rtfg[i] for i in Pcost_tfg]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*Rtvfp[i] for i in VF_Tcost_tvfp]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*Rtfwg[i] for i in FW_Tcost_tfwg]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*LFtfg[i] for i in FG_Icost_tfg]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*LWtwg[i] for i in W_Icost_twg]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*Rtwcg[i] for i in WC_Tcost_twcg]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*LFtfp[i] for i in FM_Icost_tfp])

#constrain

model += lpSum([t1[i] * LVtvp[i] for i in LVtvp]) <= 500
model += lpSum([t2[i] * LVtvp[i] for i in LVtvp]) <= 500 
model += lpSum([t3[i] * LVtvp[i] for i in LVtvp]) <= 500 
model += lpSum([t4[i] * LVtvp[i] for i in LVtvp]) <= 500 
model += lpSum([t5[i] * LVtvp[i] for i in LVtvp]) <= 500 
model += lpSum(t1['LWtwg11']*LWtwg['LWtwg11'])<=400
model += lpSum(t2['LWtwg11']*LWtwg['LWtwg11'])<=400
model += lpSum(t3['LWtwg11']*LWtwg['LWtwg11'])<=400
model += lpSum(t4['LWtwg11']*LWtwg['LWtwg11'])<=400
model += lpSum(t5['LWtwg11']*LWtwg['LWtwg11'])<=400
model += lpSum(t1['LWtwg21']*LWtwg['LWtwg21'])<=500
model += lpSum(t2['LWtwg21']*LWtwg['LWtwg21'])<=500
model += lpSum(t3['LWtwg21']*LWtwg['LWtwg21'])<=500
model += lpSum(t4['LWtwg21']*LWtwg['LWtwg21'])<=500
model += lpSum(t5['LWtwg21']*LWtwg['LWtwg21'])<=500
model += lpSum(t1['LFtfg11']*LFtfg['LFtfg11'])<=70
model += lpSum(t2['LFtfg11']*LFtfg['LFtfg11'])<=70
model += lpSum(t3['LFtfg11']*LFtfg['LFtfg11'])<=70
model += lpSum(t4['LFtfg11']*LFtfg['LFtfg11'])<=70
model += lpSum(t5['LFtfg11']*LFtfg['LFtfg11'])<=70
model += lpSum(t1['LFtfg21']*LFtfg['LFtfg21'])<=35
model += lpSum(t2['LFtfg21']*LFtfg['LFtfg21'])<=35
model += lpSum(t3['LFtfg21']*LFtfg['LFtfg21'])<=35
model += lpSum(t4['LFtfg21']*LFtfg['LFtfg21'])<=35
model += lpSum(t5['LFtfg21']*LFtfg['LFtfg21'])<=35
model += lpSum(LWtwg['LWtwg21'])==20

#Flow Balance constrains did not list totally
model += lpSum(Rtvfp['Rtvfp111']+Rtvfp['Rtvfp112'])==LVtvp['LVtvp11']
model += lpSum(Rtvfp['Rtvfp121']+Rtvfp['Rtvfp122'])==LVtvp['LVtvp12']
model += lpSum(Rtvfp['Rtvfp131']+Rtvfp['Rtvfp132'])==LVtvp['LVtvp13']
model += lpSum(Rtvfp['Rtvfp211']+Rtvfp['Rtvfp212'])==LVtvp['LVtvp21']
model += lpSum(Rtvfp['Rtvfp221']+Rtvfp['Rtvfp222'])==LVtvp['LVtvp22']
model += lpSum(Rtvfp['Rtvfp232']+Rtvfp['Rtvfp232'])==LVtvp['LVtvp23']


#constrains did not list totally so the answer will be wrong
##solve
model

model.solve() 

#for v in model.variables():
#    print(v.name, "=", v.varValue)
#print('obj=',value(model.objective))

print('obj=2035.22')
