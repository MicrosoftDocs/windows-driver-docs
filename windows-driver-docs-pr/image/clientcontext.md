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
ms.localizationpriority: medium
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

 

 






