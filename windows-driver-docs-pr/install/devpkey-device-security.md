---
title: DEVPKEY_Device_Security
description: DEVPKEY_Device_Security
keywords: ["DEVPKEY_Device_Security Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_Security
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# DEVPKEY_Device_Security


The DEVPKEY_Device_Security device property represents a security descriptor structure for a device instance.

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
<td align="left"><p>DEVPKEY_Device_Security</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-security-descriptor.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_SECURITY_DESCRIPTOR&lt;/strong&gt;](devprop-type-security-descriptor.md)"><strong>DEVPROP_TYPE_SECURITY_DESCRIPTOR</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read and write access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_SECURITY</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

You can set the value of DEVPKEY_Device_Security by using an [**INF AddReg directive**](./inf-addreg-directive.md) that is included in the [**INF *DDInstall*.HW section**](./inf-ddinstall-hw-section.md) of the INF file that installs a device.

You can retrieve the value of DEVPKEY_Device_Security by calling [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) or you can set this property by calling [**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw).

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_Security property key. Instead, you can use the corresponding SPDRP_SECURITY identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP_Xxx Properties](./accessing-device-instance-spdrp-xxx-properties.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**INF AddReg Directive**](./inf-addreg-directive.md)

[**INF *DDInstall*.HW Section**](./inf-ddinstall-hw-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

[**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw)

 

