---
title: QueryDisplayConfig Summary and Scenarios
description: QueryDisplayConfig Summary and Scenarios
ms.assetid: a556b3d7-3cac-49b1-99db-7ce8a844a8a8
keywords:
- connecting displays WDK Windows 7 display , CCD APIs, QueryDisplayConfig
- connecting displays WDK Windows Server 2008 R2 display , CCD APIs, QueryDisplayConfig
- configuring displays WDK Windows 7 display , CCD APIs, QueryDisplayConfig
- configuring displays WDK Windows Server 2008 R2 display , CCD APIs, QueryDisplayConfig
- CCD concepts WDK Windows 7 display , QueryDisplayConfig
- CCD concepts WDK Windows Server 2008 R2 display , QueryDisplayConfig
- QueryDisplayConfig WDK Windows 7 display
- QueryDisplayConfig WDK Windows Server 2008 R2 display
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# QueryDisplayConfig Summary and Scenarios


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following sections summarize how a caller uses the [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) CCD function and provide scenarios for using **QueryDisplayConfig**.

### <span id="querydisplayconfig_summary"></span><span id="QUERYDISPLAYCONFIG_SUMMARY"></span>QueryDisplayConfig Summary

The caller can use [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) to enumerate any of the following information:

-   All of the individual paths that are possible for the current set of connected monitors. The caller can then combine the paths to construct possible topologies.

-   All of the paths that are currently active.

-   The active paths as they are currently defined in the persistence database for the set of connected displays.

-   The source and target mode along with orientation, scaling, layout, and connector type on a per-path basis.

-   The hot-key options that the current topology maps to.

### <span id="querydisplayconfig_scenarios"></span><span id="QUERYDISPLAYCONFIG_SCENARIOS"></span>QueryDisplayConfig Scenarios

[**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) is called in the following scenarios:

-   The display control panel applet calls [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) to populate the Control Panel's user interface with the current applied topology when the Control Panel first starts. The current applied topology includes those displays on which forced projection is enabled.

-   The display control panel applet calls [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) to enumerate all of the possible paths to populate the **multimon** drop-down box.

-   Before the Control Panel user interface starts, the display hot key calls [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) to obtain the display option (that is, clone, internal, external, or extended) that is currently set.

-   A third party application might call [**QueryDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569215) to query the current settings that are stored in the database for the set of connected displays.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20QueryDisplayConfig%20Summary%20and%20Scenarios%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




