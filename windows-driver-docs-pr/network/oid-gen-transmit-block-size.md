---
title: OID_GEN_TRANSMIT_BLOCK_SIZE
description: As a query, the OID_GEN_TRANSMIT_BLOCK_SIZE OID specifies the minimum number of bytes that a single net packet occupies in the transmit buffer space of the NIC.
ms.assetid: 81874999-029a-4e7e-8dbe-fc8e34bcae67
ms.date: 08/08/2017
keywords: 
 -OID_GEN_TRANSMIT_BLOCK_SIZE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
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

 

 




