<h1><b>Example of SCM</b></h1>
d

```
from pulp import *
```


```matlab
% xlsread(filename,sheet,xlRange): use Excel range syntax in "xlRange".
j_num = xlsread('JSP_dataset.xlsx','Parameters','B2'); % Job Counts
ma_num = xlsread('JSP_dataset.xlsx','Parameters','B3'); % Machine Counts
PT = xlsread('JSP_dataset.xlsx','ProcessingTime','B2:K11'); % Processing Time
Ma = xlsread('JSP_dataset.xlsx','MachineSequence','B2:K11'); % Machine Sequence
```
