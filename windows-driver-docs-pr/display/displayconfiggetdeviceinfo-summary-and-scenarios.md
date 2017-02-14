---
title: DisplayConfigGetDeviceInfo Summary and Scenarios
description: DisplayConfigGetDeviceInfo Summary and Scenarios
ms.assetid: 19d9a77c-252e-4623-b4bc-f0b990ed31e2
keywords: ["connecting displays WDK Windows 7 display , CCD APIs, DisplayConfigGetDeviceInfo", "connecting displays WDK Windows Server 2008 R2 display , CCD APIs, DisplayConfigGetDeviceInfo", "configuring displays WDK Windows 7 display , CCD APIs, DisplayConfigGetDeviceInfo", "configuring displays WDK Windows Server 2008 R2 display , CCD APIs, DisplayConfigGetDeviceInfo", "CCD concepts WDK Windows 7 display , DisplayConfigGetDeviceInfo", "CCD concepts WDK Windows Server 2008 R2 display , DisplayConfigGetDeviceInfo", "DisplayConfigGetDeviceInfo WDK Windows 7 display", "DisplayConfigGetDeviceInfo WDK Windows Server 2008 R2 display"]
---

# DisplayConfigGetDeviceInfo Summary and Scenarios


This section applies only to Windows 7 and later, and Windows Server 2008 R2 and later versions of Windows operating system.

The following sections summarize how a caller uses the [**DisplayConfigGetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553903) CCD function and provide scenarios for using **DisplayConfigGetDeviceInfo**.

### <span id="displayconfiggetdeviceinfo_summary"></span><span id="DISPLAYCONFIGGETDEVICEINFO_SUMMARY"></span>DisplayConfigGetDeviceInfo Summary

The caller can use [**DisplayConfigGetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553903) to obtain more friendly names to display in the user interface. The caller can obtain names for the adapter, the source, and the target. The caller can also use **DisplayConfigGetDeviceInfo** to obtain the native resolution of the connected display device.

### <span id="displayconfiggetdeviceinfo_scenarios"></span><span id="DISPLAYCONFIGGETDEVICEINFO_SCENARIOS"></span>DisplayConfigGetDeviceInfo Scenarios

[**DisplayConfigGetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553903) is called in the following scenarios:

-   The display control panel applet calls [**DisplayConfigGetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553903) to obtain the monitor name to display in the drop-down menu that lists all the connected monitors.

-   The display control panel applet calls [**DisplayConfigGetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553903) to obtain the name of the adapters that are connected to the system.

-   The display control panel applet calls [**DisplayConfigGetDeviceInfo**](https://msdn.microsoft.com/library/windows/hardware/ff553903) to obtain the native resolution of each connected monitor so the resolution can be highlighted in the user interface.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DisplayConfigGetDeviceInfo%20Summary%20and%20Scenarios%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




