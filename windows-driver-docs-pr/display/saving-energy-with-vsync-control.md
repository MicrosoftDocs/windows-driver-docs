---
title: Saving Energy with VSync Control
description: Saving Energy with VSync Control
ms.assetid: d7ee7461-0d2a-4103-9225-57ca10a75a7a
keywords:
- display driver model WDK Windows Vista , saving energy
- Windows Vista display driver model WDK , saving energy
- display driver model WDK Windows Vista , VSync control
- Windows Vista display driver model WDK , VSync control
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Saving Energy with VSync Control


To save power on a computer, your kernel-mode display driver can reduce the number of VSync monitor refresh interrupts that occur.

Newer processors and platforms often work with the operating system to conserve energy when the computer system is idle. However, periodic system activity, such as the firing of interrupts, causes peak power usage and can prevent the computer system from entering transient sleep states that would conserve energy.

Beginning with Windows Vista with Service Pack 1 (SP1) and Windows Server 2008, the operating system can turn off periodic VSync interrupt counting when the screen is not being refreshed from new graphics or mouse activity. By controlling the VSync interrupt interval, your driver can save significant energy.

You can take advantage of this feature by rebuilding Windows Display Driver Model (WDDM) drivers by using the Windows Server 2008 or later versions of the Windows Driver Kit (WDK).

### <span id="driver_changes_for_vsync_control"></span><span id="DRIVER_CHANGES_FOR_VSYNC_CONTROL"></span>Windows Vista with SP1 Driver Changes for VSync Control

For drivers to take advantage of this feature, they must support the **VSyncPowerSaveAware** member in the [**DXGK\_VIDSCHCAPS**](https://msdn.microsoft.com/library/windows/hardware/ff562863) structure that was introduced in Windows Vista with SP1. Existing drivers that follow the WDDM must be recompiled with the **VSyncPowerSaveAware** member by using the Windows Server 2008 or later versions of the WDK.

A Windows Vista with SP1 or later system with a driver that follows the WDDM and that supports this feature will turn off the counting feature of the VSync interrupt if no GPU activity occurs for 10 continuous periods of 1/Vsync, where VSync is the monitor refresh rate. If the VSync rate is 60 hertz (Hz), the VSync interrupt occurs one time every 16 milliseconds. Thus, in the absence of a screen update, the VSync interrupt is turned off after 160 milliseconds. If GPU activity resumes, the VSync interrupt is turned on again to refresh the screen.

### <span id="Windows_8_Display-Only_VSync_Requirements"></span><span id="windows_8_display-only_vsync_requirements"></span><span id="WINDOWS_8_DISPLAY-ONLY_VSYNC_REQUIREMENTS"></span>Windows 8 Display-Only VSync Requirements

Starting in Windows 8, it's optional for a [kernel mode display-only driver (KMDOD)](https://msdn.microsoft.com/library/windows/hardware/jj673962) to support VSync functionality, as follows:

<span id="Display-only_driver_supports_VSync_control"></span><span id="display-only_driver_supports_vsync_control"></span><span id="DISPLAY-ONLY_DRIVER_SUPPORTS_VSYNC_CONTROL"></span>Display-only driver supports VSync control  
If the KMDOD supports the VSync control feature, it must implement both [*DxgkDdiControlInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559602) and [*DxgkDdiGetScanLine*](https://msdn.microsoft.com/library/windows/hardware/ff559668) functions and must provide valid function pointers to both of these functions in the [**KMDDOD\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/hh451571) structure.

In this case the KMDOD must also implement the [*DxgkDdiInterruptRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff559680) and [*DxgkDdiDpcRoutine*](https://msdn.microsoft.com/library/windows/hardware/ff559645) functions in order to report VSync interrupts to the operating system.

In addition, the values of the **PixelRate**, **hSyncFreq**, and **vSyncFreq** members of the [**DISPLAYCONFIG\_VIDEO\_SIGNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff554007) structure cannot be **D3DKMDT\_FREQUENCY\_NOTSPECIFIED**.

<span id="Display-only_driver_does_not_support_VSync_control"></span><span id="display-only_driver_does_not_support_vsync_control"></span><span id="DISPLAY-ONLY_DRIVER_DOES_NOT_SUPPORT_VSYNC_CONTROL"></span>Display-only driver does not support VSync control  
If the KMDOD does not support the VSync control feature, it must not implement either [*DxgkDdiControlInterrupt*](https://msdn.microsoft.com/library/windows/hardware/ff559602) or [*DxgkDdiGetScanLine*](https://msdn.microsoft.com/library/windows/hardware/ff559668) functions and must not provide valid function pointers to either of these functions in the [**KMDDOD\_INITIALIZATION\_DATA**](https://msdn.microsoft.com/library/windows/hardware/hh451571) structure.

In this case the Microsoft DirectX graphics kernel subsystem simulates values of VSync interrupts and scan lines based on the current mode and the time of the last simulated VSync.

In addition, the values of the **PixelRate**, **hSyncFreq**, and **vSyncFreq** members of the [**DISPLAYCONFIG\_VIDEO\_SIGNAL\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff554007) structure must be set to **D3DKMDT\_FREQUENCY\_NOTSPECIFIED**.

If these conditions are not met, the DirectX graphics kernel subsystem will not load the KMDOD.

### <span id="registry_control"></span><span id="REGISTRY_CONTROL"></span> Registry Control

For Windows Vista with SP1 and later versions of the Windows operating systems, the default VSync idle time-out is 10 VSync periods. Optionally, for testing purposes, the time-out can be controlled by using registry settings.

**Important**   To avoid application compatibility problems, do not change the default registry setting in production drivers.

 

<span id="Key_Path_"></span><span id="key_path_"></span><span id="KEY_PATH_"></span>Key Path:  
**RTL\_REGISTRY\_CONTROL\\GraphicsDrivers\\Scheduler**

<span id="Key_Value_"></span><span id="key_value_"></span><span id="KEY_VALUE_"></span>Key Value:  
**VsyncIdleTimeout**

<span id="ValueType_"></span><span id="valuetype_"></span><span id="VALUETYPE_"></span>ValueType:  
**REG\_DWORD**

<span id="Value_"></span><span id="value_"></span><span id="VALUE_"></span>Value:  
10 = default

<span id="Value_"></span><span id="value_"></span><span id="VALUE_"></span>Value:  
0 = disable VSync control (produces the same behavior same as Windows Vista)

 

 





