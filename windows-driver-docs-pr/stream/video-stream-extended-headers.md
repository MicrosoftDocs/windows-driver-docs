---
title: Video Stream Extended Headers
description: Video Stream Extended Headers
ms.assetid: 6540026c-a41a-49e2-a41f-fe64106408f5
keywords:
- video capture WDK AVStream , extended headers
- capturing video WDK AVStream , extended headers
- extended headers WDK video capture
- headers WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Video Stream Extended Headers


A video capture minidriver uses an extended header in its output streams to provide auxiliary information about the stream and current frame contents. For example, image stream headers provide information about the current frame number, number of dropped frames, and field polarity flags. As each frame is completed, the minidriver fills in the extended header with the auxiliary information about the frame captured.

Stream class video capture minidrivers indicate their ability to provide this additional information for a pin by setting the **StreamHeaderMediaSpecific** member of the [**HW\_STREAM\_OBJECT**](https://msdn.microsoft.com/library/windows/hardware/ff559697) structure to the **sizeof** one of the two following structures.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Structure name</th>
<th>Purpose</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567645" data-raw-source="[&lt;strong&gt;KS_FRAME_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567645)"><strong>KS_FRAME_INFO</strong></a></p></td>
<td><p>Frame count, drop frame count, field polarity flags, and DirectDraw surface handles.</p></td>
</tr>
<tr class="even">
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567694" data-raw-source="[&lt;strong&gt;KS_VBI_FRAME_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567694)"><strong>KS_VBI_FRAME_INFO</strong></a></p></td>
<td><p>VBI format, channel change information, video standard.</p></td>
</tr>
</tbody>
</table>

 

If a Stream class minidriver does not provide this additional information, it should set **StreamHeaderMediaSpecific** to zero.

For more information about when to specify a value in **StreamHeaderMediaSpecific**, see [Stream Categories](stream-categories.md).

 

 




