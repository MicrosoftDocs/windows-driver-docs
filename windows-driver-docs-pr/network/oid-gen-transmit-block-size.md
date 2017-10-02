---
title: OID_GEN_TRANSMIT_BLOCK_SIZE
author: windows-driver-content
description: As a query, the OID\_GEN\_TRANSMIT\_BLOCK\_SIZE OID specifies the minimum number of bytes that a single net packet occupies in the transmit buffer space of the NIC.
ms.assetid: 81874999-029a-4e7e-8dbe-fc8e34bcae67
ms.author: windowsdriverdev
ms.date: 08/08/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
keywords: 
 -OID_GEN_TRANSMIT_BLOCK_SIZE Network Drivers Starting with Windows Vista
---

# OID\_GEN\_TRANSMIT\_BLOCK\_SIZE


As a query, the OID\_GEN\_TRANSMIT\_BLOCK\_SIZE OID specifies the minimum number of bytes that a single net packet occupies in the transmit buffer space of the NIC.

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

The OID\_GEN\_TRANSMIT\_BLOCK\_SIZE OID specifies the minimum number of bytes that a single net packet occupies in the transmit buffer space of the NIC. For example, a NIC that has a transmit space divided into 256-byte pieces would have a transmit block size of 256 bytes. To calculate the total transmit buffer space on such a NIC, its driver multiplies the number of transmit buffers on the NIC by its transmit block size.

For other NICs, the transmit block size is identical to its maximum packet size.

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

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bnetvista\netvista%5D:%20OID_GEN_TRANSMIT_BLOCK_SIZE%20%20RELEASE:%20%288/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


