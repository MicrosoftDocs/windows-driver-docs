---
title: DestinationToken element
description: The required DestinationToken element contains a device-specific string that the scanner assigns to the current client destination.
ms.assetid: 92ff99a2-079a-4001-aa01-ff5db09f6fd2
keywords: ["DestinationToken element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn DestinationToken
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# DestinationToken element


The required **DestinationToken** element contains a device-specific string that the scanner assigns to the current client destination.

Usage
-----

```xml
<wscn:DestinationToken>
  text
</wscn:DestinationToken>
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
<td><p><a href="createscanjobrequest.md" data-raw-source="[&lt;strong&gt;CreateScanJobRequest&lt;/strong&gt;](createscanjobrequest.md)"><strong>CreateScanJobRequest</strong></a></p></td>
</tr>
<tr class="even">
<td><p><a href="destinationresponse.md" data-raw-source="[&lt;strong&gt;DestinationResponse&lt;/strong&gt;](destinationresponse.md)"><strong>DestinationResponse</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The client includes the **DestinationToken** token when it sends a [**CreateScanJobRequest**](createscanjobrequest.md) operation element after the [**ScanAvailableEvent**](scanavailableevent.md) event. The WSD Scan Service uses the specified string to check that the correct client is sending the scan request.

## See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**DestinationResponse**](destinationresponse.md)

[**ScanAvailableEvent**](scanavailableevent.md)

[**ScanDestination**](scandestination.md)

 

 






