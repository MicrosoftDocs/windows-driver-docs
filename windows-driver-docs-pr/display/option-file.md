---
title: Option: File
description: "By default, GPUView inspects the command for the name of the ETL file to open."
ms.date: 05/10/2022
---

# Option: File  

By default, GPUView inspects the command for the name of the ETL file to open. The ETL file name should always be the last parameter unless you use this switch.   

You can use the following syntax with this option:  

Gpuview /f NameOfEtlFile.etl 
Gpuview /File NameOfEtlFile.etl  

> [!NOTE]
> Spaces and quotes are not allowed in the file name. Also, when GPUView loads, it tries to verify that the file name that is specified is an actual file. If the file name does not exist, GPUView does not load. 
