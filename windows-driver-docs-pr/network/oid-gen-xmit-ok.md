---
title: OID_GEN_XMIT_OK
description: As a query, the OID_GEN_XMIT_OK OID specifies the number of frames that are transmitted without errors.
ms.assetid: ac7120a3-58bb-4047-b4b7-ad9fbaf14e4f
ms.date: 08/08/2017
keywords: 
 -OID_GEN_XMIT_OK Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_XMIT\_OK


As a query, the OID\_GEN\_XMIT\_OK OID specifies the number of frames that are transmitted without errors.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-drivers"></a>NDIS 6.0 and later drivers  
Mandatory.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-drivers"></a>NDIS 5.1 drivers  
Mandatory.

Remarks
-------

OID\_GEN\_XMIT\_OK specifies the number of frames that are transmitted without errors. However, the [OID\_GEN\_STATISTICS](oid-gen-statistics.md) does not include this information.

NOTE: Statistics OIDs are mandatory for NDIS 6.0 and later miniport drivers unless NDIS handles them. For general information about statistics OIDs, see [General Statistics](https://msdn.microsoft.com/library/windows/hardware/ff552485).

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


[OID\_GEN\_STATISTICS](oid-gen-statistics.md)

 

 




