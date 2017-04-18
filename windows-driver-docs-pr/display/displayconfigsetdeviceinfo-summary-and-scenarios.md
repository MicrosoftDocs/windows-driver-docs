---
title: DisplayConfigSetDeviceInfo Summary and Scenarios
description: DisplayConfigSetDeviceInfo Summary and Scenarios
ms.assetid: b00c1586-26f0-4fe1-8cc8-3db552ebba86
keywords: ["connecting displays WDK Windows 7 display , CCD APIs, DisplayConfigSetDeviceInfo", "connecting displays WDK Windows Server 2008 R2 display , CCD APIs, DisplayConfigSetDeviceInfo", "configuring displays WDK Windows 7 display , CCD APIs, DisplayConfigSetDeviceInfo", "configuring displays WDK Windows Server 2008 R2 display , CCD APIs, DisplayConfigSetDeviceInfo", "CCD concepts WDK Windows 7 display , DisplayConfigSetDeviceInfo", "CCD concepts WDK Windows Server 2008 R2 display , DisplayConfigSetDeviceInfo", "DisplayConfigSetDeviceInfo WDK Windows 7 display", "DisplayConfigSetDeviceInfo WDK Windows Server 2008 R2 display"]
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

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20DisplayConfigSetDeviceInfo%20Summary%20and%20Scenarios%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




