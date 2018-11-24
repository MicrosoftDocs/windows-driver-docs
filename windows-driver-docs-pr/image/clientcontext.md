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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ClientContext element


The required **ClientContext** element specifies a client-specific string.

Usage
-----

```xml
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
<td><p><a href="destinationresponse.md" data-raw-source="[&lt;strong&gt;DestinationResponse&lt;/strong&gt;](destinationresponse.md)"><strong>DestinationResponse</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="scanavailableevent.md" data-raw-source="[&lt;strong&gt;ScanAvailableEvent&lt;/strong&gt;](scanavailableevent.md)"><strong>ScanAvailableEvent</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="scandestination.md" data-raw-source="[&lt;strong&gt;ScanDestination&lt;/strong&gt;](scandestination.md)"><strong>ScanDestination</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

When the parent element of the **ClientContext** element is [**ScanDestination**](scandestination.md), **ClientContext** specifies the string value that the client provides during a **&lt;wse:Subscribe&gt;** request to receive [**ScanAvailableEvent**](scanavailableevent.md) events.

When the parent element is [**DestinationResponse**](destinationresponse.md), **ClientContext** is a copy of the data that the client sends in the subscribe operation. The WSD Scan Service returns this copy in **&lt;wse:SubscribeResponse&gt;** when it responds to a client's subscription request .

When the parent element is [**ScanAvailableEvent**](scanavailableevent.md), **ClientContext** contains the string value the scanner received as a part of the **ScanAvailableEvent** subscription request. This string enables the client to associate the **ScanAvailableEvent** with the correct scanner device and service.

The **&lt;wse:Subscribe&gt;** and **&lt;wse:SubscribeResponse&gt;** elements are described in the specification.

## See also


[**DestinationResponse**](destinationresponse.md)

[**ScanAvailableEvent**](scanavailableevent.md)

[**ScanDestination**](scandestination.md)

 

 






