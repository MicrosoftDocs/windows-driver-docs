---
title: DEVPKEY_DeviceInterface_ClassGuid
description: DEVPKEY_DeviceInterface_ClassGuid
ms.assetid: f7346189-9986-4b26-b059-b1a58c8313d1
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

 

Remarks
-------

The format of {*device-interface-class*} key value is "{*nnnnnnnn*-*nnnn*-*nnnn*-*nnnn*-*nnnnnnnnnnnn*}", where each *n* is a hexadecimal digit.

You can call [**SetupDiGetDeviceInterfaceProperty**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw) to retrieve the value of DEVPKEY_DeviceInterface_ClassGuid.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_DeviceInterface_ClassGuid property key. For information about how to retrieve the class GUID of a device interface on these earlier versions of Windows, see the information about how to use [**SetupDiEnumDeviceInterfaces**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces) that is provided in [Accessing Device Interface Properties](https://docs.microsoft.com/windows-hardware/drivers/install/accessing-device-interface-properties).

For information about how to install and accessing device interfaces, see [Device Interface Classes](https://docs.microsoft.com/windows-hardware/drivers/install/device-interface-classes) and the [**INF AddInterface Directive**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addinterface-directive).

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p>Version</p></td>
<td align="left"><p>Available in Windows Vista and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**INF AddInterface Directive**](https://docs.microsoft.com/windows-hardware/drivers/install/inf-addinterface-directive)

[**SetupDiEnumDeviceInterfaces**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdienumdeviceinterfaces)

[**SetupDiGetDeviceInterfaceProperty**](https://docs.microsoft.com/windows/desktop/api/setupapi/nf-setupapi-setupdigetdeviceinterfacepropertyw)

 

 






