---
title: DEVPKEY_Device_BusReportedDeviceDesc
description: The DEVPKEY_Device_BusReportedDeviceDesc device property represents a string value that was reported by the bus driver for the device instance.
keywords: ["DEVPKEY_Device_BusReportedDeviceDesc Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_BusReportedDeviceDesc
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 06/23/2022
---

# DEVPKEY_Device_BusReportedDeviceDesc

The DEVPKEY_Device_BusReportedDeviceDesc device property represents a string value that was reported by the bus driver for the device instance.

| Attribute | Value |
|--|--|
| Property key | DEVPKEY_Device_BusReportedDeviceDesc |
| Property-data-type identifier | [**DEVPROP_TYPE_STRING**](./devprop-type-string.md) |
| Property access | Read-only access by installation applications and installers |
| Localized? | No |

## Remarks

The value of DEVPKEY_Device_BusReportedDeviceDesc is set by Windows Plug and Play (PnP) with the string value that is reported by the bus driver for a device instance. The bus driver returns this value when queried with [**IRP_MN_QUERY_DEVICE_TEXT**](../kernel/irp-mn-query-device-text.md).

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_BusReportedDeviceDesc.

## Requirements

**Version**: Windows 7 and later versions of Windows

**Header**: Devpkey.h (include Devpkey.h)

## See also

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)
