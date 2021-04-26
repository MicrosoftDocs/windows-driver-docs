---
title: DirectShow Filter to Stream Class Minidriver Communication
description: DirectShow Filter to Stream Class Minidriver Communication
keywords:
- filter graph configurations WDK video capture , DirectShow
- DirectShow WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="/windows-hardware/drivers/stream/srb-set-device-property" data-raw-source="[&lt;strong&gt;SRB_SET_DEVICE_PROPERTY&lt;/strong&gt;](./srb-set-device-property.md)"><strong>SRB_SET_DEVICE_PROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/stream/srb-set-stream-property" data-raw-source="[&lt;strong&gt;SRB_SET_STREAM_PROPERTY&lt;/strong&gt;](./srb-set-stream-property.md)"><strong>SRB_SET_STREAM_PROPERTY</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Property</p>
<div>
 
</div>
Read</td>
<td><p><a href="/windows-hardware/drivers/stream/srb-get-device-property" data-raw-source="[&lt;strong&gt;SRB_GET_DEVICE_PROPERTY&lt;/strong&gt;](./srb-get-device-property.md)"><strong>SRB_GET_DEVICE_PROPERTY</strong></a></p></td>
<td><p><a href="/windows-hardware/drivers/stream/srb-get-stream-property" data-raw-source="[&lt;strong&gt;SRB_GET_STREAM_PROPERTY&lt;/strong&gt;](./srb-get-stream-property.md)"><strong>SRB_GET_STREAM_PROPERTY</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>Stream</p>
<div>
 
</div>
Write</td>
<td><p>None</p></td>
<td><p><a href="/windows-hardware/drivers/stream/srb-write-data" data-raw-source="[&lt;strong&gt;SRB_WRITE_DATA&lt;/strong&gt;](./srb-write-data.md)"><strong>SRB_WRITE_DATA</strong></a></p></td>
</tr>
<tr class="even">
<td><p>Stream</p>
<div>
 
</div>
Read</td>
<td><p>None</p></td>
<td><p><a href="/windows-hardware/drivers/stream/srb-read-data" data-raw-source="[&lt;strong&gt;SRB_READ_DATA&lt;/strong&gt;](./srb-read-data.md)"><strong>SRB_READ_DATA</strong></a></p></td>
</tr>
<tr class="odd">
<td><p>Open</p>
<div>
 
</div>
Stream</td>
<td><p><a href="/windows-hardware/drivers/stream/srb-open-stream" data-raw-source="[&lt;strong&gt;SRB_OPEN_STREAM&lt;/strong&gt;](./srb-open-stream.md)"><strong>SRB_OPEN_STREAM</strong></a></p></td>
<td><p>None</p></td>
</tr>
<tr class="even">
<td><p>Close</p>
<div>
 
</div>
Stream</td>
<td><p><a href="/windows-hardware/drivers/stream/srb-close-stream" data-raw-source="[&lt;strong&gt;SRB_CLOSE_STREAM&lt;/strong&gt;](./srb-close-stream.md)"><strong>SRB_CLOSE_STREAM</strong></a></p></td>
<td><p>None</p></td>
</tr>
<tr class="odd">
<td><p>Create</p>
<div>
 
</div>
Format</td>
<td><p><a href="/windows-hardware/drivers/stream/srb-get-data-intersection" data-raw-source="[&lt;strong&gt;SRB_GET_DATA_INTERSECTION&lt;/strong&gt;](./srb-get-data-intersection.md)"><strong>SRB_GET_DATA_INTERSECTION</strong></a></p></td>
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
<td><p><a href="/windows-hardware/drivers/stream/srb-set-stream-state" data-raw-source="[&lt;strong&gt;SRB_SET_STREAM_STATE&lt;/strong&gt;](./srb-set-stream-state.md)"><strong>SRB_SET_STREAM_STATE</strong></a></p></td>
</tr>
</tbody>
</table>

 

Of the filters that constitute the "front end" of a video capture filter graph, such as the video capture filter, TV/radio tuner filter, TV audio filter, and crossbar filter, only the video capture filter truly participates in kernel streaming. The other filters are used to control device-level property sets in the video capture minidriver itself. Thus, minidrivers that support TV/radio tuning, TV audio, and crossbars do not expose kernel pins for each of their streams. These streams exist only as user-mode constructs to create the graph topology.

