---
title: "Option: Limit"
description: "This option causes GPUView to filter unimportant events and objects to prevent GPUView from using too much memory."
ms.date: 05/10/2022
---

# Option: Limit  

This option causes GPUView to filter unimportant events and objects to prevent GPUView from using too much memory. If GPUView uses less memory, the user can load large ETL files. Different events and objects have different levels of importance to GPUView. Therefore, with this option the user can filter out things that are unimportant and consume memory space.  

There are several different filter levels. Examples of the different levels can be viewed in the GuidStats.txt file. The following table shows the numbers that you can use to filter the indicated events and objects.   

| Number | What events and objects are filtered                                                                                                                                                                                                  |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0      | Critical events like process and thread events that are used to generate  execution information.                                                                                                                                      |
| 1      | Key objects that provide context information like queue packets, DMA  packets, and object allocations.                                                                                                                                |
| 2      | Useful objects, like VSync, stackwalk, and page fault information.                                                                                                                                                                    |
| 3      | Extra information. That is, events that are nice to see, but do not provide  any other information than a name and an event handler, which dumps its own  data.                                                                       |
| 4      | Default. Any information that has a name. In other words, if the event has a  GUID that is named in GuidStats.txt, that event is shown.                                                                                               |
| 5      | No name events. If an ETL file has events in it that GPUView cannot  interpret, the events are not named. GPUView typically filters out these events  with the default level (4). To see these events, you should specify this level. |

You can use the following syntax with this option:  

Gpuview /l 3  
Gpuview -Limit 5  

> [!NOTE]
> If you specify a level greater than the supported levels, GPUView ignores the input, sets the level to the default level, and loads typically. If you do not specify a level, which is the default, GPUView automatically loads as if you specified level 4 on the command line. If you specify more than one level, GPUView does not load. 
