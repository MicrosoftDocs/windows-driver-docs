---
title: Updating Cached Variables
description: Updating Cached Variables
ms.assetid: 1263c6de-8c96-4c87-a5cc-dd874de3dd8f
keywords:
- updating offloaded TCP chimney state, cached variables
- cached variables WDK TCP chimney offload
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Updating Cached Variables


\[The TCP chimney offload feature is deprecated and should not be used.\]




Because the host stack owns and maintains cached variables, it must alert the offload target to any changes in the values of such variables. The host stack changes the values of cached variables with one or more update operations. The host stack can update cached variables in offloaded neighbor, path, and TCP connection state objects.

The following table lists some of the events that require updates to cached variables in offloaded state objects.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">State object</th>
<th align="left">Event</th>
<th align="left">Updated variables</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Neighbor</p></td>
<td align="left"><p>The destination address of a neighbor changes because of an Address Resolution Protocol (ARP) update (IPv4) or through neighbor discovery (IPv6).</p></td>
<td align="left"><p><strong>DestinationAddress</strong></p></td>
</tr>
<tr class="even">
<td align="left"><p>Path</p></td>
<td align="left"><p>The host stack receives an Internet Control Message Protocol (ICMP) message that changes the <strong>PathMtu</strong> variable.</p></td>
<td align="left"><p><strong>PathMtu</strong></p></td>
</tr>
<tr class="odd">
<td align="left"><p>TCP</p></td>
<td align="left"><p>A client application enables keepalive functionality on the TCP connection.</p></td>
<td align="left"><p><strong>Flags</strong>(set to TCP_FLAG_KEEP_ALIVE_ENABLED)</p></td>
</tr>
<tr class="even">
<td align="left"></td>
<td align="left"><p>A client applications sets socket options to enable or disable keepalives.</p></td>
<td align="left"><p><strong>KaProbeCount</strong>, <strong>KaTimeout</strong>, and/or <strong>KaInterval</strong></p></td>
</tr>
<tr class="odd">
<td align="left"></td>
<td align="left"><p>A client application sets the SO_RCVBUF socket option variable to increase or decrease the receive window. The offload target must honor the updated receive window.</p></td>
<td align="left"><p><strong>InitialRcvWnd</strong></p></td>
</tr>
</tbody>
</table>

 

Note that, if an offloaded TCP connection's TCP\_FLAG\_MAX\_RT\_RESTART flag is set (in the **Flags** member of [**TCP\_OFFLOAD\_STATE\_CACHED**](https://msdn.microsoft.com/library/windows/hardware/ff570937)), the offload target must:

-   Reset that connection's delegated *KeepaliveProbeCount* variable when the host stack updates that connection's cached *KaProbeCount* variable.

-   Reset that connection's delegated *KeepaliveTimeoutDelta* variable when the host stack updates that connection's cached *KaTimeout* variable or *KaInterval* variable or both.

 

 





