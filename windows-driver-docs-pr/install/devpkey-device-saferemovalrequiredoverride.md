---
title: DEVPKEY_Device_SafeRemovalRequiredOverride
description: DEVPKEY_Device_SafeRemovalRequiredOverride
ms.assetid: 8289effe-3849-41bf-b870-69e3d8cb8850
keywords: ["DEVPKEY_Device_SafeRemovalRequiredOverride Device and Driver Installation"]
topic_type:
- apiref
api_name:
- DEVPKEY_Device_SafeRemovalRequiredOverride
api_location:
- Devpkey.h
api_type:
- HeaderDef
ms.localizationpriority: medium
ms.date: 10/17/2018
---

# DEVPKEY_Device_SafeRemovalRequiredOverride


The DEVPKEY_Device_SafeRemovalRequiredOverride device property represents the safe removal override for the device instance.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
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

 

Remarks
-------

This device property can be used to override the result of the heuristic that Windows Plug and Play (PnP) uses to calculate the value of the [**DEVPKEY_Device_SafeRemovalRequired**](devpkey-device-saferemovalrequired.md) device property. This override is performed as follows:

-   If the DEVPKEY_Device_SafeRemovalRequiredOverride device property is set to DEVPROP_TRUE and the device instance is removable or has a removable ancestor, PnP sets the DEVPKEY_Device_SafeRemovalRequired device property to DEVPROP_TRUE and does not use the heuristic.

    **Note**  A device instance is considered removable if its removable device capability is set. For more information, see [Overview of the Removable Device Capability](https://msdn.microsoft.com/library/windows/hardware/ff549564).

     

-   If the DEVPKEY_Device_SafeRemovalRequiredOverride device property is set to DEVPROP_TRUE and the device instance (or an ancestor) is not removable, PnP sets the DEVPKEY_Device_SafeRemovalRequired to DEVPROP_FALSE and does not use the heuristic.

-   If the DEVPKEY_Device_SafeRemovalRequiredOverride device property is either not set or set to DEVPROP_FALSE, PnP sets the DEVPKEY_Device_SafeRemovalRequired device property to a value that is determined by using the heuristic.

You can retrieve the value of DEVPKEY_Device_SafeRemovalRequiredOverride by calling [**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963). You can also set this value by calling [**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163).

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


[**SetupDiGetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff551963)

[**SetupDiSetDeviceProperty**](https://msdn.microsoft.com/library/windows/hardware/ff552163)

 

 






