---
title: OID_GEN_RECEIVE_BUFFER_SPACE
description: As a query, the OID_GEN_RECEIVE_BUFFER_SPACE OID specifies the amount of memory on the NIC that is available for buffering receive data.
ms.assetid: 6eec18fa-22cd-4f65-acf4-0dd438dea2ff
ms.date: 08/08/2017
keywords: 
 -OID_GEN_RECEIVE_BUFFER_SPACE Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_RECEIVE\_BUFFER\_SPACE


As a query, the OID\_GEN\_RECEIVE\_BUFFER\_SPACE OID specifies the amount of memory on the NIC that is available for buffering receive data.

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

A protocol driver can use this OID as a guide for advertising its receive window after it establishes sessions with remote nodes.

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

 

 




