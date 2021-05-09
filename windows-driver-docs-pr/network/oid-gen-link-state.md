---
title: OID_GEN_LINK_STATE
description: As a query, NDIS and overlying drivers use the OID_GEN_LINK_STATE OID to determine the current link state of a miniport adapter.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_LINK_STATE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_LINK\_STATE


As a query, NDIS and overlying drivers use the OID\_GEN\_LINK\_STATE OID to determine the current link state of a miniport adapter. The miniport driver receives the link state in an [**NDIS\_LINK\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_link_state) structure.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. (see Remarks section)

## Remarks

Miniport drivers supply the link state during initialization and provide updates with status indications.

To specify the link state, set the **MediaConnectState**, **MediaDuplexState**, **XmitLinkSpeed**, **RcvLinkSpeed**, **PauseFunctions**, and **AutoNegotiationFlags** members of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure that the miniport driver passes to the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function.

If a miniport driver does not support this OID, the driver should return NDIS\_STATUS\_NOT\_SUPPORTED. If the miniport driver supports this OID, it returns the connection state, duplex state, and link speeds in an [**NDIS\_LINK\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_link_state) structure.

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


[**NDIS\_LINK\_STATE**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_link_state)

[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes)

[**NDIS\_OBJECT\_HEADER**](/windows-hardware/drivers/ddi/ntddndis/ns-ntddndis-_ndis_object_header)

[**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes)

[OID\_GEN\_MEDIA\_CONNECT\_STATUS\_EX](oid-gen-media-connect-status-ex.md)

[OID\_GEN\_MEDIA\_DUPLEX\_STATE](oid-gen-media-duplex-state.md)

 

