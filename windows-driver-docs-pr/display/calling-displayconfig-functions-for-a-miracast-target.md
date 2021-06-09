---
title: Calling DisplayConfig functions for a Miracast target
description: Calling DisplayConfig functions for a Miracast target
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Calling DisplayConfig functions for a Miracast target


To reduce compatibility issues of existing apps being exposed to new Miracast targets, the [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) and [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig) function implementations have ways for apps to find Miracast targets:

-   A value of **DISPLAYCONFIG\_OUTPUT\_TECHNOLOGY\_MIRACAST** in the [**DISPLAYCONFIG\_VIDEO\_OUTPUT\_TECHNOLOGY**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_video_output_technology) enumeration indicates that the VidPN target is a Miracast device.
-   The Flags parameter value of **QDC\_ALL\_PATHS** in a call to [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) won’t return any paths that connect to a Miracast target that does not have an active monitor attached.
-   For each path that has a connected Miracast monitor, [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig) returns the connector type that’s reported by the Miracast sink. Internal Miracast sinks report a value of **DISPLAYCONFIG\_OUTPUT\_TECHNOLOGY\_MIRACAST** in the [**DISPLAYCONFIG\_VIDEO\_OUTPUT\_TECHNOLOGY**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_video_output_technology) enumeration. For example, if a Miracast sink reports that a TV is connected to the sink with a High-Definition Multimedia Interface (HDMI) cable, then **QueryDisplayConfig** would report the target type as **DISPLAYCONFIG\_OUTPUT\_TECHNOLOGY\_HDMI**.
-   The [**DISPLAYCONFIG\_VIDEO\_SIGNAL\_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_video_signal_info) structure has a VSync frequency divider member, **vSyncFreqDivider**, that’s used similarly to [**D3DKMDT\_VIDEO\_SIGNAL\_INFO**](/windows-hardware/drivers/ddi/d3dkmdt/ns-d3dkmdt-_d3dkmdt_video_signal_info).**vSyncFreqDivider**.
-   The [**DisplayConfigGetDeviceInfo**](/windows/win32/api/winuser/nf-winuser-displayconfiggetdeviceinfo) function provides the base connector type for any target. In the case of a Miracast target, this function always returns a value of **DISPLAYCONFIG\_OUTPUT\_TECHNOLOGY\_MIRACAST** in the [**DISPLAYCONFIG\_VIDEO\_OUTPUT\_TECHNOLOGY**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_video_output_technology) enumeration.

 

