---
title: Graphics System Overview
description: Graphics System Overview
ms.assetid: d120a9df-d8ed-4862-b421-2e7545be1ed0
keywords:
- GDI WDK Windows 2000 display , about graphics system
- graphics drivers WDK Windows 2000 display , about graphics system
- drawing WDK GDI , about graphics system
ms.date: 04/20/2017
ms.localizationpriority: medium
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

 

 





