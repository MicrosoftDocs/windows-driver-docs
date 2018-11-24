---
title: DisplayConfigSetDeviceInfo Summary and Scenarios
description: DisplayConfigSetDeviceInfo Summary and Scenarios
ms.assetid: b00c1586-26f0-4fe1-8cc8-3db552ebba86
keywords:
- connecting displays WDK Windows 7 display , CCD APIs, DisplayConfigSetDeviceInfo
- connecting displays WDK Windows Server 2008 R2 display , CCD APIs, DisplayConfigSetDeviceInfo
- configuring displays WDK Windows 7 display , CCD APIs, DisplayConfigSetDeviceInfo
- configuring displays WDK Windows Server 2008 R2 display , CCD APIs, DisplayConfigSetDeviceInfo
- CCD concepts WDK Windows 7 display , DisplayConfigSetDeviceInfo
- CCD concepts WDK Windows Server 2008 R2 display , DisplayConfigSetDeviceInfo
- DisplayConfigSetDeviceInfo WDK Windows 7 display
- DisplayConfigSetDeviceInfo WDK Windows Server 2008 R2 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# DisplayConfigSetDeviceInfo Summary and Scenarios


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following sections summarize how a caller uses the [**DisplayConfigSetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553909) CCD function and provide scenarios for using **DisplayConfigSetDeviceInfo**.

### <span id="displayconfigsetdeviceinfo_summary"></span><span id="DISPLAYCONFIGSETDEVICEINFO_SUMMARY"></span>DisplayConfigSetDeviceInfo Summary

The caller can use [**DisplayConfigSetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553909) to set the properties of a target. **DisplayConfigSetDeviceInfo** can only be currently used to start and stop boot persisted force projection on an analog target.

### <span id="displayconfigsetdeviceinfo_scenarios"></span><span id="DISPLAYCONFIGSETDEVICEINFO_SCENARIOS"></span>DisplayConfigSetDeviceInfo Scenarios

[**DisplayConfigSetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553909) is called in the following scenarios:

-   Suppose that a user used S-video or composite connector to connect a television and that the operating system is unable to detect the television. The display control panel applet can call [**DisplayConfigSetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553909) to force the output on the connector.

-   Suppose that a user used a switchbox or KVM switch and that the operating system is unable to read the EDID from the monitor. The display control panel applet can call [**DisplayConfigSetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553909) to force the output on the connector and set a resolution.

 

 





