---
title: DEVPKEY_Device_InstallState
description: DEVPKEY_Device_InstallState
keywords: ["DEVPKEY_Device_InstallState Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_InstallState
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# DEVPKEY_Device_InstallState


The DEVPKEY_Device_InstallState device property represents the installation state of a device instance.

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
<td align="left"><p>DEVPKEY_Device_InstallState</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-uint32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_UINT32&lt;/strong&gt;](devprop-type-uint32.md)"><strong>DEVPROP_TYPE_UINT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_INSTALL_STATE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Windows sets the value of DEVPKEY_Device_InstallState to one of the CM_INSTALL_STATE_*Xxx* values that are defined in Cfgmgr32.h. The CM_INSTALL_STATE_*Xxx* values correspond to the [**DEVICE_INSTALL_STATE**](/windows-hardware/drivers/ddi/wdm/ne-wdm-_device_install_state) enumeration values.

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_InstallState.

Windows Server 2003 and Windows XP support this property, but do not support the DEVPKEY_Device_InstallState property key. Instead, you can use the corresponding SPDRP_INSTALL_STATE identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP_Xxx Properties](./accessing-device-instance-spdrp-xxx-properties.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

 

