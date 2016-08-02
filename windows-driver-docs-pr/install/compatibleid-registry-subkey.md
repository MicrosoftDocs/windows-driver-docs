---
title: CompatibleID Registry Subkey
description: CompatibleID Registry Subkey
ms.assetid: 0111b013-d559-47bb-9cc8-d3930661a0a3
---

# CompatibleID Registry Subkey


Beginning with Windows 7, the **CompatibleID** registry subkey specifies a removable device capability override for a device installed in the computer. For more information about removable device capability overrides, see [DeviceOverrides Registry Key](deviceoverrides-registry-key.md).

The name of the **CompatibleID** registry subkey specifies the [compatible ID](compatible-ids.md) of the device, and is formatted based on the requirements described below.

The following table defines the format and requirements of the **CompatibleID** registry subkey.

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
<th align="left">Parent key</th>
<th align="left">Child subkeys</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Valid [compatible ID](compatible-ids.md) value</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Must include the compatible ID's bus prefix.</p>
<p>All slash () path separator characters within the compatible ID must be replaced with number (#) characters.</p></td>
<td align="left">[DeviceOverrides](deviceoverrides-registry-key.md)</td>
<td align="left"><p>[LocationPaths](locationpaths-registry-subkey.md) and/or [ChildLocationPaths](childlocationpaths-registry-subkey.md)</p></td>
</tr>
</tbody>
</table>

 

The compatible ID value must follow the format requirements described in this table. Each **CompatibleID** subkey must contain either the **LocationPaths** or **ChildLocationPaths** subkeys. Both subkeys could be specified within the **CompatbleID** subkey if necessary.

Because the slash character is not a valid character in a registry subkey name, you must replace it with the number character when specifying a bus prefix for the **CompatibleID** registry subkey name. For example, if a removable device capability override is specified for the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) with a [hardware ID](hardware-ids.md) of PCI\\VEN\_ABCD&DEV\_1234&SUBSYS\_000, you must create a **CompatibleID** registry subkey with a name of PCI\#VEN\_ABCD&DEV\_1234&SUBSYS\_000.

 

 





