---
title: HardwareID Registry Subkey
description: HardwareID Registry Subkey
ms.assetid: c6c52aa1-68ee-4d64-be97-509203db6970
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# HardwareID Registry Subkey


Beginning with Windows 7, the **HardwareID** registry subkey specifies a removable device capability override for a device installed in the computer. For more information about removable device capability overrides, see [DeviceOverrides Registry Key](deviceoverrides-registry-key.md).

The name of the **HardwareID** registry subkey specifies the [hardware ID](hardware-ids.md) of the device, and is formatted based on the requirements described below.

The following table defines the format and requirements of the **HardwareID** registry subkey.

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
<td align="left"><p>Valid <a href="hardware-ids.md" data-raw-source="[hardware ID](hardware-ids.md)">hardware ID</a> value</p></td>
<td align="left"><p>Required</p></td>
<td align="left"><p>Must include the hardware ID&#39;s bus prefix.</p>
<p>All slash () path separator characters within the hardware ID must be replaced with number (#) characters.</p></td>
<td align="left"><a href="deviceoverrides-registry-key.md" data-raw-source="[DeviceOverrides](deviceoverrides-registry-key.md)">DeviceOverrides</a></td>
<td align="left"></td>
</tr>
</tbody>
</table>

 

The hardware ID value must follow the format requirements described in this table. Each **HardwareID** subkey must contain either the **LocationPaths** or **ChildLocationPaths** subkeys. Both subkeys could be specified within the **HardwareID** subkey if necessary.

Because the slash character is not a valid character in a registry subkey name, you must replace it with the number character when specifying a bus prefix for the **HardwareID** registry subkey name. For example, if a removable device capability override is specified for the device node ([*devnode*](https://msdn.microsoft.com/library/windows/hardware/ff556277#wdkgloss-devnode)) with a [hardware ID](hardware-ids.md) of USB\\VID_1234&PID_ABCD&REV_0001, you must create a **HardwareID** registry subkey with a name of USB\#VID_1234&PID_ABCD&REV_0001.

 

 





