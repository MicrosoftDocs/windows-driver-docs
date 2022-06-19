---
title: DEVPKEY_Device_SafeRemovalRequiredOverride
description: DEVPKEY_Device_SafeRemovalRequiredOverride
keywords: ["DEVPKEY_Device_SafeRemovalRequiredOverride Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_SafeRemovalRequiredOverride
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.date: 10/17/2018
---

# DEVPKEY_Device_SafeRemovalRequiredOverride


The DEVPKEY_Device_SafeRemovalRequiredOverride device property represents the safe removal override for the device instance.

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
<td align="left"><p>DEVPKEY_Device_SafeRemovalRequiredOverride</p></td>
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
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

## Remarks

This device property can be used to override the result of the heuristic that Windows Plug and Play (PnP) uses to calculate the value of the [**DEVPKEY_Device_SafeRemovalRequired**](devpkey-device-saferemovalrequired.md) device property. This override is performed as follows:

-   If the DEVPKEY_Device_SafeRemovalRequiredOverride device property is set to DEVPROP_TRUE and the device instance is removable or has a removable ancestor, PnP sets the DEVPKEY_Device_SafeRemovalRequired device property to DEVPROP_TRUE and does not use the heuristic.

    **Note**  A device instance is considered removable if its removable device capability is set. For more information, see [Overview of the Removable Device Capability](./overview-of-the-removable-device-capability.md).

     

-   If the DEVPKEY_Device_SafeRemovalRequiredOverride device property is set to DEVPROP_TRUE and the device instance (or an ancestor) is not removable, PnP sets the DEVPKEY_Device_SafeRemovalRequired to DEVPROP_FALSE and does not use the heuristic.

-   If the DEVPKEY_Device_SafeRemovalRequiredOverride device property is either not set or set to DEVPROP_FALSE, PnP sets the DEVPKEY_Device_SafeRemovalRequired device property to a value that is determined by using the heuristic.

You can retrieve the value of DEVPKEY_Device_SafeRemovalRequiredOverride by calling [**CM_Get_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_get_devnode_propertyw) or [**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw). You can also set this value by calling [**CM_Set_DevNode_Property**](/windows/win32/api/cfgmgr32/nf-cfgmgr32-cm_set_devnode_propertyw) or [**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw).

## Requirements

**Version**: Windows 7 and later versions of Windows
**Header**: Devpkey.h (include Devpkey.h)

## See also


[**SetupDiGetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdigetdevicepropertyw)

[**SetupDiSetDeviceProperty**](/windows/win32/api/setupapi/nf-setupapi-setupdisetdevicepropertyw)

 

