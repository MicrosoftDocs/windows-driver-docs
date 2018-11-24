---
title: ElementData for ScannerElements element
description: The required ElementData element contains the data that is returned for a scanner-related schema request.
ms.assetid: 852a7f8a-cd87-467b-8793-8a7d7943f2a9
keywords: ["ElementData for ScannerElements element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ElementData Name "" Valid ""
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ElementData for ScannerElements element


The required **ElementData** element contains the data that is returned for a scanner-related schema request.

Usage
-----

```xml
<wscn:ElementData Name="" Valid=""
  Name = "xs:string"
  Valid = "xs:string">
  child elements
</wscn:ElementData Name="" Valid="">
```

Attributes
----------

<table>
<colgroup>
<col width="25%" />
<col width="25%" />
<col width="25%" />
<col width="25%" />
</colgroup>
<thead>
<tr class="header">
<th>Attribute</th>
<th>Type</th>
<th>Required</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong><strong>Name</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Required. One of the following QNames:xmlns:ScannerDescriptionReturn the currentScannerDescription schema.xmlns:ScannerConfigurationReturn the current ScannerConfiguration schema.xmlns:ScannerStatusReturn the current ScannerStatus schema.xmlns:DefaultScanTicketReturn the current DefaultScanTicket schema.xmlns:VendorSectionReturn the identified section of a vendor-defined extension to the WSD Scan Service.</p></td>
</tr>
<tr class="even">
<td><p><strong><strong>Valid</strong></strong></p></td>
<td><p>xs:string</p></td>
<td><p>No</p></td>
<td><p></p>
<p>Required. A Boolean value that must be 0, false, 1, or true.</p></td>
</tr>
</tbody>
</table>

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
<tr class="even">
<td><p><a href="scannerstatus.md" data-raw-source="[&lt;strong&gt;ScannerStatus&lt;/strong&gt;](scannerstatus.md)"><strong>ScannerStatus</strong></a></p></td>
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
<td><p><a href="scannerelements.md" data-raw-source="[&lt;strong&gt;ScannerElements&lt;/strong&gt;](scannerelements.md)"><strong>ScannerElements</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

A client calls [**GetScannerElementsRequest**](getscannerelementsrequest.md) to determine the values of scanner-related elements. The WSD Scan Service returns this information in the **ElementData** element through the [**GetScannerElementsResponse**](getscannerelementsresponse.md) operation.

The QName value for the **Name** attribute must be a schema keyword that represents the top-level section within the WSD Scan Service for which a client requested information. The Scan Service must specify both the namespace prefix and valid, colon-separated element name.

The **Valid** attribute indicates whether the schema keyword provided by the client was valid. The WSD Scan Service sets this attribute to **true** if it can map the requested schema keyword to a valid section of its schema; otherwise, it must set this attribute to **false**.

## See also


[**DefaultScanTicket**](defaultscanticket.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**GetScannerElementsResponse**](getscannerelementsresponse.md)

[**ScannerConfiguration**](scannerconfiguration.md)

[**ScannerDescription**](scannerdescription.md)

[**ScannerElements**](scannerelements.md)

[**ScannerStatus**](scannerstatus.md)

 

 






