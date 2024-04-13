---
title: OID_GEN_DRIVER_VERSION
ms.topic: reference
description: As a query, the OID_GEN_DRIVER_VERSION OID specifies the NDIS version in use by the miniport driver.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_DRIVER_VERSION Network Drivers Starting with Windows Vista
---

# OID\_GEN\_DRIVER\_VERSION


As a query, the OID\_GEN\_DRIVER\_VERSION OID specifies the NDIS version in use by the miniport driver.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Not requested.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

## Remarks

NDIS handles this OID for NDIS 6.0 and later miniport drivers.

The high byte is the major version number; the low byte is the minor version number.

## Requirements

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

 

 




