---
title: Video Capture Events
author: windows-driver-content
description: Video Capture Events
ms.assetid: 9d40b9f7-41c1-4410-afc7-9b4ff1c2fe7e
keywords:
- events WDK video capture
- KSEVENTSETID_VIDCAPNotify
- video capture events WDK AVStream
ms.author: windowsdriverdev
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Video Capture Events


The [KSEVENTSETID\_VIDCAPNotify](https://msdn.microsoft.com/library/windows/hardware/ff561773) event set contains events related to tuner events. The following table describes the events that are part of the KSEVENTSETID\_VIDCAPNotify event set.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KSEVENTSETID_VIDCAPNotify KS events</th>
<th>Event description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSEVENT_VIDCAPTOSTI_EXT_TRIGGER</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561912)</p></td>
<td><p>Signals to a registered client when a button on a video capture device is triggered.</p></td>
</tr>
<tr class="even">
<td><p>[<strong>KSEVENT_VIDCAP_AUTO_UPDATE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561916)</p></td>
<td><p>Signals to a registered client when a property value changes.</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>KSEVENT_VIDCAP_SEARCH</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561923)</p></td>
<td><p>Signals to a registered client when a search completes.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Video%20Capture%20Events%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


