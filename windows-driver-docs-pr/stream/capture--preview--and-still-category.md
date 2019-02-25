---
title: Capture, Preview, and Still Category
description: Capture, Preview, and Still Category
ms.assetid: b82cc3b6-1cea-4864-9501-95919f05455f
keywords:
- stream categories WDK video capture , capture video streams
- stream categories WDK video capture , preview video streams
- stream categories WDK video capture , capture still images
- capture video streams category WDK video capture
- preview video streams category WDK video capture
- capture still images category WDK video capture
- PINNAME_VIDEO_CAPTURE
- NAME_VIDEO_PREVIEW
- PINNAME_VIDEO_STILL
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Capture, Preview, and Still Category


The following GUIDs correspond to categories that capture video streams, preview video streams, and capture still images (if supported by the hardware):

-   **PINNAME\_VIDEO\_CAPTURE**

    Capture category output pins provide a stream of compressed or uncompressed digital video. This stream category is used to write movies to disk, to video conference, and for image analysis.

-   **PINNAME\_VIDEO\_PREVIEW**

    Preview category output pins provide a stream of uncompressed digital video. This stream category is used to view the video stream on the local monitor, in either RGB or YUV formats that can be directly displayed by DirectDraw. In resource-limited situations, capture minidrivers should prioritize preview stream pins lower than capture stream pins.

-   **PINNAME\_VIDEO\_STILL**

    Still category output pins are used with dual-mode cameras that are capable of producing both a capture stream and a still image stream (that is often of higher quality than the capture stream). The still image stream includes the ability to externally or programmatically trigger acquisition of an image.

The capture, preview, and still stream pin categories are almost identical in terms of data formats and stream characteristics.

**Note**  : Because many cameras produce only a single output stream, Microsoft DirectShow includes a Smart Tee filter that splits a single stream into a Capture and a Preview stream. Therefore, minidrivers for cameras that produce only a single stream should not internally duplicate their data streams to produce a preview stream.

 

When specifying **PINNAME\_VIDEO\_CAPTURE**, or **PINNAME\_VIDEO\_PREVIEW**, or **PINNAME\_VIDEO\_STILL** pins, use the information listed in the following table.

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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567628" data-raw-source="[&lt;strong&gt;KS_DATARANGE_VIDEO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567628)"><strong>KS_DATARANGE_VIDEO</strong></a> (frames only)</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567629" data-raw-source="[&lt;strong&gt;KS_DATARANGE_VIDEO2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567629)"><strong>KS_DATARANGE_VIDEO2</strong></a> (fields or frames, bob or weave settings)</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567353" data-raw-source="[&lt;strong&gt;KS_DATARANGE_MPEG1_VIDEO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567353)"><strong>KS_DATARANGE_MPEG1_VIDEO</strong></a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567362" data-raw-source="[&lt;strong&gt;KS_DATARANGE_MPEG2_VIDEO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567362)"><strong>KS_DATARANGE_MPEG2_VIDEO</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>DataFormat Structure</strong></p></td>
<td><p>KS_DATAFORMAT_VIDEO (frames only)</p>
<p>KS_DATAFORMAT_VIDEO2 (fields or frames, bob or weave settings)</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567658" data-raw-source="[&lt;strong&gt;KS_MPEG1VIDEOINFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567658)"><strong>KS_MPEG1VIDEOINFO</strong></a> (for MPEG1)</p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567667" data-raw-source="[&lt;strong&gt;KS_MPEGVIDEOINFO2&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567667)"><strong>KS_MPEGVIDEOINFO2</strong></a> (for MPEG2)</p></td>
</tr>
<tr class="odd">
<td><p><strong>Major Format GUID</strong></p></td>
<td><p>KSDATAFORMAT_TYPE_VIDEO</p></td>
</tr>
<tr class="even">
<td><p><strong>Sub-Format GUID</strong></p></td>
<td><p>RGB16, RGB24, UYVY, JPEG</p></td>
</tr>
<tr class="odd">
<td><p><strong>Specifier GUID</strong></p></td>
<td><p>KSDATAFORMAT_SPECIFIER_VIDEOINFO (frames only)</p>
<p>KSDATAFORMAT_SPECIFIER_VIDEOINFO2 (fields or frames)</p></td>
</tr>
<tr class="even">
<td><p><strong>Extended Header Size</strong></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567645" data-raw-source="[&lt;strong&gt;KS_FRAME_INFO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567645)"><strong>KS_FRAME_INFO</strong></a> if not an MPEG format. Zero if an MPEG format.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Required Property Sets</strong></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff566568" data-raw-source="[KSPROPSETID_Connection](https://msdn.microsoft.com/library/windows/hardware/ff566568)">KSPROPSETID_Connection</a></p>
<p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567806" data-raw-source="[PROPSETID_VIDCAP_DROPPEDFRAMES](https://msdn.microsoft.com/library/windows/hardware/ff567806)">PROPSETID_VIDCAP_DROPPEDFRAMES</a></p></td>
</tr>
<tr class="even">
<td><p><strong>Required Event Sets</strong></p></td>
<td><p>None</p></td>
</tr>
<tr class="odd">
<td><p><strong>DirectShow majortype</strong></p></td>
<td><p>MEDIATYPE_Video</p></td>
</tr>
<tr class="even">
<td><p><strong>DirectShow formattype</strong></p></td>
<td><p>FORMAT_VideoInfo (frames only)</p>
<p>FORMAT_VideoInfo2 (fields or frames)</p></td>
</tr>
</tbody>
</table>

 

 

 




