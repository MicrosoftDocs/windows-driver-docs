---
title: Streaming States
description: Streaming States
ms.assetid: 1030e5cd-441b-4f6a-8f6a-21ce11aaca96
keywords:
- video capture WDK AVStream , stream states
- capturing video WDK AVStream , stream states
- stream states WDK video capture
- states WDK video capture
- STOP state WDK video capture
- ACQUIRE state WDK video capture
- PAUSE state WDK video capture
- RUN state WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Streaming States


Each stream provided by the minidriver exists in one of four states: KSSTATE\_STOP, KSSTATE\_ACQUIRE, KSSTATE\_PAUSE, or KSSTATE\_RUN. Upon initialization, the stream is, by default, in the **KSSTATE\_STOP** state. Transitions to the other states are made when the Stream class interface sends an [**SRB\_SET\_STREAM\_STATE**](https://msdn.microsoft.com/library/windows/hardware/ff568210) request to the minidriver. The following table identifies and describes the four stream states.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>State</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>KSSTATE_STOP</p></td>
<td><p>When the stream state is stopped, the minidriver uses the absolute minimum of resources, and there are no outstanding data SRBs in the minidriver&#39;s queue.</p></td>
</tr>
<tr class="even">
<td><p>KSSTATE_ACQUIRE</p></td>
<td><p>When the stream state is acquiring resources, the minidriver allocates all needed resources, such as bandwidth on USB and IEEE 1394.</p></td>
</tr>
<tr class="odd">
<td><p>KSSTATE_PAUSE</p></td>
<td><p>When the stream state is paused, the minidriver is prepared to instantly make a transition to KSSTATE_RUN.</p></td>
</tr>
<tr class="even">
<td><p>KSSTATE_RUN</p></td>
<td><p>When the stream state is streaming, the minidriver fills buffers and completes SRBs using <strong>CompleteStreamSRB</strong>.</p></td>
</tr>
</tbody>
</table>

 

 

 




