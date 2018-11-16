---
title: NDIS_STATUS_PM_WOL_PATTERN_REJECTED
description: The NDIS_STATUS_PM_WOL_PATTERN_REJECTED status indicates to overlying drivers that a power management wake on LAN (WOL) pattern was rejected.
ms.assetid: 49180c69-a3b8-4a6f-b34f-93e063c88f43
ms.date: 07/18/2017
keywords:
 - NDIS_STATUS_PM_WOL_PATTERN_REJECTED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED


The NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED status indicates to overlying drivers that a power management wake on LAN (WOL) pattern was rejected.

Remarks
-------

NDIS or miniport drivers can generate the NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED status indication when either of them removes a WOL pattern. The **StatusBuffer** member of the [**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373) structure contains a ULONG for the WOL pattern identifier of the rejected WOL pattern. NDIS provided the WOL pattern identifier in the **PatternId** member of the [**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768) structure.

NDIS generates an NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED status indication when it must remove a previously added WOL pattern from a network adapter. For example, NDIS might remove the WOL pattern to free resources for a higher priority WOL pattern. The notification event will only be sent to the binding that added the removed pattern.

For wireless network adapters that use infrastructure elements to offload the patterns and roam across the infrastructure, it is possible that a new infrastructure element might not support the same capabilities as the previous one. In this case, the miniport driver can issue a status indication to NDIS, and NDIS will issue NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED with a specific error code.

A WiFi driver might cache wake-up patterns locally. When the driver processes an OID for adding or deleting a wake-up pattern, the driver can choose to only update its local cache. The driver can defer the update of the infrastructure until it receives the [OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768) OID.

The infrastructure might not have enough resources to accommodate all of the wake-up patterns. In this case, the infrastructure can accept a partial list of the wake-up patterns. When the miniport driver completes the OID\_PM\_PARAMETERS set request, the driver must make NDIS\_STATUS\_PM\_WOL\_PATTERN\_REJECTED status indications for each of the WOL patterns that the access point (AP) rejects.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.20 and later.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_WOL\_PATTERN**](https://msdn.microsoft.com/library/windows/hardware/ff566768)

[**NDIS\_STATUS\_INDICATION**](https://msdn.microsoft.com/library/windows/hardware/ff567373)

[OID\_PM\_PARAMETERS](https://msdn.microsoft.com/library/windows/hardware/ff569768)

 

 




