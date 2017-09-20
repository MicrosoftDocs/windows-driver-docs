---
title: Writing an Unload Routine
author: windows-driver-content
description: Writing an Unload Routine
ms.assetid: 578f3499-28fc-412b-bbb7-75f8023fa7c1
keywords: ["standard driver routines WDK kernel , Unload routines", "driver routines WDK kernel , Unload routines", "routines WDK kernel , Unload routines", "Unload routines WDK kernel", "Unload routines WDK kernel , about Unload routines", "replacing drivers", "driver replacements WDK kernel", "unloading drivers", "reloading drivers WDK kernel", "driver unloading WDK kernel", "driver reloading WDK kernel"]
ms.author: windowsdriverdev
ms.date: 06/16/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Writing an Unload Routine


## <a href="" id="ddk-writing-an-unload-routine-kg"></a>


Any driver that can be replaced, or unloaded and reloaded, while the system is running must have an [*Unload*](https://msdn.microsoft.com/library/windows/hardware/ff564886) routine. All WDM drivers must have *Unload* routines.

Although *Unload* routines are optional for non-WDM drivers, [Driver Verifier](https://msdn.microsoft.com/library/windows/hardware/ff545448) will fail any driver that does not provide an *Unload* routine.

This section contains the following topics:

[Unload Routine Environment](unload-routine-environment.md)

[Unload Routine Functionality](unload-routine-functionality.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bkernel\kernel%5D:%20Writing%20an%20Unload%20Routine%20%20RELEASE:%20%286/14/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


