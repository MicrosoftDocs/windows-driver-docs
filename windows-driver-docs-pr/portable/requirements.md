---
Description: Requirements
title: Requirements
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Requirements


To create a Windows Portable Devices (WPD) driver, you must have the latest [Windows Driver Kit (WDK)](http://go.microsoft.com/fwlink/p/?linkid=178709) installed on your computer. The required header and library files are shown in the following list and are included in the WDK:

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

## <span id="related_topics"></span>Related topics


[**WPD Drivers**](wpd-drivers.md)

 

 





