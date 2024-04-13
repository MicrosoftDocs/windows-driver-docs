---
title: OID_GEN_MAXIMUM_SEND_PACKETS
ms.topic: reference
description: As a query, the OID_GEN_MAXIMUM_SEND_PACKETS OID specifies the maximum number of send packet descriptors that a miniport driver's MiniportSendPackets function can accept.
ms.date: 08/08/2017
keywords: 
 -OID_GEN_MAXIMUM_SEND_PACKETS Network Drivers Starting with Windows Vista
---

# OID\_GEN\_MAXIMUM\_SEND\_PACKETS


As a query, the OID\_GEN\_MAXIMUM\_SEND\_PACKETS OID specifies the maximum number of send packet descriptors that a miniport driver's [*MiniportSendPackets*](/previous-versions/windows/hardware/network/ff550524(v=vs.85)) function can accept.

**Version Information**

<a href="" id="windows-vista-and-later-versions-of-windows"></a>Windows Vista and later versions of Windows  
Obsolete.

<a href="" id="ndis-6-0-and-later-miniport-drivers"></a>NDIS 6.0 and later miniport drivers  
Obsolete.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

<a href="" id="windows-xp"></a>Windows XP  
Supported.

<a href="" id="ndis-5-1-miniport-drivers"></a>NDIS 5.1 miniport drivers  
Mandatory.

## Remarks

NDIS ignores any value returned by a deserialized driver in response to a query of OID\_GEN\_MAXIMUM\_SEND\_PACKETS. NDIS does not adjust the size of the array of packet descriptors that it supplies to a deserialized miniport driver's *MiniportSendPackets* function.

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

## See also


[*MiniportSendPackets*](/previous-versions/windows/hardware/network/ff550524(v=vs.85))

 

