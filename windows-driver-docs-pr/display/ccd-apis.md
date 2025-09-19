---
title: CCD APIs
description: Connecting and Configuring Display (CCD) APIs
keywords:
- connecting displays WDK Windows 7 display , CCD APIs
- connecting displays WDK Windows Server 2008 R2 display , CCD APIs
- configuring displays WDK Windows 7 display , CCD APIs
- configuring displays WDK Windows Server 2008 R2 display , CCD APIs
- CCD APIs WDK Windows 7 display
- CCD APIs WDK Windows Server 2008 R2 display
ms.date: 12/18/2024
ms.topic: reference
---

# CCD APIs

This article lists the Connecting and Configuring Display (CCD) APIs that user-mode drivers (UMDs) can use to connect and configure displays in Windows operating systems. The CCD API is available starting with Windows 7 (Windows Server 2008 R2).

For more details, see the following articles:

* [CCD Summaries and Scenarios](ccd-summaries-and-scenarios.md)

* [CCD Example Code](ccd-example-code.md)

## CCD Functions

* [**DisplayConfigGetDeviceInfo**](/windows/win32/api/winuser/nf-winuser-displayconfiggetdeviceinfo)
* [**DisplayConfigSetDeviceInfo**](/windows/win32/api/winuser/nf-winuser-displayconfigsetdeviceinfo)
* [**GetDisplayConfigBufferSizes**](/windows/win32/api/winuser/nf-winuser-getdisplayconfigbuffersizes)
* [**QueryDisplayConfig**](/windows/win32/api/winuser/nf-winuser-querydisplayconfig)
* [**SetDisplayConfig**](/windows/win32/api/winuser/nf-winuser-setdisplayconfig)

## CCD Structures

* [**DISPLAYCONFIG_2DREGION**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_2dregion)
* [**DISPLAYCONFIG_ADAPTER_NAME**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_adapter_name)
* [**DISPLAYCONFIG_DEVICE_INFO_HEADER**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_device_info_header)
* [**DISPLAYCONFIG_MODE_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_mode_info)
* [**DISPLAYCONFIG_PATH_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_path_info)
* [**DISPLAYCONFIG_PATH_SOURCE_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_path_source_info)
* [**DISPLAYCONFIG_PATH_TARGET_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_path_target_info)
* [**DISPLAYCONFIG_RATIONAL**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_rational)
* [**DISPLAYCONFIG_SET_TARGET_PERSISTENCE**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_set_target_persistence)
* [**DISPLAYCONFIG_SOURCE_DEVICE_NAME**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_source_device_name)
* [**DISPLAYCONFIG_SOURCE_MODE**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_source_mode)
* [**DISPLAYCONFIG_TARGET_DEVICE_NAME**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_target_device_name)
* [**DISPLAYCONFIG_TARGET_DEVICE_NAME_FLAGS**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_target_device_name_flags)
* [**DISPLAYCONFIG_TARGET_MODE**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_target_mode)
* [**DISPLAYCONFIG_TARGET_PREFERRED_MODE**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_target_preferred_mode)
* [**DISPLAYCONFIG_VIDEO_SIGNAL_INFO**](/windows/win32/api/wingdi/ns-wingdi-displayconfig_video_signal_info)

## CCD Enumerations

* [**DISPLAYCONFIG_DEVICE_INFO_TYPE**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_device_info_type)
* [**DISPLAYCONFIG_MODE_INFO_TYPE**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_mode_info_type)
* [**DISPLAYCONFIG_PIXELFORMAT**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_pixelformat)
* [**DISPLAYCONFIG_ROTATION**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_rotation)
* [**DISPLAYCONFIG_SCALING**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_scaling)
* [**DISPLAYCONFIG_SCANLINE_ORDERING**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_scanline_ordering)
* [**DISPLAYCONFIG_TOPOLOGY_ID**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_topology_id)
* [**DISPLAYCONFIG_VIDEO_OUTPUT_TECHNOLOGY**](/windows/win32/api/wingdi/ne-wingdi-displayconfig_video_output_technology)
