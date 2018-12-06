---
title: ClientDisplayName element
description: The required ClientDisplayName element specifies the string that the scanner should display in its user interface.
ms.assetid: e43e5c51-5f8e-47af-b5da-707b89401935
keywords: ["ClientDisplayName element Imaging Devices"]
topic_type:
- apiref
api_name:
- wscn ClientDisplayName
api_type:
- Schema
ms.date: 11/28/2017
ms.localizationpriority: medium
---

# ClientDisplayName element


The required **ClientDisplayName** element specifies the string that the scanner should display in its user interface.

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
<td><p><a href="scandestination.md" data-raw-source="[&lt;strong&gt;ScanDestination&lt;/strong&gt;](scandestination.md)"><strong>ScanDestination</strong></a></p></td>
</tr>
</tbody>
</table>

Remarks
-------

The displayed name enables a user to select the requesting client as a scan destination. When the user chooses this display name and presses the scan button, the WSD Scan Service will send a [**ScanAvailableEvent**](scanavailableevent.md) event to the scan destination that subscribed to receive it.

## See also


[**ScanAvailableEvent**](scanavailableevent.md)

[**ScanDestination**](scandestination.md)

 

 






