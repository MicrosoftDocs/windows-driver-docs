---
title: OID_PNP_ADD_WAKE_UP_PATTERN
ms.topic: reference
description: OID_PNP_ADD_WAKE_UP_PATTERN
ms.date: 08/08/2017
keywords: 
 -OID_PNP_ADD_WAKE_UP_PATTERN Network Drivers Starting with Windows Vista
---

# OID\_PNP\_ADD\_WAKE\_UP\_PATTERN





The OID\_PNP\_ADD\_WAKE\_UP\_PATTERN OID is sent by a protocol driver to a miniport driver to specify a wake-up pattern. The wake-up pattern, along with its mask, is described by an [**NDIS\_PM\_PACKET\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_packet_pattern) structure.

A protocol that enables pattern-match wake-up for a miniport driver (see [OID\_PNP\_ENABLE\_WAKE\_UP](oid-pnp-enable-wake-up.md)) uses OID\_PNP\_ADD\_WAKE\_UP\_PATTERN to specify a wake-up pattern. The wake-up pattern can be stored in host memory or on the network adapter, depending on the capabilities of the network adapter.

The **InformationBuffer** member of the [**NDIS\_OID\_REQUEST**](/windows-hardware/drivers/ddi/oidrequest/ns-oidrequest-ndis_oid_request) structure contains the following:

-   An [**NDIS\_PM\_PACKET\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_packet_pattern) structure that provides information about the pattern and its mask.

-   A mask that indicates which bytes of an incoming packet should be compared with corresponding bytes in the pattern. The mask starts with the first byte of the packet. The mask immediately follows the [**NDIS\_PM\_PACKET\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_packet_pattern) structure in the *InformationBuffer*. For more information about how this mask works, see the [Network Device Class Power Management Reference specification](https://download.microsoft.com/download/1/6/1/161ba512-40e2-4cc9-843a-923143f3456c/netpmspc.rtf).

-   A wake-up pattern, which begins **PatternOffset** bytes from the beginning of the *InformationBuffer*. For more information about wake-up patterns, see the [Network Device Class Power Management Reference specification](https://download.microsoft.com/download/1/6/1/161ba512-40e2-4cc9-843a-923143f3456c/netpmspc.rtf).

The number of wake-up patterns that the miniport driver can accept from a protocol might depend on the availability of resources, such as the host memory that the miniport driver has allocated for such patterns, or the available storage in the network adapter. If a miniport driver cannot add a wake-up pattern due to insufficient resources, the miniport driver returns **NDIS\_STATUS\_RESOURCES** in response to OID\_PNP\_ADD\_WAKE\_UP\_PATTERN.

If a protocol driver tries to add a duplicate pattern, the miniport driver should return **NDIS\_STATUS\_INVALID\_DATA** in response to OID\_PNP\_ADD\_WAKE\_UP\_PATTERN.

An intermediate driver in which the upper edge receives this OID request must always propagate the request to the underlying miniport driver by calling [**NdisRequest**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndisrequest) or [**NdisCoRequest**](/previous-versions/windows/hardware/network/ff551877(v=vs.85)).

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Supported in NDIS 6.0 and NDIS 6.1. For NDIS 6.20 and later, use <a href="oid-pm-add-wol-pattern.md" data-raw-source="[OID_PM_ADD_WOL_PATTERN](oid-pm-add-wol-pattern.md)">OID_PM_ADD_WOL_PATTERN</a> instead.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_PM\_PACKET\_PATTERN**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_pm_packet_pattern)

[OID\_PM\_ADD\_WOL\_PATTERN](oid-pm-add-wol-pattern.md)

 

