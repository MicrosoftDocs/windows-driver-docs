---
title: "Option: Stats"
description: "This option causes GPUView to process all events in an ETL file."
ms.date: 05/10/2022
---

# Option: Stats  

This option causes GPUView to process all events in an ETL file. GPUView performs a first pass over the data. GPUView then exits and leaves the GuidStats.txt file. GuidStats.txt is a comma-delimited file.   

With large ETL files, there is sometimes not enough memory available to load an entire file into memory. When this happens, you might still be able to have GPUView process the events in the file and log the standard GuidStats.txt file. GuidStats.txt shows the number of times that a particular type of GUID is found in the file along with the memory that would be consumed by the GUID if GPUView is loaded typically.  

Another key item in the GuidStats.txt file is the Level value that is currently found on the end of the line. This value can be used with the /limit option to ignore groupings of events in the file. For more information about how this value is used, see Option: Limit.   

You can use the following syntax with this option:  

Gpuview /s merged.etl 
Gpuview /stats merged.etl 
