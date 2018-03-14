---
title: DirectShow Filter to Stream Class Minidriver Communication
author: windows-driver-content
description: DirectShow Filter to Stream Class Minidriver Communication
ms.assetid: d2122827-758c-4557-b2fd-8774179b5da4
keywords:
- filter graph configurations WDK video capture , DirectShow
- DirectShow WDK video capture
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DirectShow Filter to Stream Class Minidriver Communication


User-mode DirectShow filters interact with video capture minidrivers using Win32 API **DeviceIoControl** function calls. These calls are translated by the Stream class interface into stream request blocks (SRBs) and are then sent to video capture minidrivers for processing. There are two categories of SRBs: SRBs that are used for general device-level control, and SRBs that affect an individual stream. The major SRBs for each category are shown in the following table.

<table>
<colgroup>
<col width="33%" />
<col width="33%" />
<col width="33%" />
</colgroup>
<thead>
<tr class="header">
<th>Function</th>
<th>Device</th>
<th>Stream</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Property</p>
<div>
 
</div>
Write</td>
<td><p>[<strong>SRB_SET_DEVICE_PROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568204)</p></td>
<td><p>[<strong>SRB_SET_STREAM_PROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568207)</p></td>
</tr>
<tr class="even">
<td><p>Property</p>
<div>
 
</div>
Read</td>
<td><p>[<strong>SRB_GET_DEVICE_PROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568170)</p></td>
<td><p>[<strong>SRB_GET_STREAM_PROPERTY</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568175)</p></td>
</tr>
<tr class="odd">
<td><p>Stream</p>
<div>
 
</div>
Write</td>
<td><p>None</p></td>
<td><p>[<strong>SRB_WRITE_DATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568220)</p></td>
</tr>
<tr class="even">
<td><p>Stream</p>
<div>
 
</div>
Read</td>
<td><p>None</p></td>
<td><p>[<strong>SRB_READ_DATA</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568200)</p></td>
</tr>
<tr class="odd">
<td><p>Open</p>
<div>
 
</div>
Stream</td>
<td><p>[<strong>SRB_OPEN_STREAM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568191)</p></td>
<td><p>None</p></td>
</tr>
<tr class="even">
<td><p>Close</p>
<div>
 
</div>
Stream</td>
<td><p>[<strong>SRB_CLOSE_STREAM</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568165)</p></td>
<td><p>None</p></td>
</tr>
<tr class="odd">
<td><p>Create</p>
<div>
 
</div>
Format</td>
<td><p>[<strong>SRB_GET_DATA_INTERSECTION</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568168)</p></td>
<td><p>None</p></td>
</tr>
<tr class="even">
<td><p>Change</p>
<div>
 
</div>
Stream
<div>
 
</div>
State</td>
<td><p>None</p></td>
<td><p>[<strong>SRB_SET_STREAM_STATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff568210)</p></td>
</tr>
</tbody>
</table>

 

Of the filters that constitute the "front end" of a video capture filter graph, such as the video capture filter, TV/radio tuner filter, TV audio filter, and crossbar filter, only the video capture filter truly participates in kernel streaming. The other filters are used to control device-level property sets in the video capture minidriver itself. Thus, minidrivers that support TV/radio tuning, TV audio, and crossbars do not expose kernel pins for each of their streams. These streams exist only as user-mode constructs to create the graph topology.

 

 




