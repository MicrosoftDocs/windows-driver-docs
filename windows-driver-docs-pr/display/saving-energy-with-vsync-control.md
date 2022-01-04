---
title: Saving Energy with VSync Control
description: Saving Energy with VSync Control
keywords:
- display driver model WDK Windows Vista , saving energy
- Windows Vista display driver model WDK , saving energy
- display driver model WDK Windows Vista , VSync control
- Windows Vista display driver model WDK , VSync control
ms.date: 10/14/2019
---

# Saving Energy with VSync Control

To save power on a computer, your kernel-mode display driver can reduce the number of VSync monitor refresh interrupts that occur.

Newer processors and platforms often work with the operating system to conserve energy when the computer system is idle. However, periodic system activity, such as the firing of interrupts, causes peak power usage and can prevent the computer system from entering transient sleep states that would conserve energy.

Beginning with Windows Vista with Service Pack 1 (SP1) and Windows Server 2008, the operating system can turn off periodic VSync interrupt counting when the screen is not being refreshed from new graphics or mouse activity. By controlling the VSync interrupt interval, your driver can save significant energy.

You can take advantage of this feature by rebuilding Windows Display Driver Model (WDDM) drivers by using the Windows Server 2008 or later versions of the Windows Driver Kit (WDK).

## Windows Vista with SP1 Driver Changes for VSync Control

For drivers to take advantage of this feature, they must support the **VSyncPowerSaveAware** member in the [DXGK_VIDSCHCAPS](/windows-hardware/drivers/ddi/d3dkmddi/ns-d3dkmddi-_dxgk_vidschcaps) structure that was introduced in Windows Vista with SP1. Existing drivers that follow the WDDM must be recompiled with the **VSyncPowerSaveAware** member by using the Windows Server 2008 or later versions of the WDK.

A Windows Vista with SP1 or later system with a driver that follows the WDDM and that supports this feature will turn off the counting feature of the VSync interrupt if no GPU activity occurs for 10 continuous periods of 1/Vsync, where VSync is the monitor refresh rate. If the VSync rate is 60 hertz (Hz), the VSync interrupt occurs one time every 16 milliseconds. Thus, in the absence of a screen update, the VSync interrupt is turned off after 160 milliseconds. If GPU activity resumes, the VSync interrupt is turned on again to refresh the screen.

## Display-Only VSync Requirements for Windows 8 and later versions

In Windows 8 and later versions of the Windows operating system, it's optional for a kernel mode display-only driver (KMDOD) to support VSync functionality, as follows:

- **Display-only driver supports VSync control**

  If the KMDOD supports the VSync control feature, it must implement both [*DxgkDdiControlInterrupt*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_controlinterrupt) and [*DxgkDdiGetScanLine*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getscanline) functions and must provide valid function pointers to both of these functions in the [KMDDOD_INITIALIZATION_DATA](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_kmddod_initialization_data) structure.

  In this case the KMDOD must also implement the [*DxgkDdiInterruptRoutine*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_interrupt_routine) and [*DxgkDdiDpcRoutine*](/windows-hardware/drivers/ddi/dispmprt/nc-dispmprt-dxgkddi_dpc_routine) functions in order to report VSync interrupts to the operating system.

  In addition, the values of the **PixelRate**, **hSyncFreq**, and **vSyncFreq** members of the [DISPLAYCONFIG_VIDEO_SIGNAL_INFO](/windows/win32/api/wingdi/ns-wingdi-displayconfig_video_signal_info) structure cannot be **D3DKMDT_FREQUENCY_NOTSPECIFIED**.

- **Display-only driver does not support VSync control**

  If the KMDOD does not support the VSync control feature, it must not implement either [*DxgkDdiControlInterrupt*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_controlinterrupt) or [*DxgkDdiGetScanLine*](/windows-hardware/drivers/ddi/d3dkmddi/nc-d3dkmddi-dxgkddi_getscanline) functions and must not provide valid function pointers to either of these functions in the [KMDDOD_INITIALIZATION_DATA](/windows-hardware/drivers/ddi/dispmprt/ns-dispmprt-_kmddod_initialization_data) structure.

  In this case the Microsoft DirectX graphics kernel subsystem simulates values of VSync interrupts and scan lines based on the current mode and the time of the last simulated VSync.

  In addition, the values of the **PixelRate**, **hSyncFreq**, and **vSyncFreq** members of the [DISPLAYCONFIG_VIDEO_SIGNAL_INFO](/windows/win32/api/wingdi/ns-wingdi-displayconfig_video_signal_info) structure must be set to **D3DKMDT_FREQUENCY_NOTSPECIFIED**.

If these conditions are not met, the DirectX graphics kernel subsystem will not load the KMDOD.

## Registry Control

For Windows Vista with SP1 and later versions of the Windows operating systems, the default VSync idle time-out is 10 VSync periods. Optionally, for testing purposes, the time-out can be controlled by using registry settings.

> [!IMPORTANT]
> To avoid application compatibility problems, do not change the default registry setting in production drivers.

Key Path:  
**RTL_REGISTRY_CONTROL\GraphicsDrivers\Scheduler**

Full Path:  
**[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\GraphicsDrivers\Scheduler]**

Key Value:  
**VsyncIdleTimeout**

ValueType:  
**REG_DWORD**

Value:  
10 = default

Value:  
0 = disable VSync control (produces the same behavior same as Windows Vista)
