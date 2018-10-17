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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
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
<td><p>[<strong>ADFBack</strong>](adfback.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ADFFront</strong>](adffront.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ADFSupportsDuplex</strong>](adfsupportsduplex.md)</p></td>
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

If the scan device has an ADF, the WSD Scan Service must provide configuration information for all **ADF** child elements.

## See also


[**ADFBack**](adfback.md)

[**ADFFront**](adffront.md)

[**ADFSupportsDuplex**](adfsupportsduplex.md)

[**ScannerConfiguration**](scannerconfiguration.md)

 

 






