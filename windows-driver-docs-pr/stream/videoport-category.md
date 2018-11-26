---
title: Videoport Category
description: Videoport Category
ms.assetid: c11a407f-4ff0-4337-b989-e3ec42418ec3
keywords:
- stream categories WDK video capture , videoport
- videoport category WDK video capture
- video port category WDK video capture
- PINNAME_VIDEO_VIDEOPORT
ms.date: 04/20/2017
ms.localizationpriority: medium
---

# Videoport Category


The following GUID corresponds to the video port category:

-   **PINNAME\_VIDEO\_VIDEOPORT**

    Videoport category pins transfer image streams from an analog video decoder directly to DirectDraw surfaces through a hardware video port connection.

When specifying **PINNAME\_VIDEO\_VIDEOPORT** pins, use the information listed in the following table.

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
<td><p><strong>Major Format GUID</strong></p></td>
<td><p>KSDATAFORMAT_TYPE_VIDEO</p></td>
</tr>
<tr class="even">
<td><p><strong>Sub-Format GUID</strong></p></td>
<td><p>KSDATAFORMAT_SUBTYPE_VPVideo</p></td>
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
<td><p>KSPROPSETID_VPConfig</p></td>
</tr>
<tr class="even">
<td><p><strong>Required Event Sets</strong></p></td>
<td><p><a href="https://msdn.microsoft.com/library/windows/hardware/ff561780" data-raw-source="[KSEVENTSETID_VPNotify](https://msdn.microsoft.com/library/windows/hardware/ff561780)">KSEVENTSETID_VPNotify</a></p></td>
</tr>
<tr class="odd">
<td><p><strong>DirectShow majortype</strong></p></td>
<td><p>Mediatype_Video</p></td>
</tr>
<tr class="even">
<td><p><strong>DirectShow formattype</strong></p></td>
<td><p>None</p></td>
</tr>
</tbody>
</table>

 

 

 




