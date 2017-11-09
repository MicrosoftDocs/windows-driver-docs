---
title: ElementData for JobElements element
description: The required ElementData element contains the data that is returned for a job-related schema request.
MS-HAID:
- 'wsdss\_ops\_15f43fde-ec5b-4676-9cb0-51eea367ecb7.xml'
- 'image.elementdata\_for\_jobelements\_element'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 6d9724cd-c076-4c87-9c01-ec2c16cd2aac
keywords: ["ElementData for JobElements element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ElementData Name "" Valid ""
api_type:
- Schema
---

# ElementData for JobElements element


The required **ElementData** element contains the data that is returned for a job-related schema request.

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
<p>Required. One of the following QName values:xmlns:JobStatusReturn the current JobStatusschema.xmlns:ScanTicketReturn the ScanTicket element.xmlns:DocumentsReturn the Documents element.xmlns:VendorSectionGet the identified section of a vendor-defined extension to the WSD Scan Service.</p></td>
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
<td><p>Any vendor-defined elements</p></td>
</tr>
<tr class="even">
<td><p>[<strong>Documents</strong>](documents.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>JobStatus</strong>](jobstatus.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScanTicket</strong>](scanticket.md)</p></td>
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
<td><p>[<strong>JobElements</strong>](jobelements.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The WSD Scan Service returns the **ElementData** element in a [**GetJobElementsResponse**](getjobelementsresponse.md) operation element.

## <span id="see_also"></span>See also


[**Documents**](documents.md)

[**GetJobElementsResponse**](getjobelementsresponse.md)

[**JobElements**](jobelements.md)

[**JobStatus**](jobstatus.md)

[**ScanTicket**](scanticket.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ElementData%20for%20JobElements%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





