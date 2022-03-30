---
title: DEVPKEY_DeviceInterface_Restricted
description: DEVPKEY_DeviceInterface_Restricted
keywords: ["DEVPKEY_DeviceInterface_Restricted Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceInterface_Restricted
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# DEVPKEY_DeviceInterface_Restricted


The DEVPKEY_DeviceInterface_Restricted device interface property indicates that the device interface on which it is present and set to TRUE, should be treated with privileged access by system components that honor the setting.

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
<td align="left"><p>DEVPKEY_DeviceInterface_Restricted</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-boolean.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_BOOLEAN&lt;/strong&gt;](devprop-type-boolean.md)"><strong>DEVPROP_TYPE_BOOLEAN</strong></a></p></td>
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

You can call [**CM_Get_Device_Interface_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_device_interface_propertyw) or [**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw) to retrieve the value of DEVPKEY_DeviceInterface_Restricted.

## Requirements

**Version**: Windows 8 and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)

## See also


[**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw)

 

