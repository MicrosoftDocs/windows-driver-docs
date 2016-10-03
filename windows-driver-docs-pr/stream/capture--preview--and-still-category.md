---
title: Capture, Preview, and Still Category
author: windows-driver-content
description: Capture, Preview, and Still Category
MS-HAID:
- 'vidcapds\_7a02c099-5a76-4945-9847-497d305cf9f4.xml'
- 'stream.capture\_\_preview\_\_and\_still\_category'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: b82cc3b6-1cea-4864-9501-95919f05455f
keywords: ["stream categories WDK video capture , capture video streams", "stream categories WDK video capture , preview video streams", "stream categories WDK video capture , capture still images", "capture video streams category WDK video capture", "preview video streams category WDK video capture", "capture still images category WDK video capture", "PINNAME_VIDEO_CAPTURE", "NAME_VIDEO_PREVIEW", "PINNAME_VIDEO_STILL"]
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
<td><p>[<strong>KS_DATARANGE_VIDEO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567628) (frames only)</p>
<p>[<strong>KS_DATARANGE_VIDEO2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567629) (fields or frames, bob or weave settings)</p>
<p>[<strong>KS_DATARANGE_MPEG1_VIDEO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567353)</p>
<p>[<strong>KS_DATARANGE_MPEG2_VIDEO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567362)</p></td>
</tr>
<tr class="even">
<td><p><strong>DataFormat Structure</strong></p></td>
<td><p>KS_DATAFORMAT_VIDEO (frames only)</p>
<p>KS_DATAFORMAT_VIDEO2 (fields or frames, bob or weave settings)</p>
<p>[<strong>KS_MPEG1VIDEOINFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567658) (for MPEG1)</p>
<p>[<strong>KS_MPEGVIDEOINFO2</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567667) (for MPEG2)</p></td>
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
<td><p>[<strong>KS_FRAME_INFO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567645) if not an MPEG format. Zero if an MPEG format.</p></td>
</tr>
<tr class="odd">
<td><p><strong>Required Property Sets</strong></p></td>
<td><p>[KSPROPSETID_Connection](https://msdn.microsoft.com/library/windows/hardware/ff566568)</p>
<p>[PROPSETID_VIDCAP_DROPPEDFRAMES](https://msdn.microsoft.com/library/windows/hardware/ff567806)</p></td>
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Capture,%20Preview,%20and%20Still%20Category%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


