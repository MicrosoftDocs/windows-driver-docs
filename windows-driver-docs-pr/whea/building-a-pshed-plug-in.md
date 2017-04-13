---
title: Building a PSHED Plug-In
author: windows-driver-content
description: Building a PSHED Plug-In
ms.assetid: 2d4dc052-af8b-4ee1-a8e7-4dbbb3817616
---

# Building a PSHED Plug-In


A PSHED plug-in is built by using the WDK like any other Windows Driver Model (WDM) device driver except that in addition to linking to the kernel and the hardware abstraction layer (HAL), a PSHED plug-in must also explicitly link to *Pshed.lib*.

**Note**  Starting with Windows 7, various Windows Hardware Error Architecture (WHEA) data types have been renamed from earlier versions of the WDK. For more information about these changes, see [Renamed WHEA Data Types](renamed-whea-data-types.md). If you plan to build an existing PSHED plug-in with Windows 7 or later version of the WDK, you can still use the former WHEA data type names. To do this, add the following information to the *sources* file that is used to build the plug-in:
`C_DEFINES = $(C_DEFINES) /DWHEA_DOWNLEVEL_TYPE_NAMES`

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bwhea\whea%5D:%20Building%20a%20PSHED%20Plug-In%20%20RELEASE:%20%289/14/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


