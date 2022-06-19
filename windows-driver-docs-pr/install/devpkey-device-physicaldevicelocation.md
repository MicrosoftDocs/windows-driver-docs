---
title: DEVPKEY_Device_PhysicalDeviceLocation
description: DEVPKEY_Device_PhysicalDeviceLocation
keywords: ["DEVPKEY_Device_PhysicalDeviceLocation Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_PhysicalDeviceLocation
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# DEVPKEY_Device_PhysicalDeviceLocation


The DEVPKEY_Device_PhysicalDeviceLocation device property encapsulates the physical device location information provided by a device's firmware to Windows.

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
<td align="left"><p>DEVPKEY_Device_PhysicalDeviceLocation</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-string.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_BINARY&lt;/strong&gt;](devprop-type-string.md)"><strong>DEVPROP_TYPE_BINARY</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_<em>Xxx</em></strong> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_PHYSICAL_DEVICE_LOCATION</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Windows sets the value of DEVPKEY_Device_PhysicalDeviceLocation with the physical device location information. The format of the information is defined in the ACPI 4.0a Specification, section 6.1.6.

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_PhysicalDeviceLocation.

## Requirements

**Version**: Windows 8 and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)

## See also


[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

 

