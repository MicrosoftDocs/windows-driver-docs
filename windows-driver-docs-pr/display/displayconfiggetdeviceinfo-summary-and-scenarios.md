---
title: DisplayConfigGetDeviceInfo Summary and Scenarios
description: DisplayConfigGetDeviceInfo Summary and Scenarios
keywords:
- connecting displays WDK Windows 7 display , CCD APIs, DisplayConfigGetDeviceInfo
- connecting displays WDK Windows Server 2008 R2 display , CCD APIs, DisplayConfigGetDeviceInfo
- configuring displays WDK Windows 7 display , CCD APIs, DisplayConfigGetDeviceInfo
- configuring displays WDK Windows Server 2008 R2 display , CCD APIs, DisplayConfigGetDeviceInfo
- CCD concepts WDK Windows 7 display , DisplayConfigGetDeviceInfo
- CCD concepts WDK Windows Server 2008 R2 display , DisplayConfigGetDeviceInfo
- DisplayConfigGetDeviceInfo WDK Windows 7 display
- DisplayConfigGetDeviceInfo WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
---

# DisplayConfigGetDeviceInfo Summary and Scenarios


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following sections summarize how a caller uses the [**DisplayConfigGetDeviceInfo**](/windows/win32/api/winuser/nf-winuser-displayconfiggetdeviceinfo) CCD function and provide scenarios for using **DisplayConfigGetDeviceInfo**.

### <span id="displayconfiggetdeviceinfo_summary"></span><span id="DISPLAYCONFIGGETDEVICEINFO_SUMMARY"></span>DisplayConfigGetDeviceInfo Summary

The caller can use [**DisplayConfigGetDeviceInfo**](/windows/win32/api/winuser/nf-winuser-displayconfiggetdeviceinfo) to obtain more friendly names to display in the user interface. The caller can obtain names for the adapter, the source, and the target. The caller can also use **DisplayConfigGetDeviceInfo** to obtain the native resolution of the connected display device.

### <span id="displayconfiggetdeviceinfo_scenarios"></span><span id="DISPLAYCONFIGGETDEVICEINFO_SCENARIOS"></span>DisplayConfigGetDeviceInfo Scenarios

[**DisplayConfigGetDeviceInfo**](/windows/win32/api/winuser/nf-winuser-displayconfiggetdeviceinfo) is called in the following scenarios:

-   The display control panel applet calls [**DisplayConfigGetDeviceInfo**](/windows/win32/api/winuser/nf-winuser-displayconfiggetdeviceinfo) to obtain the monitor name to display in the drop-down menu that lists all the connected monitors.

-   The display control panel applet calls [**DisplayConfigGetDeviceInfo**](/windows/win32/api/winuser/nf-winuser-displayconfiggetdeviceinfo) to obtain the name of the adapters that are connected to the system.

-   The display control panel applet calls [**DisplayConfigGetDeviceInfo**](/windows/win32/api/winuser/nf-winuser-displayconfiggetdeviceinfo) to obtain the native resolution of each connected monitor so the resolution can be highlighted in the user interface.

 

