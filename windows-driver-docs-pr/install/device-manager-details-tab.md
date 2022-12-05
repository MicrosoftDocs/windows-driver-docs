---
title: Device Manager Details tab
description: Device Manager Details tab displays information useful to driver developers and testers, and aids Microsoft Customer Support Services (CSS) in diagnosing customer problems.
keywords:
- Device Manager WDK, Details tab
- firmware revision numbers WDK Device Manager
- revision numbers WDK Device Manager
- Details tab WDK Device Manager
ms.date: 12/05/2022
---

# Device Manager Details tab

Device Manager provides a **Details** tab for each device in the Properties dialog for that device. This tab displays information useful to driver developers and testers, and aids Microsoft Customer Support Services (CSS) in diagnosing customer problems. The tab's page displays [device identification strings](device-identification-strings.md), together with device and driver configuration information that can be useful when you debug drivers.

## Providing firmware revision numbers for the Details tab

Device Manager's **Details** tab can display a device's firmware revision number, if available. A driver can supply a firmware revision number by responding to a WMI request. Specifically, the driver's [**DpWmiQueryDataBlock**](/windows-hardware/drivers/ddi/wmilib/nc-wmilib-wmi_query_datablock_callback) routine should support **MSDeviceUI_FirmwareRevision_GUID** by returning a DEVICE_UI_FIRMWARE_REVISION structure (defined in Wmidata.h). The structure must contain the firmware revision number as a NULL-terminated WCHAR string, preceded by a USHORT value that contains the string length (including the **NULL**).
