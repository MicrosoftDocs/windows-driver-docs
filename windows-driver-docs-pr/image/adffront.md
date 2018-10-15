---
title: ADFFront element
description: The required ADFFront element describes the capabilities of the front side of the automatic document feeder (ADF) that is attached to the scanner.
ms.assetid: 6b49f5da-6866-4ec6-8973-7c582bd3a1a1
keywords: ["ADFFront element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ADFFront
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ADFFront element


The required **ADFFront** element describes the capabilities of the front side of the automatic document feeder (ADF) that is attached to the scanner.

Usage
-----

```xml
<wscn:ADFFront>
  child elements
</wscn:ADFFront>
```

Attributes
----------

There are no attributes.

## Child elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>ADFColor</strong>](adfcolor.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ADFMaximumSize</strong>](adfmaximumsize.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ADFMinimumSize</strong>](adfminimumsize.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ADFOpticalResolution</strong>](adfopticalresolution.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ADFResolutions</strong>](adfresolutions.md)</p></td>
</tr>
</tbody>
</table>

## Parent elements


<table>
<colgroup>
<col width="100%" />
</colgroup>
<thead>
<tr class="header">
<th>Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>[<strong>ADF</strong>](adf.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the scanner has an ADF the WSD Scan Service must provide details for it in the **ADFFront** element, regardless of the ADF's duplexing capabilities.

## See also


[**ADF**](adf.md)

[**ADFColor**](adfcolor.md)

[**ADFMaximumSize**](adfmaximumsize.md)

[**ADFMinimumSize**](adfminimumsize.md)

[**ADFOpticalResolution**](adfopticalresolution.md)

[**ADFResolutions**](adfresolutions.md)

 

 






