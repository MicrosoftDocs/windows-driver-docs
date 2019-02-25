---
title: CC Category
description: CC Category
ms.assetid: 742955f3-85a2-4627-b1b1-0bd85cdb1e77
keywords:
- stream categories WDK video capture , closed-captioning category
- CC category WDK video capture
- PINNAME_VIDEO_CC
- closed-captioning category WDK video capture
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# CC Category


The following GUID corresponds to the closed-captioning (CC) category:

-   **PINNAME\_VIDEO\_CC**

    CC category output pins provide a stream of decoded, closed-caption byte pairs from field 1, line 21.

When specifying **PINNAME\_VIDEO\_CC** pins, use the information listed in the following table.

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
<td><p>KSDATAFORMAT_TYPE_AUXLine21Data</p></td>
</tr>
<tr class="even">
<td><p><strong>Sub-Format GUID</strong></p></td>
<td><p>KSDATAFORMAT_SUBTYPE_Line21_BytePair</p></td>
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
<td><p>None</p></td>
</tr>
<tr class="even">
<td><p><strong>DirectShow formattype</strong></p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>

 

 

 




