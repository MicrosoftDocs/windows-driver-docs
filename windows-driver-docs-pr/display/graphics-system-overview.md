---
title: Graphics System Overview
description: Graphics System Overview
ms.assetid: d120a9df-d8ed-4862-b421-2e7545be1ed0
keywords:
- GDI WDK Windows 2000 display , about graphics system
- graphics drivers WDK Windows 2000 display , about graphics system
- drawing WDK GDI , about graphics system
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Graphics System Overview


## <span id="ddk_graphics_system_overview_gg"></span><span id="DDK_GRAPHICS_SYSTEM_OVERVIEW_GG"></span>


Microsoft Windows NTâˆ’based operating systems provide a robust graphics architecture in which third-party graphics hardware companies can easily integrate their video displays and printing devices. These sections provide design guidelines for writing effective graphics drivers:

-   [**Graphics DDI**](using-the-graphics-ddi.md)

    This section describes the Windows Graphics Device Interface (GDI) and Graphics device driver interface (DDI). Design and implementation details that are common to both display and printing drivers are discussed.

-   [**Windows Display Driver Model (WDDM) Design Guide**](windows-vista-display-driver-model-design-guide.md)

    [**Windows 2000 Display Driver Model (XDDM) Design Guide**](windows-2000-display-driver-model-design-guide.md)

    These sections describe the video display environment in Windows NTâˆ’based operating systems and provide design and implementation details for display, video miniport, and monitor driver writers. Note that drivers that comply with the Windows 2000 Display Driver Model cannot be installed on Windows 8 and later computers.

-   [**Print Devices Design Guide**](https://msdn.microsoft.com/library/windows/hardware/ff561035)

    This section describes the drivers and print spooler that make up the printing environment in Windows NTâˆ’based operating systems. Sections within this part of the Windows Driver Kit (WDK) specify how to provide customized driver and spooler components, so that new printer hardware and network configurations can be supported.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Graphics%20System%20Overview%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




