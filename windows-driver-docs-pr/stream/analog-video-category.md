---
title: Analog Video Category
author: windows-driver-content
description: Analog Video Category
MS-HAID:
- 'vidcapds\_2f2633e0-230c-4043-a925-b203f1d40cdc.xml'
- 'stream.analog\_video\_category'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 64564c81-b1e1-482b-ae70-59b229a5e86f
keywords: ["stream categories WDK video capture , analog video", "analog video category WDK video capture", "PINNAME_VIDEO_ANALOGVIDEOIN", "analog audio WDK video capture"]
---

# Analog Video Category


The following GUID corresponds to the analog video in category:

-   **PINNAME\_VIDEO\_ANALOGVIDEOIN**

    The Analog Video In category represents the stream of analog video input to a video decoder filter.

When specifying **PINNAME\_VIDEO\_ANALOGVIDEOIN**, pins, use the information listed in the following table.

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
<td><p>[<strong>KS_DATARANGE_ANALOGVIDEO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567340)</p></td>
</tr>
<tr class="even">
<td><p><strong>DataFormat Structure</strong></p></td>
<td><p>[<strong>KS_DATARANGE_ANALOGVIDEO</strong>](https://msdn.microsoft.com/library/windows/hardware/ff567340)</p></td>
</tr>
<tr class="odd">
<td><p><strong>MajorFormat GUID</strong></p></td>
<td><p>KSDATAFORMAT_TYPE_ANALOGVIDEO</p></td>
</tr>
<tr class="even">
<td><p><strong>Sub-Format GUID</strong></p></td>
<td><p>KSDATAFORMAT_SUBTYPE_NONE</p></td>
</tr>
<tr class="odd">
<td><p><strong>Specifier GUID</strong></p></td>
<td><p>KSDATAFORMAT_SPECIFIER_ANALOGVIDEO</p></td>
</tr>
<tr class="even">
<td><p><strong>Extended Header Size</strong></p></td>
<td><p>0</p></td>
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
<td><p>MEDIATYPE_AnalogVideo</p></td>
</tr>
<tr class="even">
<td><p><strong>DirectShow formattype</strong></p></td>
<td><p>FORMAT_AnalogVideo</p></td>
</tr>
</tbody>
</table>

 

There is no special category defined for analog audio, such as TV or radio audio. When specifying a category for devices with analog audio pins, the value of the **MajorFormat** member should be KSDATAFORMAT\_TYPE\_ANALOGAUDIO. The value of the **Specifier** member should be KSDATAFORMAT\_SPECIFIER\_NONE and the **subtype** member and the format block should be set to KSDATAFORMAT\_SUBTYPE\_NONE. For more information about radio audio, see [Video Capture Devices with Radio Tuners](video-capture-devices-with-radio-tuners.md).

Although the analog video stream essentially mimics the input to the analog video decoder, it simultaneously acts as a data transport for tuning information. Tuning packets, originating at the TV tuner filter, are passed through any intervening crossbar filters at the start and end of every tuning operation. The data packet is a [**KS\_TVTUNER\_CHANGE\_INFO**](https://msdn.microsoft.com/library/windows/hardware/ff567691) structure that contains the country/region code, channel, frequency, and analog video standard in use.

Capture filters must propagate this tuning packet in the extended header of VBI output streams to downstream VBI codecs.

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Analog%20Video%20Category%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


