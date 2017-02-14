---
title: Multiple-Monitor Support in the Display Driver
description: Multiple-Monitor Support in the Display Driver
ms.assetid: ba15af67-94c0-4c37-8b3d-b1472e731d88
keywords: ["display drivers WDK Windows 2000 , multiple monitors", "multiple monitors WDK", "multiple-monitor systems WDK Windows 2000 display"]
---

# Multiple-Monitor Support in the Display Driver


## <span id="ddk_multiple_monitor_support_in_the_display_driver_gg"></span><span id="DDK_MULTIPLE_MONITOR_SUPPORT_IN_THE_DISPLAY_DRIVER_GG"></span>


Multiple-monitor support is provided by Windows 2000 and later; therefore, display driver writers must not implement any special code to provide this support.

Display drivers must be implemented without using global variables. All state must exist in the [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) for a particular display driver. GDI will call [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) for every hardware device extension that is created by the video miniport driver.

To track window changes in a multiple-monitor system, a driver can request GDI to create WNDOBJ objects with desktop coordinates. The driver does this by calling [**EngCreateWnd**](https://msdn.microsoft.com/library/windows/hardware/ff564769) using the flag WO\_RGN\_DESKTOP\_COORD. See [Tracking Window Changes](tracking-window-changes.md) for more information.

In a multiple-monitor system, GDI stores the device's desktop position in the **dmPosition** member of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure.

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20[display\display]:%20Multiple-Monitor%20Support%20in%20the%20Display%20Driver%20%20RELEASE:%20%282/10/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")




