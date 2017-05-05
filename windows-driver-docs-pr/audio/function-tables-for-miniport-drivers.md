---
title: Function Tables for Miniport Drivers
description: Function Tables for Miniport Drivers
ms.assetid: 86b8bfa7-0c57-480b-b6f6-7c0214f53773
keywords:
- function tables WDK audio
- audio miniport drivers WDK , function tables
- miniport drivers WDK audio , function tables
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Function Tables for Miniport Drivers


## <span id="function_tables_for_miniport_drivers"></span><span id="FUNCTION_TABLES_FOR_MINIPORT_DRIVERS"></span>


A generic miniport driver's upper-edge interfaces (see [WDM Audio Terminology](wdm-audio-terminology.md)) consist of function tables. Some non-audio miniport drivers supply the function table to the port driver during registration, at which time the miniport driver informs the port driver of the size of the context structure that the miniport driver will require. The port driver copies the function table to some private location, allocates the context structure, and calls an initialization function in the function table, passing a pointer to the context structure.

Similarly, audio miniport drivers use function tables, but they are statically allocated and do not need to be copied by the port driver. The port driver also retrieves its context ("object") memory from a specified pool and installs a pointer to the function table into the context. Because the function table pointer is always the first field in the context, the port driver needs only a context pointer and can access the function table through the context.

This approach was taken because COM supplies a solid, efficient, widely-understood model for creating abstracted objects. The audio miniport driver model leverages industry experience with COM and the body of COM literature. Objects can be implemented and used in C or C++. Assembly language can also be used, but should only be used where portability is not required.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[audio\audio]:%20Function%20Tables%20for%20Miniport%20Drivers%20%20RELEASE:%20%287/18/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


