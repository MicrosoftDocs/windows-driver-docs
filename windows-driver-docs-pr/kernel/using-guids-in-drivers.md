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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Using%20GUIDs%20in%20Drivers%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


