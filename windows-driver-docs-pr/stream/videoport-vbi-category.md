---
title: Videoport VBI Category
description: Videoport VBI Category
ms.assetid: 99a4d204-45af-4b73-8d31-d745387a38ac
keywords:
- stream categories WDK video capture , videoport VBI
- videoport VBI category WDK video capture
- VBI WDK video capture
- vertical blanking interval WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Videoport VBI Category


The following GUID corresponds to the video port vertical-blanking-interval (VBI) category:

-   **PINNAME\_VIDEO\_VIDEOPORT\_VBI**

    Videoport VBI category pins transfer VBI streams from an analog decoder directly to DirectDraw surfaces through a hardware connection.

When specifying **PINNAME\_VIDEO\_VIDEOPORT\_VBI** pins, use the information listed in the following table.

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
<td><p>KSDATARANGE</p></td>
</tr>
<tr class="even">
<td><p><strong>DataFormat Structure</strong></p></td>
<td><p>KSDATAFORMAT</p></td>
</tr>
<tr class="odd">
<td><p><strong>MajorFormat GUID</strong></p></td>
<td><p>KSDATAFORMAT_TYPE_VIDEO</p></td>
</tr>
<tr class="even">
<td><p><strong>Sub-Format GUID</strong></p></td>
<td><p>KSDATAFORMAT_SUBTYPE_VPVBIVideo</p></td>
</tr>
<tr class="odd">
<td><p><strong>Specifier GUID</strong></p></td>
<td><p>KSDATAFORMAT_SPECIFIER_NONE</p></td>
</tr>
<tr class="even">
<td><p><strong>Extended Header Size</strong></p></td>
<td><p>0</p></td>
</tr>
<tr class="odd">
<td><p><strong>Required Property Sets</strong></p></td>
<td><p>KSPROPSETID_VPVBIConfig</p></td>
</tr>
<tr class="even">
<td><p><strong>Required Event Sets</strong></p></td>
<td><p>KSEVENTSETID_VPVBINotify</p></td>
</tr>
<tr class="odd">
<td><p><strong>DirectShow majortype</strong></p></td>
<td><p>MEDIATYPE_Video</p></td>
</tr>
<tr class="even">
<td><p><strong>DirectShow formattype</strong></p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>

 

 

 




