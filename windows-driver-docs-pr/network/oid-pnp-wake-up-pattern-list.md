---
title: OID_PNP_WAKE_UP_PATTERN_LIST
description: OID_PNP_WAKE_UP_PATTERN_LIST
ms.date: 08/08/2017
keywords: 
 -OID_PNP_WAKE_UP_PATTERN_LIST Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_PNP\_WAKE\_UP\_PATTERN\_LIST





The OID\_PNP\_WAKE\_UP\_PATTERN\_LIST OID is used by a protocol to query a list of the wake-up patterns currently set for the miniport driver's network adapter. A protocol specifies a wake-up pattern with [OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](oid-pnp-add-wake-up-pattern.md).

OID\_PNP\_WAKE\_UP\_PATTERN\_LIST is handled by NDIS rather than the miniport driver.

NDIS returns to the protocol a description of each wake-up pattern set in the miniport driver. Each wake-up pattern, along with its mask, is described by an [**NDIS\_PM\_PACKET\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_packet_pattern) structure.

For each wake-up pattern, the **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains the following:

-   An [**NDIS\_PM\_PACKET\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_packet_pattern) structure that provides information about the pattern and its mask.

-   A mask that indicates which bytes of an incoming packet should be compared with corresponding bytes in the pattern. The mask starts with the first byte of the packet. The mask immediately follows the [**NDIS\_PM\_PACKET\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_packet_pattern) structure in the **InformationBuffer**.

-   A wake-up pattern, which begins **PatternOffset** bytes from the beginning of the **InformationBuffer**.

An intermediate driver in which the upper edge receives this OID request must always propagate the request to the underlying miniport driver by calling Ndis(Co)Request.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and 6.1. For NDIS 6.20 and later, use <a href="oid-pm-wol-pattern-list.md" data-raw-source="[OID_PM_WOL_PATTERN_LIST](oid-pm-wol-pattern-list.md)">OID_PM_WOL_PATTERN_LIST</a> instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_PACKET\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_packet_pattern)

[**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request)

[OID\_PM\_WOL\_PATTERN\_LIST](oid-pm-wol-pattern-list.md)

[OID\_PNP\_ADD\_WAKE\_UP\_PATTERN](oid-pnp-add-wake-up-pattern.md)

[OID\_PNP\_REMOVE\_WAKE\_UP\_PATTERN](oid-pnp-remove-wake-up-pattern.md)

 

