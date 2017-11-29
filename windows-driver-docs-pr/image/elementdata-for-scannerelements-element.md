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
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ElementData for ScannerElements element


The required **ElementData** element contains the data that is returned for a scanner-related schema request.

Usage
-----

``` syntax
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
<td><p>[<strong>DefaultScanTicket</strong>](defaultscanticket.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScannerConfiguration</strong>](scannerconfiguration.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScannerDescription</strong>](scannerdescription.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScannerStatus</strong>](scannerstatus.md)</p></td>
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
<td><p>[<strong>ScannerElements</strong>](scannerelements.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

A client calls [**GetScannerElementsRequest**](getscannerelementsrequest.md) to determine the values of scanner-related elements. The WSD Scan Service returns this information in the **ElementData** element through the [**GetScannerElementsResponse**](getscannerelementsresponse.md) operation.

The QName value for the **Name** attribute must be a schema keyword that represents the top-level section within the WSD Scan Service for which a client requested information. The Scan Service must specify both the namespace prefix and valid, colon-separated element name.

The **Valid** attribute indicates whether the schema keyword provided by the client was valid. The WSD Scan Service sets this attribute to **true** if it can map the requested schema keyword to a valid section of its schema; otherwise, it must set this attribute to **false**.

## <span id="see_also"></span>See also


[**DefaultScanTicket**](defaultscanticket.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**GetScannerElementsResponse**](getscannerelementsresponse.md)

[**ScannerConfiguration**](scannerconfiguration.md)

[**ScannerDescription**](scannerdescription.md)

[**ScannerElements**](scannerelements.md)

[**ScannerStatus**](scannerstatus.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ElementData%20for%20ScannerElements%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





