---
title: DVD Decoder Related KS Events
author: windows-driver-content
description: DVD Decoder Related KS Events
MS-HAID:
- 'dvd-design\_65149264-702d-4668-82c0-5eb54d337b2a.xml'
- 'stream.dvd\_decoder\_related\_ks\_events'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 19fd2c88-72f4-4742-8c96-74be250dd59d
keywords: ["DVD decoder minidrivers WDK , KS events", "decoder minidrivers WDK DVD , KS events", "KS events WDK DVD decoder", "events WDK DVD decoder"]
---

# DVD Decoder Related KS Events


## <a href="" id="ddk-dvd-decoder-related-ks-events-ksg"></a>


The following tables describe the kernel streaming event set and its respective event that is related to DVD decoder hardware:

The [KSEVENTSETID\_VPNotify](https://msdn.microsoft.com/library/windows/hardware/ff561780) event set groups all kernel streaming events that are related to tuner events.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>KSEVENTSETID_VPNotify KS Events</th>
<th>Event Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>KSEVENT_VPNOTIFY_FORMATCHANGE</strong>](https://msdn.microsoft.com/library/windows/hardware/ff561933)</p></td>
<td><p>Notifies DirectShow of a change in the video port configuration, such as a change in resolution from 640x480 to 720x480.</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20DVD%20Decoder%20Related%20KS%20Events%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


