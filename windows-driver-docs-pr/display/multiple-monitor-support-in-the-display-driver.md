---
title: Multiple-Monitor Support in the Display Driver
description: Multiple-Monitor Support in the Display Driver
ms.assetid: ba15af67-94c0-4c37-8b3d-b1472e731d88
keywords:
- display drivers WDK Windows 2000 , multiple monitors
- multiple monitors WDK
- multiple-monitor systems WDK Windows 2000 display
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Multiple-Monitor Support in the Display Driver


## <span id="ddk_multiple_monitor_support_in_the_display_driver_gg"></span><span id="DDK_MULTIPLE_MONITOR_SUPPORT_IN_THE_DISPLAY_DRIVER_GG"></span>


Multiple-monitor support is provided by Windows 2000 and later; therefore, display driver writers must not implement any special code to provide this support.

Display drivers must be implemented without using global variables. All state must exist in the [*PDEV*](https://msdn.microsoft.com/library/windows/hardware/ff556325#wdkgloss-pdev) for a particular display driver. GDI will call [**DrvEnablePDEV**](https://msdn.microsoft.com/library/windows/hardware/ff556211) for every hardware device extension that is created by the video miniport driver.

To track window changes in a multiple-monitor system, a driver can request GDI to create WNDOBJ objects with desktop coordinates. The driver does this by calling [**EngCreateWnd**](https://msdn.microsoft.com/library/windows/hardware/ff564769) using the flag WO\_RGN\_DESKTOP\_COORD. See [Tracking Window Changes](tracking-window-changes.md) for more information.

In a multiple-monitor system, GDI stores the device's desktop position in the **dmPosition** member of the [**DEVMODEW**](https://msdn.microsoft.com/library/windows/hardware/ff552837) structure.

 

 





