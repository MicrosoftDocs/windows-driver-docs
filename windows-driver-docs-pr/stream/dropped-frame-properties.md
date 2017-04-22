---
title: Dropped Frame Properties
author: windows-driver-content
description: Dropped Frame Properties
ms.assetid: 9c8bd66f-aa25-49e2-a442-9046a4d46466
keywords:
- dropped frame properties WDK video capture
- PROPSETID_VIDCAP_DROPPEDFRAMES
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Dropped Frame Properties


The [PROPSETID\_VIDCAP\_DROPPEDFRAMES](https://msdn.microsoft.com/library/windows/hardware/ff567806) property set contains properties related to the dropping of video frames during a capture operation. The following table describes the properties that are part of the PROPSETID\_VIDCAP\_DROPPEDFRAMES property set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>PROPSETID_VIDCAP_DROPPEDFRAMES KS properties</th>
<th>Property description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSPROPERTY_DROPPEDFRAMES_CURRENT</strong>](https://msdn.microsoft.com/library/windows/hardware/ff565135)</p></td>
<td><p>Returns the dropped frame information for a capture operation, including the current picture number and the average video frame size.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Dropped%20Frame%20Properties%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


