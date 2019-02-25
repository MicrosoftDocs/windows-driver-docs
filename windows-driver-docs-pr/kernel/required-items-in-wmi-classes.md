---
title: Required Items in WMI Classes
description: Required Items in WMI Classes
ms.assetid: c978d8d0-5281-481a-b1e5-fd9a57d583d5
keywords: ["classes WDK WMI", "WMI WDK kernel , classes"]
ms.date: 06/16/2017
ms.localizationpriority: medium
---

# Required Items in WMI Classes





All class definitions except embedded classes must include the items **InstanceName** and **Active**, which must appear exactly as shown:

```cpp
//WMI class definition
[
    //Class qualifiers
]
ClassName : BaseClassName
{
    [key, read]
     string InstanceName;
    [read] 
     boolean Active;
 
    // Driver-defined data items
}
```

The **InstanceName** and **Active** items are required and used internally by WMI. The MOF class definitions of a driver's data and event blocks must include these items, but the driver must not set these items when responding to a query for the data block or sending an event, because they are not part of the driver's data block.

 

 




