---
title: OID_GEN_TRANSMIT_BUFFER_SPACE
description: As a query, the OID_GEN_TRANSMIT_BUFFER_SPACE OID specifies the amount of memory, in bytes, on the NIC that is available for buffering transmit data.
ms.assetid: 23d242fc-8447-4660-ab84-b8cbdb638a71
ms.date: 08/08/2017
keywords: 
 -OID_GEN_TRANSMIT_BUFFER_SPACE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_TRANSMIT\_BUFFER\_SPACE


As a query, the OID\_GEN\_TRANSMIT\_BUFFER\_SPACE OID specifies the amount of memory, in bytes, on the NIC that is available for buffering transmit data.

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

A protocol can use this OID as a guide for sizing the amount of transmit data per send.

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

 

 




