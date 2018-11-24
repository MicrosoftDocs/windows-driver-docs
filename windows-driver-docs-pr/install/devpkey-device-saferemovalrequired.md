---
title: DEVPKEY_Device_SafeRemovalRequired
description: DEVPKEY_Device_SafeRemovalRequired
ms.assetid: a162e259-21aa-40d9-a65a-af175a59df6a
keywords: ["DEVPKEY_Device_SafeRemovalRequired Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_SafeRemovalRequired
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_SafeRemovalRequired


The DEVPKEY_Device_SafeRemovalRequired device property represents a Boolean value that indicates whether a hot-plug device instance requires safe removal from the computer.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td align="left"><p><strong>Property key</strong></p></td>
<td align="left"><p>DEVPKEY_Device_SafeRemovalRequired</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Property-data-type identifier</strong></p></td>
<td align="left"><p><a href="devprop-type-boolean.md" data-raw-source="[&lt;strong&gt;DEVPROP_TYPE_BOOLEAN&lt;/strong&gt;](devprop-type-boolean.md)"><strong>DEVPROP_TYPE_BOOLEAN</strong></a></p></td>
</tr>
<tr class="odd">
<td align="left"><p><strong>Property access</strong></p></td>
<td align="left"><p>Read-only access by installation applications and installers</p></td>
</tr>
<tr class="even">
<td align="left"><p><strong>Localized?</strong></p></td>
<td align="left"><p>No</p></td>
</tr>
</tbody>
</table>

 

Remarks
-------

If this property for a hot-plug device instance has a value of DEVPROP_TRUE, the device instance requires safe removal from the computer. In this case, Windows displays the **Safely Remove Hardware** icon in the notification area on the right side of the taskbar. When the user clicks this icon, the system starts the **Safely Remove Hardware** program. By using this program, the user can instruct the system to prepare the device instance for removal before it can be surprise-removed from the computer.

**Note**   If the device instance is a removable media device, such as an optical disk drive, the device instance must have media inserted and must have the DEVPKEY_Device_SafeRemovalRequired property value of DEVPROP_TRUE. If both are true, the device instance is displayed in the **Safely Remove Hardware** program.

 

Windows Plug and Play (PnP) determines that the hot-plug device instance requires safe removal from the system if the following are true:

-   The device instance is currently connected to the system.

-   The device instance is either started or can be ejected automatically by the system.

-   The CM_DEVCAP_SURPRISEREMOVALOK device capability bit for the device instance is not set. For more information about device capabilities, see [**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967).

-   The device instance does not have the [**DEVPKEY_Device_SafeRemovalRequiredOverride**](devpkey-device-saferemovalrequiredoverride.md) device property set to DEVPROP_FALSE.

    **Note**   PnP unconditionally determines that the hot-plug device requires safe removal if the DEVPKEY_Device_SafeRemovalRequiredOverride device property is set to DEVPROP_TRUE.

     

-   The device instance is either directly removable from its parent device instance or has a removable ancestor in its device tree.

You can call [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963) to retrieve the value of DEVPKEY_Device_SafeRemovalRequired.

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
<td align="left"><p>Available in Windows 7 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Header</p></td>
<td align="left">Devpkey.h (include Devpkey.h)</td>
</tr>
</tbody>
</table>

## See also


[**DEVPKEY_Device_SafeRemovalRequiredOverride**](devpkey-device-saferemovalrequiredoverride.md)

[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

[**SetupDiGetDeviceRegistryProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551967)

 

 






