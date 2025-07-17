---
description: Requirements to create a WPD driver
title: Requirements to create a WPD driver
ms.date: 12/09/2024
ms.topic: checklist
---

# Requirements to create a WPD driver

To create a Windows Portable Devices (WPD) driver, you must have the latest [Windows Driver Kit (WDK)](../download-the-wdk.md) installed on your computer. The required header and library files are shown in the following list and are included in the WDK:

-   *PortableDeviceGuids.lib*
-   *PortableDeviceClassExtension.h*
-   *PortableDeviceTypes.h*
-   *PortableDevice.h*
-   Any other required library or header files that are required by the User-Mode Driver Framework (UMDF).

If your driver supports the new Device Services model, it will also include one or more of the following header files:

-   *AnchorSyncDeviceService.h*
-   *BridgeDeviceService.h*
-   *CalendarDeviceService.h*
-   *ContactDeviceService.h*
-   *DeviceServices.h*
-   *FullEnumSyncDeviceService.h*
-   *HintsDeviceService.h*
-   *MessageDeviceService.h*
-   *MetadataDeviceService.h*
-   *NotesDeviceService.h*
-   *RingtoneDeviceService.h*
-   *StatusDeviceService.h*
-   *SyncDeviceService.h*
-   *TaskDeviceService.h*

Of these files, *BridgeDeviceService.h* and *DeviceService.h* are required for all service applications. Other applications must include one or more of these other files to support a particular device.

## Related topics

- [Introduction to WPD Drivers](wpd-drivers-overview.md)
- [Device Installation](device-installation.md)
- [Architecture overview](architecture-overview.md)
 

