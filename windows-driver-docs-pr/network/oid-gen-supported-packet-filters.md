---
title: OID_GEN_SUPPORTED_PACKET_FILTERS
description: NDIS and overlying drivers obtain the types of net packets that the miniport adapter can filter during initialization.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_SUPPORTED_PACKET_FILTERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_SUPPORTED\_PACKET\_FILTERS


NDIS and overlying drivers obtain the types of net packets that the miniport adapter can filter during initialization.

**Note**  This OID is not implemented in the Windows Vista and later versions of Windows operating system. For more information, see the Remarks section.

 

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not implemented. (See Remarks section.)

## Remarks

Miniport drivers supply the supported packet filters during initialization.

To specify the supported packet filters, a miniport driver sets the **SupportedPacketFilters** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes) structure and passes the structure to the [**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes) function.

NDIS passes the information to protocol drivers in the **SupportedPacketFilters** member of the [**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters) structure.

The values in **SupportedPacketFilters** are a bitwise OR of the filter type flags. For a list of the filter type flags, see the [OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md) OID.

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


[**NdisMSetMiniportAttributes**](/windows-hardware/drivers/ddi/ndis/nf-ndis-ndismsetminiportattributes)

[**NDIS\_BIND\_PARAMETERS**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_bind_parameters)

[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](/windows-hardware/drivers/ddi/ndis/ns-ndis-_ndis_miniport_adapter_general_attributes)

[OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md)

 

