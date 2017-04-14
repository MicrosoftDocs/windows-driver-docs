---
title: VBI Category
author: windows-driver-content
description: VBI Category
ms.assetid: c33c0427-5162-435a-bb96-a230455a1035
keywords: ["stream categories WDK video capture , VBI", "VBI WDK video capture", "vertical blanking interval WDK video capture", "PINNAME_VIDEO_VBI"]
---

# VBI Category


The following GUID corresponds to the vertical blanking interval (VBI) category:

-   **PINNAME\_VIDEO\_VBI**

    VBI category output pins provide a stream of VBI waveform samples. This stream is passed to downstream codecs that extract closed captioning (CC), NABTS, WST, timecode, and other digital data streams.

When specifying **PINNAME\_VIDEO\_VBI** pins, use the information listed in the following table.

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Value</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DataRange Structure</strong></p></td>
<td><p>[<strong>KS_DATARANGE_VIDEO_VBI</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567631)</p></td>
</tr>
<tr class="even">
<td><p><strong>DataFormat Structure</strong></p></td>
<td><p>KS_DATAFORMAT_VIDEO_VBI</p></td>
</tr>
<tr class="odd">
<td><p><strong>MajorFormat GUID</strong></p></td>
<td><p>KS_DATAFORMAT_TYPE_VBI</p></td>
</tr>
<tr class="even">
<td><p><strong>SubFormat GUID</strong></p></td>
<td><p>KSDATAFORMAT_SUBTYPE_RAW8</p></td>
</tr>
<tr class="odd">
<td><p><strong>Specifier GUID</strong></p></td>
<td><p>KSDATAFORMAT_SPECIFIER_VBI</p></td>
</tr>
<tr class="even">
<td><p><strong>Extended Header Size</strong></p></td>
<td><p>[<strong>KS_VBI_FRAME_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567694)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Required Property Sets</strong></p></td>
<td><p>None</p></td>
</tr>
<tr class="even">
<td><p><strong>Required Event Sets</strong></p></td>
<td><p>None</p></td>
</tr>
<tr class="odd">
<td><p><strong>DirectShow majortype</strong></p></td>
<td><p>MEDIATYPE_VBI</p></td>
</tr>
<tr class="even">
<td><p><strong>DirectShow formattype</strong></p></td>
<td><p>FORMAT_VBI</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20VBI%20Category%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


