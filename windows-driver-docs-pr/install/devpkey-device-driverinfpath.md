---
title: DEVPKEY_Device_DriverInfPath
description: DEVPKEY_Device_DriverInfPath
keywords: ["DEVPKEY_Device_DriverInfPath Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_DriverInfPath
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# DEVPKEY_Device_DriverInfPath


The PKEY_Device_DriverInfPath device property represents the name of the INF file that installed a device instance.

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
<td align="left"><p>DEVPKEY_Device_DriverInfPath</p></td>
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
<td align="left"><p><strong>Corresponding registry value identifier and registry value name</strong></p></td>
<td align="left"><p>REGSTR_VAL_INFPATH</p>
<p><strong>InfPath</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Windows sets the value of DEVPKEY_Device_DriverInfPath. A copy of the INF file that installed a device is located in the system INF file directory. The name of the INF file copy is Oem*Nnn*.inf, where *Nnn* is a decimal number from 0 through 9999.

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_DriverInfPath.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_DriverInfPath property key. On these earlier versions of Windows, you can access the value of this property by accessing the corresponding **InfPath** registry value under the software key for the device instance. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Driver Properties](./accessing-device-driver-properties.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

 

