# Dynamic-Supply-Chain model
<br>
<ul>
<li><h2><b>Background introduce of supply chain</b></h2></li>
Overall, the supply chain can be divided into <b>internal supply chain</b> and <b>external supply chain</b>.
<br><br>
In the process of production and circulation, the internal supply chain is a network formed by many departments of a company, including the <b>internal purchasing , production, warehousing, and sales.</b>
<br><br>
On the other hand, the external supply chain refers to the network composed of <b>raw material vendors, facilities, warehouses, and final consumers </b> which related to the enterprise.
<br><br>
In this part, we only focus on the external supply chain.
<br><br>

There are some important roles in a supply chian:
<br><br>
<ol>
<li> Vender <br>  </li>
<li> Facility <br>  </li>
<li> Warehouse <br>  </li>
<li> Customer <br>  </li>
</ol>
<br>
And these four roles will have the following five activities:<br><br>
<ol>
<li> Purchase raw materials from venders (suppliers)<br></li>
<li> Transport raw materials from venders to facilities<br></li>
<li> Assemble products in facilities<br></li>
<li> Transport products from facilities to warehouses<br></li>
<li> Transport products from warehouses to customers<br></li>
</ol>
<br>
Below figure is an example which shows the structure of a supply chain. 
<br><br>
<img src=https://github.com/peng1055/Dynamic-Supply-Chain/blob/master/activities.png width="500" height="500">
<br>
<br>
From the above picture, we could understand the supply chain is a network structure, and there is a demand and supply relationship between the downstream nodes and upstream nodes.
<br><br>
Moreover, in order to adapt to the demand of the market, each enterprises <b>need to update their strategy frequently or periodically</b>, and this circumstance makes the <b>supply chain dynamically</b>.
<br>
<br>
<li><h2><b> Build a Supply Chain Model (SCM): Notation, Variables, and Input data</b></h2></li>
To genereate a strategy that can fit market demand, we can start from the aspect of cost, and analyze the following costs from the above five activities:<br><br>
1. Material costs<br>
2. Transportation costs from suppliers to facilities<br>
3. Production cost paid to facilities<br>
4. Material inventory costs<br>
5. Inventory costs of products in facilities<br>
6. Transportation costs from facilities to warehouses<br>
7. Inventory costs of products in warehouses<br>
8. Transportation costs from warehouses to customers<br>


<br><br>
From above description, we could know the purpose of SCM is to minimize the above cost. Suppose these eight costs are all linear functions, we will introduce the notations, decision variables, and input data required by the model in the following part.
<br><br>
<ol>
<li><h3><b> Notations of SCM</b></h3></li>
The notations of SCM are as following table. 
<br><br>
<table>
<tr>
<th>Set</th> <th>Description</th> <th>Remark </th>
</tr>
<tr>
<th>V</th> <th>vender(supplier)</th> <th>v ∈ V </th>
</tr>
<tr>
<th>F</th> <th>Facility</th> <th>f ∈ F </th>
</tr>
<tr>
<th>W</th> <th>Warehouse</th> <th>w ∈ W </th>
</tr>
<tr>
<th>C</th> <th>Customer</th> <th>c ∈ C </th>
</tr>
<tr>
<th>T</th> <th>Time unit</th> <th>t ∈ T </th>
</tr>
<tr>
<th>P</th> <th>Raw material</th> <th>p ∈ P </th>
</tr>
<tr>
<th>G</th> <th>Goods</th> <th>g ∈ G </th>
</tr>
</table>
<br><br>

<li><h3><b> Input data of SCM</b></h3></li>
All values are constant and should be provided by user. 
<br><br>
<table>
<tr>
<th>Data</th> <th>Description</th> 
</tr>
<tr>
<th>Mcost<sub>tvp</sub></th> <th>the cost of material p which provided by vender v at time t</th> 
</tr>
<tr>
<th>Pcost<sub>tfg</sub> </th><th>the production cost of goods g which is produced by facility f at time t</th>
</tr>
<tr>
<th>VF_Tcost<sub>tvfp</sub> </th><th>the transportation cost of material p from vender v to facility f at time t</th>
</tr>
<tr>
<th>FW_Tcost<sub>tfwg</sub> </th><th>the transportation cost of goods g from facility f to warehouse w at time t</th>
</tr>
<tr>
<th>WC_Tcost<sub>twcg</sub> </th><th>the transportation cost of goods g from warehouse w to customer c at time t</th>
</tr>
<tr>
<th>FM_Icost<sub>tfp</sub> </th><th>the inventory cost of material p in facility f at time t</th>
</tr>
<tr>
<th>FG_Icost<sub>tfg</sub> </th><th>the inventory cost of goods g in facility f at time t</th>
</tr>
<tr>
<th>W_Icost<sub>twg</sub> </th><th>the inventory cost of goods g in warehouse w at time t</th>
</tr>
<tr>
<th>T<sub>vf</sub> </th><th>the transportation lead time from vender v to facility f</th>
</tr>
<tr>
<th>T<sub>fw</sub> </th><th>the transportation lead time from facility f to warehouse w</th>
</tr>
<tr>
<th>T<sub>wc</sub> </th><th>the transportation lead time from warehouse w to customer c</th>
</tr>
<tr>
<th>T<sub>bomfc</sub> </th><th>Time required for facility f to produce goods g</th>
</tr>
<tr>
<th>BOM<sub>gp</sub> </th><th>Quantity of raw material p required for producting goods g</th>
</tr>
</table>
<br>
<br>
<li><h3><b> Decision variables of SCM</b></h3></li>
Variables can be divided into L(Level) and R(Rate).<br>
<b>The values of these variables are what users want to know. </b>
</ol>
<br>
<br>
<table>
<tr>
<th>Decision Variables</th> <th>Description</th> 
</tr>
<tr>
<th>LV<sub>tvp</sub></th> <th>Quantity of material p purchased from vender v at time t</th> 
</tr>
<tr>
<th>R<sub>tvfp</sub> </th><th>Quantity of material p transported from vender v to facility f at time t</th>
</tr>
<tr>
<th>LF<sub>tfp</sub> </th><th>Inventory of material p in facility f at time t</th>
</tr>
<tr>
<th>R<sub>tfg</sub> </th><th>Quantity of goods g produced by facility f at time t</th>
</tr>
<tr>
<th>LF<sub>tfg</sub> </th><th>Inventory of goods g in facility f at time t</th>
</tr>
<tr>
<th>R<sub>tfwg</sub> </th><th>Quantity of goods g transported from facility f to warehouse w at time t</th>
</tr>
<tr>
<th>LW<sub>twg</sub> </th><th>Inventory of goods g in warehouse w at time t</th>
</tr>
<tr>
<th>R<sub>twcg</sub> </th><th>Quantity of goods g transported from warehouse w to customer c at time t</th>
</tr>
<tr>
<th>LC<sub>tcg</sub> </th><th>Quantity of goods g required for customer c at time t</th>
</tr>
</table>

<br>
<br>
<li><h2><b> Build a Supply Chain Model (SCM): Constrains</b></h2></li>
<ol>
<li><h3><b> Objective function</b></h3></li>
In the previous part, we mentioned that this is a minimization problem. So, the objective function is the sum of total cost, and  we try to minimize it.
<br><br>
<ul>
<li>Min &sum;<sub>t</sub> ( &sum;<sub>vp</sub> Mcost<sub>tvp</sub> &middot; LV<sub>tvp</sub> + &sum;<sub>vfp</sub> VF_Tcost<sub>tvfp</sub> &middot; R<sub>tvfp</sub> + &sum;<sub>fg</sub> Pcost<sub>tfg</sub> &middot; R<sub>tfg</sub> + &sum;<sub>fp</sub> FM_Icost<sub>tfp</sub> &middot; LF<sub>tfp</sub> + &sum;<sub>fg</sub> FG_Icost<sub>tfg</sub> &middot; LF<sub>tfg</sub> + &sum;<sub>wg</sub> W_Icost<sub>twg</sub> &middot; LW<sub>twg</sub> + &sum;<sub>fwg</sub> FW_Tcost<sub>tfwg</sub> &middot; R<sub>tfwg</sub> + &sum;<sub>wcg</sub> WC_Tcost<sub>twcg</sub> &middot; R<sub>twcg</sub> )
</li></ul>
<br><br>
<li><h3><b> Upperbound and Lowerbound constrains</b></h3></li>
<ul>
  <li>0	&le; R<sub>tvfp</sub> &le; upper R<sub>tvfp</sub>                        for all t, v, f, p</li>
  <li>0	&le; R<sub>tfwg</sub> &le; upper R<sub>tfwg</sub>                       for all t, f, w,g</li>
  <li>0	&le; R<sub>twcg</sub> &le; upper R<sub>twcg</sub>                       for all t, w, c, g</li>
  <li>lower R<sub>tfg</sub>	&le; R<sub>tfg</sub> &le; upper R<sub>tfg</sub>     for all t, g, f</li>
  <li>lower LF<sub>tfp</sub>	&le; LF<sub>tfp</sub> &le; upper LF<sub>tfp</sub>  for all t, f, p</li>
  <li>lower LF<sub>tfg</sub>	&le; LF<sub>tfg</sub> &le; upper LF<sub>tfg</sub>  for all t, f, g</li>
  <li>lower LW<sub>twg</sub>	&le; LW<sub>twg</sub> &le; upper LW<sub>twg</sub>  for all t, w, g</li>
</ul>
<li><h3><b> Flow conservation constraints</b></h3></li>
<ul>
  <li>&sum;<sub>f</sub> R<sub>tvfp</sub> = LV<sub>tvp</sub> for all t, v, p</li>
  <li>LF<sub>tfp</sub> &minus; &sum;<sub>g</sub> BOM<sub>gp</sub>R<sub>tfg</sub> = LF<sub>(t+1)fp</sub> for all f, p, and 0 < t &le; T<sub>vf</sub></li>
  <li>LF<sub>tfp</sub> + &sum;<sub>v</sub> R<sub>(t &minus; T<sub>vf</sub>)vfp</sub> &minus; &sum;<sub>g</sub> BOM<sub>gp</sub>R<sub>tfg</sub> = LF<sub>(t+1)fp</sub> for all f, p, and T<sub>vf</sub> < t &le; n</li>
  <li>LF<sub>tfg</sub> &minus; &sum;<sub>w</sub> R<sub>tfwg</sub> = LF<sub>(t+1)fg</sub> for all f, g, and 0 < t &le; T<sub>bomfg</sub></li>
  <li>LF<sub>tfg</sub> + R<sub>(t &minus; T<sub>bomfg</sub>)fg</sub> &minus; &sum;<sub>w</sub> R<sub>tfwg</sub> = LF<sub>(t+1)fg</sub> for all f, g, and T<sub>bomfg</sub> < t &le; n</sub></li>
  <li>LW<sub>twg</sub> &minus; &sum;<sub>c</sub> R<sub>twcg</sub> = LW<sub>(t+1)wg</sub> for all w, g, and 0 < t &le; T<sub>fw</sub></li>
  <li>LW<sub>twg</sub> + &sum;<sub>f</sub> R<sub>(t &minus; T<sub>fw</sub>)fwg</sub> &minus; &sum;<sub>c</sub> R<sub>twcg</sub> = LW<sub>(t+1)wg</sub> for all w, g, and T<sub>fw</sub> < t &le; n</sub></li>
  <li>&sum;<sub>w</sub> R<sub>(t &minus; T<sub>wc</sub>)wcg</sub> = LC<sub>tcg</sub> for all t, c, g</sub></li>
</ul>
</ol>
<br><br>
<li><h2><b> An example of supply chain model</b></h2></li>
Please refer to the <a href="https://github.com/peng1055/Dynamic-Supply-Chain/blob/master/SCM%20example.md">SCM Example</a>.
<br><br>
<li><h2><b>Summary</b></h2></li>
In this article, we introduced the basic concepts of supply chain and the conditions required to build the supply chain models. However, in reality, the cost functions may not be linear, and there may be a quantity discount. This is the part that the linear model cannot explain.


<li><h2><b>Reference</b></h2></li>
<ul>
  <li>Handout of Operations Research Applications, ORA_03_Capacity_Scheduling_SCM_2020, Dr. Chia-Yen Lee</li>
  <li>黎漢林, 供應鏈管理與決策, 儒林</li>
  <li>https://wiki.mbalib.com/zh-tw/%E4%BE%9B%E5%BA%94%E9%93%BE</li>
    
    
</ul>
</ul>
