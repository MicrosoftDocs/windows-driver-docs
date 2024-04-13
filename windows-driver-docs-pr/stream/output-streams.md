---
title: Output Streams
description: Output Streams
keywords:
- output streams WDK DVD decoder
ms.date: 04/20/2017
---

# Output Streams





The following table describes the video port output stream media types used by DVDs:

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
<td><p>KSDATAFORMAT_TYPE_VIDEO</p></td>
</tr>
<tr class="even">
<td><p>Minor Format GUID</p></td>
<td><p>KSDATAFORMAT_SUBTYPE_VPVideo</p></td>
</tr>
<tr class="odd">
<td><p>Format Block Specifier GUID</p></td>
<td><p>KSDATAFORMAT_SPECIFIER_NULL</p>
<div>
 
</div>
No format block.</td>
</tr>
</tbody>
</table>

 

Kernel-mode interface provides control of video port extensions (VPE) settings. For more information, see [VideoPort Extensions Background](../display/video-port-extensions-background.md).

The following table describes the closed caption (CC) output stream media type used by DVDs:

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
<td><p>KSDATAFORMAT_TYPE_AUXLine21Data</p></td>
</tr>
<tr class="even">
<td><p>Minor Format GUID</p></td>
<td><p>KSDATAFORMAT_SUBTYPE_Line21_GOPPacket</p></td>
</tr>
<tr class="odd">
<td><p>Format Block Specifier GUID</p></td>
<td><p>KSDATAFORMAT_SPECIFIER_NONE</p>
<div>
 
</div>
No format block.</td>
</tr>
</tbody>
</table>

 

A frame size of 200 (decimal) in the **SampleSize** member of the [**KSDATAFORMAT**](/windows-hardware/drivers/ddi/ks/ns-ks-ksdataformat) structure must be specified. For more information, see [Closed Captioning Streams](closed-captioning-streams.md).

 

