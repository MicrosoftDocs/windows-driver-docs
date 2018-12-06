---
title: WDI data transfer
description: This section covers WDI data transfer. The following terminology is used in this section.
ms.assetid: DA07E2C2-6478-40DD-AAD8-8ABD2777CA73
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# WDI data transfer


This section covers WDI data transfer. The following terminology is used in this section.

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
<td align="left"><p>Target WLAN device (target)</p></td>
<td align="left"><p>A physical NIC.</p></td>
</tr>
<tr class="even">
<td align="left"><p>Virtual WLAN device (port)</p></td>
<td align="left"><p>A virtual NIC (for example, P2P role ports).</p></td>
</tr>
<tr class="odd">
<td align="left"><p>WDI</p></td>
<td align="left"><p>A Microsoft WLAN component. It is a target-agnostic component.</p></td>
</tr>
<tr class="even">
<td align="left"><p><a href="" id="target-interface-layer---til-"></a>Target Interface Layer (TIL)</p></td>
<td align="left"><p>A target-specific software layer that interfaces with the target through the bus-specific APIs. It creates and manages DMA channels and provides bus abstraction.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>RX Manager / RxMgr</p></td>
<td align="left"><p>RxMgr performs receive processing steps that are not offloaded to the target.</p></td>
</tr>
<tr class="even">
<td align="left"><p>RxEngine</p></td>
<td align="left"><p>RxEngine sends and receives data-synchronous messages to and from the target, interprets RX descriptor formats, and manages buffers for direct hardware to software RX DMA.</p></td>
</tr>
<tr class="odd">
<td align="left"><p> TX Manager / TxMgr</p></td>
<td align="left"><p>The WDI-compliant driver component that gets TX frames from the operating system, delivers them to the TxEngine at the appropriate time, and returns the completed TX frames back to the operating system.</p></td>
</tr>
<tr class="even">
<td align="left"><p> TxEngine</p></td>
<td align="left"><p>The target-specific software component that handles the TX data transfer from host to target, and handles TX completion messages from the target.</p></td>
</tr>
<tr class="odd">
<td align="left"><p>Target Abstraction Layer (TAL)</p></td>
<td align="left"><p>The &quot;lower-edge&quot; that has a standardized API to the WDI compliant driver, but has a target-specific internal implementation. The TAL is a container layer for individual target-specific host software components such as TxEngine and RxEngine.</p></td>
</tr>
</tbody>
</table>

 

 

 





