---
title: DEVPKEY_Device_BusReportedDeviceDesc
description: DEVPKEY_Device_BusReportedDeviceDesc
keywords: ["DEVPKEY_Device_BusReportedDeviceDesc Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_BusReportedDeviceDesc
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# DEVPKEY_Device_BusReportedDeviceDesc


The DEVPKEY_Device_BusReportedDeviceDesc device property represents a string value that was reported by the bus driver for the device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr>
<th>Attribute</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_BusReportedDeviceDesc</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_STRING&lt;/strong&gt;](devprop-type-string.md)"><strong>DEVPROP_TYPE_STRING</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The value of DEVPKEY_Device_BusReportedDeviceDesc is set by Windows Plug and Play (PnP) with the string value that is reported by the bus driver for a device instance. The bus driver returns this value when queried with [**IRP_MN_QUERY_DEVICE_TEXT**](../kernel/irp-mn-query-device-text.md).

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_BusReportedDeviceDesc.

## Requirements

**Version**: Windows 7 and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)

## See also


[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

 

