---
title: Analog Video Category
description: Analog Video Category
ms.assetid: 64564c81-b1e1-482b-ae70-59b229a5e86f
keywords:
- stream categories WDK video capture , analog video
- analog video category WDK video capture
- PINNAME_VIDEO_ANALOGVIDEOIN
- analog audio WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
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
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567340" data-raw-source="[&lt;strong&gt;KS_DATARANGE_ANALOGVIDEO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567340)"><strong>KS_DATARANGE_ANALOGVIDEO</strong></a></p></td>
</tr>
<tr class="even">
<td><p><strong>DataFormat Structure</strong></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff567340" data-raw-source="[&lt;strong&gt;KS_DATARANGE_ANALOGVIDEO&lt;/strong&gt;](https://msdn.microsoft.com/library/windows/hardware/ff567340)"><strong>KS_DATARANGE_ANALOGVIDEO</strong></a></p></td>
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

 

 




