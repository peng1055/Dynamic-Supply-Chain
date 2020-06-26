<h1><b>Example of SCM</b></h1>
&#9733  If you  haven’t read the SC model, please check <a herf="https://github.com/peng1055/Dynamic-Supply-Chain/blob/master/DSCM.md#-build-a-supply-chain-model-scm-notation-variables-and-input-data">HERE</a>!
<br>
After introducing the SC model, we take an example for it. 
<br>
<br>
Define the struture of SCM as below:
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
<br>












```
from pulp import *
```
