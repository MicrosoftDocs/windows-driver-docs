---
title: OID_GEN_PROTOCOL_OPTIONS
description: As a set, the OID_GEN_PROTOCOL_OPTIONS OID specifies a bitmask that defines optional properties of the protocol driver.
ms.assetid: 48c3468b-2d8b-48cb-9a25-19470923f582
ms.date: 08/08/2017
keywords: 
 -OID_GEN_PROTOCOL_OPTIONS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_PROTOCOL\_OPTIONS


As a set, the OID\_GEN\_PROTOCOL\_OPTIONS OID specifies a bitmask that defines optional properties of the protocol driver.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested. This OID is for protocol drivers.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

A protocol informs NDIS of its properties, which can optionally take advantage of them. If the protocol driver does not set its flags on a binding, NDIS assumes they are all clear.

The following flags are currently defined:

<a href="" id="ndis-prot-option-estimated-length"></a>NDIS\_PROT\_OPTION\_ESTIMATED\_LENGTH  
Specifies that packets can be indicated at the worst-case estimate of packet size, instead of an exact value, to this protocol.

<a href="" id="ndis-prot-option-no-loopback"></a>NDIS\_PROT\_OPTION\_NO\_LOOPBACK  
Specifies that the protocol does not require loopback support on the binding.

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

 

 




