---
title: LocationPaths Registry Subkey
description: LocationPaths Registry Subkey
ms.assetid: d34ba7f4-97d2-4e63-a820-436c0336c584
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# LocationPaths Registry Subkey


Beginning with Windows 7, the **LocationPaths** registry subkey is used in the specification of a removable device capability override for a device identified through either the [HardwareID](hardwareid-registry-subkey.md) or [CompatibleID](compatibleid-registry-subkey.md) registry subkey. The **LocationPaths** registry subkey specifies that only the location path of the device's parent device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) will have the removable device capability override applied. For more information about removable device capability overrides, see [DeviceOverrides Registry Key](deviceoverrides-registry-key.md).

The **LocationPaths** registry subkey applies to only the parent devnode of the device specified through the name of the **HardwareID** or **CompatibleID** subkeys. As a result, only the parent devnode of the specified device is affected by the removable device capability override value. Child devnodes of the specified device are not affected by the removable device capability override, unless a [ChildLocationPaths](childlocationpaths-registry-subkey.md) registry subkey is also specified.

The following table defines the format and requirements of the **LocationPaths** registry subkey.

<table>
<colgroup>
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
<col width="20%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Registry subkey name</th>
<th align="left">Required/optional</th>
<th align="left">Format requirements</th>
<th align="left">Parent subkey</th>
<th align="left">Child subkeys</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p><strong>LocationPaths</strong></p></td>
<td align="left"><p>Optional</p></td>
<td align="left"><p>None</p></td>
<td align="left"><p><a href="hardwareid-registry-subkey.md" data-raw-source="[HardwareID](hardwareid-registry-subkey.md)">HardwareID</a> or <a href="compatibleid-registry-subkey.md" data-raw-source="[CompatibleID](compatibleid-registry-subkey.md)">CompatibleID</a></p></td>
<td align="left"><p><a href="locationpath-registry-subkey.md" data-raw-source="[LocationPath](locationpath-registry-subkey.md)">LocationPath</a> or <a href="--registry-subkey.md" data-raw-source="[*](--registry-subkey.md)">*</a></p></td>
</tr>
</tbody>
</table>

 

Either the **LocationPaths** or [ChildLocationPaths](childlocationpaths-registry-subkey.md) registry subkeys must be present to indicate the parent/child relationship to which the removable device capability override applies.

 

 





