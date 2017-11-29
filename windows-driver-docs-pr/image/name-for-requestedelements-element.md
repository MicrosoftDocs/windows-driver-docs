---
title: Name for RequestedElements element
description: This required Name element identifies the section of the WSD Scan Service schema that the client wants data for when it calls GetScannerElementsRequest or GetJobElementsRequest.
ms.assetid: 1b2bc3b4-24de-4957-a72a-6788425dc3b9
keywords: ["Name for RequestedElements element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn Name
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# Name for RequestedElements element


This required **Name** element identifies the section of the WSD Scan Service schema that the client wants data for when it calls [**GetScannerElementsRequest**](getscannerelementsrequest.md) or [**GetJobElementsRequest**](getjobelementsrequest.md).

Usage
-----

``` syntax
<wscn:Name>
  text
</wscn:Name>
```

Attributes
----------

There are no attributes.

Text value
----------

Required.

For [**GetScannerElementsRequest**](getscannerelementsrequest.md), one of the following QName values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>QName</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="wscn_ScannerDescription"></span><span id="wscn_scannerdescription"></span><span id="WSCN_SCANNERDESCRIPTION"></span>wscn:ScannerDescription</p></td>
<td><p>Get all of the descriptive information for the scan device.</p></td>
</tr>
<tr class="even">
<td><p><span id="wscn_ScannerConfiguration"></span><span id="wscn_scannerconfiguration"></span><span id="WSCN_SCANNERCONFIGURATION"></span>wscn:ScannerConfiguration</p></td>
<td><p>Get all of the configuration information for the scan device.</p></td>
</tr>
<tr class="odd">
<td><p><span id="wscn_ScannerStatus"></span><span id="wscn_scannerstatus"></span><span id="WSCN_SCANNERSTATUS"></span>wscn:ScannerStatus</p></td>
<td><p>Get the entire status section, including [<strong>ActiveConditions</strong>](activeconditions.md) and [<strong>ConditionHistory</strong>](conditionhistory.md).</p></td>
</tr>
<tr class="even">
<td><p><span id="xmlns_VendorSection"></span><span id="xmlns_vendorsection"></span><span id="XMLNS_VENDORSECTION"></span>xmlns:VendorSection</p></td>
<td><p>Get the identified section of a vendor-defined extension to the WSD Scan Service.</p></td>
</tr>
</tbody>
</table>

 

For [**GetJobElementsRequest**](getjobelementsrequest.md), one of the following QName values:

<table>
<colgroup>
<col width="50%" />
<col width="50%" />
</colgroup>
<thead>
<tr class="header">
<th>QName</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><span id="wscn_JobStatus"></span><span id="wscn_jobstatus"></span><span id="WSCN_JOBSTATUS"></span>wscn:JobStatus</p></td>
<td><p>Get the current [<strong>JobStatus</strong>](jobstatus.md) element data for the specified job.</p></td>
</tr>
<tr class="even">
<td><p><span id="wscn_ScanTicket"></span><span id="wscn_scanticket"></span><span id="WSCN_SCANTICKET"></span>wscn:ScanTicket</p></td>
<td><p>Get the [<strong>ScanTicket</strong>](scanticket.md) element data for the specified job.</p></td>
</tr>
<tr class="odd">
<td><p><span id="wscn_Documents"></span><span id="wscn_documents"></span><span id="WSCN_DOCUMENTS"></span>wscn:Documents</p></td>
<td><p>Get the [<strong>Documents</strong>](documents.md) element data for the specified job.</p></td>
</tr>
<tr class="even">
<td><p><span id="xmlns_VendorSection"></span><span id="xmlns_vendorsection"></span><span id="XMLNS_VENDORSECTION"></span>xmlns:VendorSection</p></td>
<td><p>Get the identified section of a vendor-defined extension to the WSD Scan Service.</p></td>
</tr>
</tbody>
</table>

 

## Child elements


There are no child elements.

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
<td><p>[<strong>RequestedElements</strong>](requestedelements.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The Qname must identify the top-level element within the WSD Scan Service schema that the client wants information for. The client must specify both the schema namespace and element name.

## <span id="see_also"></span>See also


[**GetJobElementsRequest**](getjobelementsrequest.md)

[**ActiveConditions**](activeconditions.md)

[**ConditionHistory**](conditionhistory.md)

[**Documents**](documents.md)

**GetJobElementsRequest**
[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**JobStatus**](jobstatus.md)

[**RequestedElements**](requestedelements.md)

[**ScanTicket**](scanticket.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20Name%20for%20RequestedElements%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





