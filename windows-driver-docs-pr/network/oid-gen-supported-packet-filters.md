---
title: OID_GEN_SUPPORTED_PACKET_FILTERS
description: NDIS and overlying drivers obtain the types of net packets that the miniport adapter can filter during initialization.
ms.assetid: c19cecf3-ae47-4fd1-b5dc-1f3de469e548
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

Remarks
-------

Miniport drivers supply the supported packet filters during initialization.

To specify the supported packet filters, a miniport driver sets the **SupportedPacketFilters** member of the [**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923) structure and passes the structure to the [**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672) function.

NDIS passes the information to protocol drivers in the **SupportedPacketFilters** member of the [**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832) structure.

The values in **SupportedPacketFilters** are a bitwise OR of the filter type flags. For a list of the filter type flags, see the [OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md) OID.

Requirements
------------

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


[**NdisMSetMiniportAttributes**](https://msdn.microsoft.com/library/windows/hardware/ff563672)

[**NDIS\_BIND\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff564832)

[**NDIS\_MINIPORT\_ADAPTER\_GENERAL\_ATTRIBUTES**](https://msdn.microsoft.com/library/windows/hardware/ff565923)

[OID\_GEN\_CURRENT\_PACKET\_FILTER](oid-gen-current-packet-filter.md)

 

 




