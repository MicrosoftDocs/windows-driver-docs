---
title: Required Items in WMI Classes
author: windows-driver-content
description: Required Items in WMI Classes
ms.assetid: c978d8d0-5281-481a-b1e5-fd9a57d583d5
keywords: ["classes WDK WMI", "WMI WDK kernel , classes"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Required Items in WMI Classes


## <a href="" id="ddk-required-items-in-wmi-classes-kg"></a>


All class definitions except embedded classes must include the items **InstanceName** and **Active**, which must appear exactly as shown:

```
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

 

 




