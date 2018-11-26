---
title: OID_GEN_LINK_SPEED
description: As a query, the OID_GEN_LINK_SPEED OID specifies the maximum speed of the NIC.
ms.assetid: f8ee887a-969e-4167-9b39-9ee6ef8b1fbc
ms.date: 08/08/2017
keywords: 
 -OID_GEN_LINK_SPEED Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_LINK\_SPEED


As a query, the OID\_GEN\_LINK\_SPEED OID specifies the maximum speed of the NIC.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Obsolete.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Obsolete. (see Remarks section)

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

Remarks
-------

The [OID\_GEN\_LINK\_STATE](oid-gen-link-state.md) is the NDIS 6.0 and later and later equivalent of this OID. However NDIS 6.0 and later miniport drivers must use the [**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391) status indication instead to indicate link speed changes.

The unit of measurement is 100 bps, so a value of 100,000 represents a hardware bit rate of 10 Mbps.

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


[**NDIS\_STATUS\_LINK\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff567391)

[OID\_GEN\_LINK\_STATE](oid-gen-link-state.md)

 

 




