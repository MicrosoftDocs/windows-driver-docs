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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ADFBack element


The optional **ADFBack** element describes the capabilities of the back side of a duplex automatic document feeder (ADF) that is attached to the scanner.

Usage
-----

```xml
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
<td><p><a href="adfcolor.md" data-raw-source="[&lt;strong&gt;ADFColor&lt;/strong&gt;](adfcolor.md)"><strong>ADFColor</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="adfmaximumsize.md" data-raw-source="[&lt;strong&gt;ADFMaximumSize&lt;/strong&gt;](adfmaximumsize.md)"><strong>ADFMaximumSize</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="adfminimumsize.md" data-raw-source="[&lt;strong&gt;ADFMinimumSize&lt;/strong&gt;](adfminimumsize.md)"><strong>ADFMinimumSize</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="adfopticalresolution.md" data-raw-source="[&lt;strong&gt;ADFOpticalResolution&lt;/strong&gt;](adfopticalresolution.md)"><strong>ADFOpticalResolution</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="adfresolutions.md" data-raw-source="[&lt;strong&gt;ADFResolutions&lt;/strong&gt;](adfresolutions.md)"><strong>ADFResolutions</strong></a></p></td>
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
<td><p><a href="adf.md" data-raw-source="[&lt;strong&gt;ADF&lt;/strong&gt;](adf.md)"><strong>ADF</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service should specify the **ADFBack** elements and its children only if the scanner's ADF supports duplexing.

## See also


[**ADF**](adf.md)

[**ADFColor**](adfcolor.md)

[**ADFMaximumSize**](adfmaximumsize.md)

[**ADFMinimumSize**](adfminimumsize.md)

[**ADFOpticalResolution**](adfopticalresolution.md)

[**ADFResolutions**](adfresolutions.md)

 

 






