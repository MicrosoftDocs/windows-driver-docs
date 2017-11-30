---
title: OID_GEN_MAXIMUM_TOTAL_SIZE
author: windows-driver-content
description: As a query, the OID_GEN_MAXIMUM_TOTAL_SIZE OID specifies the maximum total packet length, in bytes, the NIC supports.
ms.assetid: 4973b4bd-58a5-4242-b33f-1ff8c3a7ec4b
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_MAXIMUM_TOTAL_SIZE Network Drivers Starting with Windows Vista
---

# OID\_GEN\_MAXIMUM\_TOTAL\_SIZE


As a query, the OID\_GEN\_MAXIMUM\_TOTAL\_SIZE OID specifies the maximum total packet length, in bytes, the NIC supports. This specification includes the header.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Mandatory.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

The returned length specifies the largest packet size for the underlying medium. Thus, the returned length depends on the particular medium. A protocol driver might use this returned length as a gauge to determine the maximum size packet that a miniport driver could forward to the protocol driver. If the protocol driver preallocates buffers, it allocates buffers accordingly. The returned length also specifies the largest packet that a protocol driver can pass to the [**NdisSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564535) function.

If the miniport driver for a NIC enables [802.1p packet priority](https://msdn.microsoft.com/library/windows/hardware/ff562331)(that is, the miniport driver specifies the NDIS\_MAC\_OPTION\_8021P\_PRIORITY bit in the [OID\_GEN\_MAC\_OPTIONS](oid-gen-mac-options.md) OID bitmask), then the miniport driver must specify its maximum total packet length as 4 bytes less than the maximum size of packets received or sent over the network. For example, if a NIC that has 802.1p packet priority enabled receives and sends packets on the wire that are 1514 bytes in length, the miniport driver for the NIC must report its maximum total packet length as 1510 bytes. The miniport driver must never indicate up to the bound protocol driver packets received over the network that are longer than the packet size specified by OID\_GEN\_MAXIMUM\_TOTAL\_SIZE. That is, even if the miniport driver receives packets over the network that are not marked with priority values but are still the maximum size that the underlying medium supports, the miniport driver can only indicate up packets that are no longer than the size specified by OID\_GEN\_MAXIMUM\_TOTAL\_SIZE.

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


[**NdisSendNetBufferLists**](https://msdn.microsoft.com/library/windows/hardware/ff564535)

[OID\_GEN\_MAC\_OPTIONS](oid-gen-mac-options.md)

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_MAXIMUM_TOTAL_SIZE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


