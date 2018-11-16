---
title: OID_GEN_CURRENT_LOOKAHEAD
description: As a query, the OID_GEN_CURRENT_LOOKAHEAD OID returns the number of bytes of received packet data that will be indicated to the protocol driver.
ms.assetid: ccfcb5ca-04bd-416b-91ec-690e78daeda0
ms.date: 08/08/2017
keywords: 
 -OID_GEN_CURRENT_LOOKAHEAD Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_CURRENT\_LOOKAHEAD


As a query, the OID\_GEN\_CURRENT\_LOOKAHEAD OID returns the number of bytes of received packet data that will be indicated to the protocol driver. This specification does not include the header.

As a set, the OID\_GEN\_CURRENT\_LOOKAHEAD OID specifies the number of bytes of received packet data that the miniport driver should indicate to the protocol driver. This specification does not include the header.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Mandatory. (see Remarks section)

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

NDIS handles query and unsuccessful set requests for NDIS 6.0 and later miniport drivers. NDIS obtains the information from the miniport driver during initialization and miniport adapter restart. However, NDIS sends valid set requests to the miniport driver.

For a query, NDIS returns the largest lookahead size from among all the bindings. A protocol driver can set a suggested value for the number of bytes to be used in its binding; however, the underlying miniport driver is never required to limit its indications to the value set.

If the underlying driver supports multipacket receive indications, bound protocol drivers are given full net packets on every indication. Consequently, this value is identical to that returned for [OID\_GEN\_RECEIVE\_BLOCK\_SIZE](oid-gen-receive-block-size.md).

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


[OID\_GEN\_RECEIVE\_BLOCK\_SIZE](oid-gen-receive-block-size.md)

 

 




