---
title: Timecode Category
author: windows-driver-content
description: Timecode Category
ms.assetid: 273e0233-357e-4e13-bf8e-77ca36834ee7
keywords:
- stream categories WDK video capture , imecode
- Timecode category WDK video capture
- PINNAME_VIDEO_TIMECODE
ms.author: windows-driver-content
ms.date: 04/20/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Timecode Category


The following GUID corresponds to the Timecode category:

-   **PINNAME\_VIDEO\_TIMECODE**

    Timecode category output pins provide a stream of timecode.

When creating **PINNAME\_VIDEO\_TIMECODE** pins, use the information listed in the following table.

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
<td><p>None defined. Define GUID using Direct Show's MEDIATYPE_Timecode.</p></td>
</tr>
<tr class="even">
<td><p><strong>Sub-Format GUID</strong></p></td>
<td><p>KSDATAFORMAT_SUBTYPE_NONE</p></td>
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
<td><p>MEDIATYPE_Timecode</p></td>
</tr>
<tr class="even">
<td><p><strong>DirectShow formattype</strong></p></td>
<td><p>MEDIASUBTYPE_None</p></td>
</tr>
</tbody>
</table>

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20Timecode%20Category%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


