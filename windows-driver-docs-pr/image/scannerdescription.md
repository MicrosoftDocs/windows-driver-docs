---
title: ScannerDescription element
description: ScannerDescription element
MS-HAID:
- 'wsdss\_desc\_a60b847e-b48a-4466-b00e-f82f7203e5ea.xml'
- 'image.scannerdescription'
MSHAttr:
- 'PreferredSiteName:MSDN'
- 'PreferredLib:/library/windows/hardware'
ms.assetid: 4429702e-18de-4b7c-83a2-ac405517e730
keywords: ["ScannerDescription element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScannerDescription
api_type:
- Schema
---

# ScannerDescription element


Usage
-----

``` syntax
<wscn:ScannerDescription>
  child elements
</wscn:ScannerDescription>
```

Attributes
----------

There are no attributes.

Text value
----------

None

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
<td><p>[<strong>ScannerInfo</strong>](scannerinfo.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScannerLocation</strong>](scannerlocation.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScannerName</strong>](scannername.md)</p></td>
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
<td><p>[<strong>ElementChanges</strong>](elementchanges.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ElementData for parent ScannerElements</strong>](elementdata-for-scannerelements-element.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

The **ScannerDescription** element contains information about the scanner that rarely or never changes. A client retrieves this information by calling the [**GetScannerElementsRequest**](getscannerelementsrequest.md) operation element.

## <span id="see_also"></span>See also


[**ElementChanges**](elementchanges.md)

[**ElementData for parent ScannerElements**](elementdata-for-scannerelements-element.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**ScannerInfo**](scannerinfo.md)

[**ScannerLocation**](scannerlocation.md)

[**ScannerName**](scannername.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ScannerDescription%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





