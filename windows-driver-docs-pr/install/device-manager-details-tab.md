---
title: Device Manager Details Tab
description: Device Manager Details Tab
ms.assetid: 5f1e345f-72c6-4bd4-a0fa-304e5d0d91be
keywords:
- Device Manager WDK , Details tab
- firmware revision numbers WDK Device Manager
- revision numbers WDK Device Manager
- Details tab WDK Device Manager
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Device Manager Details Tab


## <a href="" id="ddk-device-manager-details-tab-dg"></a>


For Windows XP and later versions of Windows, Device Manager provides a **Details** tab for each device. This tab displays lots of information useful to driver developers and testers, and aids Microsoft Customer Support Services (CSS) in diagnosing customer problems. The tab's page displays [device identification strings](device-identification-strings.md), together with device and driver configuration information that can be useful when you debug drivers.

### <a href="" id="ddk-viewing-a-device-s-details-tab-dg"></a>Viewing a Device's Details Tab

Starting with Windows Server 2003 SP1 and Windows XP SP2, the details tab is enabled by default.

On Windows Server 2003, Windows XP SP1, Windows XP, and Windows 2000, the details tab is disabled by default.

To enable this tab, set the user environment variable DEVMGR\_SHOW\_DETAILS to 1. After you set this environment variable, the **Details** tab of the device will be available in Device Manager. To permanently set a user environment variable, use the **Advanced** tab of the system property sheet. For information about how to set environment variables, see "Setting environment variables" in the Help and Support Center.

### <a href="" id="ddk-providing-firmware-revision-numbers-for-the-details-tab-dg"></a>Providing Firmware Revision Numbers for the Details Tab

Device Manager's **Details** tab can display a device's firmware revision number, if available. A driver can supply a firmware revision number by responding to a WMI request. Specifically, the driver's [**DpWmiQueryDataBlock**](https://msdn.microsoft.com/library/windows/hardware/ff544096) routine should support **MSDeviceUI\_FirmwareRevision\_GUID** by returning a DEVICE\_UI\_FIRMWARE\_REVISION structure (defined in Wmidata.h). The structure must contain the firmware revision number as a NULL-terminated WCHAR string, preceded by a USHORT value that contains the string length (including the **NULL**).

 

 





