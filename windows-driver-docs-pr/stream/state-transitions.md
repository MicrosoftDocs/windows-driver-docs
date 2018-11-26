---
title: State Transitions
description: State Transitions
ms.assetid: c71fd395-28aa-4421-9443-b5b0a1f3ac7e
keywords:
- video capture WDK AVStream , stream states
- capturing video WDK AVStream , stream states
- stream states WDK video capture
- states WDK video capture
- state transitions WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# State Transitions


To ensure orderly resource allocation, only a subset of the possible kernel streaming state transitions is allowed. The following table lists the allowed transitions along with tasks that a Stream class minidriver typically performs during such transitions.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Transition</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Stop to pause</p></td>
<td><p>Allocate resources. The read SRBs are queued after the transition to <strong>KSSTATE_PAUSE</strong> has completed.</p></td>
</tr>
<tr class="even">
<td><p>Pause to run</p></td>
<td><p>Begin streaming.</p></td>
</tr>
<tr class="odd">
<td><p>Run to pause</p></td>
<td><p>Stop streaming. The outstanding read SRBs remain in the queue maintained by the minidriver.</p></td>
</tr>
<tr class="even">
<td><p>Pause to stop</p></td>
<td><p>Deallocate resources and complete all outstanding read SRBs. SRBs that have not been filled with an image are completed with zero length in the <strong>DataUsed</strong> member of the <a href="https://msdn.microsoft.com/library/windows/hardware/ff567138" data-raw-source="[&lt;strong&gt;KSSTREAM_HEADER&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567138)"><strong>KSSTREAM_HEADER</strong></a> structure.</p></td>
</tr>
</tbody>
</table>

 

**Note**  : Transitions can cycle multiple times between the **KSSTATE\_PAUSE** and **KSSTATE\_RUN** states before returning to the **KSSTATE\_STOP** state. Video capture minidrivers should expect transitions such as:

 

KSSTATE\_STOP -&gt; **KSSTATE\_ACQUIRE** -&gt; **KSSTATE\_PAUSE** -&gt; **KSSTATE\_RUN** -&gt; **KSSTATE\_PAUSE** -&gt; **KSSTATE\_RUN** -&gt; **KSSTATE\_PAUSE** -&gt; KSSTATE\_STOP

When a stream is in a **KSSTATE\_STOP** state, the minidriver must immediately complete all outstanding data-read SRBs.

Because a user-mode application can end unexpectedly while streaming, all Stream class minidrivers must accept and process an [**SRB\_CLOSE\_STREAM**](https://msdn.microsoft.com/library/windows/hardware/ff568165) request from the Stream class interface at any time. Before the Stream class interface sends SRB\_CLOSE\_STREAM to a minidriver, it cancels all outstanding buffers through the minidriver's **HwCancelPacket** routine. Note that the stream state cannot be set to **KSSTATE\_STOP** before the application terminates.

Do not update the **PictureNumber** or **DropCount** members of [**KS\_FRAME\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567645), [**KS\_VBI\_FRAME\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567694), or [**KSPROPERTY\_DROPPEDFRAMES\_CURRENT\_S**](https://msdn.microsoft.com/library/windows/hardware/ff565138) on transition from **KSSTATE\_PAUSE** to **KSSTATE\_RUN** or **KSSTATE\_RUN** to KSSTATE\_PAUSE. For more information, see [Capturing Video](capturing-video.md).

 

 




