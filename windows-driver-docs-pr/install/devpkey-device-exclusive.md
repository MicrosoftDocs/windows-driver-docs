---
title: DEVPKEY_Device_Exclusive
description: DEVPKEY_Device_Exclusive
keywords: ["DEVPKEY_Device_Exclusive Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_Exclusive
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_Exclusive


The DEVPKEY_Device_Exclusive device property represents a Boolean value that determines whether a device instance can be opened for exclusive use.

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
<td align="left"><p>DEVPKEY_Device_Exclusive</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-boolean.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_BOOLEAN&lt;/strong&gt;](devprop-type-boolean.md)"><strong>DEVPROP_TYPE_BOOLEAN</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_EXCLUSIVE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The value of the DEVPKEY_Device_Exclusive property is DEVPROP_TRUE if the device can be opened for exclusive use. Otherwise, the value of the property is DEVPROP_FALSE.

You can set the value of DEVPKEY_Device_Exclusive by using an [**INF AddReg directive**](./inf-addreg-directive.md) that is included in the [**INF *DDInstall*.HW section**](./inf-ddinstall-hw-section.md) that installs a device.

You can retrieve or set the value of DEVPKEY_Device_Exclusive by calling [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) and [**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_Exclusive property key. Instead, you can use the corresponding SPDRP_EXCLUSIVE identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP_Xxx Properties](./accessing-device-instance-spdrp-xxx-properties.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**INF AddReg Directive**](./inf-addreg-directive.md)

[**INF *DDInstall*.HW Section**](./inf-ddinstall-hw-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

[**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw)

 

