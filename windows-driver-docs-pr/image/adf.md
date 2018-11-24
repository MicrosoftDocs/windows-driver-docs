---
title: ADF element
description: The optional ADF element describes the capabilities of the automatic document feeder (ADF) that is attached to the scanner.
ms.assetid: 2c9114c3-0c6e-4404-a1ee-fd8d63c6e8eb
keywords: ["ADF element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ADF
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ADF element


The optional **ADF** element describes the capabilities of the automatic document feeder (ADF) that is attached to the scanner.

Usage
-----

```xml
<wscn:ADF>
  child elements
</wscn:ADF>
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
<td><p><a href="adfback.md" data-raw-source="[&lt;strong&gt;ADFBack&lt;/strong&gt;](adfback.md)"><strong>ADFBack</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="adffront.md" data-raw-source="[&lt;strong&gt;ADFFront&lt;/strong&gt;](adffront.md)"><strong>ADFFront</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="adfsupportsduplex.md" data-raw-source="[&lt;strong&gt;ADFSupportsDuplex&lt;/strong&gt;](adfsupportsduplex.md)"><strong>ADFSupportsDuplex</strong></a></p></td>
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
<td><p><a href="scannerconfiguration.md" data-raw-source="[&lt;strong&gt;ScannerConfiguration&lt;/strong&gt;](scannerconfiguration.md)"><strong>ScannerConfiguration</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

If the scan device has an ADF, the WSD Scan Service must provide configuration information for all **ADF** child elements.

## See also


[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**ADFSupportsDuplex**](adfsupportsduplex.md)

[**ScannerConfiguration**](scannerconfiguration.md)

 

 






