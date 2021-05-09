---
title: DEVPKEY_DeviceInterface_ClassGuid
description: DEVPKEY_DeviceInterface_ClassGuid
keywords: ["DEVPKEY_DeviceInterface_ClassGuid Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_DeviceInterface_ClassGuid
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_DeviceInterface_ClassGuid


The DEVPKEY_DeviceInterface_ClassGuid device property represents the GUID that identifies a device interface class.

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
<td align="left"><p>DEVPKEY_DeviceInterface_ClassGuid</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-guid.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_GUID&lt;/strong&gt;](devprop-type-guid.md)"><strong>DEVPROP_TYPE_GUID</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The format of {*device-interface-class*} key value is "{*nnnnnnnn*-*nnnn*-*nnnn*-*nnnn*-*nnnnnnnnnnnn*}", where each *n* is a hexadecimal digit.

You can call [**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw) to retrieve the value of DEVPKEY_DeviceInterface_ClassGuid.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceInterface_ClassGuid property key. For information about how to retrieve the class GUID of a device interface on these earlier versions of Windows, see the information about how to use [**SetupDiEnumDeviceInterfaces**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces) that is provided in [Accessing Device Interface Properties](./accessing-device-interface-properties.md).

For information about how to install and accessing device interfaces, see [Device Interface Classes](./overview-of-device-interface-classes.md) and the [**INF AddInterface Directive**](./inf-addinterface-directive.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**INF AddInterface Directive**](./inf-addinterface-directive.md)

[**SetupDiEnumDeviceInterfaces**](/windows/win32/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces)

[**SetupDiGetDeviceInterfaceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw)

 

