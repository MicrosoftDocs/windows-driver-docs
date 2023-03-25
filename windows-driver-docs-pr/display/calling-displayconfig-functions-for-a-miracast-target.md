---
title: Calling DisplayConfig functions for a Miracast target
description: Calling DisplayConfig functions for a Miracast target
ms.date: 03/24/2023
---

# Calling DisplayConfig functions for a Windows 8.1 Miracast target

> [!NOTE]
> Starting in Windows 10 (WDDM 2.0), the operating system ships with a built-in Miracast stack that can work on any GPU. For information about the Microsoft Miracast stack and the requirements of drivers and hardware to support Miracast displays starting in Windows 10, see the following documentation:
>
> * [Building best-in-class Wireless projection solutions with Windows 10](/windows-hardware/design/device-experiences/wireless-projection)
>
> * The relevant [WHLK documentation](/windows-hardware/test/hlk/windows-hardware-lab-kit) at **Device.Graphics.WDDM13.DisplayRender.WirelessDisplay**
>
> Driver developers should no longer implement a custom Miracast stack. Microsoft might remove support for custom Miracast stacks in a future version of Windows.

To reduce compatibility issues of existing apps being exposed to new Miracast targets, the [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) and [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) function implementations have ways for apps to find Miracast targets:

* A value of **DISPLAYCONFIG_OUTPUT_TECHNOLOGY_MIRACAST** in the [**DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_video_output_technology) enumeration indicates that the VidPN target is a Miracast device.
* The **Flags** parameter value of **QDC_ALL_PATHS** in a call to [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) won’t return any paths that connect to a Miracast target that doesn't have an active monitor attached.
* For each path that has a connected Miracast monitor, [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) returns the connector type that the Miracast sink reported. Internal Miracast sinks report a value of **DISPLAYCONFIG_OUTPUT_TECHNOLOGY_MIRACAST** in the [**DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_video_output_technology) enumeration. For example, if a Miracast sink reports that a TV is connected to the sink with a High-Definition Multimedia Interface (HDMI) cable, then **QueryDisplayConfig** would report the target type as **DISPLAYCONFIG_OUTPUT_TECHNOLOGY_HDMI**.
* The [**DISPLAYCONFIG_VIDEO_SIGNAL_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_video_signal_info) structure has a VSync frequency divider member, **vSyncFreqDivider**, that’s used similarly to [**D3DKMDT_VIDEO_SIGNAL_INFO**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_signal_info).**vSyncFreqDivider**.
* The [**DisplayConfigGetDeviceInfo**](/windows/win32/api/winuser/nf-winuser-displayconfiggetdeviceinfo) function provides the base connector type for any target. For a Miracast target, this function always returns a value of **DISPLAYCONFIG_OUTPUT_TECHNOLOGY_MIRACAST** in the [**DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_video_output_technology) enumeration.
