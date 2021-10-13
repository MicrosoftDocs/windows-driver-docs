---
title: OID_GEN_MEDIA_DUPLEX_STATE
description: As a query, the OID_GEN_MEDIA_DUPLEX_STATE OID returns the duplex state of an interface. Version Information Windows Vista and laterSupported. NDIS 6.0 and later miniport driversNot requested. For NDIS interface providers only.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MEDIA_DUPLEX_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_MEDIA\_DUPLEX\_STATE


As a query, the OID\_GEN\_MEDIA\_DUPLEX\_STATE OID returns the duplex state of an interface.

**Version Information**

<a href="" id="windows-vista-and-later"></a>Windows Vista and later  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. For NDIS interface providers only.

## Remarks

NDIS uses this OID to query the duplex state of an [NDIS network interface](./ndis-network-interfaces2.md) provider. Only NDIS interface providers, and therefore not miniport drivers or filter drivers, must support this OID as an OID request.

If the query succeeds, the interface provider returns NDIS\_STATUS\_SUCCESS, and the result of the query can be one of the values in the [**NET\_IF\_MEDIA\_DUPLEX\_STATE**](/windows/win32/api/ifdef/ne-ifdef-net_if_media_duplex_state) enumeration.

Miniport drivers supply the media duplex state during initialization and provide updates with status indications.

To specify the duplex state in a miniport driver, set the **MediaDuplexState** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure that the miniport driver passes to the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function.

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


[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes)

[**NET\_IF\_MEDIA\_DUPLEX\_STATE**](/windows/win32/api/ifdef/ne-ifdef-net_if_media_duplex_state)

[**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes)

[NDIS Network Interface OIDs](./ndis-network-interface-oids.md)

 

