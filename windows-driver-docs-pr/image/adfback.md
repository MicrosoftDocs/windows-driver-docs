---
title: ADFBack element
description: The optional ADFBack element describes the capabilities of the back side of a duplex automatic document feeder (ADF) that is attached to the scanner.
ms.assetid: f364c001-ec1a-4f8c-b25a-eaa5368ba05f
keywords: ["ADFBack element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ADFBack
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ADFBack element


The optional **ADFBack** element describes the capabilities of the back side of a duplex automatic document feeder (ADF) that is attached to the scanner.

Usage
-----

``` syntax
<wscn:ADFBack>
  child elements
</wscn:ADFBack>
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

The WSD Scan Service should specify the **ADFBack** elements and its children only if the scanner's ADF supports duplexing.

## <span id="see_also"></span>See also


[**ADF**](adf.md)

[**ADFColor**](adfcolor.md)

[**ADFMaximumSize**](adfmaximumsize.md)

[**ADFMinimumSize**](adfminimumsize.md)

[**ADFOpticalResolution**](adfopticalresolution.md)

[**ADFResolutions**](adfresolutions.md)

 

 






