---
title: Platen element
description: The optional Platen element describes the capabilities of the flatbed platen that is available on the scanner.
ms.assetid: bda5aa6d-ac19-4af2-9b21-64b29d726e80
keywords: ["Platen element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Platen
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# Platen element


The optional **Platen** element describes the capabilities of the flatbed platen that is available on the scanner.

Usage
-----

```xml
<wscn:Platen>
  child elements
</wscn:Platen>
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
<td><p>[<strong>PlatenColor</strong>](platencolor.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>PlatenMaximumSize</strong>](platenmaximumsize.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>PlatenMinimumSize</strong>](platenminimumsize.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>PlatenOpticalResolution</strong>](platenopticalresolution.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>PlatenResolutions</strong>](platenresolutions.md)</p></td>
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
<td><p>[<strong>ScannerConfiguration</strong>](scannerconfiguration.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the scan device has a flatbed platen, the WSD Scan Service must provide configuration information for all **Platen** child elements.

## See also


[**PlatenColor**](platencolor.md)

[**PlatenMaximumSize**](platenmaximumsize.md)

[**PlatenMinimumSize**](platenminimumsize.md)

[**PlatenOpticalResolution**](platenopticalresolution.md)

[**PlatenResolutions**](platenresolutions.md)

[**ScannerConfiguration**](scannerconfiguration.md)

 

 






