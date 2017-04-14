---
title: Video Stream Extended Headers
author: windows-driver-content
description: Video Stream Extended Headers
ms.assetid: 6540026c-a41a-49e2-a41f-fe64106408f5
keywords: ["video capture WDK AVStream , extended headers", "capturing video WDK AVStream , extended headers", "extended headers WDK video capture", "headers WDK video capture"]
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
<td><p>[<strong>KS_FRAME_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567645)</p></td>
<td><p>Frame count, drop frame count, field polarity flags, and DirectDraw surface handles.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KS_VBI_FRAME_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567694)</p></td>
<td><p>VBI format, channel change information, video standard.</p></td>
</tr>
</tbody>
</table>

 

If a Stream class minidriver does not provide this additional information, it should set **StreamHeaderMediaSpecific** to zero.

For more information about when to specify a value in **StreamHeaderMediaSpecific**, see [Stream Categories](stream-categories.md).

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Stream%20Extended%20Headers%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


