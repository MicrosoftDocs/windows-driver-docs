---
title: CC Category
author: windows-driver-content
description: CC Category
MS-HAID:
- 'vidcapds\_aedab175-6ae0-4da7-85f2-58ecac6aa4fd.xml'
- 'stream.cc\_category'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 742955f3-85a2-4627-b1b1-0bd85cdb1e77
keywords: ["stream categories WDK video capture , closed-captioning category", "CC category WDK video capture", "PINNAME_VIDEO_CC", "closed-captioning category WDK video capture"]
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

 

 

 


--------------------
[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bstream\stream%5D:%20CC%20Category%20%20RELEASE:%20%288/23/2016%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")


