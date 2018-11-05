---
title: SetDisplayConfig Summary and Scenarios
description: SetDisplayConfig Summary and Scenarios
ms.assetid: f9bce5d4-b511-475c-8e0a-eb60765a3326
keywords:
- connecting displays WDK Windows 7 display , CCD APIs, SetDisplayConfig
- connecting displays WDK Windows Server 2008 R2 display , CCD APIs, SetDisplayConfig
- configuring displays WDK Windows 7 display , CCD APIs, SetDisplayConfig
- configuring displays WDK Windows Server 2008 R2 display , CCD APIs, SetDisplayConfig
- CCD concepts WDK Windows 7 display , SetDisplayConfig
- CCD concepts WDK Windows Server 2008 R2 display , SetDisplayConfig
- SetDisplayConfig WDK Windows 7 display
- SetDisplayConfig WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# SetDisplayConfig Summary and Scenarios


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following sections summarize how a caller uses the [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) CCD function and provide scenarios for using **SetDisplayConfig**.

### <span id="setdisplayconfig_summary"></span><span id="SETDISPLAYCONFIG_SUMMARY"></span>SetDisplayConfig Summary

The caller can use [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) to apply a topology along with other display settings. That is, the caller can use **SetDisplayConfig** to set the topology, layout, orientation, aspect ratio, bit depth, and so on. The caller can use **SetDisplayConfig** to perform the following operations:

-   Set a particular topology of sources and targets.

-   Define the source and target mode for each path along with layout, orientation, and scaling factor.

-   Update the database while applying the display settings.

-   Test whether a particular topology that was constructed by using enumerated paths is possible.

-   Directly apply the last known setting from the database that maps to one of the four options from the hot key.

-   Enable forced projection on a target.

-   Invoke the new operating system best mode logic.

### <span id="setdisplayconfig_scenarios"></span><span id="SETDISPLAYCONFIG_SCENARIOS"></span>SetDisplayConfig Scenarios

[**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) is called in the following scenarios:

-   The display control panel applet calls [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) to test all the possible options to populate the **multimon** drop-down box.

-   The display control panel applet calls [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) to apply the setting that a user selected from the drop-down menu.

-   The display control panel applet calls [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) to apply the settings that a user selected from the user interface. These settings include resolution, layout, orientation, scaling, primary, bit depth, and refresh rate.

-   After the user makes a selection, the display hot key calls [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) to apply the appropriate setting from the persistence database.

-   Tasks under the Control Panel user interface call [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) to apply the appropriate setting, which is based on the type of the task.

-   The display control panel applet calls [**SetDisplayConfig**](https://msdn.microsoft.com/library/windows/hardware/ff569533) to start or stop forced projection on a particular target.

 

 





