---
title: NABTS Categories
description: NABTS Categories
ms.assetid: 7d064ed4-1bd9-4457-83c8-8b1fee10251c
keywords:
- stream categories WDK video capture , NABTS
- PINNAME_VIDEO_NABTS
- North American Broadcast Teletext Standard WDK video capture
- NABTS WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# NABTS Categories


The following GUID corresponds to the North American Broadcast Teletext Standard (NABTS) categories:

-   **PINNAME\_VIDEO\_NABTS**

    North American Broadcast Teletext Standard (NABTS) category output pins provide a decoded stream of raw or Forward Error Correction (FEC) NABTS data.

The only difference between raw or FEC NABTS data is the value of the SubFormat GUID

When specifying **PINNAME\_VIDEO\_NABTS** pins, use the information listed in the following table.

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
<td><p>KS_DATARANGE</p></td>
</tr>
<tr class="even">
<td><p><strong>DataFormat Structure</strong></p></td>
<td><p>KS_DATAFORMAT</p></td>
</tr>
<tr class="odd">
<td><p><strong>Major Format GUID</strong></p></td>
<td><p>KS_DATAFORMAT_TYPE_NABTS</p></td>
</tr>
<tr class="even">
<td><p><strong>SubFormat GUID</strong></p></td>
<td><p>KSDATAFORMAT_SUBTYPE_NABTS (raw NABTS)</p>
<p>KSDATAFORMAT_SUBTYPE_NABTS_FEC (Forward Error Correction NABTS)</p></td>
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

 

 

 




