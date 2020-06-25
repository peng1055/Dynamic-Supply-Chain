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
From above description, we could know the purpose of SCM is to minimize the above cost. 
In the following part, we will introduce the notations, decision variables, and input data required by the model.
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
Al values are constant and should be provided by user. 
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
</ol>
Variables can be divided into L(Level) and R(Rate).<br>
<b>The values of these variables are what users want to know. </b>
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
<table>

<br>
<br>
<li><h2><b> Build a Supply Chain Model (SCM): Constrains</b></h2></li>
<ol>
<li><h3><b> Objective function</b></h3></li>
In the previous part, we mentioned that this is a minimization problem. So, the objective function is the sum of total cost, and  we try to minimize it.

```matlab
Min &sum;<sup>t</sup>
```










</ol>

</ul>
