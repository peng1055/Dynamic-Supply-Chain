<h1><b>Example of SCM</b></h1>
&#9733  If you  haven’t read the SC model, please check <a href="https://github.com/peng1055/Dynamic-Supply-Chain/blob/master/DSCM.md#-build-a-supply-chain-model-scm-notation-variables-and-input-data">HERE</a>!
<br><br>
After introducing the SC model, we take an example for it. 
<br>
<br>
Define the struture of SCM as below table and figure:
<br><br>
<table>
  <tr>
  <th>  </th> <th>Number</th> <th>Notation</th> 
  </tr>
  <tr>
  <th> vendor </th> <th>2</th> <th>V = { v<sub>1</sub> , v<sub>2</sub> }</th> 
  </tr>
  <tr>
  <th> facility </th> <th>2</th> <th>F = { f<sub>1</sub> , f<sub>2</sub> }</th> 
  </tr>
  <tr>
  <th> warehouse </th> <th>2</th> <th>W = { w<sub>1</sub> , w<sub>2</sub> }</th> 
  </tr>
  <tr>
  <th> customer </th> <th>3</th> <th>C = { c<sub>1</sub> , c<sub>2</sub> , c<sub>3</sub> }</th> 
  </tr>
  <tr>
  <th> material </th> <th>3</th> <th>P = { p<sub>1</sub> , p<sub>2</sub> , p<sub>3</sub> }</th> 
  </tr>
  <tr>
  <th> goods </th> <th>1</th> <th>G = { g<sub>1</sub> }</th> 
  </tr>
  <tr>
  <th> time units </th> <th>5</th> <th>T = { t<sub>1</sub> , t<sub>2</sub> , t<sub>3</sub>, t<sub>4</sub> , t<sub>5</sub> }</th> 
  </tr>
</table>
<br>
<br><br>
<img src=https://github.com/peng1055/Dynamic-Supply-Chain/blob/master/activities.png width="500" height="500">
<br>
<br>

The Python Code and explanation is as below parts.
<br>
<br>
Note: This code will use <b>pulp</b> to solve the probelm. If you don't install it, you can refer to <a href="https://github.com/PO-LAB/Python-Gurobi-Pulp">this article</a> which published by PO-LAB from NCKU IMIS. 
<br><br>
Import pulp into python, and define each variables.

```
from pulp import *
model = pulp.LpProblem("minimum", LpMinimize)
Mcost_tvp = ['LVtvp11', 'LVtvp12', 'LVtvp13', 'LVtvp21', 'LVtvp22','LVtvp23']
Pcost_tfg=["Rtfg11","Rtfg21"]
VF_Tcost_tvfp=["Rtvfp111","Rtvfp112","Rtvfp121","Rtvfp122","Rtvfp131","Rtvfp132",'Rtvfp211', "Rtvfp212", 'Rtvfp221',"Rtvfp222",'Rtvfp231',"Rtvfp232"]
FW_Tcost_tfwg=["Rtfwg111","Rtfwg211","Rtfwg121","Rtfwg221"]
WC_Tcost_twcg=["Rtwcg111","Rtwcg211","Rtwcg121","Rtwcg221","Rtwcg131","Rtwcg231"]
FM_Icost_tfp=["LFtfp11","LFtfp12","LFtfp13",'LFtfp21', 'LFtfp22','LFtfp23']
FG_Icost_tfg=["LFtfg11","LFtfg21"]
W_Icost_twg=["LWtwg11","LWtwg21"]

```
<br><br>
Key in the given data.
<br><br>
```
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
```
<br><br>
Declared decision variables into model.
<br><br>
```

LVtvp=['LVtvp11','LVtvp12','LVtvp13','LVtvp21','LVtvp22','LVtvp23']
Rtfg=['Rtfg11','Rtfg21']
Rtvfp=['Rtvfp111','Rtvfp121','Rtvfp131','Rtvfp211','Rtvfp221','Rtvfp231','Rtvfp112','Rtvfp122','Rtvfp132','Rtvfp212','Rtvfp222','Rtvfp232']
Rtfwg=['Rtfwg111','Rtfwg121','Rtfwg211','Rtfwg221']
LFtfg=['LFtfg11','LFtfg21']
LWtwg=['LWtwg11','LWtwg21']
Rtwcg=['Rtwcg111','Rtwcg211','Rtwcg121','Rtwcg221','Rtwcg131','Rtwcg231']
LFtfp=['LFtfp11','LFtfp12','LFtfp13','LFtfp21','LFtfp22','LFtfp23']


LVtvp = pulp.LpVariable.dicts("LVtvp",LVtvp, 0)
Rtfg = pulp.LpVariable.dicts("Rtfg",Rtfg, 0)
Rtvfp = pulp.LpVariable.dicts("Rtvfp",Rtvfp, 0)
Rtfwg =pulp. LpVariable.dicts("Rtfwg",Rtfwg, 0)
LFtfg = pulp.LpVariable.dicts("LFtfg",LFtfg, 0)
LWtwg = pulp.LpVariable.dicts("LWtwg",LWtwg, 0)
Rtwcg = pulp.LpVariable.dicts("Rtwcg",Rtwcg, 0)
LFtfp = pulp.LpVariable.dicts("LFtfp",LFtfp, 0)

```
<br><br>
Input objective function into model.
<br><br>
```
model += lpSum([(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*Mcost_tvp [i] for i in LVtvp]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*Pcost_tfg [i] for i in Rtfg]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*VF_Tcost_tvfp [i] for i in Rtvfp]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*FW_Tcost_tfwg [i] for i in Rtfwg]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*FG_Icost_tfg [i] for i in LFtfg]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*W_Icost_twg [i] for i in LWtwg]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*WC_Tcost_twcg [i] for i in Rtwcg]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*FM_Icost_tfp [i] for i in LFtfp])
```             
<br><br>
Input constrains into model. There are many constrains, the formulas as below are only partial.
<br><br>
```
# Bounded Contrains

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

.
.
.

# Flow Balance Constrain

model += lpSum(Rtvfp['Rtvfp111']+Rtvfp['Rtvfp112'])==LVtvp['LVtvp11']
model += lpSum(Rtvfp['Rtvfp121']+Rtvfp['Rtvfp122'])==LVtvp['LVtvp12']
model += lpSum(Rtvfp['Rtvfp131']+Rtvfp['Rtvfp132'])==LVtvp['LVtvp13']
model += lpSum(Rtvfp['Rtvfp211']+Rtvfp['Rtvfp212'])==LVtvp['LVtvp21']
model += lpSum(Rtvfp['Rtvfp221']+Rtvfp['Rtvfp222'])==LVtvp['LVtvp22']
model += lpSum(Rtvfp['Rtvfp232']+Rtvfp['Rtvfp232'])==LVtvp['LVtvp23']

.
.
.

``` 
<br><br>
Solve the problem and print the solution of variables.
<br><br>
```
model.solve() 

for v in model.variables():
    print(v.name, "=", v.varValue)
print('obj=',value(model.objective))
```
<br><br>
Finally, we will get the following table.
<br><br>
<table>
<tr>
  <th> Variable </th> <th>Value</th> 
</tr>
<tr>
  <th> FG_Icost_FG_Icost_t11 </th> <th>0</th> 
</tr>
<tr>
  <th> FG_Icost_FG_Icost_t21 </th> <th>0</th> 
</tr>
<tr>
  <th> FM_Icost_FM_Icost_t11 </th> <th>0</th> 
</tr>
<tr>
  <th> FM_Icost_FM_Icost_t12 </th> <th>0</th> 
</tr>
<tr>
  <th> FM_Icost_FM_Icost_t13 </th> <th>0</th> 
</tr>
<tr>
  <th> FM_Icost_FM_Icost_t21 </th> <th>0</th> 
</tr>
<tr>
  <th> FM_Icost_FM_Icost_t22 </th> <th>0</th> 
</tr>  
<tr>
  <th> FM_Icost_FM_Icost_t23 </th> <th>0</th> 
</tr> 
<tr>
  <th> FW_Tcost_FW_Tcost_tf11_1 </th> <th>0</th> 
</tr>   
<tr>
  <th> FW_Tcost_FW_Tcost_tf11_2 </th> <th>0</th> 
</tr>    
<tr>
  <th> FW_Tcost_FW_Tcost_tf12_1 </th> <th>0</th> 
</tr>   
<tr>
  <th> FW_Tcost_FW_Tcost_tf12_2 </th> <th>0</th> 
</tr> 
<tr>
  <th> Mcost_Mcost_t11 </th> <th>0</th> 
</tr>   
<tr>
  <th> Mcost_Mcost_t12 </th> <th>0</th> 
</tr>   
<tr>
  <th> Mcost_Mcost_t13 </th> <th>0</th> 
</tr>   
<tr>
  <th> Mcost_Mcost_t21 </th> <th>0</th> 
</tr>   
<tr>
  <th> Mcost_Mcost_t22 </th> <th>0</th> 
</tr> 
<tr>
  <th> Mcost_Mcost_t23 </th> <th>0</th> 
</tr> 
<tr>
  <th> Pcost_Pcost_t11 </th> <th>0</th> 
</tr> 
<tr>
  <th> Pcost_Pcost_t21 </th> <th>0</th> 
</tr> 
<tr>
  <th> VF_Tcost_VFcost_t11_1 </th> <th>0</th> 
</tr> 
<tr>
  <th> VF_Tcost_VFcost_t11_2 </th> <th>0</th> 
</tr> 
<tr>
  <th> VF_Tcost_VFcost_t12_1 </th> <th>0</th> 
</tr>
<tr>
  <th> VF_Tcost_VFcost_t12_2 </th> <th>0</th> 
</tr>
<tr>
  <th> VF_Tcost_VFcost_t13_1 </th> <th>0</th> 
</tr>  
<tr>
  <th> VF_Tcost_VFcost_t13_2 </th> <th>0</th> 
</tr>  
<tr>
  <th> VF_Tcost_VFcost_t21_1 </th> <th>0</th> 
</tr>  
<tr>
  <th> VF_Tcost_VFcost_t21_2 </th> <th>0</th> 
</tr>    
<tr>
  <th> VF_Tcost_VFcost_t22_1 </th> <th>0</th> 
</tr>    
<tr>
  <th> VF_Tcost_VFcost_t22_2 </th> <th>0</th> 
</tr>    
<tr>
  <th> VF_Tcost_VFcost_t23_1 </th> <th>0</th> 
</tr>      
<tr>
  <th> VF_Tcost_VFcost_t23_2 </th> <th>0</th> 
</tr>    
<tr>
  <th> W_Icost_W_Icost_t11 </th> <th>0</th> 
</tr>    
<tr>
  <th> W_Icost_W_Icost_t21 </th> <th>20</th> 
</tr>     
<tr>
  <th> objective function </th> <th>5</th> 
</tr>    

 





