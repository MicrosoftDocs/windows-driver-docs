---
title: OID_WWAN_NETWORK_IDLE_HINT
description: OID_WWAN_NETWORK_IDLE_HINT sends a hint to the network interface regarding whether data is expected to be active or idle on the interface.
ms.assetid: 1FE758C1-543A-45B4-A377-336A1307689F
ms.date: 08/08/2017
keywords: 
 -OID_WWAN_NETWORK_IDLE_HINT Network Drivers Starting with Windows Vista
ms.localizationpriority: medium
---

# OID\_WWAN\_NETWORK\_IDLE\_HINT


OID\_WWAN\_NETWORK\_IDLE\_HINT sends a hint to the network interface regarding whether data is expected to be active or idle on the interface. The network service uses heuristics to determine when to send this request to the interface, typically when it estimates that for a period of time there will be a reduction in network traffic or if the system is entering an idle state (such as connected standby). The network interface can use this as an input to its heuristics to implement procedures such as "fast dormancy".

Query requests are not supported.

Miniport drivers must process set requests asynchronously, initially returning NDIS\_STATUS\_INDICATION\_REQUIRED to the original request, and later completing the request with the [**NDIS\_WWAN\_NETWORK\_IDLE\_HINT**](https://msdn.microsoft.com/library/windows/hardware/dn931088) structure that indicates the network idle hint.

Requirements
------------

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>Version</p></td>
<td><p>Available in Windows 10 and later versions of Windows.</p></td>
</tr>
<tr class="even">
<td><p>Header</p></td>
<td>Ntddndis.h (include Ndis.h)</td>
</tr>
</tbody>
</table>

## See also


[**NDIS\_WWAN\_NETWORK\_IDLE\_HINT**](https://msdn.microsoft.com/library/windows/hardware/dn931088)

 

 




