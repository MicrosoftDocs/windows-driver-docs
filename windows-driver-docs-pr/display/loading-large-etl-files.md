---
title: Loading Large ETL Files
description: "ETL files are often larger than what the GPUView can load into memory."
ms.date: 05/10/2022
---

# Loading Large ETL Files  

ETL files are often larger than what the GPUView can load into memory. To make these large ETL files useful, GPUView provides the **/Limit** command-line option. For more information about this option, see Option: Limit. You can use the **/Limit** option to filter out events that do not interest you and that consume memory when GPUView loads the ETL file.   

The default level for the **/Limit** option is 4. To determine a more limiting level, open the GuidStats.txt file to find events that are consuming too much memory, and then note the level for those events. If they exist on level 4, you might want to have GPUView filter out events at a more limiting level (for example, level 3). To set level 3, use the following command:   

Gpuview /l 3   

GPUView filters out unnamed events by default (that is, at level 4). Therefore, if you want to view an ETL file that is known to contain private events of GPUView-unknown events, use the following command to make GPUView show these unknown events by using their GUID as the name:  

Gpuview /l 5 
