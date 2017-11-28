---
title: RequestedElements element
description: The required RequestedElements element identifies the elements that the client wants data for when it calls GetScannerElementsRequest or GetJobElementsRequest.
ms.assetid: 0023afc1-723d-4b6a-9f1a-0bc21a309a65
keywords: ["RequestedElements element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn RequestedElements
api_type:
- Schema
---

# RequestedElements element


The required **RequestedElements** element identifies the elements that the client wants data for when it calls [**GetScannerElementsRequest**](getscannerelementsrequest.md) or [**GetJobElementsRequest**](getjobelementsrequest.md).

Usage
-----

``` syntax
<wscn:RequestedElements>
  child elements
</wscn:RequestedElements>
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
<td><p>[<strong>Name for RequestedElements Element</strong>](name-for-requestedelements-element.md)</p></td>
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
<td><p>[<strong>GetJobElementsRequest</strong>](getjobelementsrequest.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>GetScannerElementsRequest</strong>](getscannerelementsrequest.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **RequestedElements** element contains one or more **Name** elements for parent **RequestedElements** elements that identify the data that the client is querying.

## <span id="see_also"></span>See also


[**GetJobElementsRequest**](getjobelementsrequest.md)

[**GetScannerElementsRequest**](getscannerelementsrequest.md)

[**Name for RequestedElements Element**](name-for-requestedelements-element.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20RequestedElements%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





