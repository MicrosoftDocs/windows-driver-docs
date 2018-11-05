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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScanRegion element


The optional **ScanRegion** element specifies the area to scan within the input document boundaries.

Usage
-----

```xml
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
<td><p><a href="scanregionheight.md" data-raw-source="[&lt;strong&gt;ScanRegionHeight&lt;/strong&gt;](scanregionheight.md)"><strong>ScanRegionHeight</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="scanregionwidth.md" data-raw-source="[&lt;strong&gt;ScanRegionWidth&lt;/strong&gt;](scanregionwidth.md)"><strong>ScanRegionWidth</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="scanregionxoffset.md" data-raw-source="[&lt;strong&gt;ScanRegionXOffset&lt;/strong&gt;](scanregionxoffset.md)"><strong>ScanRegionXOffset</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="scanregionyoffset.md" data-raw-source="[&lt;strong&gt;ScanRegionYOffset&lt;/strong&gt;](scanregionyoffset.md)"><strong>ScanRegionYOffset</strong></a></p></td>
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
<td><p><a href="mediaback.md" data-raw-source="[&lt;strong&gt;MediaBack&lt;/strong&gt;](mediaback.md)"><strong>MediaBack</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="mediafront.md" data-raw-source="[&lt;strong&gt;MediaFront&lt;/strong&gt;](mediafront.md)"><strong>MediaFront</strong></a></p></td>
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

## See also


[**DocumentFinalParameters**](documentfinalparameters.md)

[**InputSize**](inputsize.md)

[**MediaBack**](mediaback.md)

[**MediaFront**](mediafront.md)

[**ScanRegionHeight**](scanregionheight.md)

[**ScanRegionWidth**](scanregionwidth.md)

[**ScanRegionXOffset**](scanregionxoffset.md)

[**ScanRegionYOffset**](scanregionyoffset.md)

 

 






