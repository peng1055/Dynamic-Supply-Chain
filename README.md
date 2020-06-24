# Dynamic-Supply-Chain model
<br>
<h3><b>Background introduce of supply chain</b></h3><br>
Overall, the supply chain can be divided into <b>internal supply chain</b> and <b>external supply chain</b>.
<br><br>
In the process of production and circulation, the internal supply chain is a network formed by many departments of a company, including the <b>internal purchasing , production, warehousing, and sales.</b> On the other hand, the external supply chain refers to the network composed of <b>raw material vendors, facilities, Warehouses, and final consumers </b> which related to the enterprise.
<br>
In this part, we only focus on the external supply chain.
<br>

There are some important roles in a supply chian:
<br>
1. Vender <br>  
2. Facility <br>  
3. Warehouse <br>  
4. Customer <br>  

And these four roles will have the following five activities:<br>
1. Purchase raw materials from venders (suppliers)<br>
2. Transport raw materials from venders to facilities<br>
3. Assemble products in facilities<br>
4. Transport products from facilities to warehouses<br>
5. Transport products from warehouses to customers<br>

Below figure is an example which shows the structure of a supply chain.  <br>
<br>
<img src=https://github.com/peng1055/Dynamic-Supply-Chain/blob/master/activities.png width="500" height="500">
<br><br>

From the above picture, we could understand the supply chain is a network structure, and there is a demand and supply relationship between the downstream nodes and upstream nodes.
<br><br>
Moreover, in order to adapt to the demand of the market, each enterprises <b>need to update their strategy frequently or periodically</br>, and this circumstance makes the <b>supply chain dynamically</b>.
<br><br>

<h3><b> Build a Supply Chain Model (SCM)</b></h3>

To genereate a strategy that can fit market demand, we can start from the aspect of cost, and analyze the following costs from the above five activities:<br>
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
In the following space, we will introduce the variables, constraints, and input data required by the model.
