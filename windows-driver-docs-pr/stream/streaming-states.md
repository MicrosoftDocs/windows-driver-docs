---
title: Streaming States
author: windows-driver-content
description: Streaming States
ms.assetid: 1030e5cd-441b-4f6a-8f6a-21ce11aaca96
keywords: ["video capture WDK AVStream , stream states", "capturing video WDK AVStream , stream states", "stream states WDK video capture", "states WDK video capture", "STOP state WDK video capture", "ACQUIRE state WDK video capture", "PAUSE state WDK video capture", "RUN state WDK video capture"]
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
<td><p>When the stream state is stopped, the minidriver uses the absolute minimum of resources, and there are no outstanding data SRBs in the minidriver's queue.</p></td>
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Streaming%20States%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


