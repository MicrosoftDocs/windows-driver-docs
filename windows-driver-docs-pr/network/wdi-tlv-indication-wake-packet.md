---
title: WDI_TLV_INDICATION_WAKE_PACKET
description: WDI_TLV_INDICATION_WAKE_PACKET is a TLV that contains a wake packet for NDIS_STATUS_WDI_INDICATION_WAKE_REASON. When the wake reason is WDI_WAKE_REASON_CODE PACKET, the status must include the wake packet encapsulated in a WDI_TLV_INDICATION_WAKE_PACKET.
ms.assetid: 3C566FED-4594-403F-93D4-1CA6F2F655F9
ms.date: 07/18/2017
keywords:
 - WDI_TLV_INDICATION_WAKE_PACKET Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# WDI\_TLV\_INDICATION\_WAKE\_PACKET


WDI\_TLV\_INDICATION\_WAKE\_PACKET is a TLV that contains a wake packet for [NDIS\_STATUS\_WDI\_INDICATION\_WAKE\_REASON](https://msdn.microsoft.com/library/windows/hardware/dn925669). When the wake reason is WDI\_WAKE\_REASON\_CODE PACKET, the status must include the wake packet encapsulated in a WDI\_TLV\_INDICATION\_WAKE\_PACKET.

## TLV Type


0x9D

## Length


The size (in bytes) of the array of UINT8 elements. The array must contain 1 or more elements.

## Values


| Type      | Description                                                                                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------|
| UINT8\[\] | The wake packet. The size is the size of the flat memory version of the packet that will be indicated in the normal receive path. |

 

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Minimum supported client</p></td>
<td><p>Windows 10</p></td>
</tr>
<tr class="even">
<td><p>Minimum supported server</p></td>
<td><p>Windows Server 2016</p></td>
</tr>
<tr class="odd">
<td><p>Header</p></td>
<td>Wditypes.hpp</td>
</tr>
</tbody>
</table>

 

 




