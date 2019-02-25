---
title: DestinationResponses element
description: The required DestinationResponses element is a collection of all of the responses to a client's scan destination requests.
ms.assetid: f373b584-eec9-412e-80b2-3d8a69f4b7ca
keywords: ["DestinationResponses element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DestinationResponses
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DestinationResponses element


The required **DestinationResponses** element is a collection of all of the responses to a client's scan destination requests.

Usage
-----

```xml
<wscn:DestinationResponses>
  child elements
</wscn:DestinationResponses>
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
<td><p><a href="destinationresponse.md" data-raw-source="[&lt;strong&gt;DestinationResponse&lt;/strong&gt;](destinationresponse.md)"><strong>DestinationResponse</strong></a></p></td>
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
<td><p>&lt;wse:SubscribeResponse&gt;</p></td>
</tr>
</tbody>
</table>

Remarks
-------

A WSD Scan Service must specify one [**DestinationResponse**](destinationresponse.md) child element in a **DestinationResponses** element for each [**ScanDestination**](scandestination.md) element that a client specifies in a **&lt;wse:Subscribe&gt;** request. The **&lt;wse:Subscribe&gt;** element is described in the specification.

## See also


[**DestinationResponse**](destinationresponse.md)

[**ScanDestination**](scandestination.md)

 

 






