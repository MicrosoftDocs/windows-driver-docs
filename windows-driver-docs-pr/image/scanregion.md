---
title: ScanRegion element
description: The optional ScanRegion element specifies the area to scan within the input document boundaries.
ms.assetid: 29b94df7-503d-4bbd-99a8-9092140c6629
keywords: ["ScanRegion element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScanRegion
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
ms.localizationpriority: medium
---

# ScanRegion element


The optional **ScanRegion** element specifies the area to scan within the input document boundaries.

Usage
-----

``` syntax
<wscn:ScanRegion>
  child elements
</wscn:ScanRegion>
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
<td><p>[<strong>ScanRegionHeight</strong>](scanregionheight.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScanRegionWidth</strong>](scanregionwidth.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScanRegionXOffset</strong>](scanregionxoffset.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScanRegionYOffset</strong>](scanregionyoffset.md)</p></td>
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
<td><p>[<strong>MediaBack</strong>](mediaback.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>MediaFront</strong>](mediafront.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

All **ScanRegion** values represent one-thousandths (1/1000) of an inch.

If the requested scan region of a scan job would fall completely outside the supported acquisition area of the scan device, the scan operation should be rejected.

[**ScanRegionXOffset**](scanregionxoffset.md) + [**ScanRegionWidth**](scanregionwidth.md) must be equal or less than the [**InputSize**](inputsize.md) width.

[**ScanRegionYOffset**](scanregionyoffset.md) + [**ScanRegionHeight**](scanregionheight.md) must be equal or less than the **InputSize** height.

The WSD Scan Service can adjust a requested scan region if it cannot fulfill the specified dimensions. Any changes to the scan region should be reported in the [**DocumentFinalParameters**](documentfinalparameters.md) elements in the scan job.

## <span id="see_also"></span>See also


[**DocumentFinalParameters**](documentfinalparameters.md)

[**InputSize**](inputsize.md)

[**MediaBack**](mediaback.md)

[**MediaFront**](mediafront.md)

[**ScanRegionHeight**](scanregionheight.md)

[**ScanRegionWidth**](scanregionwidth.md)

[**ScanRegionXOffset**](scanregionxoffset.md)

[**ScanRegionYOffset**](scanregionyoffset.md)

 

 






