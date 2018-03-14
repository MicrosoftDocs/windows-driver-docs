---
title: Using GUIDs in Drivers
author: windows-driver-content
description: Using GUIDs in Drivers
ms.assetid: b70a2f64-dd7b-4d76-a4cf-dcb60ce0585c
keywords: ["globally unique identifiers WDK kernel", "GUIDs WDK kernel", "identifiers WDK GUIDs", "header files WDK GUIDs", "kernel-mode drivers WDK , GUIDs"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Using GUIDs in Drivers


## <a href="" id="ddk-using-guids-in-drivers-kg"></a>


Drivers and other system components use *globally unique identifiers* (GUIDs) to identify a variety of items. System components define GUIDs for items such as [device setup classes](https://msdn.microsoft.com/library/windows/hardware/ff541509), PnP events, WMI events, and still image events. Driver writers can create GUIDs for items such as [device interface classes](https://msdn.microsoft.com/library/windows/hardware/ff541339), custom PnP events, and custom WMI events. Drivers and applications include header files that define the GUIDs that they use.

This section includes the following topics:

[Defining and Exporting New GUIDs](defining-and-exporting-new-guids.md)

[Including GUIDs in Driver Code](including-guids-in-driver-code.md)

For information about using GUIDs in user-mode applications, see Microsoft Windows SDK documentation.

 

 




