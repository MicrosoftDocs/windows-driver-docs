---
title: DEVPKEY_Device_FirstInstallDate
description: DEVPKEY_Device_FirstInstallDate
keywords: ["DEVPKEY_Device_FirstInstallDate Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_FirstInstallDate
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# DEVPKEY_Device_FirstInstallDate


The DEVPKEY_Device_FirstInstallDate device property specifies the time stamp when the device instance was first installed in the system.

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
<td align="left"><p>DEVPKEY_Device_FirstInstallDate</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-filetime.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_FILETIME&lt;/strong&gt;](devprop-type-filetime.md)"><strong>DEVPROP_TYPE_FILETIME</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers.</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Windows sets the value of DEVPKEY_Device_FirstInstallDate with the time stamp that specifies when the device instance was first installed in the system.

**Note**   Unlike the [**DEVPKEY_Device_InstallDate**](devpkey-device-installdate.md) property, the value of the DEVPKEY_Device_FirstInstallDate property does not change with each successive update of the device driver. For example, a driver that was updated through Windows Update does not change the value of this property,

 

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_FirstInstallDate property.

## Requirements

**Version**: Windows 7 and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)

## See also


[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

 

