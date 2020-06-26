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
  <th> time units </th> <th>5</th> <th>W = { t<sub>1</sub> , t<sub>2</sub> , t<sub>3</sub>, t<sub>4</sub> , t<sub>5</sub> }</th> 
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
Mcost_tvp = ["Mcost_t11", "Mcost_t12", "Mcost_t13", "Mcost_t21", "Mcost_t22","Mcost_t23"]
Pcost_tfg=["Pcost_t11","Pcost_t21"]
VF_Tcost_tvfp=["VFcost_t11_1","VFcost_t11_2","VFcost_t12_1","VFcost_t12_2","VFcost_t13_1","VFcost_t13_2",'VFcost_t21_1',"VFcost_t21_2",'VFcost_t22_1',"VFcost_t22_2",'VFcost_t23_1',"VFcost_t23_2"]
FW_Tcost_tfwg=["FW_Tcost_tf11_1","FW_Tcost_tf11_2","FW_Tcost_tf12_1","FW_Tcost_tf12_2"]
WC_Tcost_twcg=["WC_Tcost_tf11_1","WC_Tcost_tf11_2","WC_Tcost_tf21_1","WC_Tcost_tf21_2","WC_Tcost_tf31_1","WC_Tcost_tf31_2"]
FM_Icost_tfp=["FM_Icost_t11","FM_Icost_t12","FM_Icost_t13",'FM_Icost_t21', 'FM_Icost_t22','FM_Icost_t23']
FG_Icost_tfg=["FG_Icost_t11","FG_Icost_t21"]
W_Icost_twg=["W_Icost_t11","W_Icost_t21"]

```
<br><br>
Key in the given data.
<br><br>
```
t1={
    'Mcost_t11':10.5,
    'Mcost_t12':6.5,
    'Mcost_t13':8.5,
    'Mcost_t21':20.5,
    'Mcost_t22':7.5,
    'Mcost_t23':7.5,
    'Pcost_t11':0.4,
    'Pcost_t21':0.45,
    'VFcost_t11_1':10.5,
    'VFcost_t12_1':6.5,
    'VFcost_t13_1':8.5,
    'VFcost_t21_1':20.5,
    'VFcost_t22_1':7.5,
    'VFcost_t23_1':7.5,
    'VFcost_t11_2':10.5,
    'VFcost_t12_2':6.5,
    'VFcost_t13_2':8.5,
    'VFcost_t21_2':20.5,
    'VFcost_t22_2':7.5,
    'VFcost_t23_2':7.5,
    "FW_Tcost_tf11_1":0.2,
    "FW_Tcost_tf12_1":0.3,
    "FW_Tcost_tf11_2":0.5,
    "FW_Tcost_tf12_2":0.1,
    "FG_Icost_t11":0.1,
    "FG_Icost_t21":0.09,
    "W_Icost_t11":0.07,
    "W_Icost_t21":0.05,
    "WC_Tcost_tf11_1":0.6,
    "WC_Tcost_tf11_2":0.3,
    "WC_Tcost_tf21_1":0.4,
    "WC_Tcost_tf21_2":0.5,
    "WC_Tcost_tf31_1":0.3,
    "WC_Tcost_tf31_2":0.4,
    'FM_Icost_t11':0.02,
    'FM_Icost_t12':0.02,
    'FM_Icost_t13':0.02,
    'FM_Icost_t21':0.01,
    'FM_Icost_t22':0.01,
    'FM_Icost_t23':0.01,
    
}
t2={
    'Mcost_t11':10.4,
    'Mcost_t12':6.4,
    'Mcost_t13':8.4,
    'Mcost_t21':20.4,
    'Mcost_t22':7.4,
    'Mcost_t23':7.4,
    'Pcost_t11':0.4,
    'Pcost_t21':0.45,
    'VFcost_t11_1':10.5,
    'VFcost_t12_1':6.5,
    'VFcost_t13_1':8.5,
    'VFcost_t21_1':20.5,
    'VFcost_t22_1':7.5,
    'VFcost_t23_1':7.5,
    'VFcost_t11_2':10.5,
    'VFcost_t12_2':6.5,
    'VFcost_t13_2':8.5,
    'VFcost_t21_2':20.5,
    'VFcost_t22_2':7.5,
    'VFcost_t23_2':7.5,
    "FW_Tcost_tf11_1":0.2,
    "FW_Tcost_tf12_1":0.3,
    "FW_Tcost_tf11_2":0.5,
    "FW_Tcost_tf12_2":0.1,
    "FG_Icost_t11":0.1,
    "FG_Icost_t21":0.09,
    "W_Icost_t11":0.07,
    "W_Icost_t21":0.05,
    "WC_Tcost_tf11_1":0.6,
    "WC_Tcost_tf11_2":0.3,
    "WC_Tcost_tf21_1":0.4,
    "WC_Tcost_tf21_2":0.5,
    "WC_Tcost_tf31_1":0.3,
    "WC_Tcost_tf31_2":0.4,
    'FM_Icost_t11':0.02,
    'FM_Icost_t12':0.02,
    'FM_Icost_t13':0.02,
    'FM_Icost_t21':0.01,
    'FM_Icost_t22':0.01,
    'FM_Icost_t23':0.01,
}
t3={
    'Mcost_t11':10.3,
    'Mcost_t12':6.3,
    'Mcost_t13':8.3,
    'Mcost_t21':20.3,
    'Mcost_t22':7.3,
    'Mcost_t23':7.3,
    'Pcost_t11':0.4,
    'Pcost_t21':0.45,
    'VFcost_t11_1':0.01,
    'VFcost_t12_1':0.01,
    'VFcost_t13_1':0.01,
    'VFcost_t21_1':0.01,
    'VFcost_t22_1':0.01,
    'VFcost_t23_1':0.01,
    'VFcost_t11_2':0.01,
    'VFcost_t12_2':0.01,
    'VFcost_t13_2':0.01,
    'VFcost_t21_2':0.01,
    'VFcost_t22_2':0.01,
    'VFcost_t23_2':0.01,
    "FW_Tcost_tf11_1":0.2,
    "FW_Tcost_tf12_1":0.3,
    "FW_Tcost_tf11_2":0.5,
    "FW_Tcost_tf12_2":0.1,
    "FG_Icost_t11":0.1,
    "FG_Icost_t21":0.09,
    "W_Icost_t11":0.07,
    "W_Icost_t21":0.05,
    "WC_Tcost_tf11_1":0.6,
    "WC_Tcost_tf11_2":0.3,
    "WC_Tcost_tf21_1":0.4,
    "WC_Tcost_tf21_2":0.5,
    "WC_Tcost_tf31_1":0.3,
    "WC_Tcost_tf31_2":0.4,
    'FM_Icost_t11':0.02,
    'FM_Icost_t12':0.02,
    'FM_Icost_t13':0.02,
    'FM_Icost_t21':0.01,
    'FM_Icost_t22':0.01,
    'FM_Icost_t23':0.01,
}
t4={
    'Mcost_t11':10.2,
    'Mcost_t12':6.2,
    'Mcost_t13':8.2,
    'Mcost_t21':20.2,
    'Mcost_t22':7.2,
    'Mcost_t23':7.2,
    'Pcost_t11':0.4,
    'Pcost_t21':0.45,
    'VFcost_t11_1':0.01,
    'VFcost_t12_1':0.01,
    'VFcost_t13_1':0.01,
    'VFcost_t21_1':0.01,
    'VFcost_t22_1':0.01,
    'VFcost_t23_1':0.01,
    'VFcost_t11_2':0.01,
    'VFcost_t12_2':0.01,
    'VFcost_t13_2':0.01,
    'VFcost_t21_2':0.01,
    'VFcost_t22_2':0.01,
    'VFcost_t23_2':0.01,
    "FW_Tcost_tf11_1":0.2,
    "FW_Tcost_tf12_1":0.3,
    "FW_Tcost_tf11_2":0.5,
    "FW_Tcost_tf12_2":0.1,
    "FG_Icost_t11":0.1,
    "FG_Icost_t21":0.09,
    "W_Icost_t11":0.07,
    "W_Icost_t21":0.05,
    "WC_Tcost_tf11_1":0.6,
    "WC_Tcost_tf11_2":0.3,
    "WC_Tcost_tf21_1":0.4,
    "WC_Tcost_tf21_2":0.5,
    "WC_Tcost_tf31_2":0.3,
    "WC_Tcost_tf31_2":0.4,
    'FM_Icost_t11':0.02,
    'FM_Icost_t12':0.02,
    'FM_Icost_t13':0.02,
    'FM_Icost_t21':0.01,
    'FM_Icost_t22':0.01,
    'FM_Icost_t23':0.01,
}
t5={
    'Mcost_t11':10.1,
    'Mcost_t12':6.1,
    'Mcost_t13':8.1,
    'Mcost_t21':20.1,
    'Mcost_t22':7.1,
    'Mcost_t23':7.1,
    'Pcost_t11':0.4,
    'Pcost_t21':0.45,
    'VFcost_t11_1':0.01,
    'VFcost_t12_1':0.01,
    'VFcost_t13_1':0.01,
    'VFcost_t21_1':0.01,
    'VFcost_t22_1':0.01,
    'VFcost_t23_1':0.01,
    'VFcost_t11_2':0.01,
    'VFcost_t12_2':0.01,
    'VFcost_t13_2':0.01,
    'VFcost_t21_2':0.01,
    'VFcost_t22_2':0.01,
    'VFcost_t23_2':0.01,
    "FW_Tcost_tf11_1":0.2,
    "FW_Tcost_tf12_1":0.3,
    "FW_Tcost_tf11_2":0.5,
    "FW_Tcost_tf12_2":0.1,
    "FG_Icost_t11":0.1,
    "FG_Icost_t21":0.09,
    "W_Icost_t11":0.07,
    "W_Icost_t21":0.05,
    "WC_Tcost_tf11_1":0.6,
    "WC_Tcost_tf11_2":0.3,
    "WC_Tcost_tf21_1":0.4,
    "WC_Tcost_tf21_2":0.5,
    "WC_Tcost_tf31_1":0.3,
    "WC_Tcost_tf31_2":0.4,
    'FM_Icost_t11':0.02,
    'FM_Icost_t12':0.02,
    'FM_Icost_t13':0.02,
    'FM_Icost_t21':0.01,
    'FM_Icost_t22':0.01,
    'FM_Icost_t23':0.01,
}
```
<br><br>
Declared decision variables into model.
<br><br>
```
Mcost = pulp.LpVariable.dicts("Mcost",Mcost_tvp, 0)
Pcost = pulp.LpVariable.dicts("Pcost",Pcost_tfg, 0)
VF_Tcost = pulp.LpVariable.dicts("VF_Tcost",VF_Tcost_tvfp, 0)
FW_Tcost =pulp. LpVariable.dicts("FW_Tcost",FW_Tcost_tfwg, 0)
WC_Tcost = pulp.LpVariable.dicts("WC_Tcost",WC_Tcost_twcg, 0)
FM_Icost = pulp.LpVariable.dicts("FM_Icost",FM_Icost_tfp, 0)
FG_Icost = pulp.LpVariable.dicts("FG_Icost",FG_Icost_tfg, 0)
W_Icost = pulp.LpVariable.dicts("W_Icost",W_Icost_twg, 0)

```
<br><br>
Input objective function into model.
<br><br>
```
model += lpSum([(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*Mcost [i] for i in Mcost]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*Pcost [i] for i in Pcost]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*VF_Tcost [i] for i in VF_Tcost]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*FW_Tcost [i] for i in FW_Tcost]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*FG_Icost [i] for i in FG_Icost]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*W_Icost [i] for i in W_Icost]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*FG_Icost [i] for i in FG_Icost]+
              [(t1[i]+t2[i]+t3[i]+t4[i]+t5[i])*FM_Icost [i] for i in FM_Icost])
```             
<br><br>
Input constrains into model.
<br><br>
```
model += lpSum([t1[i] * Mcost[i] for i in Mcost]) <= 500
model += lpSum([t2[i] * Mcost[i] for i in Mcost]) <= 500 
model += lpSum([t3[i] * Mcost[i] for i in Mcost]) <= 500 
model += lpSum([t4[i] * Mcost[i] for i in Mcost]) <= 500 
model += lpSum([t5[i] * Mcost[i] for i in Mcost]) <= 500 
model += lpSum(t1['W_Icost_t11']*W_Icost['W_Icost_t11'])<=400
model += lpSum(t2['W_Icost_t11']*W_Icost['W_Icost_t11'])<=400
model += lpSum(t3['W_Icost_t11']*W_Icost['W_Icost_t11'])<=400
model += lpSum(t4['W_Icost_t11']*W_Icost['W_Icost_t11'])<=400
model += lpSum(t5['W_Icost_t11']*W_Icost['W_Icost_t11'])<=400
model += lpSum(t1['W_Icost_t21']*W_Icost['W_Icost_t21'])<=500
model += lpSum(t2['W_Icost_t21']*W_Icost['W_Icost_t21'])<=500
model += lpSum(t3['W_Icost_t21']*W_Icost['W_Icost_t21'])<=500
model += lpSum(t4['W_Icost_t21']*W_Icost['W_Icost_t21'])<=500
model += lpSum(t5['W_Icost_t21']*W_Icost['W_Icost_t21'])<=500
model += lpSum(t1['FG_Icost_t11']*FG_Icost['FG_Icost_t11'])<=70
model += lpSum(t2['FG_Icost_t11']*FG_Icost['FG_Icost_t11'])<=70
model += lpSum(t3['FG_Icost_t11']*FG_Icost['FG_Icost_t11'])<=70
model += lpSum(t4['FG_Icost_t11']*FG_Icost['FG_Icost_t11'])<=70
model += lpSum(t5['FG_Icost_t11']*FG_Icost['FG_Icost_t11'])<=70
model += lpSum(t1['FG_Icost_t21']*FG_Icost['FG_Icost_t21'])<=35
model += lpSum(t2['FG_Icost_t21']*FG_Icost['FG_Icost_t21'])<=35
model += lpSum(t3['FG_Icost_t21']*FG_Icost['FG_Icost_t21'])<=35
model += lpSum(t4['FG_Icost_t21']*FG_Icost['FG_Icost_t21'])<=35
model += lpSum(t5['FG_Icost_t21']*FG_Icost['FG_Icost_t21'])<=35
model += lpSum([t1[i]*FM_Icost[i] for i in FM_Icost])<=[t1[i]*FW_Tcost[i] for i in FW_Tcost]+[t2[i]*FW_Tcost[i] for i in FW_Tcost]
model += lpSum([t2[i]*FM_Icost[i] for i in FM_Icost])<=[t2[i]*FW_Tcost[i] for i in FW_Tcost]+[t3[i]*FW_Tcost[i] for i in FW_Tcost]
model += lpSum([t3[i]*FM_Icost[i] for i in FM_Icost])<=[t3[i]*FW_Tcost[i] for i in FW_Tcost]+[t4[i]*FW_Tcost[i] for i in FW_Tcost]
model += lpSum([t4[i]*FM_Icost[i] for i in FM_Icost])<=[t4[i]*FW_Tcost[i] for i in FW_Tcost]+[t5[i]*FW_Tcost[i] for i in FW_Tcost]
model += lpSum(W_Icost['W_Icost_t21'])==20
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
Finally, get the following table.
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

 





