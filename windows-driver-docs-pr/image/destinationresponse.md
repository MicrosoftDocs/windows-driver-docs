---
title: DestinationResponse element
description: The required DestinationResponse element contains the response information for a single ScanDestination registration.
ms.assetid: 388304ca-4d62-40cf-ad68-13607a836caf
keywords: ["DestinationResponse element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DestinationResponse
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# DestinationResponse element


The required **DestinationResponse** element contains the response information for a single [**ScanDestination**](scandestination.md) registration.

Usage
-----

``` syntax
<wscn:DestinationResponse>
  child elements
</wscn:DestinationResponse>
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
<td><p>&lt;Any vendor-defined elements&gt;</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ClientContext</strong>](clientcontext.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>DestinationToken</strong>](destinationtoken.md)</p></td>
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
<td><p>[<strong>DestinationResponses</strong>](destinationresponses.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **DestinationResponse** element contains the [**ClientContext**](clientcontext.md) element from its matching [**ScanDestination**](scandestination.md) element so that the client can identify the response. **DestinationResponse** also contains a [**DestinationToken**](destinationtoken.md) element for use in all [**CreateScanJobRequest**](createscanjobrequest.md) operation elements from this destination.

## <span id="see_also"></span>See also


[**ClientContext**](clientcontext.md)

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DestinationResponses**](destinationresponses.md)

[**DestinationToken**](destinationtoken.md)

[**ScanDestination**](scandestination.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20DestinationResponse%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





