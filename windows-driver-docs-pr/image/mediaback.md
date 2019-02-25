---
title: MediaBack element
description: The optional MediaBack element contains all parameters that are specific to the scanning of the back side of the physical media.
ms.assetid: d736c76f-7ea7-49ca-9ad9-df35924fc7b4
keywords: ["MediaBack element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn MediaBack
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# MediaBack element


The optional **MediaBack** element contains all parameters that are specific to the scanning of the back side of the physical media.

Usage
-----

```xml
<wscn:MediaBack>
  child elements
</wscn:MediaBack>
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
<td><p><a href="colorprocessing.md" data-raw-source="[&lt;strong&gt;ColorProcessing&lt;/strong&gt;](colorprocessing.md)"><strong>ColorProcessing</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="resolution.md" data-raw-source="[&lt;strong&gt;Resolution&lt;/strong&gt;](resolution.md)"><strong>Resolution</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="scanregion.md" data-raw-source="[&lt;strong&gt;ScanRegion&lt;/strong&gt;](scanregion.md)"><strong>ScanRegion</strong></a></p></td>
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
<td><p><a href="mediasides.md" data-raw-source="[&lt;strong&gt;MediaSides&lt;/strong&gt;](mediasides.md)"><strong>MediaSides</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **MediaBack** element is valid only when the scanner supports duplex scanning and the current input source, which is defined in the [**InputSource**](inputsource.md) element, is **ADFDuplex**.

If the **MediaBack** element does not contain a [**ScanRegion**](scanregion.md) element, the WSD Scan Service should use 0 as the offsets and the width and height of the [**InputMediaSize**](inputmediasize.md), if given. If **ScanRegion** is missing and **InputMediaSize** is not specified or cannot be determined by the scan device, you can determine the implementation.

If the input source is **ADFDuplex** and the **MediaBack** element is missing, all parameters that are specified in [**MediaFront**](mediafront.md) will apply to the back side scanning as well.

## See also


[**ColorProcessing**](colorprocessing.md)

[**InputMediaSize**](inputmediasize.md)

[**InputSource**](inputsource.md)

[**MediaFront**](mediafront.md)

[**MediaSides**](mediasides.md)

[**Resolution**](resolution.md)

[**ScanRegion**](scanregion.md)

 

 






