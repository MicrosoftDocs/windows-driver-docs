---
title: DEVPKEY_Device_DevType
description: DEVPKEY_Device_DevType
keywords: ["DEVPKEY_Device_DevType Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_DevType
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
ms.topic: reference
---

# DEVPKEY_Device_DevType


The DEVPKEY_Device_DevType device property represents the device type of a device instance.

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
<td align="left"><p>DEVPKEY_Device_DevType</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-int32.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_INT32&lt;/strong&gt;](devprop-type-int32.md)"><strong>DEVPROP_TYPE_INT32</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Corresponding SPDRP_</strong><em>Xxx</em> <strong>identifier</strong></p></td>
<td align="left"><p>SPDRP_DEVTYPE</p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

Windows sets the value of DEVPKEY_Device_DevType to the value of the DeviceType member of the [**DEVICE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object) structure for a device instance. The value of DEVPKEY_Device_DevType is one of the system-defined device type values that are listed in [Specifying Device Types](../kernel/specifying-device-types.md).

You can set the value of DEVPKEY_Device_DevType by using an [**INF AddReg directive**](./inf-addreg-directive.md) that is included in the [**INF *DDInstall*.HW section**](./inf-ddinstall-hw-section.md) in the INF file that installs a device.

You can call [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw) to retrieve the value of DEVPKEY_Device_DevType.

Windows Server 2003, Windows XP, and Windows 2000 support this property, but do not support the DEVPKEY_Device_DevType property key. Instead, you can use the corresponding SPDRP_DEVTYPE identifier to access the value of the property on these earlier versions of Windows. For information about how to access this property value on these earlier versions of Windows, see [Accessing Device Instance SPDRP_Xxx Properties](./accessing-device-instance-spdrp-xxx-properties.md).

## Requirements

**Version**: Windows Vista and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)


## See also


[**DEVICE_OBJECT**](/windows-hardware/drivers/ddi/wdm/ns-wdm-_device_object)

[**INF *DDInstall*.HW section**](./inf-ddinstall-hw-section.md)

[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

 

