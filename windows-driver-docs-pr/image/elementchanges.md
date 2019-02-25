---
title: ElementChanges element
description: The required ElementChanges element contains the changes to the ScannerDescription, ScannerConfiguration, DefaultScanTicket, and vendor-extended elements.
ms.assetid: d6f1d188-beb6-4ea3-a362-de64d8d8dacb
keywords: ["ElementChanges element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ElementChanges
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ElementChanges element


The required **ElementChanges** element contains the changes to the [**ScannerDescription**](scannerdescription.md), [**ScannerConfiguration**](scannerconfiguration.md), [**DefaultScanTicket**](defaultscanticket.md), and vendor-extended elements.

Usage
-----

```xml
<wscn:ElementChanges>
  child elements
</wscn:ElementChanges>
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
<td><p><a href="defaultscanticket.md" data-raw-source="[&lt;strong&gt;DefaultScanTicket&lt;/strong&gt;](defaultscanticket.md)"><strong>DefaultScanTicket</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="scannerconfiguration.md" data-raw-source="[&lt;strong&gt;ScannerConfiguration&lt;/strong&gt;](scannerconfiguration.md)"><strong>ScannerConfiguration</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="scannerdescription.md" data-raw-source="[&lt;strong&gt;ScannerDescription&lt;/strong&gt;](scannerdescription.md)"><strong>ScannerDescription</strong></a></p></td>
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
<td><p><a href="scannerelementschangeevent.md" data-raw-source="[&lt;strong&gt;ScannerElementsChangeEvent&lt;/strong&gt;](scannerelementschangeevent.md)"><strong>ScannerElementsChangeEvent</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service must include an **ElementChanges** element when it generates a [**ScannerElementsChangeEvent**](scannerelementschangeevent.md) element. Each child element of **ElementChanges** must contain all of its required child elements. If an optional element is missing from the returned XML, the WSD Scan Service is indicating to the client that the service no longer supports that element.

## See also


[**DefaultScanTicket**](defaultscanticket.md)

[**ScannerConfiguration**](scannerconfiguration.md)

[**ScannerDescription**](scannerdescription.md)

[**ScannerElementsChangeEvent**](scannerelementschangeevent.md)

 

 






