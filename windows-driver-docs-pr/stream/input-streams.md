---
title: Input Streams
description: Input Streams
ms.assetid: 0aa378d8-e7e2-4555-b541-dd1ed77b4a12
keywords:
- input streams WDK DVD decoder
- DVD PACKs WDK DVD decoder
- subpicture streams WDK DVD decoder
- SDDS audio input streams WDK DVD decoder
- DTS audio input streams WDK DVD decoder
- LPCM audio input streams WDK DVD decoder
- AC-3 WDK DVD decoder
- MPEG2 video input streams WDK DVD decoder
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Input Streams





DVD input streams are provided to the minidriver as arrays of encrypted DVD PACKs. PACKs are as defined in the DVD specification. Note that the system clock reference (SCR) field of the PACK is set to zero because Microsoft's DVD architecture uses the "master clock" paradigm for audio and video synchronization. Typically, the audio stream of the DVD decoder minidriver provides the master clock. For more information, see [Master Clock](master-clock.md).

DVD data streams are sent to the minidriver through the [**SRB\_WRITE\_DATA**](https://msdn.microsoft.com/library/windows/hardware/ff568220) request. For more information about SRB requests, see [Handling Stream Request Blocks](handling-stream-request-blocks.md) and [Stream Class SRB Reference](https://msdn.microsoft.com/library/windows/hardware/ff568295). Hardware should support scatter/gather DMA, because several DVD PACKs may be present in a single request packet.

The following table describes the MPEG2 video input stream media types used by DVD movies:

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
<td><p>Major Format GUID</p></td>
<td><p>KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK</p></td>
</tr>
<tr class="even">
<td><p>Minor Format GUID</p></td>
<td><p>KSDATAFORMAT_SUBTYPE_MPEG2_VIDEO</p></td>
</tr>
<tr class="odd">
<td><p>Format Block Specifier GUID</p></td>
<td><p>KSDATAFORMAT_SPECIFIER_MPEG2_VIDEO</p></td>
</tr>
<tr class="even">
<td><p>Format Block Structure</p></td>
<td><p>MPEG2VIDEOINFO</p>
<div>
 
</div>
(Superset of VIDEOINFO2 structure. Also indicates MPEG profile and level.)</td>
</tr>
</tbody>
</table>

 

The following table describes the AC-3 audio input stream media types used by DVD movies:

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
<td><p>Major Format GUID</p></td>
<td><p>KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK</p></td>
</tr>
<tr class="even">
<td><p>Minor Format GUID</p></td>
<td><p>KSDATAFORMAT_SUBTYPE_AC3_AUDIO</p></td>
</tr>
<tr class="odd">
<td><p>Format Block Specifier GUID</p></td>
<td><p>KSDATAFORMAT_SPECIFIER_WAVEFORMATEX</p>
<p>(Note that this is expected to change.)</p></td>
</tr>
<tr class="even">
<td><p>Format Block Structure</p></td>
<td><p>KSDATAFORMAT_WAVEFORMATEX</p>
<div>
 
</div>
Superset of WaveFormatEx
<p>(More than two channels. Down-mix descriptor.)</p></td>
</tr>
</tbody>
</table>

 

The following table describes the LPCM audio input stream media types used by DVD movies:

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
<td><p>Major Format GUID</p></td>
<td><p>KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK</p></td>
</tr>
<tr class="even">
<td><p>Minor Format GUID</p></td>
<td><p>KSDATAFORMAT_SUBTYPE_LPCM_AUDIO</p></td>
</tr>
<tr class="odd">
<td><p>Format Block Specifier GUID</p></td>
<td><p>KSDATAFORMAT_SPECIFIER_WAVEFORMATEX</p></td>
</tr>
<tr class="even">
<td><p>Format Block Structure</p></td>
<td><p>KSDATAFORMAT_WAVEFORMATEX</p></td>
</tr>
</tbody>
</table>

 

The following table describes the DTS audio input stream media types used by DVD movies:

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
<td><p>Major Format GUID</p></td>
<td><p>KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK</p></td>
</tr>
<tr class="even">
<td><p>Minor Format GUID</p></td>
<td><p>KSDATAFORMAT_SUBTYPE_DTS_AUDIO</p></td>
</tr>
<tr class="odd">
<td><p>Format Block Specifier GUID</p></td>
<td><p>KSDATAFORMAT_SPECIFIER_WAVEFORMATEX</p>
<p>(Note that this is expected to change.)</p></td>
</tr>
<tr class="even">
<td><p>Format Block Structure</p></td>
<td><p>KSDATAFORMAT_WAVEFORMATEX</p>
<div>
 
</div>
Superset of WaveFormatEx
<p>(More than two channels. Down-mix descriptor.)</p></td>
</tr>
</tbody>
</table>

 

The following table describes the SDDS audio input stream media types used by DVD movies:

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
<td><p>Major Format GUID</p></td>
<td><p>KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK</p></td>
</tr>
<tr class="even">
<td><p>Minor Format GUID</p></td>
<td><p>KSDATAFORMAT_SUBTYPE_SDDS_AUDIO</p></td>
</tr>
<tr class="odd">
<td><p>Format Block Specifier GUID</p></td>
<td><p>KSDATAFORMAT_SPECIFIER_WAVEFORMATEX</p>
<p>(Note that this is expected to change.)</p></td>
</tr>
<tr class="even">
<td><p>Format Block Structure</p></td>
<td><p>KSDATAFORMAT_WAVEFORMATEX</p>
<div>
 
</div>
Superset of WaveFormatEx
<p>(More than two channels. Down-mix descriptor.)</p></td>
</tr>
</tbody>
</table>

 

The following table describes the subpicture stream media types used by DVD movies:

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
<td><p>Major Format GUID</p></td>
<td><p>KSDATAFORMAT_TYPE_DVD_ENCRYPTED_PACK</p></td>
</tr>
<tr class="even">
<td><p>Minor Format GUID</p></td>
<td><p>KSDATAFORMAT_SUBTYPE_SUBPICTURE</p></td>
</tr>
<tr class="odd">
<td><p>Format Block Specifier GUID</p></td>
<td><p>KSDATAFORMAT_SPECIFIER_NONE</p></td>
</tr>
<tr class="even">
<td><p>Format Block Structure</p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>

 

For subpicture highlighting, palette information and highlight information are passed as properties. The subpicture data stream consists of packets of data, as provided by the DVD specification. Although the PACK header is stripped off, it is still provided.

The Microsoft supplied DVD navigator filter parses all button and keyboard information and only passes one highlight rectangle down to the subpicture decoder at any given time. As a result, highlight information is sent to the decoder more often than it is present in the DVD stream. This is different from the DVD specification.

The DVD navigator/splitter filter processes all keystroke information and sends new highlight information each time a button state changes. The information describes only one mode of one button at a time. It includes a display rectangle in pixel coordinates of the screen, or a display of the subpicture, if present. The [**KSPROPERTY\_SPHLI**](https://msdn.microsoft.com/library/windows/hardware/ff565627) structure also contains color and contrast information but only for the present state of the currently selected button. The format is defined in the DVD specification.

The highlight information arrives asynchronously to the data stream. The DVD decoder minidriver must use the highlight Start and End time stamps to correlate the highlight information to the relevant subpicture information, if any. If the DVD decoder minidriver has not received any subpicture stream information for the requested time stamps, the decoder assumes that the highlight information is stand-alone and does not apply to a subpicture. In this case, the color and contrast information can be assumed to be all the same color.

Highlight information contains Start and End time-stamps. These are in the same units as other time stamps, with two exceptions: A Start time-stamp of 0xFFFFFFFF means the highlight property is effective upon receipt, and an End time-stamp of 0xFFFFFFFF means the highlight property is valid until the next highlight is received.

 

 




