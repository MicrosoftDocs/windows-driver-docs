---
title: MediaFront element
description: The required MediaFront element contains all parameters that are specific to the scanning of the front side of the physical media.
ms.assetid: 1bde587b-4057-4368-b075-c22561ee45cc
keywords: ["MediaFront element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn MediaFront
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# MediaFront element


The required **MediaFront** element contains all parameters that are specific to the scanning of the front side of the physical media.

Usage
-----

``` syntax
<wscn:MediaFront>
  child elements
</wscn:MediaFront>
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
<td><p>[<strong>ColorProcessing</strong>](colorprocessing.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Resolution</strong>](resolution.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScanRegion</strong>](scanregion.md)</p></td>
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
<td><p>[<strong>MediaSides</strong>](mediasides.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the **MediaFront** element does not contain a [**ScanRegion**](scanregion.md) element, the WSD Scan Service should use 0 as the offsets and the width and height of the [**InputMediaSize**](inputmediasize.md), if given. If **ScanRegion** is missing and **InputMediaSize** is not specified or cannot be determined by the scan device, you can determine the implementation.

## <span id="see_also"></span>See also


[**ColorProcessing**](colorprocessing.md)

[**InputMediaSize**](inputmediasize.md)

[**MediaBack**](mediaback.md)

[**MediaSides**](mediasides.md)

[**Resolution**](resolution.md)

[**ScanRegion**](scanregion.md)

 

 






