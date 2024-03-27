---
title: Initialize the Battery Class Device
ms.date: 10/04/2023
description: Discover how to initialize the battery class device and register the miniclass driver with the class driver to enable their support routines and make the battery device visible to the composite battery and power meter.
---

# Initialize the battery class device

In the [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine, you must initialize the battery class device and register the miniclass driver with the class driver. To do this, call the [**BatteryClassInitializeDevice**](/windows/win32/api/batclass/nf-batclass-batteryclassinitializedevice) routine. This action registers the miniclass driver with the class driver, allowing them to use each other's support routines. Additionally, it registers the battery device with the system, making it visible to the composite battery and the power meter.

To call **BatteryClassInitializeDevice**, provide a pointer to a [**BATTERY_MINIPORT_INFO**](/windows/win32/api/batclass/ns-batclass-battery_miniport_info) structure containing the following information:

- **MajorVersion** and **MinorVersion**: The major and minor version numbers of the class driver supported by this miniclass driver. These version numbers are defined in Batclass.h as BATTERY_CLASS_MAJOR_VERSION and BATTERY_CLASS_MINOR_VERSION, respectively.
- **QueryTag**: The entry point of the miniclass driver's [*BatteryMiniQueryTag*](/windows/win32/api/batclass/nc-batclass-bclass_query_tag_callback) routine.
- **QueryInformation**: The entry point of the miniclass driver's [*BatteryMiniQueryInformation*](/windows/win32/api/batclass/nc-batclass-bclass_query_information_callback) routine.
- **SetInformation**: The entry point of the miniclass driver's [*BatteryMiniSetInformation*](/windows/win32/api/batclass/nc-batclass-bclass_set_information_callback) routine.
- **SetStatusNotify**: The entry point of the miniclass driver's [*BatteryMiniSetStatusNotify*](/windows/win32/api/batclass/nc-batclass-bclass_set_status_notify_callback) routine.
- **DisableStatusNotify**: The entry point of the miniclass driver's [*BatteryMiniDisableStatusNotify*](/windows/win32/api/batclass/nc-batclass-bclass_disable_status_notify_callback) routine.
- **Context**: A pointer to the miniclass driver's context information, typically a pointer to the FDO device extension. This pointer is passed back to the miniclass driver each time the class driver calls a [BatteryMini*Xxx*](/windows-hardware/drivers/ddi/_battery/) routine.
- **Pdo**: A pointer to the PDO for the device.
- **DeviceName**: A NULL parameter, as PnP devices should not have names.

After setting up this structure, call **BatteryClassInitializeDevice** and pass a pointer to the BATTERY_MINIPORT_INFO structure. In return, you'll receive a handle for subsequent calls to battery class driver support routines. Store the returned class handle in nonpaged memory.

Following the **BatteryClassInitializeDevice** call, the [*AddDevice*](/windows-hardware/drivers/ddi/wdm/nc-wdm-driver_add_device) routine may also need to initialize other device-specific data.
