---
title: WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY
author: windows-driver-content
description: WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY is a TLV that contains RSN Rekey protocol offload parameters.
ms.assetid: 4FDB56EA-444B-4EA2-B8D1-5E740734EEED
ms.author: windowsdriverdev 
ms.date: 07/18/2017 
ms.topic: article 
ms.prod: windows-hardware 
ms.technology: windows-devices 
keywords:
 - WDI_TLV_PM_PROTOCOL_OFFLOAD_80211RSN_REKEY Network Drivers Starting with Windows Vista
---

# WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_80211RSN\_REKEY


WDI\_TLV\_PM\_PROTOCOL\_OFFLOAD\_80211RSN\_REKEY is a TLV that contains RSN Rekey protocol offload parameters.

## TLV Type


0x63

## Length


The sum (in bytes) of the sizes of all contained elements.

## Values


| Type        | Description                                                                                                                                                                                                                                                                                                 |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UINT32      | Specifies the protocol offload ID. This is an OS-provided value that identifies the offloaded protocol. Before the OS sends an Add request down or completes the request to the overlying driver, the OS sets ProtocolOffloadId to a value that is unique among the protocol offloads on a network adapter. |
| UINT64      | Specifies the replay counter.                                                                                                                                                                                                                                                                               |
| UINT8\[16\] | Specifies the IEEE 802.11 key confirmation key (KCK).                                                                                                                                                                                                                                                       |
| UINT8\[16\] | Specifies the IEEE 802.11 key encryption key (KEK).                                                                                                                                                                                                                                                         |

 

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

 

 




