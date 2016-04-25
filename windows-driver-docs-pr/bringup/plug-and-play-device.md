---
title: Plug and play device
description: The presence of an ESRT configuration table will direct Windows to enumerate a separate PnP device instance for each firmware resource.
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 85EE32E7-1871-490D-9FF6-07E0891C78E3
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

--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bp_OEMBringUp\p_oembringup%5D:%20Plug%20and%20play%20device%20%20RELEASE:%20%284/22/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


