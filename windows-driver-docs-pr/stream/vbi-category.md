---
title: VBI Category
description: VBI Category
ms.assetid: c33c0427-5162-435a-bb96-a230455a1035
keywords:
- stream categories WDK video capture , VBI
- VBI WDK video capture
- vertical blanking interval WDK video capture
- PINNAME_VIDEO_VBI
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567631" data-raw-source="[&lt;strong&gt;KS_DATARANGE_VIDEO_VBI&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567631)"><strong>KS_DATARANGE_VIDEO_VBI</strong></a></p></td>
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567694" data-raw-source="[&lt;strong&gt;KS_VBI_FRAME_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567694)"><strong>KS_VBI_FRAME_INFO</strong></a></p></td>
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

 

 

 




