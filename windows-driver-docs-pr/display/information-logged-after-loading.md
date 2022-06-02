---
title: Information Logged After Loading
description: "When GPUView successfully loads, it logs the GuidStats.txt and FuncStats.txt text files and places these files in the same directory that contains GPUView.exe."
ms.date: 05/10/2022
---

# Information Logged After Loading  

When GPUView successfully loads, it logs the GuidStats.txt and FuncStats.txt text files and places these files in the same directory that contains GPUView.exe. The following sections describe these text files.  

### GuidStats.txt  
GuidStats.txt is a text file that lists all the different GUIDs that GPUView is aware of along with the hit count, memory-consumption estimate, friendly name, and level for the GUID. This GUID information provides a quick overview about the different events that GPUView found in an ETL file.   

The following table describes the overview information that GuidStats.txt provides for each GUID:  

| Overview       | Description                                                                                                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Hit count      | The number of times that an event of a particular type occurred in the ETL file.                                                                                                                    |
| Bytes consumed | The amount of memory that was allocated to store the event's data.                                                                                                                                  |
| Friendly name  | The friendly name that GPUView associates with the GUID for reference.                                                                                                                              |
| Level          | A value that GPUView assigns to the event. You can use this value with the /**Limit** command-line option. For more information about how this value is used, see [Option: Limit](option-limit.md). |


### FuncStats.txt  
FuncStats.txt is a text file that contains information about all profiled functions that GPUView is aware of. GPUView scans all processes and threads and summarizes the hit count and time spent in the functions. FuncStats.txt is useful for quickly determining whether a particular function was called during the generation of the ETL file.

