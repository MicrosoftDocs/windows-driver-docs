---
title: OID_GEN_SUPPORTED_LIST
ms.topic: reference
description: As a query, the OID_GEN_SUPPORTED_LIST OID specifies an array of OIDs for objects that the miniport driver or a NIC supports.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_SUPPORTED_LIST Network Drivers Starting with Windows Vista
---

# OID\_GEN\_SUPPORTED\_LIST


As a query, the OID\_GEN\_SUPPORTED\_LIST OID specifies an array of OIDs for objects that the miniport driver or a NIC supports. Objects include general, media-specific, and implementation-specific objects.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory. See [OID\_GEN\_SUPPORTED\_LIST (NDIS 5.1)](/previous-versions/windows/hardware/network/ff560258(v=vs.85)).

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory. See [OID\_GEN\_SUPPORTED\_LIST (NDIS 5.1)](/previous-versions/windows/hardware/network/ff560258(v=vs.85)).

## Remarks

NDIS 6.0 and later miniport drivers do not receive this OID request. NDIS handles this OID with a cached value that miniport drivers supply during initialization.

To specify the list of supported OIDs during initialization, a miniport driver sets the **SupportedOidList** member of the [**NDIS_MINIPORT_ADAPTER_GENERAL_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure and passes the structure to the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function.

NDIS forwards a subset of the provided list to protocol drivers that make this query. That is, NDIS filters any supported statistics OIDs out of the list because protocol drivers never make statistics queries.

If a miniport driver lists an OID in its supported OIDs list, it must fully support the OID. That is, the miniport driver must return valid data when it responds to a query or set request for the OIDs that it includes in the list. For example, the [OID\_GEN\_STATISTICS](oid-gen-statistics.md) OID is a required OID for NDIS 6.0 and later miniport drivers. If a miniport driver does not support the statistics in hardware or software and returns incorrect statistics information, the driver cannot specify OID\_GEN\_STATISTICS in its supported OIDs list.

Duplicates might appear in the supported OIDs list. Drivers are not required to guarantee that there is only one entry for each OID in the list.

## Requirements

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[OID\_GEN\_STATISTICS](oid-gen-statistics.md)

 

