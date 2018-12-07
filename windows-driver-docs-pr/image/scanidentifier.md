---
title: ScanIdentifier element
description: The required ScanIdentifier element contains a device-specific string that the scanner provides through a ScanAvailableEvent event.
ms.assetid: 77116871-63dc-4388-9b36-a553219ddcf7
keywords: ["ScanIdentifier element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ScanIdentifier
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ScanIdentifier element


The required **ScanIdentifier** element contains a device-specific string that the scanner provides through a [**ScanAvailableEvent**](scanavailableevent.md) event.

Usage
-----

```xml
<wscn:ScanIdentifier>
  text
</wscn:ScanIdentifier>
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
<td><p><a href="scanavailableevent.md" data-raw-source="[&lt;strong&gt;ScanAvailableEvent&lt;/strong&gt;](scanavailableevent.md)"><strong>ScanAvailableEvent</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The client can send the **ScanIdentifier** element to the WSD Scan Service in a [**CreateScanJobRequest**](createscanjobrequest.md) operation element. The WSD Scan Service can use **ScanIdentifier** to ensure that the correct client is requesting the scan after a user has selected the destination.

The **ScanIdentifier** value must be unique for every [**ScanAvailableEvent**](scanavailableevent.md) instance.

## See also


[**CreateScanJobRequest**](createscanjobrequest.md)

[**ScanAvailableEvent**](scanavailableevent.md)

 

 






