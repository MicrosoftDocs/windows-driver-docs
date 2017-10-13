---
title: OID_GEN_SUPPORTED_PACKET_FILTERS
author: windows-driver-content
description: NDIS and overlying drivers obtain the types of net packets that the miniport adapter can filter during initialization.
ms.assetid: c19cecf3-ae47-4fd1-b5dc-1f3de469e548
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_SUPPORTED_PACKET_FILTERS Network Drivers Starting with Windows Vista
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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_SUPPORTED_PACKET_FILTERS%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


