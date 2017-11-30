---
title: ClientContext element
description: The required ClientContext element specifies a client-specific string.
ms.assetid: 09bc5f5b-6198-4553-9f6f-8219e620f634
keywords: ["ClientContext element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ClientDisplayName
api_type:
- Schema
ms.author: windowsdriverdev
ms.date: 11/28/2017
ms.topic: article
ms.prod: windows-hardware
ms.technology: windows-devices
---

# ClientContext element


The required **ClientContext** element specifies a client-specific string.

Usage
-----

``` syntax
<wscn:ClientDisplayName>
  text
</wscn:ClientDisplayName>
```

Attributes
----------

There are no attributes.

Text value
----------

Required. Any valid character string.

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
<td><p>[<strong>DestinationResponse</strong>](destinationresponse.md)</p></td>
</tr>
<tr class="even">
<td><p>[<strong>ScanAvailableEvent</strong>](scanavailableevent.md)</p></td>
</tr>
<tr class="odd">
<td><p>[<strong>ScanDestination</strong>](scandestination.md)</p></td>
</tr>
</tbody>
</table>

Remarks
-------

When the parent element of the **ClientContext** element is [**ScanDestination**](scandestination.md), **ClientContext** specifies the string value that the client provides during a **&lt;wse:Subscribe&gt;** request to receive [**ScanAvailableEvent**](scanavailableevent.md) events.

When the parent element is [**DestinationResponse**](destinationresponse.md), **ClientContext** is a copy of the data that the client sends in the subscribe operation. The WSD Scan Service returns this copy in **&lt;wse:SubscribeResponse&gt;** when it responds to a client's subscription request .

When the parent element is [**ScanAvailableEvent**](scanavailableevent.md), **ClientContext** contains the string value the scanner received as a part of the **ScanAvailableEvent** subscription request. This string enables the client to associate the **ScanAvailableEvent** with the correct scanner device and service.

The **&lt;wse:Subscribe&gt;** and **&lt;wse:SubscribeResponse&gt;** elements are described in the specification.

## <span id="see_also"></span>See also


[**DestinationResponse**](destinationresponse.md)

[**ScanAvailableEvent**](scanavailableevent.md)

[**ScanDestination**](scandestination.md)

 

 

[Send comments about this topic to Microsoft](mailto:wsddocfb@microsoft.com?subject=Documentation%20feedback%20%5Bimage\image%5D:%20ClientContext%20element%20%20RELEASE:%20%2811/8/2017%29&body=%0A%0APRIVACY%20STATEMENT%0A%0AWe%20use%20your%20feedback%20to%20improve%20the%20documentation.%20We%20don't%20use%20your%20email%20address%20for%20any%20other%20purpose,%20and%20we'll%20remove%20your%20email%20address%20from%20our%20system%20after%20the%20issue%20that%20you're%20reporting%20is%20fixed.%20While%20we're%20working%20to%20fix%20this%20issue,%20we%20might%20send%20you%20an%20email%20message%20to%20ask%20for%20more%20info.%20Later,%20we%20might%20also%20send%20you%20an%20email%20message%20to%20let%20you%20know%20that%20we've%20addressed%20your%20feedback.%0A%0AFor%20more%20info%20about%20Microsoft's%20privacy%20policy,%20see%20http://privacy.microsoft.com/default.aspx. "Send comments about this topic to Microsoft")





