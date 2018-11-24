---
title: WDI task command priority and existing state
description: When the adapter is in a particular state, new commands may come down to it that could affect the existing state (for example, a scan that affects existing connections).
ms.assetid: 11EE42BF-2C44-4601-B262-570E6D154151
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI task command priority and existing state


When the adapter is in a particular state, new commands may come down to it that could affect the existing state (for example, a scan that affects existing connections). The table below describes how new commands should be prioritized against the existing state in the adapter. The columns describe how to service the existing state when the new command comes in.

New command
Existing state
Connection Quality (EAP) - Priority 1
P2P Listen - Priority 2
Connection Quality Latency (Media Streaming) - Priority 3
Existing Connections - Priority 4
Scan/P2P Discovery (forced)
Important (delay scan)
Pause
Pause
Throttle
Scan/P2P Discovery (not forced)
Important (skip scan)
Maintain
Important (skip scan)
Throttle
Station Connect, Roam, Disconnect
Delay Connect
Pause
Pause
Throttle
P2P GO Start, GO Stop
Delay Connect
Pause
Pause
Throttle
P2P Client Connect, Disconnect
Delay Connect
Pause
Pause
Throttle
P2P Send Action Response
Pause
Pause
Pause
Throttle
P2P Send Action Request
Delay Send
Maintain
Pause
Throttle
 

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th align="left">Term</th>
<th align="left">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td align="left"><p>Important</p></td>
<td align="left"><p>Prioritize the existing state higher than the new request.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Maintain</p></td>
<td align="left"><p>Prioritize the existing state and the new command equally.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Throttle</p></td>
<td align="left"><p>Throttle down the servicing of the existing state so that it works, but prioritize the new command higher.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Pause</p></td>
<td align="left"><p>Stop servicing the existing state and attempt to finish the existing state as soon as possible.</p></td>
</tr>
</tbody>
</table>

 

 

 





