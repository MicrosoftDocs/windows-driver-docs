---
title: OID_GEN_PORT_AUTHENTICATION_PARAMETERS
description: As a set, NDIS and overlying drivers use the OID_GEN_PORT_AUTHENTICATION_PARAMETERS OID to set the current state of an NDIS port.
ms.assetid: 676601c1-2647-4341-9a5c-cee895d2dbf7
ms.date: 08/08/2017
keywords: 
 -OID_GEN_PORT_AUTHENTICATION_PARAMETERS Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_GEN\_PORT\_AUTHENTICATION\_PARAMETERS


As a set, NDIS and overlying drivers use the OID\_GEN\_PORT\_AUTHENTICATION\_PARAMETERS OID to set the current state of an NDIS port.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Supported.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Optional. Mandatory for NDIS ports. (see Remarks section)

Remarks
-------

Miniport drivers that support NDIS ports must support this OID.

If a miniport driver does not support this OID, the miniport driver should return NDIS\_STATUS\_NOT\_SUPPORTED.

If the miniport driver supports this OID, the driver returns NDIS\_STATUS\_SUCCESS and provides the receive port direction, port control state, and authenticate state in an [**NDIS\_PORT\_AUTHENTICATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566788) structure.

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


[**NDIS\_PORT\_AUTHENTICATION\_PARAMETERS**](https://msdn.microsoft.com/library/windows/hardware/ff566788)

 

 




