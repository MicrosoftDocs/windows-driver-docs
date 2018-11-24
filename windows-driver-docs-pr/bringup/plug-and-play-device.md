---
title: Plug and play device
description: The presence of an ESRT configuration table will direct Windows to enumerate a separate PnP device instance for each firmware resource.
ms.assetid: 85EE32E7-1871-490D-9FF6-07E0891C78E3
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Plug and play device


The presence of an ESRT configuration table will direct Windows to enumerate a separate PnP device instance for each firmware resource. For driver matching purposes, a firmware resource device is uniquely identified by its hardware IDs, which embed the Firmware ID GUID. Referring to the ESRT example in [ESRT table definition](esrt-table-definition.md), the corresponding device instances are enumerated.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Device instance ID</th>
<th>Hardware ID</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>UEFI\RES_{SYSTEM_FIRMWARE}\0</td>
<td><p>UEFI\RES_{SYSTEM_FIRMWARE}&amp;REV_1</p>
<p>UEFI\RES_{SYSTEM_FIRMWARE}</p></td>
</tr>
<tr class="even">
<td>UEFI\RES_{DEVICE_FIRMWARE}\0</td>
<td><p>UEFI\RES_{DEVICE_FIRMWARE}&amp;REV_1</p>
<p>UEFI\RES_{DEVICE_FIRMWARE}</p></td>
</tr>
</tbody>
</table>

 

Notice that two hardware IDs are reported by each firmware resource device; the first hardware ID includes the current firmware resource version, while the second one does not. Since the firmware resource version is expected to change as a result of applying a firmware update, it is important that a driver be targeted for the second un-versioned hardware ID so that it can be applicable for installation across all firmware resource versions, no matter which version is currently present on a given system.

## Related topics
[ESRT table definition](esrt-table-definition.md)  
[Authoring an update driver package](authoring-an-update-driver-package.md)  
[Processing updates](processing-updates.md)  
[Device I/O from the UEFI environment](device-i-o-from-the-uefi-environment.md)  
[Seamless crisis prevention and recovery](seamless-crisis-prevention-and-recovery.md)  
[Firmware update status](firmware-update-status.md)  



