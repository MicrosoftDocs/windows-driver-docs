---
title: DEVPKEY_NAME (Device Instance)
description: DEVPKEY_NAME (Device Instance)
keywords: ["DEVPKEY_NAME (Device Instance) Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_NAME (Device Instance)
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# DEVPKEY_NAME (Device Instance)


The DEVPKEY_NAME device property represents the name of a device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_NAME</p></td>
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
<td align="left"><p>Yes</p></td>
</tr>
</tbody>
</table>

 

## Remarks

The value of DEVPKEY_NAME device should be used to identify a device instance to an end-user in a user interface item.

The retrieved property value is the same as the value of the [**DEVPKEY_Device_FriendlyName**](devpkey-device-friendlyname.md) device property, if **DEVPKEY_Device_FriendlyName** is set. Otherwise, the value of DEVPKEY_NAME is same as the value of the [**DEVPKEY_Device_DeviceDesc**](devpkey-device-devicedesc.md) device property.

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_NAME property.

Windows Server 2003, Windows XP, and Windows 2000 do not directly support a corresponding name property. However, these earlier versions of Windows do support properties that correspond to DEVPKEY_Device_FriendlyName and DEVPKEY_Device_DeviceDesc.

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)

## See also


[**DEVPKEY_Device_DeviceDesc**](devpkey-device-devicedesc.md)

[**DEVPKEY_Device_FriendlyName**](devpkey-device-friendlyname.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

 

