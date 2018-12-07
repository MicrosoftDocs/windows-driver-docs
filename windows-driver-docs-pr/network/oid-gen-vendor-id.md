---
title: OID_GEN_VENDOR_ID
description: As a query, the OID_GEN_VENDOR_ID OID specifies a three-byte IEEE-registered vendor code, followed by a single byte that the vendor assigns to identify a particular NIC.
ms.assetid: dce0a2e4-5d34-417f-9764-85644fe2ce46
ms.date: 08/08/2017
keywords: 
 -OID_GEN_VENDOR_ID Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_VENDOR\_ID


As a query, the OID\_GEN\_VENDOR\_ID OID specifies a three-byte IEEE-registered vendor code, followed by a single byte that the vendor assigns to identify a particular NIC.

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

The IEEE code uniquely identifies the vendor and is the same as the three bytes appearing at the beginning of the NIC hardware address.

Vendors without an IEEE-registered code should use the value 0xFFFFFF.

Independent hardware vendor's filter drivers or intermediate drivers might query this OID.

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

 

 




