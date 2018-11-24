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
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DestinationResponse element


The required **DestinationResponse** element contains the response information for a single [**ScanDestination**](scandestination.md) registration.

Usage
-----

```xml
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
<td><p><a href="clientcontext.md" data-raw-source="[&lt;strong&gt;ClientContext&lt;/strong&gt;](clientcontext.md)"><strong>ClientContext</strong></a></p></td>
</tr>
<tr class="odd">
<td><p><a href="destinationtoken.md" data-raw-source="[&lt;strong&gt;DestinationToken&lt;/strong&gt;](destinationtoken.md)"><strong>DestinationToken</strong></a></p></td>
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
<td><p><a href="destinationresponses.md" data-raw-source="[&lt;strong&gt;DestinationResponses&lt;/strong&gt;](destinationresponses.md)"><strong>DestinationResponses</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The **DestinationResponse** element contains the [**ClientContext**](clientcontext.md) element from its matching [**ScanDestination**](scandestination.md) element so that the client can identify the response. **DestinationResponse** also contains a [**DestinationToken**](destinationtoken.md) element for use in all [**CreateScanJobRequest**](createscanjobrequest.md) operation elements from this destination.

## See also


[**ClientContext**](clientcontext.md)

[**CreateScanJobRequest**](createscanjobrequest.md)

[**DestinationResponses**](destinationresponses.md)

[**DestinationToken**](destinationtoken.md)

[**ScanDestination**](scandestination.md)

 

 






