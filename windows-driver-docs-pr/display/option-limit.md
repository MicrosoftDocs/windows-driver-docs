---
title: "Option: Limit"
description: "This option causes GPUView to filter unimportant events and objects to prevent GPUView from using too much memory."
ms.date: 03/14/2023
---

# Option: Limit  

The **Limit** option causes GPUView to filter out unimportant events and objects. This filtering results in GPUView using less memory, which allows the user to load large ETL files.

There are several different filter levels. You can find examples of the different levels in *GuidStats.txt*. The level specified includes the associated events and objects and all the previous levels’ events and objects. For example, if level 3 is specified then all the events and objects from levels 0, 1, 2, and 3 are included and the events and objects from levels 4 and 5 are excluded.

The following table shows the numbers that you can use to filter the indicated events and objects.

| Number | Which events and objects are included |
| ------ | ------------------------------------- |
| 0      | Critical events like process and thread events that are used to generate  execution information. |
| 1      | Key objects that provide context information like queue packets, DMA  packets, and object allocations. |
| 2      | Useful objects, like VSync, stack walk, and page fault information. |
| 3      | Extra information. That is, events that are nice to see, but don't provide any other information than a name and an event handler, which dumps its own data. |
| 4      | Default. Any information that has a name. In other words, if the event has a  GUID that is named in GuidStats.txt, that event is shown. |
| 5      | No name events. If an ETL file has events that GPUView can't interpret, the events aren't named. GPUView typically filters out these events  with the default level (4). To see these events, you should specify this level. |

You can use the following syntax with this option:  

``` cmd
Gpuview /l 3  
Gpuview -Limit 5  
```

If you specify a level greater than the supported levels, GPUView ignores the input, sets the level to the default level, and loads typically.

If you don't specify a level, GPUView automatically loads as if you specified level 4 on the command line.

If you specify more than one level, GPUView doesn't load.
